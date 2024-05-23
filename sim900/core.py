import machine
import time

class SIM900:
    def __init__(self, uart_id, tx_pin, rx_pin, baudrate=9600):
        self.uart = machine.UART(uart_id, baudrate=baudrate, tx=tx_pin, rx=rx_pin)

    def send_command(self, command, timeout=3000):
        command += '\r\n'
        self.uart.write(command)
        start_time = time.ticks_ms()
        response = []
        while time.ticks_diff(time.ticks_ms(), start_time) < timeout:
            if self.uart.any():
                response.append(self.uart.read().decode())
        return ''.join(response)

    def check_network_registration(self):
        """
        Check network registration status.
        """
        response = self.send_command('AT+CREG?')
        if "+CREG: 0,1" in response or "+CREG: 0,5" in response:
            return True
        return False

    def check_signal_quality(self):
        """
        Check signal quality. Returns the signal strength (0-31, 99).
        """
        response = self.send_command('AT+CSQ')
        csq = response.split(': ')[1].split(',')[0]
        return int(csq)

    def reset_module(self):
        """
        Reset the SIM900 module.
        """
        return self.send_command('AT+CFUN=1,1')
