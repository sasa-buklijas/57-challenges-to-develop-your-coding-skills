# From the book:  
Pulling data from a file into a complex data structure makes parsing much simpler.  
Many programming languages support the JSON format, a popular way of representing data.Create a program that takes a product name as input and retrieves the current price and quantity for that product.  
The product data is in a data file in the JSON format and looks like this:<pre>
{"products" : [           {"name": "Widget", "price": 25.00, "quantity": 5 },           {"name": "Thing", "price": 15.00, "quantity": 5 },           {"name": "Doodad", "price": 5.00, "quantity": 10 }] }
</pre>

Print out the product name, price, and quantity if the product is found.  
If no product matches the search, state that no product was found and start over.

**Example Output**  

What is the product name? iPad  Sorry, that product was not found in our inventory.  What is the product name? Widget  Name: Widget  Price: $25.00  Quantity on hand: 5  

<br />  
    
For more "**Constraint**" and "**Challenges**".  
Check the book:  
"Exercises for Programmers: 57 Challenges to Develop Your Coding Skills"  
https://pragprog.com/book/bhwb/exercises-for-programmers
