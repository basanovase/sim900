class SMS:
    def __init__(self, sim900):
        self.sim900 = sim900

    def send_sms(self, number, message):
        # Set SMS text mode
        self.sim900.send_command('AT+CMGF=1')
        # Command to initiate sending SMS
        self.sim900.send_command(f'AT+CMGS="{number}"', expect_continue=True)
        # Send the actual message followed by Ctrl+Z
        self.sim900.send_command(message + chr(26))

    def set_sms_format(self, format="1"):
        """
        Set the SMS format to text (1) or PDU (0).
        """
        return self.sim900.send_command(f'AT+CMGF={format}')

    def read_sms(self, index):
        """
        Read an SMS at a specific index in the memory.
        """
        return self.sim900.send_command(f'AT+CMGR={index}')

    def delete_sms(self, index):
        """
        Delete an SMS at a specific index.
        """
        return self.sim900.send_command(f'AT+CMGD={index}')

    def delete_all_sms(self):
        """
        Delete all SMS messages from memory.
        """
        return self.sim900.send_command('AT+CMGDA="DEL ALL"')

    def read_all_sms(self):
        """
        Retrieve all SMS messages from the memory.
        """
        # Ensure SMS is set to text mode for reading
        self.set_sms_format("1")
        return self.sim900.send_command('AT+CMGL="ALL"')
