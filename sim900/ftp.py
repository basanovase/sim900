class FTP:
    def __init__(self, sim900):
        self.sim900 = sim900

    def set_ftp_credentials(self, server, username, password):
        """
        Set FTP server, username, and password.
        """
        self.sim900.send_command('AT+FTPSERV="{}"'.format(server))
        self.sim900.send_command('AT+FTPUN="{}"'.format(username))
        self.sim900.send_command('AT+FTPPW="{}"'.format(password))

    def set_ftp_port(self, port=21):
        """
        Set the FTP server port, default is 21.
        """
        return self.sim900.send_command('AT+FTPPORT={}'.format(port))

    def set_ftp_mode(self, mode=1):
        """
        Set FTP mode: 1 for Passive, 0 for Active.
        """
        return self.sim900.send_command('AT+FTPMODE={}'.format(mode))

    def start_ftp_session(self):
        """
        Initialize the FTP session.
        """
        return self.sim900.send_command('AT+FTPCID=1')  # Assuming CID 1 for GPRS

    def upload_file(self, file_path, file_name):
        """
        Upload a file to the FTP server.
        """
        self.sim900.send_command('AT+FTPPUTNAME="{}"'.format(file_name))
        self.sim900.send_command('AT+FTPPUTPATH="{}"'.format(file_path))
        response = self.sim900.send_command('AT+FTPPUT=1')
        if 'CONNECT' in response:
            # Send file data here, e.g., self.sim900.send_command(file_data)
            self.sim900.send_command('File data', expect_continue=True)
            self.sim900.send_command('AT+FTPPUT=2,0')  # End the FTP PUT session
        return response

    def download_file(self, file_path, file_name):
        """
        Download a file from the FTP server.
        """
        self.sim900.send_command('AT+FTPGETNAME="{}"'.format(file_name))
        self.sim900.send_command('AT+FTPGETPATH="{}"'.format(file_path))
        response = self.sim900.send_command('AT+FTPGET=1')
        if 'CONNECT' in response:
            file_data = self.sim900.send_command('AT+FTPGET=2,1024')  # Read 1024 bytes
            self.sim900.send_command('AT+FTPGET=2,0')  # End the FTP GET session
            return file_data
        return response

    def close_ftp_session(self):
        """
        Close the FTP session.
        """
        return self.sim900.send_command('AT+FTPCLOSE')
