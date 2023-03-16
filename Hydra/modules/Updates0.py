from Hydra import tbot as tbot
from Hydra.events import register

PHOTO1 = "https://te.legra.ph/file/c4b3a0fb319744a2e41fd.jpg"


@register(pattern=("/updates"))
async def awake(event):
    HYDRA1 = f"""
**Hydra V-6 Started 💖🔥

Features ⁉️

- Vplay
- Telegram Files Play
- New UI
- Running On 4 instance
- Supet Fast ⚡
- Welcome MessageS Updated
- Paste Error Fix
- Renamer

Powered by: @Toon_LinkZ💖
Support: @FutureCity005❤️**"""
    await tbot.send_file(event.chat_id, PHOTO1, caption=HYDRA1)
