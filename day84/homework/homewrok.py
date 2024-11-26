string = "A&&!B"
count = 0
for i in string:
    if i == "A":
        count = count + 1

print(count)



ch = input("Please enter a letter : ")
if ch.islower() == "a" or "i" or "e" or "u" or "o":
    print("The letter is a vowel")
else:
    print("The letter is a consonant")

ch1 = ch.lower()
if ch1 in "aeiou":
    print("The letter is a vowel")
else:
    print("the letter is a consonant")





arr = []
for i in range(4):
    arr.append(int(input("Please enter a number: ")))

num1 = arr[0]
index1 = 0
for i in range(len(arr)):
    if arr[i] > num1:  
        num1 = arr[i]
        index1 = i

arr.pop(index1)
num2 = arr[0]
for i in range(len(arr)):
    if arr[i] > num2:  
        num2 = arr[i]
        
print(num1 * num2)