class TCPIP:
    def __init__(self, sim900):
        self.sim900 = sim900

    def connect(self, type, addr, port):
        self.sim900.send_command('AT+CIPSTART="{}","{}","{}"'.format(type, addr, port))
        return self.sim900.send_command('AT+CIPSEND')

    def send(self, data):
        self.sim900.send_command(data)
        return self.sim900.send_command(chr(26))  # Send data followed by Ctrl+Z

    def close(self):
        return self.sim900.send_command('AT+CIPCLOSE')
