# შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების კოლექცია. თქვენ უნდა განიხილოთ მთლიანი კოლექცია: 
# თუ რიცხვი იქნება მთელი - გაამრავლეთ ორზე, ხოლო თუ რიცხვი იქნება ათწილადი - გაამრავლეთ ოთხზე. 
# ყველა რიცხვი დაამატეთ ახალ სიაში და დააბრუნეთ ეს სია.
# [1, 1.5, 2, 2.5] -> [2, 6, 4, 10]

def multiply_operations(nums):
    x=[]
    for i in nums:
        if type(i)==int:
            x.append(i * 2)
        if type(i)==float:
            x.append(i * 4)
    return x
print(multiply_operations([1, 1.5, 2, 2.5]))



# შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. ლუწ ინდექსებზე მყოფი სახელები გადაიყვანეთ uppercase-ში,
# ხოლო კენტ ინდექსებზე მყოფნი კი lowercase-ში.
# ["chad1", "chad2", "chad3", "chad4"] -> ["CHAD1", "chad2", "CHAD3", "chad4"]

def cases(names):
    arr =[]
    for index in range(len(names)):
        if index % 2 == 0:
            arr.append(names[index].upper())
        else:
            arr.append(names[index].lower())
    return arr
print(cases(["chad1", "chad2", "chad3", "chad4"]))


# შექმენით ფუნქცია, რომელსაც გადაეცემა ერთი დიდი წინადადება. ამ წინადადებაში, ყველა სიტყვა დაიწყეთ დიდი
# ასოთი და დააბრუნეთ წინადადება ამ სახით.
# "hello, this is goa" -> "Hello, This Is Goa"

def cases(n):
	word = ""
	n= n.split()
	for char in n:
		word += f"{char.capitalize()} "
	return word
print(cases("hello, this is goa"))



# შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ ამ სიიდან მოაშოროთ დუპლიკატები 
# (ისეთი ელემენტები, რომლებიც სიაში ერთზე მეტჯერ გვხვდება) და დააბრუნოთ განახლებული სია.
# [1, 1, 1, 2, 3, 4] -> [2, 3, 4]

def duplicates(listn):
    a = listn[0]
    listm = []
    for i in listn:
        if i != a:
            listm.append(i)
    return listm
print(duplicates([1, 1, 1, 2, 3, 4]))



# შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიაში არსებული დუპლიკატები.
# [1, 1, 1, 2, 3, 4] -> [1, 1, 1]

def duplicates(listn):
    a = listn[0]
    listm = []
    for i in listn:
        if i == a:
            listm.append(i)
    return listm
print(duplicates([1, 1, 1, 2, 3, 4]))



# 7. შექმენით ფუნქცია, რომელსაც გადაეცემა კოლექცია და საძიებელი სიტყვა. თქვენი დავალებაა, რომ 
# დააბრუნოთ თუ რამდენჯერ გვხვდება საძიებელი სიტყვა კოლექციაში.
# [1, 1, 1, 2, 3, 4], 1 -> 3

def amount_of_chars(listo, char):
    amount = 0
    for i in listo:
        if i == char:
           amount +=1
    return amount
print(amount_of_chars([1, 1, 1, 2, 3, 4], 1)) 



# შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, დააბრუნოთ ახალი სია, სადაც არ იქნება ლუწი რიცხვები.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [1, 3, 5, 7, 9]

def no_evens(listq):
    lists = []
    for i in listq:
        if i % 2 != 0:
            lists.append(i)
    return lists
print(no_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# შექმენით ფუნქცია, რომელსაც გადაეცემა ორი სია. თქვენი დავალებაა, გააერთიანოთ ეს ორი სია და დააბრუნოთ ერთი დიდი სიის სახით.
# [1, 5, 8], [2, 3, 4] -> [1, 5, 8, 2, 3, 4]

def concatanation(listn, listm):
    concanetanatied = []
    for i in listn:
        concanetanatied.append(i)
    for i in listm:
        concanetanatied.append(i)
    return concanetanatied
print(concatanation([1, 5, 8], [2, 3, 4]))



# შექმენით ფუნქცია, რომელსაც გადაეცემა კოლექცია. თქვენი დავალებაა, დააბრუნოთ ახალი კოლექცია, 
# სადაც გვექნება ისეთი ელემენტები, რომლებიც საწყის კოლექციაში მარტო ერთჯერ გვხვდება.
# [1, 1, 1, 2, 3, 4] -> [2, 3, 4]

def duplicates(listn):
    a = listn[0]
    listm = []
    for i in listn:
        if i != a:
            listm.append(i)
    return listm
print(duplicates([1, 1, 1, 2, 3, 4]))

