# XI. Counting sheep

sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def count_sheeps(sheep):

    sleeping_sheeps = 0

    for one_sheep in sheep:
        if one_sheep == True:
            sleeping_sheeps = sleeping_sheeps + 1
    
    return sleeping_sheeps

print(count_sheeps(sheeps))
