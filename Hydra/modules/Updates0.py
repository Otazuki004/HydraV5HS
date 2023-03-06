from Hydra import tbot as tbot
from Hydra.events import register

PHOTO1 = "https://te.legra.ph/file/c4b3a0fb319744a2e41fd.jpg"


@register(pattern=("/updates"))
async def awake(event):
    HYDRA1 = f"""
    * Truth or Dare Feature Added ✅ *
    * Welcome (Spam) Removed ✅ *
    * Welcome Messages Are Changed✅ *
    * Music Feature Coming Soon✅ *
    * Running On New Repo✅ *
    * Almost All Errors Fixed ✅ *
    * UI Changed ✅ *
    * You can Rename Files ✅ *
Powered by: @Toon_LinkZ ™ """
    await tbot.send_file(event.chat_id, PHOTO1, caption=HYDRA1)
