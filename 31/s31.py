
pulse = int(raw_input('Your resting pulse ? '))
age = int(raw_input('Your age? '))

print 'Intensity    | Rate'
print '-------------|--------'

for i in xrange(55, 96, 5):
    thr = (((220 - age) - pulse) * i/100.0) + pulse
    print '%d%%        | %d bpm' % (i, round(thr)) 
