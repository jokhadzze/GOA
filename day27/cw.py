# ვქმნით ფუნქციას def keyword-ის გამოყენებით და ვარქევთ manual_pop.
def manual_pop(collection, remove_index):
# ვამოწმებთ, რომ გადაცემული რიცხვი(ინდექსი, რომელზეც მფგომი მნიშვნელობა უნდა წავშალოთ) არ აღემატება სთრინგის სიგრძეს.
    if remove_index >= len(collection):
# თუ აღემატება, ვაბრუნებთ:
        return "Index out of range"

# ვადეკლარირებთ ცარიელ ლისტს 
    result = []
# for ციკლის გამოყენებით index ცვლადს გადავატარებთ collection ცვლადის სიგრძის დიაპაზონს
    for index in range(len(collection)):
# ვამოწმებთ უდრის თუ არა index ცვლადის რიცხვითი მაჩვენებელი remove_index-ისას.
# თუ არ უდრის, result ლისტში ვამატებთ მოცემულ ინდექსზე მდგარ ელემენტს.
# შემდეგ კი ვაბრუნდებტ result-ს.
        if index != remove_index:
            result.append(collection[index])

    return result

print(manual_pop(["Luka", "lile"], 1))