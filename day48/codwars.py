def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    test = test.lower()
    original = original.lower()
    
    for char in test:
        if test.count(char) != original.count(char):
            return False
    
    return True



def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump



def hero(bullets, dragons):
    return bullets >= dragons * 2



def count_by(x, n):
    result = []
    for i in range(1,n + 1):
        result.append(i * x)
    return result



def sum_mix(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total




def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    joined = (test + original).lower()
    
    for char in joined:
        if joined.count(char) % 2 != 0:
            return False
    
    return True