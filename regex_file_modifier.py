import os
import fileinput
import sys
import re

#####Variables########
directory = r'C:\Users\test\Desktop\test'
file_extension = ".txt"
regex = r"45"
multiplicator = 2


#####Script########
file_list = []
for file in os.listdir(directory):
    if file.endswith(file_extension):
        file_list.append(os.path.join(directory, file))

for textfile in file_list:
    with open(textfile, 'r') as file:
        data = file.read()

    regex_results = re.findall(regex, data)

    for matches in regex_results:
        int_matches = int(matches) * multiplicator
        replaced_matches = str(int_matches)
        data = data.replace(matches, replaced_matches)
        with open(textfile, 'w') as file:
            file.write(data)
            file.close()
