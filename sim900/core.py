import machine
import time

class SIM900:
    def __init__(self, uart_id, baudrate=9600, tx_pin, rx_pin):
        self.uart = machine.UART(uart_id, baudrate=baudrate, tx=tx_pin, rx=rx_pin)

    def send_command(self, command, timeout=5000):
        self.uart.write(command + '\r\n')
        start_time = time.ticks_ms()
        response = ''
        while time.ticks_diff(time.ticks_ms(), start_time) < timeout:
            if self.uart.any():
                response += self.uart.read().decode()
        return response
