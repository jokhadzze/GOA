def litres(time):
    return time // 2



def paperwork(n, m):
    # Happy Coding! ^_^
    if m < 0 or n < 0:
        return 0
    
    else:
        return m * n
    


def grow(arr):
    result = 1
    for i in arr:
        result = result * i
    return result
    


def fake_bin(x):
    result = ""
    
    for i in x:
        if int(i) < 5:
            result += "0"
        else:
            result +="1"
    
    return result




def to_jaden_case(string):
    listn = string.split()
    new_list = []
    result = []
    for i in listn:
        capitalized = i.capitalize()
        result.append(capitalized)
    return " ".join(result)







def remove_smallest(numbers):
    if numbers == []:
        return [] 
    else:
        min_num = min(numbers)
        index = numbers.index(min_num)

        first = numbers[:index]
        second = numbers[index + 1:]
    return first + second





# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once








# # accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(st):
    listn = []
    for i in range(1, len(st) + 1):
        listn.append((st[i - 1]* i).capitalize())
    return "-".join(listn)






def likes(names):
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        return(f"{names[0]} likes this")
    elif len(names) == 2:
        return(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3:
        return(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")







# 1. თქვენ მუშაობთ სიაზე, სადაც მოცემულია ნებისმიერი მონაცემი, მაგალითად "hello", 4.14, True და ა.შ.
# თქვენი დავალებაა, რომ ამ სიაში მოცემული მთელი რიცხვების ჯამი დაბეჭდოთ ტერმინალში.
# 1. [1, 2, 3, True, False, 1.5, 3.14, 5, "Hello"] -> 11

random = [1, 2, 3, True, False, 1.5, 3.14, 5, "Hello"]
result = []
for i in random:
    if type(i) == int:
        result+=i
print(result)







# 2. თქვენ მუშაობთ რიცხვების სიაზე, შესაძლოა გქონდეთ როგორც მთელი რიცხვები, ასევე ათწილადები.
# დავალებაა, რომ დააბრუნოთ სიის რიცხვების ჯამი, მაგრამ  ამ ჯამში არ შევა მაქსიმალური და მინიმალური მნიშვნელობები.
# [4, 10, 2, 20, 4.4 6.6] -> 27

# nums = [4, 10, 2, 20, 4.4, 6.6]
# result = []
# a= nums[0]
# for i in nums:
#     if i > a and i < a:
#         a = i
#     nums.pop(a)
# result = sum(nums)
# print(result)



# 3. მომხმარებელს შემოატანინეთ დადებითი მთელი რიცხვი. შემდეგ გამოიყენეთ ციკლი, სიაში დაამატეთ ყველა ამ რიცხვის გამყოფი და დაბეჭდეთ ეს სია.
# 3. 10 - [1, 2, 5, 10]

num = int(input("enter a positive integer: "))
for i in range(1, num+1):
    if num % i == 0:
        print(i)




# 4. მომხმარებელს შემოატანინეთ სიტყვა და შემდეგ განიხილეთ ამ სიტყვის ყველა ასო. 
# lowercase გადააკეთეთ uppercase-ად, ხოლო uppercase კი lowercase-ად.
# "HeLLo WORld" -> "hEllO worLD

sentence = input("enter smth: ")
for i in sentence:
    if i.isupper():
        i.lower()
    else:
        i.upper()
print(sentence)




# 5. თქვენ გადმოგეცემათ მთელი რიცხვების სია. დავალებაა, რომ ყველაზე ხშირად განმეორებადი რიცხვის
# რაოდენობა დააბრუნოთ ამ სიიდან. ამ დავალების სია აიღეთ ქვემოთ მოცემული test case-იდან.
# [1, 1, 1, 1, 3, 4, 5, 6] -> 4

# nums = [1, 1, 1, 1, 3, 4, 5, 6]
# amount = 0
# a = nums[0]
# for i in nums:
