# შექმენით ფუნქცია, რომელსაც გადასცემთ თქვენ სახელს და გვარს. გამოიყენეთ split, 
# indexing და დაბეჭდეთ თქვენი ინიციალები. test case: input) David Tezelashvili -> output) D.T

name = "nina jokhadze"
x = name.split()
for i in x:
    print(i[0])

# შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის საშუალო არითმეტიკული (ჯამი / სიგრძე)

arr = [6, 8, 10, 12]

def Arithmetic_average(num1, num2):
    print(num1 / num2)

Arithmetic_average(sum(arr), len(arr))

# შექმენით ფუნქცია, რომელსაც გადასცემთ სიტყვას და შემოწმდება არისთუ 
# არა ის პალინდრომი (პალინდრომია სიტყვა, თუ მისი შებრუნებულიც იგივე გამოდის, მაგ: level)

x = "level"

def checking_palindromity_of_a_word():
    print(bool)

if x == x[::-1]:
    print("True")
else:
    print("False")


# შექმენით ფუნქცია, რომელსაც გადასცემთ სთრინგს. თქვენი დავალებაა, რომ ამ სთრინგს მოაშოროთ
# ყველა სფეისი - space და დაბეჭდოთ ამ სახით test case: input) "     Goal-   Oriented   Academy    "
# -> output) "Goal-OrientedAcademy"

txt = "nina hates cardio"
i = txt.replace(" ", "")
print(i)


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
