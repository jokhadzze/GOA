# 1) გადაიმეორეთ ფუნქციები სოლოლეარნის გამოყენებით და გააკეთეთ თქვენი კრეატიულობით 5 ფუნქცია,
# 2 ფუნქცია რომელიც არ აბრუნებს მნიშვნელობას და 3 ფუნქცია რომელიც აბრუნებს მნიშვნელობას

# def multiply(num1, num2):
#     result = num1 * num2

# print(multiply(3,4))


# def divide(num1, num2):
#     result = num1 / num2

# print(multiply(17,1))


# def deduction(num1, num2):
#     result = num1 / num2

# print(deduction(10,2))


# def firsr_odd_number(num_list):
#     for i in num_list:
#         if i % 2 != 0:
#             return i
# print(firsr_odd_number([2,6,7,9]))


# def multiply_list_members(num_list):
#     total = 1
#     for i in num_list:
#         total = total * i
#     return total
# print(multiply_list_members([3,8,11,7]))


# def find_result_of_deducation(num_list):
#     for i in num_list:
#         if i == num_list[3] - num_list[0]:
#             return i
# print(find_result_of_deducation([3,5,6,7,0,4,2]))


# def  replace_symbols(word, symbol1, symbol2):
#     replaced_word = " "
#     for i in word:
#         if i == symbol1:
#             replaced_word += symbol2

#         else:
#             replaced_word += i

# print(replace_symbols("nina", "n", "b"))

    

# 2) შექმენით ფუნქცია რომელიც სიაში ლუწ ინდექსებზე მდგომ რიცხვთა ჯამს დააბრუნებს, 
# შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი):  9

def sum_even_indexes(num_list):
    total = 0
    for i in num_list[::2]:
         total += i
         print(total)
    return i
            
        

sum_even_indexes([1,2,3,4,5])


# 3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე, დააბრუნეთ სია 
# სადაც იქნება ეს ჯამები ჩასმული, შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9]

def even_odd_sum(num_list):
    total1 = 0
    total2 = 0
    for i in num_list:
        if i % 2 == 0:
            total1 += i
    for x in num_list:
        if x % 2 != 0:
            total2 += x

    y = list((total1, total2))
    print(y)

even_odd_sum([1,2,3,4,5])


# 4) შექმენით ფუნქცია რომელიც დაგიბრუნებთ სიაში მყოფ ელემენტების რაოდენობას, 
# შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი): 5


# def amount_pf_members(arr):
#     amount = 0
#     for i in arr:
#         amount += 1
#     print(amount)
# amount_pf_members([1,2,3,4,5]) 


# 5) შექმენით replace ფუნქციის კოპიო

# def  replace_symbols(word, symbol1, symbol2):
#     replaced_word = " "
#     for i in word:
#         if i == symbol1:
#             replaced_word += symbol2

#         else:
#             replaced_word += i

#     print(replaced_word)
# replace_symbols("nina", "n", "b")


# 6) შექმენით join ფუნქციის კოპიო



