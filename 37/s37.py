import string
import random


l = int(raw_input("What's the minimum length? "))
s = int(raw_input("How many special characters? "))
n = int(raw_input("How many numbers? "))

password = []
for i in xrange(n):
    password.append(random.choice(string.digits))

for i in xrange(s):
    password.append(random.choice(string.punctuation))

for i in xrange(l-s-n):
    password.append(random.choice(string.letters))

random.shuffle(password)
    
password = ''.join(password)

print 'Your password is'
print password

