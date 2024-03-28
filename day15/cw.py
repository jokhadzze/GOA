# # 1

def greet_user(name):
    print("hello", name)

greet_user("nina")

greet_user("deme")

# 2

def add(amount, count):
    print(amount + count)

add(5, 10)
add(17, 90)

# 3

def multiply(price, amount):
    print(price * amount)

multiply(20, 3)
multiply(12, 2)


# დავალება: შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი და 
# სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /

def multiply(num1, num2):
    print(num1 * num2)

multiply(19, 23)

def sum(number1, number2):
    print(number1 + number2)

sum(3, 12)
def devide(num1, num2):
    print(num1 / num2)

devide(165, 10)

def deduction(num1, num2):
    print(num1 - num2)

deduction(33, 7)

# დავალება2: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის სიგრძესა და სიმაღლეს, გამოითვლით მის ფართობს

def area_of_a_rectangle(length, width):
    print(length * width)

area_of_a_rectangle(12, 5)

# დავალება3: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის ოთხ გვერდს, გამოითვლით მის პერიმეტრს

def perimetr_of_a_rectangle(length, width):
    print((length + width) * 2)

perimetr_of_a_rectangle(16, 13)

# დავალება4: შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ სიის რიცხვების ჯამი, არ გამოიყენოთ sum

def calculate_sum(lst):
    total = 0
    for num in lst:
        total += num
    print("The sum of the numbers in the list is:", total)
my_list = [1, 2, 3, 4, 5]
calculate_sum(my_list)
    

#  შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და 
# მაქსიმალურ რიცხვებს, არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else, indexing, print


def min_max ( arr ):
    a = arr[0]
    for i in arr:
        if i < a:
            a = i

    
    y = arr[0]
    for x in arr:
        if x > y:
            y = x
            
             
        
    print(a, y)

min_max ([1,3,4,5,-6,5,6,1,-2,-3,-4,-5])


    
