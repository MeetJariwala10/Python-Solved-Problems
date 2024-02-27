import urllib.parse

url = 'https://stackoverflow.com'

tuple1 = urllib.parse.urlparse(url)

print(tuple1)

print(f"\nScheme = {tuple1.scheme}")
print(f"Net Location = {tuple1.netloc}")
print(f"Path = {tuple1.path}")
print(f"Parameters = {tuple1.params}")
print(f"Port Number = {tuple1.port}")
print(f"Total URL = {tuple1.geturl()}")
