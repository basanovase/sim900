class SMS:
    def __init__(self, sim900):
        self.sim900 = sim900

    def send_sms(self, number, message):
        self.sim900.send_command('AT+CMGF=1')
        self.sim900.send_command(f'AT+CMGS="{number}"')
        self.sim900.uart.write(message + chr(26))
        return self.sim900.get_response()

    def read_sms(self, index):
        return self.sim900.send_command(f'AT+CMGR={index}')

    def delete_sms(self, index):
        return self.sim900.send_command(f'AT+CMGD={index}')

    def delete_all_sms(self):
        return self.sim900.send_command('AT+CMGDA="DEL ALL"')

    def read_all_sms(self):
        self.set_sms_format("1")
        return self.sim900.send_command('AT+CMGL="ALL"')

    def list_sms_indices(self):
        response = self.sim900.send_command('AT+CMGL="ALL"')
        indices = []
        for line in response.splitlines():
            if "+CMGL:" in line:
                index = int(line.split(',')[0].split(':')[1].strip())
                indices.append(index)
        return indices

    def set_sms_format(self, format="1"):
        return self.sim900.send_command(f'AT+CMGF={format}')
