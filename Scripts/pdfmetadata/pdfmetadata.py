import pikepdf
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('Directory', help='Directory containing PDF files to extract metadata from')
parser.add_argument('-r','--results', help='Name of the file to output results')
args = parser.parse_args()

dir = args.Directory

count = 0

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        if path.endswith('.pdf'):
            count += 1            
print('Processing', count, 'files...')

if args.Directory and args.results:
    f = open(args.results, 'a')
    for file in os.listdir(dir):
        if file.endswith('.pdf'):
            with pikepdf.open(os.path.join(dir, file)) as pdf:
                meta = pdf.open_metadata()
                f.write('@@ ' + file + ' @@' + '\n' + str(meta) + '\n')
    f.close

else:
    for file in os.listdir(dir):    
        if file.endswith('.pdf'):
            with pikepdf.open(os.path.join(dir, file)) as pdf:
                meta = pdf.open_metadata()
                print('@@ ' + file + ' @@' + '\n' + str(meta) + '\n')

print('Done!')
