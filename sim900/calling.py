class Calling:
    def __init__(self, sim900):
        self.sim900 = sim900

    def make_call(self, number):
        """
        Make a voice call to the specified number.
        """
        return self.sim900.send_command(f'ATD{number};')

    def answer_call(self):
        """
        Answer an incoming call.
        """
        return self.sim900.send_command('ATA')

    def hang_up(self):
        """
        Hang up the ongoing call.
        """
        return self.sim900.send_command('ATH')

    def redial_last_number(self):
        """
        Redial the last dialed number.
        """
        return self.sim900.send_command('ATDL')

    def check_call_status(self):
        """
        Check the status of the current call.
        """
        return self.sim900.send_command('AT+CLCC')

    def call_waiting(self, enable=True):
        """
        Enable or disable call waiting.
        """
        mode = '1' if enable else '0'
        return self.sim900.send_command(f'AT+CCWA=1,{mode}')

    def hold_call(self):
        """
        Hold the current call.
        """
        return self.sim900.send_command('AT+CHLD=2')

    def retrieve_call(self):
        """
        Retrieve a held call.
        """
        return self.sim900.send_command('AT+CHLD=1')
