class GPRS:
    def __init__(self, sim900):
        self.sim900 = sim900

    def connect(self, apn, user='', pwd=''):
        """
        Connect to the GPRS network using the provided APN, username, and password.
        """
        self.sim900.send_command('AT+CGATT=1')
        self.sim900.send_command(f'AT+CSTT="{apn}","{user}","{pwd}"')
        self.sim900.send_command('AT+CIICR')
        return self.sim900.send_command('AT+CIFSR')

    def disconnect(self):
        """
        Disconnect from the GPRS network.
        """
        return self.sim900.send_command('AT+CGATT=0')

    def get_location(self):
        """
        Retrieve the latitude and longitude using AT+CLBS (Cell Locate Base Station) command.
        """
        response = self.sim900.send_command('AT+CLBS=1,1')
        if "+CLBS:" in response:
            data = response.split(":")[1].strip().split(",")
            status, lat, lon, _ = data
            if status == '0':
                return float(lat), float(lon)
            else:
                return "Error in getting location", None
        return "Failed to retrieve location", None
