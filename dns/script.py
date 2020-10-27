from urllib3.util import parse_url
import pandas as pd
from whois import whois
from whois.parser import PywhoisError
from random import choices

data = pd.read_csv('register.csv')
domains_to_check = set()
rows = choices(data.values.tolist(), k=500)
for i, row in enumerate(rows):
    print('%i of %i' % (i, len(rows)), end=" ")
    urls = row[2]
    if urls == urls:
        parsed = parse_url(urls)
        print(parsed.host, end=" ")
        if parsed.scheme == 'https':
            try:
                w = whois(parsed.host)
            except PywhoisError as e:
                pass
            if 'registrar' not in w or not w['registrar']:
                domains_to_check.add(parsed.host)
                print("available", end=" ")

    print()

for domain in domains_to_check:
    print(domain)