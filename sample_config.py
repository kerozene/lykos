# ===================================================
# ===  _       _               This is the config ===
# === | |     | |              file for lykos.    ===
# === | |_   _| | _____  ___   Most of the        ===
# === | | | | | |/ / _ \/ __|  options need no    ===
# === | | |_| |   < (_) \__ \  explanation, but I ===
# === |_|\__, |_|\_\___/|___/  provide it anyway. ===
# ===      __/ |               Happy configging!  ===
# ===     |___/                                   ===
# ===================================================

# The network for lykos to run on.
network    = "irc.freenode.net"  # if you don't know what this is, why are you running an irc bot
port       = 6667
serverpass = ""  # leave blank if none

# The channel for lykos to join.
channels   = "#channel"
opchan     = "#channel-ops"

# Bot information.
nickname   = "lykos"
nickpass   = "password"
username   = "lykos"
cmdchar    = "!"

# Admin Information
owner_host = ("unaffiliated/owner",)  # leave the trailing comma if there is 1 owner
owner_acct = ("owner",)  # this is the owners nickserv account, can be used as an alternate to their cloak.
admin_host = ("unaffiliated/admin1", "unaffiliated/admin2")
admin_acct = ("admin1", "admin2")  # same as owner_a, uses nickserv accounts and only works if idented

# Alternate toggles
ops_opchan = True  # if true, everyone that is *VOICED* in opchan will be considered a bot op.
