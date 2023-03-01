import random
from Hydra.events import register


ran1 = "1234567890"
ran2 = "¥€¢£"
ran3 = "@#$&+?!"
ran4 = "()[]{}"
ran5 = "NOPQRSTUVWXYZ"
ran6 = "Otazuki"
ran7 = "ABCDEFGHIJKLM"
ran8 = "uvwxyz"
ran9 = "ghijklmnopqrst"
ran0 = "abcdef"
ran11 = "mairupunda"

all = ran1 + ran2 + ran3 + ran4 + ran5 + ran6 + ran7 + ran8 + ran9 + ran0 + ran11

length = 11

@register(pattern=("/pass"))
async def awake(event):
   password = "".join(random.sample(all, length))
   await event.reply(password)
   






