is_male = True
if is_male:
    print('You are a male ')
else:
    print('You are not a male ')


is_male = True
is_tall = True
if is_male or is_tall:
    print('You are a male ot tall or both')
else:
    print('You neither are male nor tall')


is_male = True
is_tall = False
if is_male and is_tall:
    print('You are a tall male')
else:
    print('You are either not male or not tall ')


is_male = True
is_tall = False
if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print('You are a short male')
else:
    print('You are either not male or not tall ')
