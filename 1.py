# Friend or Foe?

def friend(x):
    names_list = []
    set_list = set(x)
    new_list = list(set_list)
    
    for name in x:
        if len(name) == 4:
            if name in new_list:
                new_list.remove(name)
                names_list.append(name)
    return names_list    
   
   
print(friend(["Иван", "Борис","Ира","Тома","Иван","Женя","Евгений","Женя","Женя","Петр"]))



        




    
