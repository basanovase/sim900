# SIM900 MicroPython Library

MicroPython library for managing various functionalities of the SIM900 GSM/GPRS module, including SMS, calling, GPRS, HTTP, FTP, and phonebook management.

## File Structure
- `__init__.py`
- `core.py`
- `sms.py`
- `calling.py`
- `gprs.py`
- `http.py`
- `ftp.py`
- `phonebook.py`
- `tcpip.py`

## Installation
1. **Copy the library files** to your MicroPython device.
2. **Import the library** into your MicroPython script.
# GPRS
```python
from sim900 import SIM900, GPRS

# Initialize the SIM900 module
sim900 = SIM900(uart_id=1, tx_pin=17, rx_pin=16)

# Initialize the GPRS class with the SIM900 instance
gprs = GPRS(sim900)

# Connect to GPRS using your APN, username, and password
# Replace 'your_apn', 'your_username', 'your_password' with actual credentials
gprs.connect('your_apn', 'your_username', 'your_password')

# Get location data
lat, lon = gprs.get_location()
if lat and lon:
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Failed to get location")

# Disconnect from GPRS
gprs.disconnect()
```
# HTTP
```python
from sim900_library import SIM900, HTTP

# Initialize the SIM900 module
sim900 = SIM900(uart_id=1, tx_pin=17, rx_pin=16)

# Initialize the HTTP class with the SIM900 instance
http = HTTP(sim900)

# Initialize the HTTP service
http.initialize()

# Set URL and content type for the HTTP request
http.set_param("URL", "http://example.com")
http.set_param("CONTENT", "application/json")

# Perform an HTTP GET request
response = http.execute_method('GET')

# Read the HTTP response
print(http.read_response())

# Terminate the HTTP service
http.terminate()
```
# SMS
``` python
from sim900 import SIM900, SMS

# Initialize the SIM900 module
sim900 = SIM900(uart_id=1, tx_pin=17, rx_pin=16)

# Initialize the SMS class with the SIM900 instance
sms = SMS(sim900)

# Send an SMS
sms.send_sms('1234567890', 'Hello, blue papers please!')

# Read an SMS at index 1
print(sms.read_sms(1))

# Delete an SMS at index 1
sms.delete_sms(1)

# Read all SMS messages
print(sms.read_all_sms())

# Delete all SMS messages
sms.delete_all_sms()
```
