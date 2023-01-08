"""Checks the commands' security"""

#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2021 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

import logging
import time
import typing

from telethon.hints import EntityLike
from telethon.utils import get_display_name
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import ChatParticipantAdmin, ChatParticipantCreator, Message

from . import main, utils
from .database import Database
from .tl_cache import CustomTelegramClient

logger = logging.getLogger(__name__)

OWNER = 1 << 0
SUDO = 1 << 1
SUPPORT = 1 << 2
GROUP_OWNER = 1 << 3
GROUP_ADMIN_ADD_ADMINS = 1 << 4
GROUP_ADMIN_CHANGE_INFO = 1 << 5
GROUP_ADMIN_BAN_USERS = 1 << 6
GROUP_ADMIN_DELETE_MESSAGES = 1 << 7
GROUP_ADMIN_PIN_MESSAGES = 1 << 8
GROUP_ADMIN_INVITE_USERS = 1 << 9
GROUP_ADMIN = 1 << 10
GROUP_MEMBER = 1 << 11
PM = 1 << 12
EVERYONE = 1 << 13

BITMAP = {
    "OWNER": OWNER,
    "SUDO": SUDO,
    "SUPPORT": SUPPORT,
    "GROUP_OWNER": GROUP_OWNER,
    "GROUP_ADMIN_ADD_ADMINS": GROUP_ADMIN_ADD_ADMINS,
    "GROUP_ADMIN_CHANGE_INFO": GROUP_ADMIN_CHANGE_INFO,
    "GROUP_ADMIN_BAN_USERS": GROUP_ADMIN_BAN_USERS,
    "GROUP_ADMIN_DELETE_MESSAGES": GROUP_ADMIN_DELETE_MESSAGES,
    "GROUP_ADMIN_PIN_MESSAGES": GROUP_ADMIN_PIN_MESSAGES,
    "GROUP_ADMIN_INVITE_USERS": GROUP_ADMIN_INVITE_USERS,
    "GROUP_ADMIN": GROUP_ADMIN,
    "GROUP_MEMBER": GROUP_MEMBER,
    "PM": PM,
    "EVERYONE": EVERYONE,
}

GROUP_ADMIN_ANY = (
    GROUP_ADMIN_ADD_ADMINS
    | GROUP_ADMIN_CHANGE_INFO
    | GROUP_ADMIN_BAN_USERS
    | GROUP_ADMIN_DELETE_MESSAGES
    | GROUP_ADMIN_PIN_MESSAGES
    | GROUP_ADMIN_INVITE_USERS
    | GROUP_ADMIN
)

DEFAULT_PERMISSIONS = OWNER | SUDO

PUBLIC_PERMISSIONS = GROUP_OWNER | GROUP_ADMIN_ANY | GROUP_MEMBER | PM

ALL = (1 << 13) - 1


def owner(func: callable) -> callable:
    return _sec(func, OWNER)


def sudo(func: callable) -> callable:
    return _sec(func, SUDO)


def support(func: callable) -> callable:
    return _sec(func, SUDO | SUPPORT)


def group_owner(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_OWNER)


def group_admin_add_admins(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_ADD_ADMINS)


def group_admin_change_info(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_CHANGE_INFO)


def group_admin_ban_users(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_BAN_USERS)


def group_admin_delete_messages(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_DELETE_MESSAGES)


def group_admin_pin_messages(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_PIN_MESSAGES)


def group_admin_invite_users(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN_INVITE_USERS)


def group_admin(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_ADMIN)


def group_member(func: callable) -> callable:
    return _sec(func, SUDO | GROUP_MEMBER)


def pm(func: callable) -> callable:
    return _sec(func, SUDO | PM)


def unrestricted(func: callable) -> callable:
    return _sec(func, ALL)


def inline_everyone(func: callable) -> callable:
    return _sec(func, EVERYONE)


def _sec(func: callable, flags: int) -> callable:
    prev = getattr(func, "security", 0)
    func.security = prev | OWNER | flags
    return func


