import time

#OPTIONS
def option1():
    print("You selected Printing  in Python")
    print()
    any = input("Press any key to continue... ")
    print()
    print("The print() function in Python is used to print a specified message on the screen.\nThe print command in Python prints strings or objects which are converted to a string while printing on a screen.")
    print("+"+"-"*56+"+")
    print("| Syntax:\t\t\tExample:\t\t |\n| print(object(s))\t\tprint('Hello World')     |")
    print("+"+"-"*56+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Creating a Comment")
    print("Comments starts with a #, and Python will ignore them:")
    print("+"+"-"*23+"+")
    print("| Example:\t\t|")
    print("| #This is a comment\t|")
    print("| print('Hello World')\t|")
    print("| \t\t\t|")
    print("| Output:\t\t|\n| Hello World\t\t|")
    print("+"+"-"*23+"+")
    while True:
        print()
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            print("Another example:\nTo print the Welcome to Programming, use the Python print statement as follows:")
            print("+"+"-"*35+"+")
            print("| Example:\t\t\t    |\n| print('Welcome to Programming')   |")
            print("+"+"-"*35+"+")
            sug1()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug1()
            break
        else:
            print("Invalid")
            continue
def option2():
    print("You selected Variable Definition\n\n\t\tVARIABLE\nVariables are containers for storing data values.")
    print("+"+"-"*66+"+")
    print("| BASIC DATA TYPES:\t\t\t\t\t\t   |\n| • string(Sentence,Phrases,Characters):identifier = 'Hello World' |")
    print("| • int(Positive&Negative Numbers);identifier = 5\t\t   |\n| • float(Decimal Numbers):identifier = 3.1415\t\t\t   |")
    print("| • bool(True or False):identifier = True\t\t\t   |\n| Syntax:\t\tExample:\t\t\t\t   |\n| variable = value\tfirstName = 'James'\t\t\t   |\n|\t\t\tlastName = 'De Mesa'\t\t\t   |")
    print("+"+"-"*66+"+")
    print()
    any = input('Press any key to continue... ')
    print()
    print("Input function")
    print("The input() function allows user to input.")
    print("You can use a variable with the input function.")
    print("+"+"-"*55+"+")
    print("| Syntax: \t\t\t\t\t\t|")
    print("| variable = input(value)\t\t\t\t|")
    print("| \t\t\t\t\t\t\t|")
    print("| Example:\t\t\t\t\t\t|")
    print("| name = input('Enter your name: ')\t\t\t|")
    print("| print(Hi, name)\t\t\t\t\t|")
    print("| \t\t\t\t\t\t\t|")
    print("| Output:\t\t\t\t\t\t|")
    print("| Enter a name:  #<-- You can input after this\t\t|")
    print("| Hi,     #<-- Then it will print the name you input\t|")
    print("+"+"-"*55+"+")
    while True:
        print()
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            print("+"+"-"*32+"+")
            print("| Another example:\t\t |")
            print("| Example:\t\tOutput:  |")
            print("| x = 5\t\t\t5\t |\n| y = 'James'\t\tJames\t |")
            print("| z = True\t\tTrue\t |")
            print("| print(x)\t\t\t |\n| print(y)\t\t\t |\n| print(z)\t\t\t |")
            print("+"+"-"*32+"+")
            sug2()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug2()
            break
        else:
            print("Invalid")
            continue
def option3():
    print("You selected Operators in Python\n\n\t\t\tPYTHON OPERATORS\nOperators are used to perform operations on variables and values.")
    print()
    print("ARITHMETIC OPERATORS\nArithmetic operators are used with numeric values to perform common mathematical operations:")
    print()
    print("+"+"-"*39+"+")
    print("| Operator\tName\t\tExample |")
    print("+"+"-"*39+"+")
    print("| +\t\tAddition\t x + y  |\n| -\t\tSubraction\t x - y  |")
    print("| *\t\tMultiplication\t x * y  |\n| /\t\tDivision\t x / y  |")
    print("| %\t\tModulus\t\t x % y  |\n| **\t\tExponentiation\t x ** y |")
    print("| //\t\tFloor Division\t x // y |")
    print("+"+"-"*39+"+")
    print()
    print("+"+"-"*23+"+")
    print("| Example:\tOutput: |\n| x = 6\t\t11\t|\n| y = 5\t\t\t|\n| print(x+y)\t\t|")
    print("+"+"-"*23+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("CONDITIONAL OPERATORS\nConditional operators are used to compare values in Conditional Statements:")
    print()
    print("+"+"-"*55+"+")
    print("| Operator\tName\t\t\t\tExample |")
    print("+"+"-"*55+"+")
    print("| ==\t\tEqual\t\t\t\tx == y  |\n| !=\t\tNot Equal\t\t\tx != y  |")
    print("| >\t\tGreater than\t\t\tx > y   |\n| <\t\tLess than\t\t\tx < y   |")
    print("| >=\t\tGreater than or equal to\tx >= y  |\n| <=\t\tLess than or equal to\t\tx <= y  |")
    print("+"+"-"*55+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("LOGICAL OPERATORS\nLogical operators are used to combine conditional statements:")
    print("+"+"-"*100+"+")
    print("| Operator\tDescription\t\t\t\t\t\t\tExample\t\t     |")
    print("+"+"-"*100+"+")
    print("| and\t\tReturns True if both statements are true\t\t\tx < 5 and x < 10     |\n| or\t\tReturns True if one of the statements is true\t\t\tx < 5 or x < 4\t     |")
    print("| not\t\tReverse the result, returns False if the result is true\t\tnot(x < 5 and x < 10)|")
    print("+"+"-"*100+"+")
    while True:
        print()
        exa = input("Do you want more example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            print("Another Example:\n")
            print("+"+"-"*39+"+")
            print("| num = int(input('Enter a number: '))  |")
            print("| product = 5*num\t\t\t|")
            print("| print(product)\t\t\t|")
            print("+"+"-"*39+"+")
            sug3()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug3()
            break
        else:
            print("Invalid")
            continue
def option4():
    print("You selected Conditions in Python\n\n\t\t\tPYTHON CONDITIONS AND IF STATEMENT\nA statement that makes the program smarter, ", end="")
    print("it makes the program decides on what to do in certain CONDITIONS")
    print("+"+"-"*63+"+")
    print("| CONDITIONAL STATEMENTS\t\t\t\t\t|")
    print("| • IF Statement (1 conditon)\t\t\t\t\t|\n| • IF-ELSE Statement(2 conditions)\t\t\t\t|\n| • IF-ELIF-ELSE Statement (3 or more conditions)\t\t|")
    print("| • NESTED Conditional Statements (Condition after a Condition  |")
    print("+"+"-"*63+"+")
    print("INDENTATION: Indentation is used indicate what statements are included inside the Conditional Statements")
    print("+"+"-"*57+"+")
    print("| Example:\t\t\t\t\t\t  |\n| a = 26\t\t\t\t\t\t  |\n| b = 300\t\t\t\t\t\t  |\n| if b > a:\t\t\t\t\t\t  |\n| print('b is greater than a') #This will create an error |")
    print("+"+"-"*57+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("IF STATEMENT\nUsed when dealing with One Condition.")
    print("+"+"-"*55+"+")
    print("| Syntax:\t\t\tExample:\t\t|\n| if ValueOne == ValueTwo:\tif age >= 18:\t\t|\n|    #Do Something\t\t    print('Legal Age')\t|")
    print("+"+"-"*55+"+")
    print()
    print("IF-ELSE STATEMENT\nUsed when dealing with TWO Conditions.")
    print("+"+"-"*55+"+")
    print("| Syntax:\t\t\tExample:\t\t|\n| if ValueOne == ValueTwo:\tif age >= 18:\t\t|\n|    #Do Something\t\t    print('Legal Age')\t|")
    print("| else:\t\t\t\telse:\t\t\t|\n|    #Do Something\t\t    print('Too Young')\t|")
    print("+"+"-"*55+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("IF-ELIF-ELSE STATEMENT\nUsed when dealing with THREE OR MORE Conditions.")
    print("+"+"-"*55+"+")
    print("| Syntax:\t\t\tExample:\t\t|\n| if Value1 == Value2:\t\tif age >= 18:\t\t|\n|    #Do Something\t\t    print('Legal Age')  |")
    print("| elif Value1 >= Value2:\telif age >= 13:\t\t|\n|    #Do Something\t\t    print('Teenager')   |\n| else:\t\t\t\telse:\t\t\t|\n|    #Do Something\t\t    print('Too Young')  |")
    print("+"+"-"*55+"+")
    print()
    print("NESTED CONDITIONAL STATEMENT\nUsed when dealing with CONDITIONAL INSIDE A CONDITION")
    print("+"+"-"*71+"+")
    print("| Syntax:\t\t\tExample:\t\t\t\t|\n| if Value1 == Value2:\t\tif age >= 18:\t\t\t\t|")
    print("|    if Value3 == value4\t    if height >= 170:\t\t\t|\n|\t#Do Something\t\t\tprint('Legal and Tall')\t\t|")
    print("|    elif value3 == Value5\t    elif height >= 156:\t\t\t|\n|\t#Do Something\t\t\tprint('Legal and Average')\t|")
    print("|    else:\t\t\t    else:\t\t\t\t|\n|\t#Do Something\t\t\tprint('Legal Age and Short')    |")
    print("+"+"-"*71+"+")
    while True:
        print()
        exa = input("Do you want an more example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            print("Another example:")
            print("+"+"-"*47+"+")
            print("| username = 'James'\t\t\t\t|")
            print("| password = '123456'\t\t\t\t|")
            print("| \t\t\t\t\t\t|")
            print("| user = input('Enter your username: ')\t\t|")
            print("| passs = input('Enter your password: ')\t|")
            print("| \t\t\t\t\t\t|")
            print("| if user == username and passs == password:    |")
            print("|    print('LOGIN SUCESSFULLY')\t\t\t|")
            print("| else:\t\t\t\t\t\t|")
            print("|    print('LOGIN DENIED')\t\t\t|")
            print("+"+"-"*47+"+")
            sug4()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug4()
            break
        else:
            print("Invalid")
            continue
def option5():
    print("You selected Loops in Python\n\nLOOPS IN PYTHON\npart of programming that allows specific statement to be repeated until a certain  condition is met or succeed.")
    print()
    print("There are two types of loops in Python:\n• For Loop - it is used to iterate through collection or to execute a block of code in a certain amount of codes\n  (Keyword: For, In) (Function: range)")
    print("• While Loop - it will repeat a block of code as long as it's conditon is fullfilled.")
    print()
    any = input("Press any key to continue... ")
    print()
    print("+"+"-"*64+"+")
    print("| For loop Syntax:\t\t\tExample:\t\t |\n| for identifier in range(number):\tfor a in range(100):\t |\n|    #Do Something\t\t\t    print('Programming') |")
    print("|\t\t\t\t\t\t\t\t |")
    print("| The output will be a 100 of 'Programming'\t\t\t |")
    print("+"+"-"*64+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("+"+"-"*31+"+")
    print("| While loop syntax:\t\t|\n| while value1 > value2\t\t|\n|    #Do Something\t\t|")
    print("|\t\t\t\t|")
    print("| Example:\t\tOutput:\t|\n| i = 3\t\t\t1\t| \n| while i < 6:\t\t2\t|\n|   print(i)\t\t3\t|\n|   i = i+1\t\t4\t|\n|\t\t\t5\t|")
    print("+"+"-"*31+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("BREAK STATEMENT - With the break statement we can stop the loop even if the while condition is true:")
    print("+"+"-"*31+"+")
    print("| Example:\t\t\t|\n| Exit the loop when i is 3.\t|")
    print("|\t\t\t\t|")
    print("| i = 1\t\t\tOutput: |\n| while i > 6:\t\t1\t|")
    print("|   print(i)\t\t2\t|\n|   if i == 3:\t\t3\t|\n|   break\t\t\t|\n|   i = i+1\t\t\t|")
    print("+"+"-"*31+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("CONTINUE STATEMENT - With the continue statement we can stop the current iteration, and continue with the next:")
    print("Skip the iteration if the variable i is 3, but continue with the next iteration:")
    print("+"+"-"*31+"+")
    print("| Example:\t\tOutput\t|")
    print("| for i in range(9):\t0\t|")
    print("|    if i ==3:\t\t1\t|")
    print("|     continue\t\t2\t|")
    print("|    print(i)\t\t4\t|")
    print("|\t\t\t5\t|")
    print("|\t\t\t6\t|")
    print("|\t\t\t7\t|")
    print("|\t\t\t8\t|")
    print("+"+"-"*31+"+")
    while True:
        print()
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            print("Another example:")
            print("A program that identify the number if even or odd and ask if you want to continue.")
            print("+"+"-"*49+"+")
            print("| crt = True\t\t\t\t\t  |\n| even = 0\t\t\t\t\t  |\n| odd = 0\t\t\t\t\t  |")
            print("|\t\t\t\t\t\t  |")
            print("|while crt = True:\t\t\t\t  |")
            print("|    num = int(input('Enter a number: '))\t  |")
            print("|    ans = input('Do you want to continue? y/n:') |")
            print("|\t\t\t\t\t\t  |")
            print("|    if num%2 == 0:\t\t\t\t  |")
            print("|        even = even+1\t\t\t\t  |")
            print("|    else:\t\t\t\t\t  |")
            print("|        odd = odd+1\t\t\t\t  |")
            print("|\t\t\t\t\t\t  |")
            print("|    if ans == 'n':\t\t\t\t  |")
            print("|        print('Program terminated')\t\t  |")
            print("|        break\t\t\t\t\t  |\n|        crt = False\t\t\t\t  |")
            print("|    elif ans == 'y':\t\t\t\t  |\n|        continue\t\t\t\t  |")
            print("|    else:\t\t\t\t\t  |")
            print("|        print('Invalid Input')\t\t\t  |\n|        break\t\t\t\t\t  |")
            print("|\t\t\t\t\t\t  |")
            print("| print('The number of even numbers is', even)\t  |")
            print("| print('The number of odd numbers is', odd)\t  |")
            print("+"+"-"*49+"+")    
            sug5()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug5()
            break
        else:
            print("Invalid")
            continue
def option6():
    print("You selected Functions in Python\n\nFUNCTIONS\nAre used to organize and divide specific tasks in a program that will only run when called.")
    print()
    print("Creating a Function\nIn Python a function is defined using the def keyword:")
    print("+"+"-"*31+"+")
    print("| Example:\t\t\t|\n| def my_function():\t\t| \n|    print('Hello World')\t|")
    print("+"+"-"*31+"+")
    print()
    print("Calling a Function\nTo call a function, use the function name followed by parenthesis:")
    print("+"+"-"*31+"+")
    print("| Example:\t\t\t|\n| def my_function():\t\t|\n|    print('Hello World')\t|")
    print("| \t\t\t\t|")
    print("| my_function()\t\t\t|")
    print("| \t\t\t\t|")
    print("| Output:\t\t\t|\n| Hello World\t\t\t|")
    print("+"+"-"*31+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Arguments\nInformation can be passed into functions as arguments.")
    print("Arguments are specified after the function name, inside the parentheses.\nYou can add as many arguments as you want, just separate them with a comma.")
    print("+"+"-"*63+"+")
    print("| Syntax:\t\t\t\tExample:\t\t|")
    print("| def function_name(parameter):\t\tdef sayHi(name):\t|")
    print("|    #Do Something\t\t\t    print('Hi,',name)   |")
    print("|\t\t\t\t\t\t\t\t|")
    print("| function_name(parameter)\t\tsayHi('James')\t\t|")
    print("|\t\t\t\t\t\t\t\t|")
    print("| Output:\t\t\t\t\t\t\t|\n| Hi, James\t\t\t\t\t\t\t|")
    print("+"+"-"*63+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Return Values\nIs a value returned after a Function is done executing")
    print("it is used to get results from a function that computes or does something that needs a result.")
    print("+"+"-"*63+"+")
    print("| Syntax:\t\t\t\tExample:\t\t|")
    print("| def function_name(parameter):\t\tdef add(num):\t\t|")
    print("|    return value\t\t\t    return 2*num\t|")
    print("|\t\t\t\t\t\t\t\t|")
    print("| function_name(parameter)\t\tprint(add(3))\t\t|")
    print("+"+"-"*63+"+")
    while True:
        print()
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print("Another example:")
            print("+"+"-"*55+"+")
            print("| def biodata(name, age, address)\t\t\t|")
            print("|    print('Hi', name,' ', age, 'Located at', address)  |")
            print("|\t\t\t\t\t\t\t|")
            print("| biodata('James', 19, 'Lucena City')\t\t\t|")
            print("+"+"-"*55+"+")
            sug6()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug6()
            break
        else:
            print("Invalid")
            continue
def option7():
    print("You selected Array in Python")
    print()
    any = input("Press any key to continue... ")
    print()
    print("ARRAYS\nArrays are used to store multiple values in one single variable.")
    print()
    print("+"+"-"*42+"+")
    print("| Example:\t\t\t\t   |\n| Create an array containing fruit names.  |")
    print("| fruits = ['apple', 'mango', 'banana']    |")
    print("+"+"-"*42+"+")
    print()
    print("To call out an specific value in an array you need to refer to the index")
    print("But what is an Index?")
    print()
    any = input("Press any key to continue... ")
    print()
    print("INDEX\nThe number of where an item is on a collection\nIndex starts with 0")
    print("+"+"-"*40+"+")
    print("| Index        0        1         3      |")
    print("| fruits = ['apple', 'mango', 'banana']  |")
    print("+"+"-"*40+"+")
    print()
    print("+"+"-"*40+"+")
    print("| Example:\t\t\t\t |\n| Get the value of the first array item: |")
    print("| fruits = ['apple', 'mango', 'banana']  |")
    print("| print(fruits[0])\t\t\t |")
    print("|\t\t\t\t\t |")
    print("| Output:\t\t\t\t |\n| apple\t\t\t\t\t |")
    print("+"+"-"*40+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("+"+"-"*47+"+")
    print("| You can also modify the value inside an array |\n| Example:\t\t\t\t\t|")
    print("| fruits = ['apple', 'mango', 'banana']\t\t|")
    print("| fruits[1] = 'orange'\t\t\t\t|")
    print("| print(fruits)\t\t\t\t\t|")
    print("|\t\t\t\t\t\t|")
    print("| Output:\t\t\t\t\t|\n| ['apple', 'orange', 'banana']\t\t\t|")
    print("+"+"-"*47+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("The Length of an Array")
    print("Use the len() method to return the length of an array")
    print("(the number of elements in an array).")
    print("+"+"-"*55+"+")
    print("| Example:\t\t\t\t\t\t|\n| Return the number of elements in the fruits array:    |")
    print("| fruits = ['apple', 'mango', 'banana']\t\t\t|")
    print("| print(len(fruits))\t\t\t\t\t|")
    print("|\t\t\t\t\t\t\t|")
    print("| Output:\t\t\t\t\t\t|\n| 3\t\t\t\t\t\t\t|")
    print("+"+"-"*55+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Adding Array Elements")
    print("You can use the append() method to add an element to an array.")
    print("+"+"-"*40+"+")
    print("| Example: \t\t\t\t |")
    print("| fruits = ['apple', 'mango', 'banana']  |")
    print("| car.append('orange')\t\t\t |")
    print("| print(fruits)\t\t\t\t |")
    print("|\t\t\t\t\t |")
    print("| Output:\t\t\t\t |\n| ['apple', 'mango', 'banana', 'orange'] |")
    print("+"+"-"*40+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("You can also use insert()")
    print("To add an element at the specified position")
    print("+"+"-"*40+"+")
    print("| Example: \t\t\t\t |")
    print("| fruits = ['apple', 'mango', 'banana']  |")
    print("| fruits.insert(1,'orange')\t\t |")
    print("| print(fruits)\t\t\t\t |")
    print("|\t\t\t\t\t |")
    print("| Output:\t\t\t\t |\n| ['apple', 'orange', 'banana', 'mango'] |")
    print("+"+"-"*40+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Removing Array Elements")
    print("You can use the pop() method to remove an element from the array.")
    print("+"+"-"*40+"+")
    print("| Example: \t\t\t\t |")
    print("| fruits = ['apple', 'mango', 'banana']  |")
    print("| fruits.pop(1)\t\t\t\t |")
    print("| print(fruits)\t\t\t\t |")
    print("|\t\t\t\t\t |")
    print("| Output:\t\t\t\t |\n| ['apple', 'banana']\t\t\t |")
    print("+"+"-"*40+"+")
    print()
    while True:
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print("Another example:")
            print("+"+"-"*39+"+")
            print("| courses = ['BSIT', 'BSCS', 'BLIS']\t|")
            print("| \t\t\t\t\t|")
            print("| print(courses[0])\t\t\t|")
            print("+"+"-"*39+"+")
            sug7()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug7()
            break
        else:
            print("Invalid")
            continue
def option8():
    print("You selected Dictionary in Python")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Dictionary")
    print("A collection of Key pairs that is Unordered, Changeable, and Indexed.")
    print("+"+"-"*46+"+")
    print("| Syntax:\t\tExample:\t       |")
    print("| identifier = {\tStudent = {\t       |")
    print("|     key1 = value1,\t    'name': 'James',   |")
    print("|     key2 = value2,\t    'course': 'BSIT',  |")
    print("|     key3 = value3\t    'age': 19\t       |")
    print("| }\t\t\t}\t\t       |")
    print("+"+"-"*46+"+")
    print("+"+"-"*48+"+")
    print("| Example: \t\t\t\t\t |")
    print("| Student = { \t\t\t\t\t |")
    print("|   'name': 'James',\t\t\t\t |")
    print("|   'course': 'BSIT'\t\t\t\t |")
    print("|   'age': 19 \t\t\t\t\t |")
    print("| }\t\t\t\t\t\t |")
    print("| print(Student)\t\t\t\t |")
    print("|\t\t\t\t\t\t |")
    print("| Output:\t\t\t\t\t |")
    print("| {'name': 'James', 'course': 'BSIT', 'age': 19} |")
    print("+"+"-"*48+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Reading Dictionary Items")
    print("You can read a dictionary by specifying the Key Value.")
    print("+"+"-"*32+"+")
    print("| Syntax:\t\t\t |")
    print("| print(dictionary[key])\t |")
    print("| \t\t\t\t |")
    print("| Example: \t\t\t |")
    print("| Student = { \t\t\t |")
    print("|   'name': 'James',\t\t |")
    print("|   'course': 'BSIT'\t\t |")
    print("|   'age': 19 \t\t\t |")
    print("| }\t\t\t\t |")
    print("| print(Student[name])\t\t |")
    print("|\t\t\t\t |")
    print("| Output:\t\t\t |")
    print("| James \t\t\t |")
    print("+"+"-"*32+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Assigning Dictionary ITEMS")
    print("You can a value of a certain item in a dictionary by specifying the Key Value and using the Assignment Operator '='")
    print("+"+"-"*32+"+")
    print("| Syntax:\t\t\t |")
    print("| dictionary[key] = value\t |")
    print("| \t\t\t\t |")
    print("| Example:\t\t\t |")
    print("| Student = { \t\t\t |")
    print("|   'name': 'James',\t\t |")
    print("|   'course': 'BSIT'\t\t |")
    print("|   'age': 19 \t\t\t |")
    print("| }\t\t\t\t |")
    print("| student[name] = 'Patrick'\t |")
    print("| \t\t\t\t |")
    print("| print(Student[name])\t\t |")
    print("|\t\t\t\t |")
    print("| Output:\t\t\t |")
    print("| Patrick \t\t\t |")
    print("+"+"-"*32+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Dictionary ADD ITEMS")
    print("You can add items on a dictionary just by assigning a non-existent key value in the dictionary")
    print("+"+"-"*66+"+")
    print("| Syntax:\t\t\t\t\t\t\t   |")
    print("| dictionary[key] = value\t\t\t\t\t   |")
    print("| \t\t\t\t\t\t\t\t   |")
    print("| Example:\t\t\t\t\t\t\t   |")
    print("| Student = { \t\t\t\t\t\t\t   |")
    print("|   'name': 'James',\t\t\t\t\t\t   |")
    print("|   'course': 'BSIT'\t\t\t\t\t\t   |")
    print("|   'age': 19 \t\t\t\t\t\t\t   |")
    print("| }\t\t\t\t\t\t\t\t   |")
    print("| Student['section'] = '1B'\t\t\t\t\t   |")
    print("| \t\t\t\t\t\t\t\t   |")
    print("| print(Student)\t\t\t\t\t\t   |")
    print("|\t\t\t\t\t\t\t\t   |")
    print("| Output:\t\t\t\t\t\t\t   |")
    print("| {'name': 'James', 'course': 'BSIT', 'age': 19, 'section' = '1B'} |")
    print("+"+"-"*66+"+")
    print()
    any = input("Press any key to continue... ")
    print()
    print("Copying a Dictionary")
    print("copy() copies the whole dictionary which can assigned to a new dictionary")
    print("+"+"-"*47+"+")
    print("| Syntax:\t\t\t\t\t|")
    print("| student = {'name': 'James', 'gender': 'male'}\t|")
    print("| StudentTwo = Student.copy()\t\t\t|")
    print("+"+"-"*47+"+")
    print()
    while True:
        exa = input("Do you want an another example? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print("Another example:")
            print("+"+"-"*48+"+")
            print("| car = { \t\t\t\t\t |")
            print("|   'brand': 'Fors',\t\t\t\t |")
            print("|   'model': 'Mustang'\t\t\t\t |")
            print("|   'year': 1964 \t\t\t\t |")
            print("| }\t\t\t\t\t\t |")
            print("| print(Student)\t\t\t\t |")
            print("+"+"-"*48+"+")
            sug8()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            sug8()
            break
        else:
            print("Invalid")
            continue
def optionc():
    print("You selected Command Prompt")
    print()
    any = input("Press any key to cotinue... ")
    print()
    print("Command prompt keys:")
    print("A backslash (\) is used as an escape character at the command prompt (also known as the Windows Command Prompt or cmd.exe).")
    print("It indicates that the following character should be regarded literally rather than as a special character.\n")
    print("In the command prompt, a forward slash (/) is utilized as a directory separator in file paths.")
    print("It is used to identify the various levels or folders in a file hierarchy.\n")
    print("The C: prompt in a command prompt or terminal window shows that the current working directory on a Windows operating system is the C disk.")
    print("This means that any commands or files entered into the command prompt will be executed or saved to the C disk.\n")
    print("A drive is a storage device or partition that is attached to the computer and accessible via the file system in the command prompt.")
    print("Hard disks, USB drives, and network drives are examples.\n")
    print("To display a list of files and directories in a certain folder, use the DIR command in the Command Prompt (Windows) or Terminal (Mac/Linux).\n")
    print("The cd command is used on the command prompt to change the current working directory.")
    print("This means that it alters the file system location to which the command prompt is now pointing.\n")
    print("The arrow up key at the command prompt can be used to traverse through previously submitted commands.")
    print("By pressing the arrow key, you can access the previous command you entered and amend or execute it again.\n")
    print("A command prompt tab is usually used for more technical operations like programming, system management, and automation.\n")
    print("The command prompt path denotes the current directory or location of the command prompt.")
    print("It is represented by the text that displays before the cursor at the start of the command prompt.\n")
    print("Command prompt commands:")
    print("MD - make directory\nREN - rename\nRD - remove directory\nDEL - delete filetype")
    print("\nCommands are entered into the command prompt and then executed by pressing the enter key.")
    print("The command prompt also allows users to run scripts, execute batch files, and perform other advanced tasks.")
    while True:
        print()
        exa = input("Do you want to go to main menu? y/n: ")
        if exa.upper() == "Y" or exa.upper() == "YES":
            print()
            choices()
            break
        elif exa.upper() == "N" or exa.upper() == "NO":
            print("Read with all your heart's content ")
            continue
        else:
            print("Invalid")
            continue

#SUGGESTIONS
#SUGGESTION 1
def sug1():
    print()
    print("Suggested Topics:")
    print("[1] Variable Definition")
    print("[2] Operators in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option2()
            break
        elif cho == 2:
            option3()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUUGESTION 2
def sug2():
    print()
    print("Suggested Topics:")
    print("[1] Operators in Python")
    print("[2] Conditions in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option3()
            break
        elif cho == 2:
            option4()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUGGESTION 3
def sug3():
    print("Suggested Topics:")
    print("[1] Conditions in Python")
    print("[2] Loop in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option4()
            break
        elif cho == 2:
            option5()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUGGESTION 4
def sug4():
    print("Suggested Topic:")
    print("[1] Loop in Python")
    print("[2] Functions in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option5()
            break
        elif cho == 2:
            option6()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUGGESTION 5
def sug5():
    print("Suggested Topic:")
    print("[1] Functions in Python")
    print("[2] Array in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option6()
            break
        elif cho == 2:
            option7()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUGGESTION 6
def sug6():
    print("Suggested Topic:")
    print("[1] Array in Python")
    print("[2] Dictionary in Python")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option7()
            break
        elif cho == 2:
            option8()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid choice")
            continue
#SUGGESTION 7
def sug7():
    print("Suggested Topic:")
    print("[1] Dictionary in Python")
    print("[2] Command Prompt")
    print("[3] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            option8()
            break
        elif cho == 2:
            optionc()
            break
        elif cho == 3:
            choices()
            break
        else:
            print("Invalid Choice")
            continue
#SUGGESTION 8
def sug8():
    print("Suggested Topic: ")
    print("[1] Command Prompt")
    print("[2] Main Menu")
    while True:
        cho = int(input("Please enter your choice: "))
        if cho == 1:
            optionc()
            break
        elif cho == 2:
            choices()
            break
        else:
            print("Invalid Choice")
            continue

#ASKING FOR NAME
name = input("Enter your name: ")
print()
print("Loading the program....")
print()
print("[■□□□□□□□□□] 10%")
time.sleep(.5)
print()
print("[■■□□□□□□□□] 20%")
time.sleep(.5)
print()
print("[■■■□□□□□□□] 30%")
time.sleep(.5)
print()
print("[■■■■□□□□□□] 40%")
time.sleep(.5)
print()
print("[■■■■■□□□□□] 50%")
time.sleep(.5)
print()
print("[■■■■■■□□□□] 60%")
time.sleep(.5)
print()
print("[■■■■■■■□□□] 70%")
time.sleep(.5)
print()
print("[■■■■■■■■□□] 80%")
time.sleep(.5)
print()
print("[■■■■■■■■■□] 90%")
time.sleep(.5)
print()
print("[■■■■■■■■■■] 100%")
time.sleep(.5)
print()
print("Starting...")
time.sleep(.5)
print()
print()
def choices():
    print()
    print("Welcome", name+"!","Here are the menu of fundamentals of Python")
    print("+"+"-"*35+"+")
    print("| [1] Printing in Python            |")
    print("| [2] Variable Definition           |")
    print("| [3] Operators in Python           |")
    print("| [4] Conditions in Python          |")
    print("| [5] Loop in Python                |")
    print("| [6] Functions in Python           |")
    print("| [7] Arrays in Python              |")
    print("| [8] Dictionary in Python          |")
    print("| [9] Command Prompt                |")
    print("| [0] Exit                          |")
    print("+"+"-"*35+"+")
    while True:
        print()
        user = input("Please enter a number of your choice: ")
        if user == "1":
            option1()
            break
        elif user == "2":
            option2()
            break
        elif user == "3":
            option3()
            break
        elif user == "4":
            option4()
            break
        elif user == "5":
            option5()
            break 
        elif user == "6":
            option6()
            break
        elif user == "7":
            option7()
            break
        elif user == "8":
            option8()
            break
        elif user == "9":
            optionc()
            break
        elif user == "0":
            print("You ended the program. Goodbye and Thank you!")
            break
        else:
            print("Invalid choice")
            continue
choices()
