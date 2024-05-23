class SMS:
    def __init__(self, sim900):
        self.sim900 = sim900

    def send_sms(self, number, message):
        self.sim900.send_command('AT+CMGF=1')  # Set to text mode
        self.sim900.send_command('AT+CMGS="{}"'.format(number), timeout=10000)
        self.sim900.send_command(message + chr(26))  # Send message followed by Ctrl+Z
