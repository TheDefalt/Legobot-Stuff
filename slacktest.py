import threading
from Legobot.Lego import Lego
from Legobot.Connectors.Slack import Slack
from Local import Defalt, Scan, test

SLACK_TOKEN = 'DOTNWORRYAS;LDKFJ'

# As usual, all the Pykka stuff to get us initialized
lock = threading.Lock()
baseplate = Lego.start(None, lock)
baseplate_proxy = baseplate.proxy()

# Now we add the slack connector
baseplate_proxy.add_child(Slack,SLACK_TOKEN)
baseplate_proxy.add_child(Defalt)
baseplate_proxy.add_child(Scan)
baseplate_proxy.add_child(test)
