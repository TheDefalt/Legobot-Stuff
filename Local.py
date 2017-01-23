from Legobot.Lego import Lego
from random import randint
import socket

class Defalt(Lego):
    def listening_for(self, message):
        return message['text'].split()[0] == '!roll'

    def handle(self, message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target':target}
        except IndexError:
            logger.error('Could not identify message source in message: %s' % str(message))
       # if message['metadata']['source_username'] != 'Defalt':
        #                self.reply(message, 'fuck off my bot', opts)
         #               return
        try:
                shit = randint(1, 6)
                resp = "Yo dumbass, you rolled %s" %(shit)
                self.reply(message, resp, opts)
        except Exception:
                self.reply(message, "something fucked up", opts)

    def get_name(self):
        return "roll"

    def get_help(self):
        help_text = "stfu Defalt you dumbass. Usage: !roll"
        return help_text

class Scan(Lego):
        def listening_for(self, message):
                return message['text'].split()[0] == '!scan'

        def handle(self, message):
                try:
                        target = message['metadata']['source_channel']
                        opts = {'target':target}
                except IndexError:
                        logger.error('Could not identify message source in message: %s' % str(message))
          #      if message['metadata']['source_username'] != 'Defalt':
           #             self.reply(message, 'fuck off my bot', opts)
            #            return
                resp = "starting scan on host: %s" %(message['text'].split()[1])
                self.reply(message, resp, opts)
                print(str(message))
                try:
                        result = self.scanHost(message)
                except Exception:
                        self.reply(message, "something fucked up", opts)
                        return
                self.reply(message, "Scan complete, displaying results...", opts)
                self.reply(message, "Open ports: %s" %(', '.join([str(x) for x in result])), opts)
        def get_name(self):
                return "scan"

        def get_help(self):
                return "Scan fuction: Usage: !scan [target] [start port] [stop port]"

        def scanHost(self, message):
                ports = [x for x in range(int(message['text'].split()[2]), int(message['text'].split()[3])+1)]
                print(ports)
                openPorts = []
                for i in range(len(ports)):
                        try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                result = s.connect_ex((message['text'].split()[1], ports[i]))
                                s.close()
                                if result == 0:
                                        openPorts.append(ports[i])
                        except Exception:
                                pass
                return openPorts

class test(Lego):
    def listening_for(self, message):
        return message['text'].split()[0] == '!test'

    def handle(self, message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target':target}
        except IndexError:
            logger.error('Could not identify message source in message: %s' % str(message))
        resp = input("What do you want to say? >>> ")
        self.reply(message, resp, opts)

    def get_name(self):
        return "test"

    def get_help(self):
        return "test function. Use !test to trigger a prompt to manually enter the response from the terminal running this bot"