class SecurityManager:
    """Manages command execution security policy"""

    def __init__(self, client: CustomTelegramClient, db: Database):
        self._client = client
        self._db = db
        self._cache = {}

        self._any_admin = db.get(__name__, "any_admin", False)
        self._default = db.get(__name__, "default", DEFAULT_PERMISSIONS)
        self._tsec_chat = db.pointer(__name__, "tsec_chat", [])
        self._tsec_user = db.pointer(__name__, "tsec_user", [])
        self._owner = db.pointer(__name__, "owner", [])
        self._sudo = db.pointer(__name__, "sudo", [])
        self._support = db.pointer(__name__, "support", [])

        self._reload_rights()

        self.any_admin = self._any_admin
        self.default = self._default
        self.tsec_chat = self._tsec_chat
        self.tsec_user = self._tsec_user
        self.owner = self._owner
        self.sudo = self._sudo
        self.support = self._support

    def _reload_rights(self):
        """
        Internal method to ensure that account owner is always in the owner list
        and to clear out outdated tsec rules
        """

        if self._client.tg_id not in self._owner:
            self._owner.append(self._client.tg_id)

        for info in self._tsec_user.copy():
            if info["expires"] and info["expires"] < time.time():
                self._tsec_user.remove(info)

        for info in self._tsec_chat.copy():
            if info["expires"] and info["expires"] < time.time():
                self._tsec_chat.remove(info)

    def add_rule(
        self,
        target_type: str,
        target: EntityLike,
        rule: str,
        duration: int,
    ):
        """
        Adds a targeted security rule

        :param target_type: "user" or "chat"
        :param target: target entity
        :param rule: rule name
        :param duration: rule duration in seconds
        :return: None
        """

        if target_type not in {"chat", "user"}:
            raise ValueError(f"Invalid target_type: {target_type}")

        if not rule.startswith("command") and not rule.startswith("module"):
            raise ValueError(f"Invalid rule: {rule}")

        if duration < 0:
            raise ValueError(f"Invalid duration: {duration}")

        (self._tsec_chat if target_type == "chat" else self._tsec_user).append(
            {
                "target": target.id,
                "rule_type": rule.split("/")[0],
                "rule": rule.split("/", maxsplit=1)[1],
                "expires": int(time.time() + duration) if duration else 0,
                "entity_name": get_display_name(target),
                "entity_url": utils.get_entity_url(target),
            }
        )

    def remove_rules(self, target_type: str, target_id: int) -> bool:
        """
        Removes all targeted security rules for the given target

        :param target_type: "user" or "chat"
        :param target_id: target entity ID
        :return: True if any rules were removed
        """

        any_ = False

        if target_type == "user":
            for rule in self.tsec_user.copy():
                if rule["target"] == target_id:
                    self.tsec_user.remove(rule)
                    any_ = True
        elif target_type == "chat":
            for rule in self.tsec_chat.copy():
                if rule["target"] == target_id:
                    self.tsec_chat.remove(rule)
                    any_ = True

        return any_

    def get_flags(self, func: typing.Union[callable, int]) -> int:
        """
        Gets the security flags for the given function

        :param func: function or flags
        :return: security flags
        """

        if isinstance(func, int):
            config = func
        else:
            # Return masks there so user don't need to reboot
            # every time he changes permissions. It doesn't
            # decrease security at all, bc user anyway can
            # access this attribute
            config = self._db.get(__name__, "masks", {}).get(
                f"{func.__module__}.{func.__name__}",
                getattr(func, "security", self._default),
            )

        if config & ~ALL and not config & EVERYONE:
            logger.error("Security config contains unknown bits")
            return False

        return config & self._db.get(__name__, "bounding_mask", DEFAULT_PERMISSIONS)

    async def check(
        self,
        message: typing.Optional[Message],
        func: typing.Union[callable, int],
        user_id: typing.Optional[int] = None,
    ) -> bool:
        """
        Checks if message sender is permitted to execute certain function

        :param message: Message to check or None if you manually pass user_id
        :param func: function or flags
        :param user_id: user ID
        :return: True if permitted, False otherwise
        """

        self._reload_rights()

        if not (config := self.get_flags(func)):
            return False

        if not user_id:
            user_id = message.sender_id

        if user_id == self._client.tg_id or getattr(message, "out", False):
            return True

        logger.debug("Checking security match for %s", config)

        f_owner = config & OWNER
        f_sudo = config & SUDO
        f_support = config & SUPPORT
        f_group_owner = config & GROUP_OWNER
        f_group_admin_add_admins = config & GROUP_ADMIN_ADD_ADMINS
        f_group_admin_change_info = config & GROUP_ADMIN_CHANGE_INFO
        f_group_admin_ban_users = config & GROUP_ADMIN_BAN_USERS
        f_group_admin_delete_messages = config & GROUP_ADMIN_DELETE_MESSAGES
        f_group_admin_pin_messages = config & GROUP_ADMIN_PIN_MESSAGES
        f_group_admin_invite_users = config & GROUP_ADMIN_INVITE_USERS
        f_group_admin = config & GROUP_ADMIN
        f_group_member = config & GROUP_MEMBER
        f_pm = config & PM

        f_group_admin_any = (
            f_group_admin_add_admins
            or f_group_admin_change_info
            or f_group_admin_ban_users
            or f_group_admin_delete_messages
            or f_group_admin_pin_messages
            or f_group_admin_invite_users
            or f_group_admin
        )

        if (
            f_owner
            and user_id in self._owner
            or f_sudo
            and user_id in self._sudo
            or f_support
            and user_id in self._support
        ):
            return True

        if user_id in self._db.get(main.__name__, "blacklist_users", []):
            return False

        if message is None:  # In case of checking inline query security map
            return bool(config & EVERYONE)

        try:
            chat = utils.get_chat_id(message)
        except Exception:
            chat = None

        try:
            cmd = message.raw_text[1:].split()[0].strip()
        except Exception:
            cmd = None

        if callable(func):
            for info in self._tsec_user.copy():
                if info["target"] == user_id:
                    if info["rule_type"] == "command" and info["rule"] == cmd:
                        logger.debug("tsec match for user %s", cmd)
                        return True

                    if (
                        info["rule_type"] == "module"
                        and info["rule"] == func.__self__.__class__.__name__
                    ):
                        logger.debug(
                            "tsec match for user %s",
                            func.__self__.__class__.__name__,
                        )
                        return True

            if chat:
                for info in self._tsec_chat.copy():
                    if info["target"] == chat:
                        if info["rule_type"] == "command" and info["rule"] == cmd:
                            logger.debug("tsec match for %s", cmd)
                            return True

                        if (
                            info["rule_type"] == "module"
                            and info["rule"] == func.__self__.__class__.__name__
                        ):
                            logger.debug(
                                "tsec match for %s",
                                func.__self__.__class__.__name__,
                            )
                            return True

        if f_group_member and message.is_group or f_pm and message.is_private:
            return True

        if message.is_channel:
            if not message.is_group:
                if message.edit_date:
                    return False

                chat_id = utils.get_chat_id(message)
                if (
                    chat_id in self._cache
                    and self._cache[chat_id]["exp"] >= time.time()
                ):
                    chat = self._cache[chat_id]["chat"]
                else:
                    chat = await message.get_chat()
                    self._cache[chat_id] = {"chat": chat, "exp": time.time() + 5 * 60}

                if (
                    not chat.creator
                    and not chat.admin_rights
                    or not chat.creator
                    and not chat.admin_rights.post_messages
                ):
                    return False

                if self._any_admin and f_group_admin_any or f_group_admin:
                    return True
            elif f_group_admin_any or f_group_owner:
                chat_id = utils.get_chat_id(message)
                cache_obj = f"{chat_id}/{user_id}"
                if (
                    cache_obj in self._cache
                    and self._cache[cache_obj]["exp"] >= time.time()
                ):
                    participant = self._cache[cache_obj]["user"]
                else:
                    participant = await message.client.get_permissions(
                        message.peer_id,
                        user_id,
                    )
                    self._cache[cache_obj] = {
                        "user": participant,
                        "exp": time.time() + 5 * 60,
                    }

                if (
                    participant.is_creator
                    or participant.is_admin
                    and (
                        self._any_admin
                        and f_group_admin_any
                        or f_group_admin
                        or f_group_admin_add_admins
                        and participant.add_admins
                        or f_group_admin_change_info
                        and participant.change_info
                        or f_group_admin_ban_users
                        and participant.ban_users
                        or f_group_admin_delete_messages
                        and participant.delete_messages
                        or f_group_admin_pin_messages
                        and participant.pin_messages
                        or f_group_admin_invite_users
                        and participant.invite_users
                    )
                ):
                    return True
            return False

        if message.is_group and (f_group_admin_any or f_group_owner):
            chat_id = utils.get_chat_id(message)
            cache_obj = f"{chat_id}/{user_id}"

            if (
                cache_obj in self._cache
                and self._cache[cache_obj]["exp"] >= time.time()
            ):
                participant = self._cache[cache_obj]["user"]
            else:
                full_chat = await message.client(GetFullChatRequest(message.chat_id))
                participants = full_chat.full_chat.participants.participants
                participant = next(
                    (
                        possible_participant
                        for possible_participant in participants
                        if possible_participant.user_id == message.sender_id
                    ),
                    None,
                )
                self._cache[cache_obj] = {
                    "user": participant,
                    "exp": time.time() + 5 * 60,
                }

            if not participant:
                return

            if (
                isinstance(participant, ChatParticipantCreator)
                or isinstance(participant, ChatParticipantAdmin)
                and f_group_admin_any
            ):
                return True

        return False

    _check = check  # Legacy
