# გადმოგეცემათ რიცხვებით სავსე სია და თქვენ უნდა დააბრუნოთ ამ სიის ელემენტების საშუალო არითმეტიკული

arr = [4,5,7,9,1,3,0]
sum = 0
lenght = len(arr)
result = 0

for i in range(len(arr)):
    sum += arr[i]
    result = sum/lenght
print(result)


# გადმოგეცემათ სია რომელშიც იქნება დადებითი და უარყოფითი რიცხვებიც, თქვენ უნდა დააბრუნოთ ორი სია
# სადაც გაფილტრური იქნება უარყოფითი რიცხვები ცალკე და დადებითი რიცხვები ცალკე

listn = [1,7,-9,6,-3,-5,3]
negnums = []
posnums = []
for i in listn:
    if i > 0:
        posnums.append(i)
    else:
        negnums.append(i)
print(posnums,negnums)