
from collections import Counter


def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
    

print "Enter two strings and I'll tell you if they are anagrams:"

a = raw_input("Enter the first string: ")
b = raw_input("Enter the second string: ")

if is_anagram(a, b):
    print '"%s" and "%s" are anagrams.' % (a, b)
else:
    print '"%s" and "%s" are NOT anagrams.' % (a, b)
