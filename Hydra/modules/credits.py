from telethon import Button

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/447ec551360a04632d5b9.jpg"


@register(pattern=("/credits"))
async def awake(event):
    HYDRA = """
    Credits
BOT OWNER : [OTAZUKI](https://telegram.dog/OTAZUKI_004)
REPO OWNER : [𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪](https://telegram.dog/Toon_LinkZ)
HELPER : [🖤「 GT ASH™ 」🖤](https://telegram.dog/Awesome_GtashXD)
SUPPORTER : [𝗧𝗢𝗙𝗨 鬼](https://telegram.dog/Awesome_Tofu)


• SUPPORT : [Here](https://telegram.dog/FutureCity005)
• UPDATES : [Here](https://telegram.dog/Updates004)
---------------------------------------------------------
**DEV LIST**

DEV 1 - @OTAZUKI_004 & @Toon_LinkZ *Owner
DEV 2 - @Awesome_GtashXD *Some module he maked
DEV 3 - @NandhaXD *He solved Many errors 
DEV 4 - @Awesome_Tofu *helped On V-5 Music player
----------------------------------------------------------
I Hope Hydra Users Have Humanity. 
Thanks For Using! 

𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪 ™
"""

    BUTTON = [
        [
            Button.url("۞ 𝙁𝙪𝙩𝙪𝙧𝙚 𝘾𝙞𝙩𝙮 ۞", "https://telegram.dog/FutureCity005"),
            Button.url(" 𓆩𝗧ᴏᴏɴ 𝗟ɪɴᴋᴢ𓆪 ", "https://telegram.dog/Toon_LinkZ"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA, buttons=BUTTON)
#V-5

__help__ = """
**Users Only**
/credits - Know Hydra Devlopers And Helpers
"""

__mod_name__ = "Credits"