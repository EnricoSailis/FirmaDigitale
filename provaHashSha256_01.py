# Hash a file with hashlib.sha256
import hashlib

with open('example.pdf', 'rb') as f:
    for line in f:
        hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
        print(hashed_line)