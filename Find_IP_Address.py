import socket

# Take the server name
host = 'www.google.com'
# host = 'www.facebook.com'

try:
    addr = socket.gethostbyname(host)
    print(f"IP Address: {addr}")

except socket.gaierror: # "Get address info" (gaierror) error
    print("The website does not exist")
