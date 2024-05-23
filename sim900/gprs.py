class GPRS:
    def __init__(self, sim900):
        self.sim900 = sim900

    def connect(self, apn):
        self.sim900.send_command('AT+CGATT=1')
        self.sim900.send_command('AT+CSTT="{}"'.format(apn))
        self.sim900.send_command('AT+CIICR')
        return self.sim900.send_command('AT+CIFSR')

    def disconnect(self):
        return self.sim900.send_command('AT+CGATT=0')
