
from pathlib import Path
import os
import re
import pyinputplus
import csv
import time

# get input for folder containing raw data files
folder = pyinputplus.inputFilepath("Enter folder containing raw data files: ")

# extract date time out from folder structure for each data file
file_time = {}
regex_pattern = re.compile(r'[a-z0-9A-Z]+_[a-z0-9A-Z]+_[a-zA-Z]+')
for file in os.listdir(folder):
    file_match = regex_pattern.search(file)
    if file_match != None:
        p = Path(folder) / file / 'AcqData' / 'sample_info.xml'
        file_time[file] = {'mtime': p.stat().st_mtime, 'ctime': time.ctime(p.stat().st_mtime)}

# get path name for new file
p = Path(folder)
output_file_name = str(p / 'file_times.csv')

# write file to csv file in same directy as raw data files
output_file = open(output_file_name,'w',newline='')
output_writer = csv.writer(output_file)
for file in file_time:
    output_writer.writerow([file,file_time[file]['ctime'],file_time[file]['mtime']])
output_file.close()
