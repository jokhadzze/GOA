 # 1) მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ დაბეჭდეთ lower, upper, capitalize ვარიანტებად.

name=(input('enter your name: '))
print(name.lower())
print(name.upper())
print(name.capitalize())


# 2) `შექმენით ფუნქცია, სახელად find_index, რომელსაც გადაეცემა სთრინგი და საპოვნელი ასო. თქვენი დავალებაა,
# რომ გადაცემულ სთრინგში არსებული ასოს ინდექსი დააბრუნოთ.

def find_index(word, char):
    for index in range (len(word)):
        if word[index] == char:
            return index
print(find_index('flower', 'w'))


# 3) def keyword'ის გამოყენებით შექმენით len()'ის მსგავსი ფუნქცია ( ფუნქცია რომელიც გამოიტანს რამდენი ელემენტია list'ში).

def my_len(arr):
    result = 0
    for i in arr:
        result+=1
    return result
print(my_len(["yba", 'bazaleti', 5, True]))

# 4) გატესტეთ insert, pop, len, append და ახსენით თქვენი სიტყვებით თუ რას აკეთებს.

listn = [4, 'bacon', False]
listn.insert(2, 14.7)
print(listn)
# insert მეთოდი ამატებს ელემენტს ლისტში მოცემულ ინდექსზე.

listm = [4, 'bacon', False]
listm.pop(1)
listm.pop()
print(listm)
# pop ფუნქცია ლისტიდან შლის მოცემულ ინდექსზე არსებულ ელემენტს(თუ ფრჩხილებში ინდექსს არ გადავცემთ, წაიშლება ბოლო ელემენტი).

listo = [4, 'bacon', False]
x = len(listo)
print(x)
# len ფუნქცია აბრუნებს ლისტში არსებული ელემენტების რაოდენობას.

listx = [4, 'bacon', False]
listx.append('audi')
print(listx)
# append მეთოდი ლისტში ამატემს გადაცემულ ელემენტს.3333333333333333