class TCPIP:
    def __init__(self, sim900):
        self.sim900 = sim900

    def connect(self, type, addr, port):
        """
        Establish a TCP or UDP connection.
        :param type: "TCP" or "UDP"
        :param addr: Address of the server
        :param port: Port number
        :return: Response from the SIM900 module
        """
        response = self.sim900.send_command('AT+CIPSTART="{}","{}","{}"'.format(type, addr, port), timeout=10000)
        if "CONNECT OK" in response:
            return "Connection established"
        return "Failed to establish connection"

    def send(self, data):
        """
        Send data over the established TCP/UDP connection.
        :param data: Data to be sent
        :return: Response from the SIM900 module
        """
        self.sim900.send_command('AT+CIPSEND')
        response = self.sim900.send_command(data + chr(26), timeout=10000)  # Send data followed by Ctrl+Z
        return response

    def receive(self, timeout=5000):
        """
        Receive data from the TCP/UDP connection.
        :param timeout: Timeout for receiving data
        :return: Received data
        """
        return self.sim900.send_command('', timeout=timeout)

    def close(self):
        """
        Close the TCP/UDP connection.
        :return: Response from the SIM900 module
        """
        return self.sim900.send_command('AT+CIPCLOSE')

    def get_ip_address(self):
        """
        Get the IP address assigned to the module.
        :return: IP address
        """
        return self.sim900.send_command('AT+CIFSR')

    def check_connection_status(self):
        """
        Check the status of the TCP/UDP connection.
        :return: Connection status
        """
        return self.sim900.send_command('AT+CIPSTATUS')
