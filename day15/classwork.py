# შექმენით ფუნქცია, რომელსაც გადასცემთ თქვენ სახელს და გვარს. გამოიყენეთ split, 
# indexing და დაბეჭდეთ თქვენი ინიციალები. test case: input) David Tezelashvili -> output) D.T

# name = "nina jokhadze"
# x = name.split()
# for i in x:
#     print(i[0])


def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    
    firstname = splited_fullname[0]
    lastname = splited_fullname[1]
    
    result = firstname[0] + "." + lastname[0]
    
    print(result)
   

initial_chars("Luka Tskhvaradze")

# შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის საშუალო არითმეტიკული (ჯამი / სიგრძე)

arr = [6, 8, 10, 12]

def Arithmetic_average(num1, num2):
    print(num1 / num2)

Arithmetic_average(sum(arr), len(arr))


def average_arithmetic(number_list):
    jami = sum(number_list)
    result = jami // len(number_list)
    print(result)

average_arithmetic([1,2,3])

# შექმენით ფუნქცია, რომელსაც გადასცემთ სიტყვას და შემოწმდება არისთუ 
# არა ის პალინდრომი (პალინდრომია სიტყვა, თუ მისი შებრუნებულიც იგივე გამოდის, მაგ: level)

x = "level"

def checking_palindromity_of_a_word():
    print(bool)

if x == x[::-1]:
    print("True")
else:
    print("False")



def is_palindrom(word):
    reversed_word = ''
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]
    
    print(reversed_word == word)


is_palindrom("ana")


# შექმენით ფუნქცია, რომელსაც გადასცემთ სთრინგს. თქვენი დავალებაა, რომ ამ სთრინგს მოაშოროთ
# ყველა სფეისი - space და დაბეჭდოთ ამ სახით test case: input) "     Goal-   Oriented   Academy    "
# -> output) "Goal-OrientedAcademy"

txt = "nina hates cardio"
i = txt.replace(" ", "")
print(i)


def remove_spaces(word):
    word_without_space = ''
    
    for char in word:
        if char != " ":
            word_without_space = word_without_space + char
    
    print(word_without_space)

remove_spaces("Luka Tskhvaradze")


# შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. ამ სიაში უნდა გქონდეთ როგორც დადებითი, ასევე უარყოფითი რიცხვები.
#  თქვენი დავალებაა, რომ გამოიტანოთ უარყოფითი რიცხვების რაოდენობა და დადებითი რიცხვების ჯამი (გამოიყენეთ for ციკლი ორივეზე)


def rkina( arr ):

    neg_num = 0
    non_neg_num = 0
    new_arr = []
    for el in arr:
        if el <= -1:
            neg_num += 1
        
        
        else:
            
            non_neg_num += el
    print(neg_num, non_neg_num)

rkina( [1,3,4,5,5,6,-1,-2,-3,-4,-5,-6] )



def func(number_list):
    sum = 0
    quantity = 0
    
    for num in number_list:
        if num >= 0:
            sum = sum + num
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

func([1,2,3,-1,-2,-3])





def my_replace(word,char1,char2):
    replaced_word = ''
    
    for i in word:
        if i == char1:
            replaced_word = replaced_word + char2 
        else:
            replaced_word = replaced_word + i
    
    print(replaced_word)

my_replace("Luka Tskhvaradze", "k", "i")
