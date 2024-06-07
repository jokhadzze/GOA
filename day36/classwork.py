ninchik = {'name': 'nina',
           'lastname': 'jokhadze',
           'height': 180,
            'age':16 }

to_join = ninchik.values
values_joined = " ".join([str(i) for i in to_join()]) 

print(values_joined)

    