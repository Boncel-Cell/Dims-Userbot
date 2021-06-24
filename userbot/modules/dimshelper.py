""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Anak Kntll {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/dims_whydi)"
        "\n[Repo](https://github.com/Boncel-Cell/kontoll)"
        "\n[Instagram](Instagram.com/Dimswhydi_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Zora24/Lord-Userbot/Lord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "dimshelper":
    "`.dimshelp`\
\nPenjelasan: Bantuan Untuk Dims-Userbot.\
\n`.dimsvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
