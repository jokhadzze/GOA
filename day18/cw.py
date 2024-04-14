# მომხმარებელს შემოატანინეთ სახელი. თქვენი დავალებაა, რომ შეადაროთ სახელი მის lowercase ვარიანტთან == ოპერატორის გამოყენებით.

# name = input("enter your name: ")
# name1 = name.lower()
# print(name == name1)


# # მომხმარებელს შემოატანინეთ სიტყვა. for ციკლის გამოყენებით შეამოწმეთ მისი თითოეული ასო და თუ რომელიმე იქნება lowercase, 
# # მაშინ მომხმარებელს შემოატანინეთ სიტყვა თავიდან. ასევე დაბეჭდეთ თუ რამდენჯერ მოუწია მომხმარებელს სიტყვის შემოტანა - counter.

# word = input("enter a word: ")
# for i in word: 
#     if i == i.lower():
#         print(input('enter again:'))


# მომხმარებელს შემოატანინეთ სიტყვა. თქვენი დავალებაა, რომ ლუწ ინდექსებზე მყოფი ასოები გარდაქმნათ uppercase-ად,
#  ხოლო კენტ ინდექსებზე მყოფები lowecase-ად, საბოლოოდ კი დაბეჭდოთ შედეგი.
        
# user_word = input("Please enter uppercase word: ")

# result = ''

# for index in range(len(user_word)):
#     if index % 2 == 0:
#         result = result + user_word[index].upper()
#     else:
#         result = result + user_word[index].lower()

# print(result)



# ცვლადში შეინახეთ თქვენი სახელი. თუ მისი სიგრძე აღემატება ხუთს, გარდაქმენით მთლიანი სიტყვა uppercase-ად, 
# სხვა შემთხვევაში კი lowecase-ად. საბოლოოდ კი დაბეჭდეთ გარდაქმნილი სახელი.

# name = "Nina"
# if len(name) > 5:
#     print(name.upper())
# else:
#     print(name.lower())


# # სიაში შეინახეთ თქვენი სახელი და გვარი. capitalize მეთოდის გამოყენებით მასივის ყველა ელემენტზე მოახდინეთ
# #  მუშაობა და ბოლოს დაბეჭდეთ უკვე შეცვლილი სია.
    

# def capitalize(my_list):
#     new_list = []
#     for x in my_list:
#         new_list.append(x.capitalize())
#     return new_list
# print(capitalize(["nina", "jokhadze"]))




# meore xerxi:

# names = ["luka", "gio", "lile", "nia"]

# for index in range(len(names)):
#     names[index] = names[index].capitalize()

# print(names)




# მომხმარებელს შემოატანინეთ სახელი, შემდეგ კი გვარი. შეინახეთ ისინი სიაში და წინა დავალების მსგავსად იმუშავეთ
#  ყველა ელემენტზე capitalize მეთოდით. თქვენი დავალებაა, რომ გამოიტანოთ მომხმარებლის ინიციალები სთრინგის
#  სახით. test case: input) "Data", "Tezelashvili" -> output: "D.T"


# firstname = input("Please enter your firstname: ").capitalize()
# lastname = input("Please enter lastname: ").capitalize()

# result = firstname[0] + '.' + lastname[0]

# print(result)




# მოხმარებელს შემოატანინეთ სიტყვა და საძიებელი ასო. თქვენი დავალებაა, რომ სიტყვაში პირველივე შემხვედრი
#  ამ ასოს ინდექსი დაბეჭდოთ, არ არსებობის შემთხვევაში კი უბრალოდ -1.

  


# word = input("enter a word: ")
# char = input("enter a letter: ")
# print(word.find(char))

    




# თქვენი დავალებაა, რომ შექმნათ იგივე ლოგიკა რაც წინა დავალებაში გქონდათ, უბრალოდ find მეთოდის 
# გარეშე - გამოიყენეთ ციკლი. საბოლოოდ შეამოწმეთ ორივე ალგორითმის მუშაობა და შეამოწმეთ იგივე შედეგებს თუ მიიღებთ.

# word = input("enter a word: ")
# char = input("enter a letter: ")
# for i in word:
#     if i == char:
#         print(word.index(char))
#     else:
#         print("-1")




# def manual_find(collection, find_item):
#     for index in range(len(collection)):
#         if collection[index] == find_item:
#             return index
#     return -1

# print(manual_find([1,2,3,4,5], 8))


# # სიაში შეინახეთ თქვენი ოჯახისწევრების სახელები. თქვენი დავალებაა, რომ ისინი
# #  ერთმანეთთან დააკავშიროთ "-"თი და დაბეჭდოთ ერთი სთრინგის სახით.

# fam = ["Vika", "Gia", "Guram", "Nina"]
# print("-".join(fam))



# მომხმარებელს შემოატანინეთ ხუთი სიტყვა და ყველა მათგანი დაამატეთ ერთ სიაში. შემდეგ შეეკითხეთ შესაერთებელი მნიშვნელობა, 
# მაგ. "-" / "+" / "^" და ა.შ. თქვენი დავალებაა რომ იმუშავოთ სიაზე: მხოლოდ ლუწ ინდექსიან სიტყვებს დაუწეროთ ბოლოში
# ეს დასაკავშირებელი მნიშვნელობა და შემდეგ დაამატოთ საერთო სთრინგში. საბოლოოდ კი უნდა დაბეჭდოთ ეს სთრინგი.
# Test case: input) ("python", "html", "css", "js", "git"), "+" -> output) "python+css+git".

# string_list = []

# for i in range(5):
#     word = input("Please enter word: ")
#     string_list.append(word)

# join_char = input("Please enter char to join strings in list: ")

# result = ""

# for index in range(len(string_list)):
#     if index % 2 == 0:
#         result = result + string_list[index] + join_char

# result = result[:-1]

# print(result)





# join_char = input("Please enter char to join strings in list: ")
# result = ""

# for i in range(5):
#     word = input("Please enter word: ")
#     if i % 2 == 0:
#         result = result + word + join_char


# print(result[0:-1])




# დავალება: ახალ მეთოდებიდან თითოეულზე - lower, upper, capitalize, find, join მოიფიქრეთ ერთი ალგორითმი თქვენით.
# ეს ალგორითმი უნდა იყოს გამოსადეგი და ბევრ სიტუაციაზე იყო მოსახერხებელი


