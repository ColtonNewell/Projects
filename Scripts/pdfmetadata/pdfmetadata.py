#WORK IN PROGRESS

import pikepdf
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('Directory', help='Directory containing PDF files to extract metadata from')
args = parser.parse_args()

path = r'c:\directory\for\testing'


if args.Directory:
    f = open(r'c:\directory\for\testing\results.txt', 'a')
    for file in os.listdir(path):
        print(file)
        if file.endswith('.pdf'):
            with pikepdf.open(os.path.join(path, file)) as pdf:
                meta = pdf.open_metadata()
                f.write('** ' + file + ' **' + '\n' + str(meta) + '\n')
  
    f.close
