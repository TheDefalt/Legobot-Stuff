import threading
from Legobot.Lego import Lego
from Legobot.Connectors.Slack import Slack
from Local import Defalt, Scan, test

SLACK_TOKEN = 'DOTNWORRYAS;LDKFJ'xoxp-130615944049-131372502388-131447952709-8ef50f341b0c3abc6f98e29cc5d2ed3f

# As usual, all the Pykka stuff to get us initialized
lock = threading.Lock()
baseplate = Lego.start(None, lock)
baseplate_proxy = baseplate.proxy()

# Now we add the slack connector
baseplate_proxy.add_child(Slack,SLACK_TOKEN)
baseplate_proxy.add_child(Defalt)
baseplate_proxy.add_child(Scan)
baseplate_proxy.add_child(test)
