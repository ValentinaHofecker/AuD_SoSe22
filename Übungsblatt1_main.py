# (1) name_age
def name_age():
    # get name and age as input from user
    name = input ("Enter your name: ")
    age = input ("Enter your age: ")
    # print name and age in format: "Hello <name>. Your age is: <age>"
    print("Hello " + name + ". Your age is: " + age)
    # return name and age (as concatenated string e.g., "Ada28")
    return (name + age)
    
print(name_age())


# (2) swap_integers
def swap_integers(x, y):
    tmp = x
    x = y
    y = tmp
    print("After swap:")
    print("x =", x)        
    print("y =", y)
    return int(x) + int(y) 

x = 10
y = 22
print("x =", x)        
print("y =", y)        
print("Return value:", swap_integers(x, y))


# (3) check_numbers
def check_numbers(num1, num2):
    print("Number 1:", num1)
    print("Number 2:", num2)
    # checks if num1 or num2 is divisable by 6
    if (num1 % 6 == 0 or num2 % 6 == 0):
        # checks if num1 and num2 is divisable by 10
        if (num1 % 10 == 0 and num2 % 10 == 0):
            return True
    # if one of the conditions (or both) is false, return false        
    return False

print("Return value:", check_numbers(6, 10))


# (4) sum_up
def sum_up(num1, num2):
    if (not (num2 > num1)):
        return 0
    if (not (num1 > 0 and num2 > 0)):
        return 0
    sum = 0
    for x in range(num1, num2 + 1):
        sum += x    # sum = sum + x
    return sum
    
print(sum_up(3, 9))


# (5) circle_area
def circle_area(r1, r2, r3):
    # area = PI * r^2
    area1 = 3.141 * r1**2
    area2 = 3.141 * r2**2
    area3 = 3.141 * r3**2
    return (area1 + area2 + area3)
    
print("The combined area of the given circles is: ", circle_area(1, 2, 3))


# (6) check_string
def check_string(text): 
    # ignore case (lower case stays lower case; turns upper case into lower case, so that it works)
    lowerText = text.lower()
    # not necessary to add return True / return False, already included in startswith / endswith 
    return (lowerText.startswith("a") or lowerText.endswith("a"))
    """ 
    Alternative solution:
    # Example: "anna" = ['a', 'n', 'n', 'a'] (= Index 0 - 4)
    
    if (lowerText[0] == "a" or lowerText[len(lowerText) - 1] == "a"):        
        return True
    else:
        return False
    """

print(check_string("annA")) # true
print(check_string("philipp")) # false
print(check_string("valentina")) # true


# (7) triangle
def triangle(rows):
    row = ""
    # for loop: x = counter, range(rows) = number iterations (Wiederholung)
    # at each iteration * gets added to row variable and prints it 
    for x in range(rows):
        row += '*'
        print(row)

triangle(4)
