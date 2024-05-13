# 1) შექმენით ფუნქცია, რომელშიც გააერთიანებთ იმ ფუნქციებს რაც დღეს ვისწავლეთ (lower(), upper(), capitalize(), find())

def funcs(w1,w2,w3,w4,w5):
    w11 = w1.upper()
    w22 = w2.lower()
    w33 = w3.capitalize()
    w44 = w4.find("d")
    w55 = "".join(w5)
    return w11, w22, w33, w44, w55
print(funcs("wild", "CoMbO", "helmet", "freedom", "a very long day"))


# 2) შექმენით ფუნქცია რომელსაც გადაეცემა list = ["name1" , "name2" , "name3"....] შემდეგ მომხმარებელს კითხეთ
# რომელი ინდექსის შეცვლა სურს და ამის მიხედვით შეცვალეთ ის კონკრეტული ინდექსი თქვენი სასურველი სტრინგით და 
# ბოლოს შეაერთეთ join() ფუნქციის მეშვეობით 


def my_func(listn):
    index = int(input("which index do you wanna change between 0-" +  str(len(listn) - 1) + ":"))
    listn[index] = "workout"
    result = ".".join(listn)
    return result
print(my_func(["leg day" , "chest day" , "cadio"]))




# 3) დეტალურად, კომენტარის სახით ახსენით split() და join() ფუნქციები, შეეცადეთ ახსნათ chad-ურად,
# წარმოიდგინეთ რომ მეგობარს უხსნით ვინც პროგრამირებაზე არაფერი იცის 

# split()--ეს ფუნქცია ჩვენმიერ დადეკლარირებული ცვლადის სტრინგ ტიპის მნიშვნელობას ხლეჩს გარდაქმნის ლისტად.
rule = "fight fix stay"
rules = rule.split()
print(rules)

# join() -- ამ ფუნქციის საშუალებით ჩვენ შეგვიძლია ლისტში ცალკეულ სტრინგებს შორის ჩავსვათ ჩვენთვის სასურველი
#           სიმბოლოები და მოვახდინოთ კონკატენაცია ლისტის ელემენტებში და გარდავქმათ ერთ, მთლიან სტრინგად. 
 

def my_func(arr):
    x = "dm".join(arr)
    return x
print(my_func(["jelly", "fish"])) 


