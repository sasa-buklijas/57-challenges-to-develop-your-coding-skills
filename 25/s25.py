import string
   
password = unicode(raw_input("Enter the password: "))

if password.isnumeric() and len(password) <=8:
    print "The password '%s' is a very weak password." % (password)
elif password.isalpha() and len(password) <=8:
    print "The password '%s' is a weak password." % (password)
elif password.isalnum() and not password.isalpha() and not password.isnumeric() and len(password) >=8:
    print "The password '%s' is a strong password." % (password)
elif any(char in (string.punctuation) for char in password) and \
     any(char in (string.digits) for char in password) and \
     any(char in (string.letters) for char in password):
    print "The password '%s' is a very strong password." % (password)
else:
    print "ELSE password '%s'" % (password)
