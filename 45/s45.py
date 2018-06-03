
in_data = open('in.txt', 'r').read()

print 'INPUT FILE'
print in_data
print

out_data = in_data.replace('utilize', 'use')

open('out.txt', 'w').write(out_data)

print 'OUTPUT FILE'
print open('out.txt', 'r').read()
print
