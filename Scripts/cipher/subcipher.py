import random
import argparse

alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!?#%@&$ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = list(alphabet)
random.shuffle(key)
key = "".join(key)

parser = argparse.ArgumentParser()
parser.add_argument('-e',
                    help='encrypt message')
parser.add_argument('-d', help='decrypt message')
parser.add_argument('-k', help='Decryption key')
args = parser.parse_args()

if args.e:
  encrypted = ""
  for char in args.e:
    if char in alphabet:
      encrypted += key[alphabet.index(char)]
    else:
      encrypted += char
  print("Encrypted message: " + encrypted + '\n' + "Key: " + key)

elif args.d:
  decrypted = ""
  for char in args.d.lower():
    if char in alphabet:
      decrypted += alphabet[args.k.index(char)]
    else:
      decrypted += char
  print("Decrypted message: " + decrypted)
