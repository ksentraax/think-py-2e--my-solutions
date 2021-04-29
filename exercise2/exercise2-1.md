## Answers to exercise 2.1

### 1. We’ve seen that n = 42 is legal. What about 42 = n?

*42 cannot act as a variable name, since Python syntax does not allow starting a name with a number. 
SyntaxError: cannot assign to literal.*

### 2. How about x = y = 1?

*Variable x and variable y will be equal to 1.*

### 3. In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?

*If you use ; there will be no error. Can be used to write one line of code (b = 4; print(b)), but PEP8 doesn't approve this.*

### 4. What if you put a period at the end of a statement?

*If you using a period at the end of the statement there will be SyntaxError: invalid syntax.*

### 5. In math notation you can multiply x and y like this: xy. What happens if you try that in Python?

*If you try to multiply two numbers without the * operator (for example, xy), it will be output as a single number.
If you try to multiply a string without the * operator then there will be SyntaxError: invalid syntax.*