from .. import loader, utils, translations
from telethon.tl.types import Message
import logging

logger = logging.getLogger(__name__)


@loader.tds
class Translations(loader.Module):
    """Processes internal translations"""

    strings = {
        "name": "Translations",
        "lang_saved": "{} <b>Language saved!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Translate pack"
            " saved!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Incorrect language"
            " specified</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Translations reset"
            " to default ones</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Invalid pack format"
            " in url</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>You need to specify"
            " valid url containing a langpack</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>Command output seems"
            " to be too long, so it's sent in file.</b>"
        ),
        "opening_form": " <b>Opening form...</b>",
        "opening_gallery": " <b>Opening gallery...</b>",
        "opening_list": " <b>Opening list...</b>",
        "inline403": "π« <b>You can't send inline units in this chat</b>",
        "invoke_failed": "<b>π« Unit invoke failed! More info in logs</b>",
        "show_inline_cmds": "π Show all available inline commands",
        "no_inline_cmds": "You have no available commands",
        "no_inline_cmds_msg": (
            "<b>πΎTo use commands you need to make Bampi</b>"
        ),
        "inline_cmds": "βΉοΈ You have {} available command(-s)",
        "inline_cmds_msg": "<b>βΉοΈ Available inline commands:</b>\n\n{}",
        "run_command": "ποΈ Run command",
        "command_msg": "<b>π Command Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π Command Β«{}Β»",
        "button403": "You are not allowed to press this button!",
        "keep_id": "β οΈ Do not remove ID! {}",
    }

    strings_ru = {
        "lang_saved": "{} <b>Π―Π·ΡΠΊ ΡΠΎΡΡΠ°Π½ΡΠ½!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΠΠ°ΠΊΠ΅Ρ ΠΏΠ΅ΡΠ΅Π²ΠΎΠ΄ΠΎΠ²"
            " ΡΠΎΡΡΠ°Π½ΡΠ½!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Π£ΠΊΠ°Π·Π°Π½ Π½Π΅Π²Π΅ΡΠ½ΡΠΉ"
            " ΡΠ·ΡΠΊ</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΠΠ΅ΡΠ΅Π²ΠΎΠ΄Ρ ΡΠ±ΡΠΎΡΠ΅Π½Ρ"
            " Π½Π° ΡΡΠ°Π½Π΄Π°ΡΡΠ½ΡΠ΅</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΠΠ΅Π²Π΅ΡΠ½ΡΠΉ ΡΠΎΡΠΌΠ°Ρ"
            " ΠΏΠ°ΠΊΠ΅ΡΠ° ΠΏΠ΅ΡΠ΅Π²ΠΎΠ΄ΠΎΠ² Π² ΡΡΡΠ»ΠΊΠ΅</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΠΡ Π΄ΠΎΠ»ΠΆΠ½Ρ ΡΠΊΠ°Π·Π°ΡΡ"
            " ΡΡΡΠ»ΠΊΡ, ΡΠΎΠ΄Π΅ΡΠΆΠ°ΡΡΡ ΠΏΠ°ΠΊΠ΅Ρ ΠΏΠ΅ΡΠ΅Π²ΠΎΠ΄ΠΎΠ²</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>ΠΡΠ²ΠΎΠ΄ ΠΊΠΎΠΌΠ°Π½Π΄Ρ ΡΠ»ΠΈΡΠΊΠΎΠΌ"
            " Π΄Π»ΠΈΠ½Π½ΡΠΉ, ΠΏΠΎΡΡΠΎΠΌΡ ΠΎΠ½ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ Π² ΡΠ°ΠΉΠ»Π΅.</b>"
        ),
        "opening_form": " <b>ΠΡΠΊΡΡΠ²Π°Ρ ΡΠΎΡΠΌΡ...</b>",
        "opening_gallery": " <b>ΠΡΠΊΡΡΠ²Π°Ρ Π³Π°Π»Π΅ΡΠ΅Ρ...</b>",
        "opening_list": " <b>ΠΡΠΊΡΡΠ²Π°Ρ ΡΠΏΠΈΡΠΎΠΊ...</b>",
        "inline403": "π« <b>ΠΡ Π½Π΅ ΠΌΠΎΠΆΠ΅ΡΠ΅ ΠΎΡΠΏΡΠ°Π²Π»ΡΡΡ Π²ΡΡΡΠΎΠ΅Π½Π½ΡΠ΅ ΡΠ»Π΅ΠΌΠ΅Π½ΡΡ Π² ΡΡΠΎΠΌ ΡΠ°ΡΠ΅</b>",
        "invoke_failed": "<b>π« ΠΡΠ·ΠΎΠ² ΠΌΠΎΠ΄ΡΠ»Ρ Π½Π΅ ΡΠ΄Π°Π»ΡΡ! ΠΠΎΠ΄ΡΠΎΠ±Π½Π΅Π΅ Π² Π»ΠΎΠ³Π°Ρ</b>",
        "show_inline_cmds": "π ΠΠΎΠΊΠ°Π·Π°ΡΡ Π²ΡΠ΅ Π΄ΠΎΡΡΡΠΏΠ½ΡΠ΅ Π²ΡΡΡΠΎΠ΅Π½Π½ΡΠ΅ ΠΊΠΎΠΌΠ°Π½Π΄Ρ",
        "no_inline_cmds": "Π£ Π²Π°Ρ Π½Π΅Ρ Π΄ΠΎΡΡΡΠΏΠ½ΡΡ inline ΠΊΠΎΠΌΠ°Π½Π΄",
        "no_inline_cmds_msg": (
            "<b>πΎΠ§ΡΠΎΠ±Ρ ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΡ ΠΊΠΎΠΌΠ°Π½Π΄Ρ Π²Π°ΠΌ Π½Π°Π΄ΠΎ ΡΠ΄Π΅Π»Π°ΡΡ Bampi</b>"
        ),
        "inline_cmds": "βΉοΈ Π£ Π²Π°Ρ {} Π΄ΠΎΡΡΡΠΏΠ½Π°Ρ(-ΡΡ) ΠΊΠΎΠΌΠ°Π½Π΄Π°(-Ρ)",
        "inline_cmds_msg": "<b>βΉοΈ ΠΠΎΡΡΡΠΏΠ½ΡΠ΅ inline ΠΊΠΎΠΌΠ°Π½Π΄Ρ:</b>\n\n{}",
        "run_command": "ποΈ ΠΡΠΏΠΎΠ»Π½ΠΈΡΡ ΠΊΠΎΠΌΠ°Π½Π΄Ρ",
        "command_msg": "<b>π ΠΠΎΠΌΠ°Π½Π΄Π° Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π ΠΠΎΠΌΠ°Π½Π΄Π° Β«{}Β»",
        "button403": "ΠΡ Π½Π΅ ΠΌΠΎΠΆΠ΅ΡΠ΅ Π½Π°ΠΆΠ°ΡΡ Π½Π° ΡΡΡ ΠΊΠ½ΠΎΠΏΠΊΡ!",
        "keep_id": "β οΈ ΠΠ΅ ΡΠ΄Π°Π»ΡΠΉΡΠ΅ ID! {}",
    }

    strings_ua = {
        "lang_saved": "{} <b>ΠΠΎΠ²Π° Π·Π±Π΅ΡΠ΅ΠΆΠ΅Π½Π°!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΠΠ°ΠΊΠ΅Ρ ΠΏΠ΅ΡΠ΅ΠΊΠ»Π°Π΄ΡΠ²"
            " Π·Π±Π΅ΡΠ΅ΠΆΠ΅Π½!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΠΠΊΠ°Π·Π°Π½ΠΎ Π½Π΅Π²ΡΡΠ½Ρ"
            " ΠΌΠΎΠ²Ρ</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΠΠ΅ΡΠ΅ΠΊΠ»Π°Π΄ΠΈ ΡΠΊΠΈΠ½ΡΡΠΎ"
            " Π½Π° ΡΡΠ°Π½Π΄Π°ΡΡΠ½Ρ</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΠΠ΅Π²ΡΡΠ½ΠΈΠΉ ΡΠΎΡΠΌΠ°Ρ"
            " ΠΏΠ°ΠΊΠ΅ΡΡ ΠΏΠ΅ΡΠ΅ΠΊΠ»Π°Π΄ΡΠ² Π½Π° Π·Π°ΡΠ»Π°Π½Π½Ρ</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΠΠΈ ΠΏΠΎΠ²ΠΈΠ½Π½Ρ Π²ΠΊΠ°Π·Π°ΡΠΈ"
            " ΠΏΠΎΡΠΈΠ»Π°Π½Π½Ρ, ΡΠΎ ΠΌΡΡΡΠΈΡΡ ΠΏΠ°ΠΊΠ΅Ρ ΠΏΠ΅ΡΠ΅ΠΊΠ»Π°Π΄ΡΠ²</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>ΠΠΈΠ²Π΅Π΄Π΅Π½Π½Ρ ΠΊΠΎΠΌΠ°Π½Π΄ΠΈ Π·Π°Π½Π°Π΄ΡΠΎ"
            " Π΄ΠΎΠ²Π³ΠΈΠΉ, ΡΠΎΠΌΡ Π²ΡΠ½ Π²ΡΠ΄ΠΏΡΠ°Π²Π»Π΅Π½ΠΈΠΉ Ρ ΡΠ°ΠΉΠ»Ρ.</b>"
        ),
        "opening_form": " <b>ΠΡΠ΄ΠΊΡΠΈΠ²Π°Ρ ΡΠΎΡΠΌΡ...</b>",
        "opening_gallery": " <b>ΠΡΠ΄ΠΊΡΠΈΠ²Π°Ρ Π³Π°Π»Π΅ΡΠ΅Ρ...</b>",
        "opening_list": " <b>ΠΡΠ΄ΠΊΡΠΈΠ²Π°Ρ ΡΠΏΠΈΡΠΎΠΊ...</b>",
        "inline403": "π« <b>ΠΠΈ Π½Π΅ ΠΌΠΎΠΆΠ΅ΡΠ΅ Π½Π°Π΄ΡΠΈΠ»Π°ΡΠΈ Π²Π±ΡΠ΄ΠΎΠ²Π°Π½Ρ Π΅Π»Π΅ΠΌΠ΅Π½ΡΠΈ Π² ΡΡΠΎΠΌΡ ΡΠ°ΡΡ</b>",
        "invoke_failed": "<b>π« ΠΠΈΠΊΠ»ΠΈΠΊ ΠΌΠΎΠ΄ΡΠ»Ρ Π½Π΅ Π²Π΄Π°Π²ΡΡ! ΠΠ΅ΡΠ°Π»ΡΠ½ΡΡΠ΅ Ρ Π»ΠΎΠ³Π°Ρ</b>",
        "show_inline_cmds": "π ΠΠΎΠΊΠ°Π·Π°ΡΠΈ Π²ΡΡ Π΄ΠΎΡΡΡΠΏΠ½Ρ Π²Π±ΡΠ΄ΠΎΠ²Π°Π½Ρ ΠΊΠΎΠΌΠ°Π½Π΄ΠΈ",
        "no_inline_cmds": "Π£ Π²Π°Ρ Π½Π΅ΠΌΠ°Ρ Π΄ΠΎΡΡΡΠΏΠ½ΠΈΡ inline ΠΊΠΎΠΌΠ°Π½Π΄",
        "no_inline_cmds_msg": (
           "<b>πΎΠ©ΠΎΠ± Π²ΠΈΠΊΠΎΡΠΈΡΡΠΎΠ²ΡΠ²Π°ΡΠΈ ΠΊΠΎΠΌΠ°Π½Π΄ΠΈ, Π²Π°ΠΌ ΡΡΠ΅Π±Π° Π·ΡΠΎΠ±ΠΈΡΠΈ Bampi</b>"
        ),
        "inline_cmds": "βΉοΈ Π£ Π²Π°Ρ {} Π΄ΠΎΡΡΡΠΏΠ½Π°(-ΠΈΡ) ΠΊΠΎΠΌΠ°Π½Π΄Π°(-ΠΈ)",
        "inline_cmds_msg": "<b>βΉοΈ ΠΠΎΡΡΡΠΏΠ½Ρ inline ΠΊΠΎΠΌΠ°Π½Π΄ΠΈ:</b>\n\n{}",
        "run_command": "ποΈ ΠΠΈΠΊΠΎΠ½Π°ΡΠΈ ΠΊΠΎΠΌΠ°Π½Π΄Ρ",
        "command_msg": "<b>π ΠΠΎΠΌΠ°Π½Π΄Π° Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π ΠΠΎΠΌΠ°Π½Π΄Π° Β«{}Β»",
        "button403": "ΠΠΈ Π½Π΅ ΠΌΠΎΠΆΠ΅ΡΠ΅ Π½Π°ΡΠΈΡΠ½ΡΡΠΈ Π½Π° ΡΡ ΠΊΠ½ΠΎΠΏΠΊΡ!",
        "keep_id": "β οΈ ΠΠ΅ Π²ΠΈΠ΄Π°Π»ΡΠΉΡΠ΅ ID! {}",
    }

    strings_de = {
        "lang_saved": "{} <b>Sprache gespeichert!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Γbersetzungs"
            " Paket gespeichert!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Falsche Sprache"
            " angegeben</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Γbersetzungen"
            " auf Standard zurΓΌckgesetzt</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>UngΓΌltiges"
            " Γbersetzungs Paket in der URL</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Sie mΓΌssen eine"
            " gΓΌltige URL angeben, die ein Γbersetzungs Paket enthΓ€lt</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>Befehlsausgabe scheint"
            " zu lang zu sein, daher wird sie in einer Datei gesendet.</b>"
        ),
        "opening_form": " <b>Formular wird geΓΆffnet...</b>",
        "opening_gallery": " <b>Galerie wird geΓΆffnet...</b>",
        "opening_list": " <b>Liste wird geΓΆffnet...</b>",
        "inline403": "π« <b>Sie kΓΆnnen Inline-Einheiten in diesem Chat nicht senden</b>",
        "invoke_failed": (
            "<b>π« Modulaufruf fehlgeschlagen! Weitere Informationen in den"
            " Protokollen</b>"
        ),
        "show_inline_cmds": "π Zeige alle verfΓΌgbaren Inline-Befehle",
        "no_inline_cmds": "Sie haben keine verfΓΌgbaren Inline-Befehle",
        "no_inline_cmds_msg": (
            "<b>π Keine verfΓΌgbaren Inline-Befehle oder Sie haben keinen Zugriff"
            " auf sie</b>"
        ),
        "inline_cmds": "βΉοΈ Sie haben {} verfΓΌgbare(n) Befehl(e)",
        "inline_cmds_msg": "<b>βΉοΈ VerfΓΌgbare Inline-Befehle:</b>\n\n{}",
        "run_command": "ποΈ Befehl ausfΓΌhren",
        "command_msg": "<b>π Befehl Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π Befehl Β«{}Β»",
        "button403": "Sie kΓΆnnen auf diese SchaltflΓ€che nicht klicken!",
        "keep_id": "β οΈ LΓΆschen sie das ID nicht! {}",
    }

    strings_tr = {
        "lang_saved": "{} <b>Dil kaydedildi!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Γeviri paketi"
            " kaydedildi!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>YanlΔ±Ε dil"
            " belirtildi</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Γeviriler varsayΔ±lan"
            " hale getirildi</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>URL'deki Γ§eviri"
            " paketi geΓ§ersiz</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>GeΓ§erli bir URL"
            " belirtmelisiniz</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>Komut Γ§Δ±ktΔ±sΔ± Γ§ok uzun"
            " gΓΆrΓΌnΓΌyor, bu yΓΌzden dosya olarak gΓΆnderildi.</b>"
        ),
        "opening_form": " <b>Form aΓ§Δ±lΔ±yor...</b>",
        "opening_gallery": " <b>Galeri aΓ§Δ±lΔ±yor...</b>",
        "opening_list": " <b>Liste aΓ§Δ±lΔ±yor...</b>",
        "inline403": "π« <b>Bu sohbete satΔ±r iΓ§i birimler gΓΆnderemezsin</b>",
        "invoke_failed": (
            "<b>π« ModΓΌl Γ§aΔrΔ±sΔ± baΕarΔ±sΔ±z! KayΔ±tlardan daha fazla bilgiye"
            " eriΕebilirsin</b>"
        ),
        "show_inline_cmds": "π TΓΌm kullanΔ±labilir inline komutlarΔ±nΔ± gΓΆster",
        "no_inline_cmds": "KullanΔ±labilir inline komutunuz yok",
        "no_inline_cmds_msg": (
            "<b>π KullanΔ±labilir inline komutunuz yok veya eriΕiminiz yok</b>"
        ),
        "inline_cmds": "βΉοΈ {} kullanΔ±labilir komutunuz var",
        "inline_cmds_msg": "<b>βΉοΈ KullanΔ±labilir inline komutlar:</b>\n\n{}",
        "run_command": "ποΈ Komutu Γ§alΔ±ΕtΔ±r",
        "command_msg": "<b>π Komut Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π Komut Β«{}Β»",
        "button403": "Bu dΓΌΔmeye basamazsΔ±nΔ±z!",
        "keep_id": "β οΈ ID'yi silmeyin! {}",
    }

    strings_uz = {
        "lang_saved": "{} <b>Til saqlandi!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Tarjima paketi"
            " saqlandi!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Noto'g'ri til"
            " belgilandi</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Tarjimalar"
            " standart holatga qaytarildi</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>URL'dagi tarjima"
            " paketi noto'g'ri</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Siz noto'g'ri URL"
            " belirtdingiz</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>Bajarilgan buyruq"
            " natijasi juda uzun, shuning uchun fayl sifatida yuborildi.</b>"
        ),
        "opening_form": " <b>Formani ochish...</b>",
        "opening_gallery": " <b>Galeriyani ochish...</b>",
        "opening_list": " <b>Ro'yxatni ochish...</b>",
        "inline403": (
            "π« <b>Siz bu guruhda inline obyektlarni yuborishingiz mumkin emas</b>"
        ),
        "invoke_failed": (
            "<b>π« Modulni chaqirish muvaffaqiyatsiz! Batafsil ma'lumotlar"
            " jurnallarda</b>"
        ),
        "show_inline_cmds": "π Barcha mavjud inline buyruqlarini ko'rsatish",
        "no_inline_cmds": "Sizda mavjud inline buyruqlar yo'q",
        "no_inline_cmds_msg": (
            "<b>π Sizda mavjud inline buyruqlar yo'q yoki ularga kirish huquqingiz"
            " yo'q</b>"
        ),
        "inline_cmds": "βΉοΈ Sizda {} mavjud buyruq bor",
        "inline_cmds_msg": "<b>βΉοΈ Mavjud inline buyruqlar:</b>\n\n{}",
        "run_command": "ποΈ Buyruqni bajarish",
        "command_msg": "<b>π Buyruq Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π Buyruq Β«{}Β»",
        "button403": "Siz ushbu tugmani bosib bo'lmaysiz!",
        "keep_id": "β οΈ ID-ni o'chirmang! {}",
    }

    strings_hi = {
        "lang_saved": "{} <b>ΰ€­ΰ€Ύΰ€·ΰ€Ύ ΰ€Έΰ€Ήΰ₯ΰ€ΰ€Ύ ΰ€ΰ€―ΰ€Ύ!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΰ€ΰ€¨ΰ₯ΰ€΅ΰ€Ύΰ€¦ ΰ€ͺΰ₯ΰ€"
            " ΰ€Έΰ€Ήΰ₯ΰ€ΰ€Ύ ΰ€ΰ€―ΰ€Ύ!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΰ€ΰ€²ΰ€€ ΰ€­ΰ€Ύΰ€·ΰ€Ύ"
            " ΰ€¨ΰ€Ώΰ€°ΰ₯ΰ€¦ΰ€Ώΰ€·ΰ₯ΰ€ ΰ€ΰ€Ώΰ€―ΰ€Ύ ΰ€ΰ€―ΰ€Ύ</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΰ€ΰ€¨ΰ₯ΰ€΅ΰ€Ύΰ€¦ ΰ€‘ΰ€Ώΰ€«ΰ€Όΰ₯ΰ€²ΰ₯ΰ€"
            " ΰ€ͺΰ€° ΰ€°ΰ₯ΰ€Έΰ₯ΰ€ ΰ€ΰ€Ώΰ€ ΰ€ΰ€</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΰ€―ΰ₯ΰ€ΰ€°ΰ€ΰ€² ΰ€?ΰ₯ΰ€ ΰ€ΰ€²ΰ€€"
            " ΰ€ΰ€¨ΰ₯ΰ€΅ΰ€Ύΰ€¦ ΰ€ͺΰ₯ΰ€ ΰ€¨ΰ€Ώΰ€°ΰ₯ΰ€¦ΰ€Ώΰ€·ΰ₯ΰ€ ΰ€ΰ€Ώΰ€―ΰ€Ύ ΰ€ΰ€―ΰ€Ύ</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΰ€ΰ€ͺΰ€¨ΰ₯ ΰ€ΰ€²ΰ€€ ΰ€―ΰ₯ΰ€ΰ€°ΰ€ΰ€²"
            " ΰ€¨ΰ€Ώΰ€°ΰ₯ΰ€¦ΰ€Ώΰ€·ΰ₯ΰ€ ΰ€ΰ€Ώΰ€―ΰ€Ύ ΰ€Ήΰ₯</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€ΰ€ΰ€ΰ€ͺΰ₯ΰ€ ΰ€¬ΰ€Ήΰ₯ΰ€€ ΰ€²ΰ€ΰ€¬ΰ€Ύ"
            " ΰ€²ΰ€ΰ€€ΰ€Ύ ΰ€Ήΰ₯, ΰ€ΰ€Έΰ€²ΰ€Ώΰ€ ΰ€«ΰ€Όΰ€Ύΰ€ΰ€² ΰ€?ΰ₯ΰ€ ΰ€­ΰ₯ΰ€ΰ€Ύ ΰ€ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯.</b>"
        ),
        "opening_form": " <b>ΰ€«ΰ₯ΰ€°ΰ₯ΰ€? ΰ€ΰ₯ΰ€² ΰ€°ΰ€Ήΰ€Ύ ΰ€Ήΰ₯...</b>",
        "opening_gallery": " <b>ΰ€ΰ₯ΰ€²ΰ€°ΰ₯ ΰ€ΰ₯ΰ€² ΰ€°ΰ€Ήΰ€Ύ ΰ€Ήΰ₯...</b>",
        "opening_list": " <b>ΰ€Έΰ₯ΰ€ΰ₯ ΰ€ΰ₯ΰ€² ΰ€°ΰ€Ήΰ€Ύ ΰ€Ήΰ₯...</b>",
        "inline403": "π« <b>ΰ€ΰ€ͺ ΰ€ΰ€Έ ΰ€ΰ₯ΰ€°ΰ₯ΰ€ͺ ΰ€?ΰ₯ΰ€ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€ΰ€ΰ€? ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€­ΰ₯ΰ€ ΰ€Έΰ€ΰ€€ΰ₯ ΰ€Ήΰ₯ΰ€</b>",
        "invoke_failed": "<b>π« ΰ€?ΰ₯ΰ€‘ΰ₯ΰ€―ΰ₯ΰ€² ΰ€ΰ€¨ΰ₯ΰ€΅ΰ₯ΰ€ ΰ€΅ΰ€Ώΰ€«ΰ€²! ΰ€΅ΰ€Ώΰ€Έΰ₯ΰ€€ΰ₯ΰ€€ ΰ€ΰ€Ύΰ€¨ΰ€ΰ€Ύΰ€°ΰ₯ ΰ€²ΰ₯ΰ€ ΰ€?ΰ₯ΰ€ ΰ€Ήΰ₯</b>",
        "show_inline_cmds": "π ΰ€Έΰ€­ΰ₯ ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€¦ΰ€Ώΰ€ΰ€Ύΰ€ΰ€",
        "no_inline_cmds": "ΰ€ΰ€ͺΰ€ΰ₯ ΰ€ͺΰ€Ύΰ€Έ ΰ€ΰ₯ΰ€ ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€Ήΰ₯ΰ€",
        "no_inline_cmds_msg": (
            "<b>π ΰ€ΰ€ͺΰ€ΰ₯ ΰ€ͺΰ€Ύΰ€Έ ΰ€ΰ₯ΰ€ ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€―ΰ€Ύ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€ΰ₯ ΰ€²ΰ€Ώΰ€ ΰ€ΰ€¨ΰ₯ΰ€?ΰ€€ΰ€Ώ ΰ€¨ΰ€Ήΰ₯ΰ€"
            " ΰ€Ήΰ₯ΰ€</b>"
        ),
        "inline_cmds": "βΉοΈ ΰ€ΰ€ͺΰ€ΰ₯ ΰ€ͺΰ€Ύΰ€Έ {} ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€Ήΰ₯ΰ€",
        "inline_cmds_msg": "<b>βΉοΈ ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€ΰ€¨ΰ€²ΰ€Ύΰ€ΰ€¨ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘:</b>\n\n{}",
        "run_command": "ποΈ ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ ΰ€ΰ€²ΰ€Ύΰ€ΰ€",
        "command_msg": "<b>π ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ Β«{}Β»</b>\n\n<i>{}</i>",
        "command": "π ΰ€ΰ€?ΰ€Ύΰ€ΰ€‘ Β«{}Β»",
        "button403": "ΰ€ΰ€ͺ ΰ€ΰ€Έ ΰ€¬ΰ€ΰ€¨ ΰ€ΰ₯ ΰ€¦ΰ€¬ΰ€Ύ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€Έΰ€ΰ€€ΰ₯!",
        "button404": "ΰ€―ΰ€Ή ΰ€¬ΰ€ΰ€¨ ΰ€ΰ€¬ ΰ€ΰ€ͺΰ€²ΰ€¬ΰ₯ΰ€§ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€Ήΰ₯!",
    }

    strings_ja = {
        "lang_saved": "{} <b>θ¨θͺγδΏε­γγγΎγγοΌ</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ηΏ»θ¨³γγγ― γδΏε­γγγΎγγοΌ</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>δΈζ­£η’Ίγͺθ¨θͺ γζε?γγγΎγγ</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ηΏ»θ¨³γγγγ©γ«γγ«"
            " γͺγ»γγγγγΎγγ</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>URLγ?ηΏ»θ¨³γγγ―γ δΈζ­£η’Ίγ§γ</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>δΈζ­£η’ΊγͺURLγζε?γγΎγγ</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>γ³γγ³γγ?εΊεγ"
            " ι·γγγγγγγγ‘γ€γ«γ¨γγ¦ιδΏ‘γγγΎγγ.</b>"
        ),
        "opening_form": " <b>γγ©γΌγ γιγγ¦γγΎγ...</b>",
        "opening_gallery": " <b>γ?γ£γ©γͺγΌγιγγ¦γγΎγ...</b>",
        "opening_list": " <b>γͺγΉγγιγγ¦γγΎγ...</b>",
        "inline403": "π« <b>γγͺγγ―γγ?γ°γ«γΌγγ§γ€γ³γ©γ€γ³γ’γ€γγ γιδΏ‘γγγγ¨γ―γ§γγΎγγ</b>",
        "invoke_failed": "<b>π« γ’γΈγ₯γΌγ«γ?εΌγ³εΊγγε€±ζγγΎγγοΌ θ©³η΄°γ―γ­γ°γ«θ¨ι²γγγ¦γγΎγ</b>",
        "show_inline_cmds": "π γγΉγ¦γ?ε©η¨ε―θ½γͺγ€γ³γ©γ€γ³γ³γγ³γγθ‘¨η€Ί",
        "no_inline_cmds": "ε©η¨ε―θ½γͺγ€γ³γ©γ€γ³γ³γγ³γγ―γγγΎγγ",
        "no_inline_cmds_msg": "<b>π ε©η¨ε―θ½γͺγ€γ³γ©γ€γ³γ³γγ³γγΎγγ―γ€γ³γ©γ€γ³γ³γγ³γγΈγ?γ’γ―γ»γΉζ¨©γγγγΎγγ</b>",
        "inline_cmds": "βΉοΈ ε©η¨ε―θ½γͺγ³γγ³γγ {} γγγΎγ",
        "inline_cmds_msg": "<b>βΉοΈ ε©η¨ε―θ½γͺγ€γ³γ©γ€γ³γ³γγ³γ:</b>\n\n{}",
        "run_command": "ποΈ γ³γγ³γγε?θ‘",
        "command_msg": "<b>π γ³γγ³γγ{}γ</b>\n\n<i>{}</i>",
        "command": "π γ³γγ³γγ{}γ",
        "button403": "γγͺγγ―γγ?γγΏγ³γζΌγγγ¨γ―γ§γγΎγγοΌ",
        "button404": "γγ?γγΏγ³γ―γγε©η¨γ§γγΎγγοΌ",
    }

    strings_kr = {
        "lang_saved": "{} <b>μΈμ΄κ° μ μ₯λμμ΅λλ€!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>λ²μ­ ν©μ΄ μ μ₯λμμ΅λλ€!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>μλͺ»λ μΈμ΄κ° μ§μ λμμ΅λλ€</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>λ²μ­μ΄ κΈ°λ³Έκ°μΌλ‘ μ¬μ€μ λμμ΅λλ€</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>URLμ λ²μ­ ν©μ΄ μλͺ»λμμ΅λλ€</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>μλͺ»λ URLμ μ§μ νμ¨μ΅λλ€</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>λͺλ Ήμ μΆλ ₯μ΄"
            " λλ¬΄ κΉλλ€. νμΌλ‘ μ μ‘λμμ΅λλ€.</b>"
        ),
        "opening_form": " <b>νΌμ μ΄κ³  μμ΅λλ€...</b>",
        "opening_gallery": " <b>κ°€λ¬λ¦¬λ₯Ό μ΄κ³  μμ΅λλ€...</b>",
        "opening_list": " <b>λ¦¬μ€νΈλ₯Ό μ΄κ³  μμ΅λλ€...</b>",
        "inline403": "π« <b>μ΄ κ·Έλ£Ήμμ μΈλΌμΈ μμ΄νμ λ³΄λ΄λ κ²μ νμ©λμ§ μμ΅λλ€</b>",
        "invoke_failed": "<b>π« λͺ¨λ νΈμΆμ΄ μ€ν¨νμ΅λλ€! μμΈν λ΄μ©μ λ‘κ·Έμ κΈ°λ‘λμ΄ μμ΅λλ€</b>",
        "show_inline_cmds": "π λͺ¨λ  μ¬μ© κ°λ₯ν μΈλΌμΈ λͺλ Ήμ νμ",
        "no_inline_cmds": "μ¬μ© κ°λ₯ν μΈλΌμΈ λͺλ Ήμ΄ μμ΅λλ€",
        "no_inline_cmds_msg": "<b>π μ¬μ© κ°λ₯ν μΈλΌμΈ λͺλ Ήμ΄ μκ±°λ μΈλΌμΈ λͺλ Ήμ λν μ‘μΈμ€ κΆνμ΄ μμ΅λλ€</b>",
        "inline_cmds": "βΉοΈ μ¬μ© κ°λ₯ν λͺλ Ήμ΄ {} κ° μμ΅λλ€",
        "inline_cmds_msg": "<b>βΉοΈ μ¬μ© κ°λ₯ν μΈλΌμΈ λͺλ Ή:</b>\n\n{}",
        "run_command": "ποΈ λͺλ Ήμ μ€ν",
        "command_msg": "<b>π λͺλ Ή '{}' </b>\n\n<i>{}</i>",
        "command": "π λͺλ Ή '{}'",
        "button403": "μ΄ λ²νΌμ λλ₯Ό μ μμ΅λλ€!",
        "button404": "μ΄ λ²νΌμ λ μ΄μ μ¬μ©ν  μ μμ΅λλ€!",
    }

    strings_ar = {
        "lang_saved": "{} <b>ΨͺΩ Ψ­ΩΨΈ Ψ§ΩΩΨΊΨ©!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΨͺΩ Ψ­ΩΨΈ Ψ­Ψ²ΩΨ©"
            " Ψ§ΩΨͺΨ±Ψ¬ΩΨ©!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΨͺΩ ΨͺΨ­Ψ―ΩΨ― ΩΨΊΨ©"
            " ΨΊΩΨ± Ψ΅Ψ­ΩΨ­Ψ©</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>ΨͺΩ Ψ₯ΨΉΨ§Ψ―Ψ© ΨͺΨΉΩΩΩ"
            " Ψ§ΩΨͺΨ±Ψ¬ΩΨ© Ψ₯ΩΩ Ψ§ΩΨ§ΩΨͺΨ±Ψ§ΨΆΩ</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΨͺΩ ΨͺΨ­Ψ―ΩΨ― Ψ­Ψ²ΩΨ©"
            " Ψ§ΩΨͺΨ±Ψ¬ΩΨ© ΨΊΩΨ± Ψ΅Ψ­ΩΨ­Ψ©</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>ΨͺΩ ΨͺΨ­Ψ―ΩΨ― URL"
            " ΨΊΩΨ± Ψ΅Ψ­ΩΨ­</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>ΨͺΩ ΨͺΨ¬Ψ§ΩΨ² Ψ§ΩΩΨ§ΨͺΨ¬"
            " ΩΩΨ£ΩΨ±. ΨͺΩ Ψ₯Ψ±Ψ³Ψ§ΩΩ ΩΩΩΩ.</b>"
        ),
        "opening_form": " <b>ΩΨͺΩ ΩΨͺΨ­ Ψ§ΩΩΩΩΨ°Ψ¬...</b>",
        "opening_gallery": " <b>ΩΨͺΩ ΩΨͺΨ­ Ψ§ΩΨ΅Ψ§ΩΨ©...</b>",
        "opening_list": " <b>ΩΨͺΩ ΩΨͺΨ­ Ψ§ΩΩΨ§Ψ¦ΩΨ©...</b>",
        "inline403": "π« <b>ΩΨ§ ΩΨ³ΩΨ­ Ψ¨Ψ₯Ψ±Ψ³Ψ§Ω ΨΉΩΨ§Ψ΅Ψ± Ψ§ΩΩΨ§Ψ¬ΩΨ© Ψ§ΩΨ³Ψ·Ψ­ΩΨ© ΩΩ ΩΨ°Ω Ψ§ΩΩΨ¬ΩΩΨΉΨ©</b>",
        "invoke_failed": "<b>π« ΩΨ΄Ω Ψ§Ψ³ΨͺΨ―ΨΉΨ§Ψ‘ Ψ§ΩΩΨ­Ψ―Ψ©! Ψ§ΩΨΈΨ± Ψ§ΩΨ³Ψ¬Ω ΩΩΨ­Ψ΅ΩΩ ΨΉΩΩ ΨͺΩΨ§Ψ΅ΩΩ</b>",
        "show_inline_cmds": "π ΨΉΨ±ΨΆ Ψ¬ΩΩΨΉ Ψ§ΩΨ£ΩΨ§ΩΨ± Ψ§ΩΩΨͺΨ§Ψ­Ψ©",
        "no_inline_cmds": "ΩΨ§ ΨͺΩΨ¬Ψ― Ψ£ΩΨ§ΩΨ± ΩΨͺΨ§Ψ­Ψ©",
        "no_inline_cmds_msg": (
            "<b>π ΩΨ§ ΨͺΩΨ¬Ψ― Ψ£ΩΨ§ΩΨ± ΩΨͺΨ§Ψ­Ψ© Ψ£Ω ΩΩΨ³ ΩΨ―ΩΩ Ψ₯Ψ°Ω ΩΩΩΨ΅ΩΩ Ψ₯ΩΩ Ψ§ΩΨ£ΩΨ§ΩΨ±</b>"
        ),
        "inline_cmds": "βΉοΈ {} Ψ£ΩΨ§ΩΨ± ΩΨͺΨ§Ψ­Ψ©",
        "inline_cmds_msg": "<b>βΉοΈ Ψ£ΩΨ§ΩΨ± ΩΨͺΨ§Ψ­Ψ©:</b>\n\n{}",
        "run_command": "ποΈ ΨͺΨ΄ΨΊΩΩ Ψ§ΩΨ£ΩΨ±",
        "command_msg": "<b>π Ψ§ΩΨ£ΩΨ± '{}' </b>\n\n<i>{}</i>",
        "command": "π Ψ§ΩΨ£ΩΨ± '{}'",
        "button403": "ΩΨ§ ΩΩΩΩΩ Ψ§ΩΨΆΨΊΨ· ΨΉΩΩ ΩΨ°Ψ§ Ψ§ΩΨ²Ψ±!",
        "button404": "ΩΨ§ ΩΩΩΩΩ Ψ§ΩΨΆΨΊΨ· ΨΉΩΩ ΩΨ°Ψ§ Ψ§ΩΨ²Ψ± Ψ¨ΨΉΨ― Ψ§ΩΨ’Ω!",
    }

    strings_es = {
        "lang_saved": "{} <b>Β‘Idioma guardado!</b>",
        "pack_saved": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Β‘Paquete de"
            " traducciΓ³n guardado!</b>"
        ),
        "incorrect_language": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Idioma"
            " incorrecto seleccionado</b>"
        ),
        "lang_removed": (
            "<emoji document_id=5368324170671202286>π</emoji> <b>Restablecer la"
            " traducciΓ³n a los valores predeterminados</b>"
        ),
        "check_pack": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>Paquete de"
            " traducciΓ³n seleccionado incorrecto</b>"
        ),
        "check_url": (
            "<emoji document_id=5436162517686557387>π«</emoji> <b>URL incorrecta"
            " seleccionada</b>"
        ),
        "too_long": (
            "<emoji document_id=5433653135799228968>π</emoji> <b>El resultado del"
            " comando excede el lΓ­mite. Enviado como archivo.</b>"
        ),
        "opening_form": " <b>Abriendo formulario...</b>",
        "opening_gallery": " <b>Abriendo galerΓ­a...</b>",
        "opening_list": " <b>Abriendo lista...</b>",
        "inline403": (
            "π« <b>No se permiten elementos de interfaz de usuario en este grupo</b>"
        ),
        "invoke_failed": (
            "<b>π« Β‘Error al invocar la unidad! Consulte el registro"
            " para obtener mΓ‘s detalles</b>"
        ),
        "show_inline_cmds": "π Mostrar todos los comandos disponibles",
        "no_inline_cmds": "No hay comandos disponibles",
        "no_inline_cmds_msg": (
            "<b>π No hay comandos disponibles o no tienes permiso para acceder a"
            " los comandos</b>"
        ),
        "inline_cmds": "βΉοΈ {} comandos disponibles",
        "inline_cmds_msg": "<b>βΉοΈ Comandos disponibles:</b>\n\n{}",
        "run_command": "ποΈ Ejecutar comando",
        "command_msg": "<b>π Comando '{}'</b>\n\n<i>{}</i>",
        "command": "π Comando '{}'",
        "button403": "Β‘No puedes presionar este botΓ³n!",
        "button404": "Β‘No puedes presionar este botΓ³n ahora!",
    }

    @loader.command(
        ru_doc="[ΡΠ·ΡΠΊΠΈ] - ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ ΡΡΠ°Π½Π΄Π°ΡΡΠ½ΡΠΉ ΡΠ·ΡΠΊ",
        de_doc="[Sprachen] - Γndere die Standard-Sprache",
        tr_doc="[Diller] - VarsayΔ±lan dili deΔiΕtir",
        uz_doc="[til] - Standart tili o'zgartirish",
        hi_doc="[ΰ€­ΰ€Ύΰ€·ΰ€Ύΰ€ΰ€] - ΰ€‘ΰ€Ώΰ€«ΰ€Όΰ₯ΰ€²ΰ₯ΰ€ ΰ€­ΰ€Ύΰ€·ΰ€Ύ ΰ€¬ΰ€¦ΰ€²ΰ₯ΰ€",
        ja_doc="[θ¨θͺ] - γγγ©γ«γγ?θ¨θͺγε€ζ΄γγΎγ",
        kr_doc="[μΈμ΄] - κΈ°λ³Έ μΈμ΄λ₯Ό λ³κ²½ν©λλ€",
        ar_doc="[Ψ§ΩΩΨΊΨ§Ψͺ] - ΨͺΨΊΩΩΨ± Ψ§ΩΩΨΊΨ© Ψ§ΩΨ§ΩΨͺΨ±Ψ§ΨΆΩΨ©",
        es_doc="[Idiomas] - Cambiar el idioma predeterminado",
    )
    async def setlang(self, message: Message):
        """[languages in the order of priority] - Change default language"""
        args = utils.get_args_raw(message)
        if not args or any(len(i) != 2 for i in args.split(" ")):
            await utils.answer(message, self.strings("incorrect_language"))
            return

        self._db.set(translations.__name__, "lang", args.lower())
        await self.translator.init()

        for module in self.allmodules.modules:
            try:
                module.config_complete(reload_dynamic_translate=True)
            except Exception as e:
                logger.debug(
                    "Can't complete dynamic translations reload of %s due to %s",
                    module,
                    e,
                )

        lang2country = {"en": "gb", "hi": "in", "ja": "jp", "ar": "sa"}

        await utils.answer(
            message,
            self.strings("lang_saved").format(
                "".join(
                    [
                        utils.get_lang_flag(lang2country.get(lang, lang))
                        for lang in args.lower().split(" ")
                    ]
                )
            ),
        )

    @loader.command(
        ru_doc="[ΡΡΡΠ»ΠΊΠ° Π½Π° ΠΏΠ°ΠΊ | ΠΏΡΡΡΠΎΠ΅ ΡΡΠΎΠ±Ρ ΡΠ΄Π°Π»ΠΈΡΡ] - ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ Π²Π½Π΅ΡΠ½ΠΈΠΉ ΠΏΠ°ΠΊ ΠΏΠ΅ΡΠ΅Π²ΠΎΠ΄Π°",
        de_doc=(
            "[Link zum Paket | leer um zu entfernen] - Γndere das externe Γbersetzungs"
            " Paket"
        ),
        tr_doc=(
            "[Γeviri paketi baΔlantΔ±sΔ± | boΕ bΔ±rakmak varsayΔ±lan hale getirir] - Harici"
            " Γ§eviri paketini deΔiΕtir"
        ),
        uz_doc=(
            "[tarjima paketi havolasini | bo'sh qoldirish standart holatga qaytaradi] -"
            " Tashqi tarjima paketini o'zgartirish"
        ),
        hi_doc="[ΰ€ΰ€¨ΰ₯ΰ€΅ΰ€Ύΰ€¦ ΰ€ͺΰ₯ΰ€ ΰ€ΰ€Ύ ΰ€²ΰ€Ώΰ€ΰ€ | ΰ€ΰ€Ύΰ€²ΰ₯ ΰ€ΰ₯ΰ€‘ΰ€Ό ΰ€¦ΰ₯ΰ€] - ΰ€¬ΰ€Ύΰ€Ήΰ€°ΰ₯ ΰ€ΰ€¨ΰ₯ΰ€΅ΰ€Ύΰ€¦ ΰ€ͺΰ₯ΰ€ ΰ€¬ΰ€¦ΰ€²ΰ₯ΰ€",
        ja_doc="[γγγ±γΌγΈγΈγ?γͺγ³γ― | η©Ίη½γ§ει€] - ε€ι¨ηΏ»θ¨³γγγ±γΌγΈγε€ζ΄γγΎγ",
        kr_doc="[ν¨ν€μ§ λ§ν¬ | λΉμλλ©΄ μ­μ ] - μΈλΆ λ²μ­ ν¨ν€μ§λ₯Ό λ³κ²½ν©λλ€",
        ar_doc="[Ψ±Ψ§Ψ¨Ψ· Ψ§ΩΨ­Ψ²ΩΨ© | Ψ§ΨͺΨ±ΩΩ ΩΨ§Ψ±ΨΊΨ§ ΩΨ­Ψ°ΩΩ] - ΨͺΨΊΩΩΨ± Ψ­Ψ²ΩΨ© Ψ§ΩΨͺΨ±Ψ¬ΩΨ© Ψ§ΩΨ?Ψ§Ψ±Ψ¬ΩΨ©",
        es_doc="[Enlace al paquete | vacΓ­o para eliminar] - Cambiar el paquete de",
    )
    async def dllangpackcmd(self, message: Message):
        """[link to a langpack | empty to remove] - Change Hikka translate pack (external)
        """
        args = utils.get_args_raw(message)

        if not args:
            self._db.set(translations.__name__, "pack", False)
            await self.translator.init()
            await utils.answer(message, self.strings("lang_removed"))
            return

        if not utils.check_url(args):
            await utils.answer(message, self.strings("check_url"))
            return

        self._db.set(translations.__name__, "pack", args)
        success = await self.translator.init()

        for module in self.allmodules.modules:
            try:
                module.config_complete(reload_dynamic_translate=True)
            except Exception as e:
                logger.debug(
                    "Can't complete dynamic translations reload of %s due to %s",
                    module,
                    e,
                )

        await utils.answer(
            message,
            self.strings("pack_saved" if success else "check_pack"),
        )
