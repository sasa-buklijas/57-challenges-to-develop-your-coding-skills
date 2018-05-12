
a = raw_input("Is the car silent when you turn the key? ").lower().strip()

if a == 'y':
    a = raw_input("Are the battery terminals corroded? ").lower().strip()

    if a == 'y':
        print 'Clean terminals and try starting again.'
    else:
       print 'Replace cables and try again.'
else:
    a = raw_input("Does the car make a clicking noise? ").lower().strip()

    if a == 'y':
        print 'Replace the battery.'
    else:
        a = raw_input("Does the car crank up but fail to start? ").lower().strip()

        if a == 'y':
            print 'Check spark plug connections.'
        else:
            a = raw_input("Does the engine start and then die? ").lower().strip()

            if a == 'y':
                a = raw_input("Does your car have fuel injection? ").lower().strip()

                if a == 'y':
                    print 'Get it in for service.'
                else:
                    print 'Check to ensure the choke is opening and closing.'
