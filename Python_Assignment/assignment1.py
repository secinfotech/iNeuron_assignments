## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
It allows us to write code in English like language which is easy to understand and it does not require us to write low level / assembly language to execute programs.

Q2. Why is Python called a dynamically typed language?
It can be run as soon as a piece of code is written, it does not need us to compile first before running.
Q3. List some pros and cons of Python programming language?
Pros:
Huge number of libraries and support from community
Easy to read syntax
Intuitive variable declaration
Needs lesser number of lines to be written compared to other languages

Cons:
Needs execution time longer than compiled languages like Java / Scala
Abstracts away a lot of code in form of libraries, causing logic building for those tasks diffcult

Q4. In what all domains can we use Python?
Data engineering / Data science / Machine learning / AI / DevOps / Cloud operations / Cyber security / Crypto currency

Q5. What are variable and how can we declare them?
Variables are name spaces pointing to memory locations for a value to be accessed, we can allocate values to a variable with help of '=' assignment operators.

Q6. How can we take an input from the user in Python?
input() function helps us to take input from users

Q7. What is the default datatype of the value that has been taken as an input using input() function?
Default data type is string

Q8. What is type casting?
Changing type of the variable for convenience of operation

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
We can take multiple inputs in form of List

Q10. What are keywords?
Reserved words for python which are pre-determined classes which are used for functionality of different types

Q11. Can we use keywords as a variable? Support your answer with reason.
We can, but we should not, as it will affect the functionality of that particular keyword and it might make the program to crash.

Q12. What is indentation? What's the use of indentaion in Python?
The whitespace is called indentation and it is used to define scope in python

Q13. How can we throw some output in Python?
with the help of print() functtion

Q14. What are operators in Python?
Operators are functionalities to perform mathematical operations like addition, subtraction, multiplication and divisin and modulo

Q15. What is difference between / and // operators?
/ is division
// is integer division

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
x=iNeuron
print(x*3)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
a = int(input("Enter the number: "))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")

Q18. What are boolean operator?
A boolean operator returns true or false. True and False are boolean operators in python

Q19. What will the output of the following?
```
1 or 0
True
0 and 0
False
True and False and True
False
1 or 0 or 0
True
```

Q20. What are conditional statements in Python?
if, elif and else are conditional statements, if the first block under if does not satisfy the given condition, the second block under elif will run and so on, and if no block of code satisfies the condition, the else block will run.

Q21. What is use of 'if', 'elif' and 'else' keywords?
if is the first block of code, if that executes and staisfies the given condition, the rest will no longer execute, if the if block does not satisfy the condition, next elif block runs and so on, if no elif block also meets the condition, the else block runs.

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age = int(input("Enter your age: "))

if age < 18:
    print("You can not vote.!")
elif age >=18:
    print("You can vote.!")
    
Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
i=0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])
    i+=1

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

num1=int(input("Insert the first number: "))
num2=int(input("Insert the second number: "))
num3=int(input("Insert the third number: "))
if num1 > num2 and num1 > num3:
    print("The largest number is {}".format(num1))
elif num2 > num1 and num2 > num3:
    print("The largest number is {}".format(num2))
else:
    print("The largest number is {}".format(num3))

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
i=0
for i in range(len(numbers)):
    if numbers[i]>500:
        break
    if numbers[i]==150:
        continue
    elif numbers[i]%5==0:
        print(numbers[i])
    i+=1
