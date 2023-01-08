# meta developer: @bampiss
import random
import logging
from .. import loader, utils
from random import randint, choice
from asyncio import sleep

logger = logging.getLogger(__name__)


def register(cb):
    cb(ModChannels())


class ModChannels(loader.Module):
    """Показывает список каналов с модулями для юзер бота)"""
    strings = {'name': 'ModChannels'}

    async def modchcmd(self, message):
        """Показать список каналов"""

        modch = ("<emoji document_id=5370869711888194012>👾</emoji>Все каналы с модулями для юзер бота<emoji document_id=5357107687484038897>🫶</emoji>\n\n<emoji document_id=5469741319330996757>💫</emoji> @modwini\n<emoji document_id=5472164874886846699>✨</emoji> @hikarimods\n<emoji document_id=5431895003821513760>❄️</emoji> @morisummermods\n<emoji document_id=5188452705546281155>🌖</emoji> @cakestwix_mods\n<emoji document_id=5471950641918121951>☃️</emoji> @nalinormods\n<emoji document_id=5445284980978621387>🚀</emoji> @AstroModules\n<emoji document_id=5472146462362048818>💡</emoji> @vsecoder_m\n<emoji document_id=5436040291507247633>🎉</emoji> @mm_mods\n<emoji document_id=5283020991981693429>🐶</emoji> @apodiktum_modules\n<emoji document_id=5370856741086960948>😈</emoji> @shadow_modules\n<emoji document_id=5373026167722876724>🤩</emoji> @wilsonmods\n<emoji document_id=5370610867094166617>🎃</emoji> @amoremods\n<emoji document_id=5467406098367521267>😀</emoji> @DorotoroMods\n<emoji document_id=5472404692975753822>✊</emoji> @HikkaFTGmods\n<emoji document_id=5449857802593901902>🎄</emoji> @Userbotik")

        await message.edit(modch)
