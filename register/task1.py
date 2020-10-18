from urllib3.util import parse_url
import socket
import sys

COLORS = {
    'red': "\033[1;31m",
    'green': "\033[0;32m",
    '_reset': "\033[0;0m",
}

def colored(color, text):
    sys.stdout.write(COLORS[color])
    print(text, end="")
    sys.stdout.write(COLORS['_reset'])


def parse(filename):
    with open(filename, 'r') as f:
        text = f.read()

    banned_urls = set()
    banned_domains = set()
    banned_ips = set()
    for text in text.splitlines():
        _, *urls, domains, ips = text.split(';')
        urls = ";".join(urls)
        banned_urls.update(urls.split(','))
        banned_domains.update(domains.split(','))
        banned_ips.update(ips.split(','))
        if 'ya.ru' in domains.split(','):
            print(domains)
    return banned_domains, banned_urls, banned_ips
        
url = input("Enter url: ")
domain = parse_url(url).netloc
ip = None
try:
    ip = socket.gethostbyname(domain)
except socket.gaierror:
    print("IP cannot be found")
domains, urls, ips = parse('register.txt')

if url in urls:
    print("1. URL is ", end="")
    colored('red', "banned")
    print()
else:
    print("1. URL is ", end="")
    colored('green', "not banned")
    print()

if domain in domains:
    print("2. Domain is ", end="")
    colored('red', "banned")
    print()
else:
    print("3. Domain is ", end="")
    colored('green', "not banned")
    print()

if ip in ips:
    print("3. IP is ", end="")
    colored('red', "banned")
    print()
else:
    print("3. IP is ", end="")
    colored('green', "not banned")
    print()
