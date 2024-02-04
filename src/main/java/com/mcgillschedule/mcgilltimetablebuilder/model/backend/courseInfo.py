# -*- coding: utf-8 -*-
"""
This is a script to scrape course data info from Mcgill official website.
Author: RENOLEVES
Date: 2/3/2024
running time: ~ 5 minutes
"""

import requests
import re
# you may need to install chardet, if this is the case
# try: pip install chardet
# pip install cchardet

from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        # User-Agent
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print('Load into page.')

    with open('output.txt', 'w+') as f:

        for index in range(531):

            response = requests.get(url + "?page=" + str(index), headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting page_info
            page_info = soup.find_all('div', class_="views-field views-field-field-course-title-long")

            for line in page_info:
                f.write(str(line))
                f.write('\n')

        f.close()


# url config
url = "https://www.mcgill.ca/study/2023-2024/courses/search"
get_data(url)

# reformat and extract course info and save to result.txt
file = open('output.txt', 'r')
file1 = open("courseList.csv","w+")

List = []

for info in file:
    # if info starts with <div> tag then it's correct, everything else should be appended to the previous line.
    if info.startswith('<div'):
        List.append(info.rstrip('\n'))
    else:
        List[-1] += info.lstrip('\n')

List1 = []

for info in List:
    # if info starts with <div> tag then it's correct, everything else should be appended to the previous line.
    if info.startswith('<div'):
        List1.append(info.rstrip('\n'))
    else:
        List1[-1] += info.lstrip('\n')

course_id = ""
course_title = ""
credit = 0

for course in List1:
    # wildcard pattern matching
    pattern = r'<a href="[^"]+">([^<]+)</a>'
    match = re.search(pattern, course)

    if match:
        result = match.group(1)
        if result:
            arr = result.split(" ")
            print(arr[0]+" "+arr[1])
            course_id = arr[0] + arr[1]
            if arr[-2].startswith('('):
                credit = arr[-2][1:]
                course_title = \
                    ' '.join([arr[i] for i in range(2, len(arr)-2)]).rstrip('\n')
            else:
                course_title = \
                    ' '.join([arr[i] for i in range(2, len(arr))]).rstrip('\n')
            file1.write(course_id + ',' + course_title + ',' + str(credit).rstrip('\n') + '\n')

file.close()
file1.close()