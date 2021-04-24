## Answers to exercise 1.1 

### 1. In a print statement, what happens if you leave out one of the parentheses, or both?

*If you leave out one of the parentheses there will be a SyntaxError: unexpected EOF while parsing. 
If you leave out both of the parentheses there will be a SyntaxError: invalid syntax.*

### 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

*If you are trying to print a string and you leave out one of the quotation marks there will be 
SyntaxError: EOL while scanning string literal. If you are trying to print a string and 
you leave out both of the quotation marks there will be SyntaxError: invalid syntax.*

### 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?

*If you write +2 or any other number with a + sign, then a positive natural number will be displayed
(without a + sign). If you use two + signs between numbers, the standard addition operation will be performed.*

### 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?

*If you use leading zeros, for example in records 09 and 011, there will be
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers.*

### 5. What happens if you have two values with no operator between them?

*If you use two values without an operator between them, then these values will be output and used as one.*
