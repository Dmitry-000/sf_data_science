import numpy as np
"""угадай число"""
game = np.random.randint (1, 101)

count = 0

while True:
    count +=1
    test_number = int (input ("введите число: "))
    
    if test_number > game:
        print ("число меньше")
    elif test_number < game:
        print ("число больше")
    else:
        print (f"вы выйграли. Число {game}, за {count} попыток")
        break