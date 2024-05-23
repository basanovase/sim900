class HTTP:
    def __init__(self, sim900):
        self.sim900 = sim900

    def initialize(self):
        return self.sim900.send_command('AT+HTTPINIT')

    def terminate(self):
        return self.sim900.send_command('AT+HTTPTERM')

    def set_param(self, tag, value):
        command = f'AT+HTTPPARA="{tag}","{value}"'
        return self.sim900.send_command(command)

    def execute_method(self, method):
        methods = {'GET': 0, 'POST': 1, 'HEAD': 2}
        command = f'AT+HTTPACTION={methods[method]}'
        return self.sim900.send_command(command)

    def send_data(self, data):
        # Calculate the length of the data
        data_length = len(data)
        # Prepare the module to accept the data length
        self.sim900.send_command(f'AT+HTTPDATA={data_length},10000')
        # Allow time for the module to respond and be ready to receive the actual data
        time.sleep(1)
        # Send the actual data
        return self.sim900.send_command(data)

    def read_response(self):
        return self.sim900.send_command('AT+HTTPREAD')

    def save_context(self):
        return self.sim900.send_command('AT+HTTPSCONT')
