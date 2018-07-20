import sys
from lxml import html
from urllib.parse import urljoin
from slugify import slugify

URL_ROOT = 'http://publications.uh.edu/'
MAJOR_LIST_XPATH = '//body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/ul[3]'

root = html.parse(sys.stdin)
ul = root.xpath(MAJOR_LIST_XPATH)[0]

for li in ul:
    program_name = li.xpath('./a/text()')[0]
    program_url = urljoin(URL_ROOT,li.xpath('./a/@href')[0])
    program_slug = slugify(program_name)
    sys.stdout.write(f'"{program_name}"|{program_url}|{program_slug}\n')
