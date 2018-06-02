import json
from operator import itemgetter


with open('in.txt') as json_data:
    json_data = json.load(json_data)

while True:
    s = raw_input('What is the product name? ')

    index = next((index for (index, d) in enumerate(json_data['products']) if d["name"] == s), None)

    if index == None:
        print 'Sorry, that product was not found in our inventory.'
    else:
        data = json_data['products'][index]
        print 'Name: %s' % data['name']
        print 'Price: $%s' % data['price']
        print 'Quantity on hand: %s' % data['quantity']
        break
        
