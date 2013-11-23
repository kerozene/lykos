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
network    = "irc.freenode.net"
port       = 6667
serverpass = "" #leave blank if none

# The channel for lykos to join.
channels   ="#channel"
opchan     = "#channel-ops"

# Bot information.
nickname   = "lykos"
nickpass   = "password"
username   = "lykos"
cmdchat    = "!"

#Admin Information
owner      = ("unaffiliated/owner",) #leave the trailing comma if there is 1 owner
admin      = ("unaffiliated/admin1", "unaffiliated/admin2")


