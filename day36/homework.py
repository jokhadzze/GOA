me = {'name': 'nina',
      'lastname': 'jokhadze',
      'height': 180,
      'age':16 }

to_join1 = me.values
joined1 = " ".join([str(i) for i in to_join1()])



mom = {'name': 'vika',
       'lastname': 'jokhadze',
       'height': 171,
       'age':48 }

to_join2 = mom.values
joined2 = " ".join([str(i) for i in to_join2()])





dad = {'name': 'giorgi',
       'lastname': 'jokhadze',
       'height': 183,
       'age':44 }

to_join3 = dad.values
joined3 = " ".join([str(i) for i in to_join3()])





boyfriend = {'name': 'deme',
             'lastname': 'beridze',
             'height': 185,
              'age':15 }


to_join4 = boyfriend.values


joined4 = " ".join([str(i) for i in to_join4()])

result = []
result.append(joined1)
result.append(joined2)
result.append(joined3)
result.append(joined4)


print(str(result))




