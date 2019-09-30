import threading
import logging
import traceback


class ClientThread(threading.Thread):

    def __init__(self, conn, ip, port, display):
        threading.Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port
        self.display = display
        logging.info("[+] New thread started for " + ip + ":" + str(port))

    def run(self):
        # Sending message to connected client
        self.conn.send('Welcome to the server. Type something and hit enter\n'.encode())  # send only takes string
        close = False

        # infinite loop so that function do not terminate and thread do not end.
        while not close:
            try:
                # Receiving from client
                data = self.conn.recv(1024)
                logging.debug(data.strip())
                data = data.decode().strip()
                if ' ' in data:
                    (cmd, arg) = data.split(' ', 1)
                else:
                    cmd = data

                if cmd == 'gen':
                    if self.display.set_generator(arg):
                        reply = 'Set generator: %s\n' % arg
                    else:
                        reply = 'No generator: %s\n' % arg
                elif cmd == 'brightness':
                    if self.display.set_brightness(arg):
                        reply = 'Set brightness to: %s\n' % arg
                    else:
                        reply = 'Couldn\'t set brightness to: %s\n' % arg
                elif cmd == 'set':
                    (option, args) = arg.split(' ', 1)
                    if option in self.display.get_generator_options():
                        if self.display.set_generator_option(option, args):
                            reply = 'Set %s to %s\n' % (option, args)
                        else:
                            reply = 'Could not set %s to %s\n' % (option, args)
                    else:
                        reply = 'Option %s not found\n' % option
                elif cmd == 'quit':
                    reply = 'Goodbye!\n'
                    close = True
                else:
                    reply = 'Unknown command: %s\n' % cmd

                if not data:
                    break
            except Exception:
                logging.error(traceback.format_exc())
                reply = 'Something broke ... kicking you out :p!\n'
                close = True

            self.conn.sendall(reply.encode())

        # came out of loop
        self.conn.close()
