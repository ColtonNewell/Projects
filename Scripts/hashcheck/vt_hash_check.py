import os
import requests
import hashlib
import argparse
import time

vt_secret = os.environ['vtkey']
url = 'https://www.virustotal.com/vtapi/v2/file/report'
api_key = vt_secret

parser = argparse.ArgumentParser()
parser.add_argument('-f',
                    help='Hash file and check vt')
parser.add_argument('-l', help='file with list of hashes')
args = parser.parse_args()

if args.f:
  with open(args.f, 'rb') as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()
    print("{} hash: ".format(args.f), file_hash)
  params = {'apikey': api_key, 'resource': file_hash}
  response = requests.get(url, params=params)
  json_response = response.json()
  if json_response['response_code'] == 0:
    print("Hash not found on VirusTotal")
  else:
    positives = json_response['positives']
    total = json_response['total']
    print("Hash found on VirusTotal. Detection rate: {}/{}".format(positives, total))


elif args.l:
  with open(args.l, 'r') as f:
    hashes = f.readlines()
  num_hashes = 0  
  for check_hashes in hashes:
    check_hashes = check_hashes.strip()
    print(check_hashes)
    
    params = {'apikey': api_key, 'resource': check_hashes}
    response = requests.get(url, params=params)
    json_response = response.json()
   
    if json_response['response_code'] == 0:
      print("Hash not found on VirusTotal")
    else:
      positives = json_response['positives']
      total = json_response['total']
      print("Hash found on VirusTotal. Detection rate: {}/{}".format(positives, total))

    num_hashes += 1
    if num_hashes >= 4:
      time.sleep(15)
    
    print("{} hashes checked.".format(num_hashes))
    
