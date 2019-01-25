# CPPJunk by @maxbridgland
# Adds unlimited junkcode to your C++ projects.
# Instructions:
# - Place this file in the root of your project's directory
# - Run "python cppjunk.py"
# - Go through the options and it will take care of the rest.

import requests
import glob
import os

junk_url = "https://junkcode.gehaxelt.in/"
currentdir = os.getcwd()
files = []
for result in glob.iglob('{}/*/*.cpp'.format(currentdir)):
    files.append(result)
if len(files) == 0:
    print('Error! No files found!')
    exit()
elif len(files) != 0:
    print(files)

for i in range(len(files)):
    r = requests.get(junk_url).text
    with open(files[i], 'a+') as f:
        f.write(r)

