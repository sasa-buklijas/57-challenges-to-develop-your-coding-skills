
def is_float(string):
    try:
        float(string)
    except ValueError:
        return False
    
    return True


while True:
    r = raw_input('What is the rate of return?: ')
   
    if not is_float(r):
        continue
    else:
        print 'It will take %.2f years to double your initial investment.' % (72 / float(r))
        break
