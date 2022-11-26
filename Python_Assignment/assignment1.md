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
Q26. What is a string? How can we declare string in Python?

Q27. How can we access the string using its index?

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

Q30. Resverse the string given in the above question.

Q31. How can you delete entire string at once?

Q32. What is escape sequence?

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```

Q34. What is a list in Python?

Q35. How can you create a list in Python?

Q36. How can we access the elements in a list?

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 

Q38. Take a list as an input from the user and find the length of the list.

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

Q40. What is a tuple? How is it different from list?

Q41. How can you create a tuple in Python?

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

Q44. Take a tuple as an input and print the count of elements in it.

Q45. What are sets in Python?

Q46. How can you create a set?

Q47. Create a set and add "iNeuron" in your set.

Q48. Try to add multiple values using add() function.

Q49. How is update() different from add()?

Q50. What is clear() in sets?

Q51. What is frozen set?

Q52. How is frozen set different from set?

Q53. What is union() in sets? Explain via code.

Q54. What is intersection() in sets? Explain via code.

Q55. What is dictionary ibn Python?

Q56. How is dictionary different from all other data structures.

Q57. How can we delare a dictionary in Python?

Q58. What will the output of the following?
```
var = {}
print(type(var))
```

Q59. How can we add an element in a dictionary?

Q60. Create a dictionary and access all the values in that dictionary.

Q61. Create a nested dictionary and access all the element in the inner dictionary.

Q62. What is the use of get() function?

Q63. What is the use of items() function?

Q64. What is the use of pop() function?

Q65. What is the use of popitems() function?

Q66. What is the use of keys() function?

Q67. What is the use of values() function?

Q68. What are loops in Python?

Q69. How many type of loop are there in Python?

Q70. What is the difference between for and while loops?

Q71. What is the use of continue statement?

Q72. What is the use of break statement?

Q73. What is the use of pass statement?

Q74. What is the use of range() function?

Q75. How can you loop over a dictionary?


### Coding problems
Q76. Write a Python program to find the factorial of a given number.

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

Q79. Write a Python program to check if a number is prime or not.

Q80. Write a Python program to check Armstrong Number.

Q81. Write a Python program to find the n-th Fibonacci Number.

Q82. Write a Python program to interchange the first and last element in a list.

Q83. Write a Python program to swap two elements in a list.

Q84. Write a Python program to find N largest element from a list.

Q85. Write a Python program to find cumulative sum of a list.

Q86. Write a Python program to check if a string is palindrome or not.

Q87. Write a Python program to remove i'th element from a string.

Q88. Write a Python program to check if a substring is present in a given string.

Q89. Write a Python program to find words which are greater than given length k.

Q90. Write a Python program to extract unquire dictionary values.

Q91. Write a Python program to merge two dictionary.

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```