# # დავალება1: შექმენით ფუნქცია სახელად manual_pop, რომელსაც გადაეცემა სია და ინდექსი. როდესაც გადაეცემა ინდექსი,
#  სიიდან უნდა ამოიშალოს ამ ინდექსზე მყოფი ელემენტი და დაბრუნდეს სია ამ სახით. ამ დავალებისთვის გამოიყენეთ for ციკლ

def manual_pop(listn, indx):
    listm = []
    for i in range(0,len(listn)):
        if i != indx:
            listm.append(i)
    return listm

print(manual_pop([1,2,3,],1))




# დავალება2: შექმენით ფუნქცია სახელად manual_count:ფუნქციას გადაეცემა სია და ელემენტი. 
# თქვენ უნდა დაითვალოთ სიაში ამ ელემენტის რაოდენობა. წინა დავალების მსგავსაც, აქაც for ციკლი გამოიყენეთ

def manual_counter(arr, item):
    counter = 0
    for i in arr:
        if i == item:
            counter += 1
    return counter
print(manual_counter(["nina", "deme", "deme", "deme", "nina"], "deme"))


# Bonus: შექმენით ფუნქცია სახელად manual index, რომელსაც გადაეცემა სია და ერთი მნიშვნელობა. როდესაც გაიგებთ ამ ელემენტის ინდექსს,
#  დააბრუნეთ ის. გამოიყენეთ for ციკლი, არ გამოიყენოთ .index. 

def manual_index(collection, value):

    for index in range(0, len(collection)):
        if collection[index] == value:
            return index
    
    return -1


print(manual_index("Luka", "k"))
