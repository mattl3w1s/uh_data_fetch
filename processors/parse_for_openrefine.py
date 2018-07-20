import sys
from lxml import html, etree
import csv
import os
from pprint import pprint

current_dir = os.path.dirname(__file__)
dir_of_sites = os.path.join(current_dir,'../data/program_data')
OUTPUT_DELIMITER = '|'

# Captures head tags: self::h2 or self::h3 or self::h4 ...
head_tags = ' or '.join([f'self::h{i}' for i in range(2,7)])

def parse_page(file_name,meta):
    root = html.parse(open(os.path.join(dir_of_sites,file_name)))

    # Find course clusters
    course_clusters = root.xpath('.//ul[child::li[@class="acalog-course"]]')

    # Loop over clusters
    for cluster in course_clusters:
        
        # Parse each cluster
        courses = cluster.xpath('.//li')
        for course in courses:
            course_row = []
            course_row.append(meta["degree_name"])
            course_info = course.xpath('./span/a/text()')
            if(course_info):
                course_row.append(f'"{course_info[0]}"'.strip())
                # Find next field up
                closest_heading_tag = course.xpath(f'./parent::*/preceding-sibling::*[{head_tags}]')[-1]
                closest_heading = closest_heading_tag.xpath('./text()')[0]
                course_row.append(closest_heading.strip())
                parent = closest_heading_tag.xpath('./parent::*')[-1]
                parent_div = parent
                while(parent_div):
                    parent_divs = parent_div.xpath(f'./parent::*/preceding-sibling::div[@class="acalog-core"][child::*[{head_tags}]]')
                    if(parent_divs):
                        parent_div = parent_divs[-1]
                        header = parent_div.xpath(f'./child::*[{head_tags}]/text()')[0]
                        course_row.append(header.strip())
                    else:
                        parent_div = False
                sys.stdout.write(OUTPUT_DELIMITER.join(course_row)+'\n')

        


for page in os.listdir(dir_of_sites):
    if('.html' in page):
        meta = dict()
        meta["degree_name"] = page
        parse_page(page,meta)