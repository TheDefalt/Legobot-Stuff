# Libs to initialize the bot
import threading
from Legobot.Lego import Lego

# A few plugins
from Legobot.Connectors.IRC import IRC
from Legobot.Legos.Help import Help
from Local import Defalt, Scan, test

# Create the "parent" lego that owns all the plugins
# This will get boiled down into a one-liner soon
lock = threading.Lock()
master = Lego.start(None, lock)
master_proxy = master.proxy()

# Add some functionality
master_proxy.add_child(IRC,
                          channels=['#test'],
                          nickname='Defalts-Retarded-Bot',
                          server='irc.0x00sec.org',)
master_proxy.add_child(Help)
master_proxy.add_child(Defalt)
master_proxy.add_child(Scan)
master_proxy.add_child(test)
