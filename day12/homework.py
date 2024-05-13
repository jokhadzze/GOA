#1

arr = []
name = input("please, enter your name: ")
last_name = input("please, enter your last name: ")
age = int(input("please, enter your age: "))
location = input("please, enter your location: ")


arr.append(name)
arr.append(last_name)
arr.append(age)
arr.append(location)
print(arr)

print(arr[0:2])
print(arr[1:3])
print(arr[0:3])
print(arr[1::])


#2

numbers = []
num = int(input("enter a negative number: "))

for i in range(num,0):


    numbers.append(i)
print(numbers)

#3   

ninchik = ["nina", "jokhadze"]
print(ninchik[0])
print(ninchik[1])

#4

movies = ["breaking bad", "the black phone", "after ever happy", "my fault", "henry danger"]
print(movies[3::])
print(movies[0:2])
print(movies[2:5])
print(movies[-1:-3])
print(movies[-3::])

#5

academy = input("please, enter your academy's name: ")

if academy[0] == "G" :
    print("GOA is the best choise")

else:
    print("you made the wrong decision")