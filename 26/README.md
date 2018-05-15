
# From the book:  
  
It can take a lot longer to pay off your credit card balance than you might realize.  
And the formula for figuring that out isn’t pretty.  
Hiding the formula’s complexity with a function can help you keep your code organized.
Write a program that will help you determine how many months it will take to pay off a credit card balance.  
The program should ask the user to enter the balance of a credit card and the APR of the card. The program should then return the number of months needed.  

The formula for this is

n = -1/30 * ( log (1 + b/p * (1 - (1 + i)<sup>30</sup> ) ) / log(1 + i) )
* n is the number of months.  * i is the daily rate (APR divided by 365).  
* b is the balance.  * p is the monthly payment.  

**Example Output**  
What is your balance? 5000  What is the APR on the card (as a percent)? 12  What is the monthly payment you can make? 100  It will take you 70 months to pay off this card.       
  
<br />  
    
For more "**Constraint**" and "**Challenges**".  
Check the book:  
"Exercises for Programmers: 57 Challenges to Develop Your Coding Skills"  
https://pragprog.com/book/bhwb/exercises-for-programmers
