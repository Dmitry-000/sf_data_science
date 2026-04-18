import numpy as np

def guess_the_number(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    
    max_border = 101 #верхняя граница
    min_border = 1 # нижняя
    count = 0 # подсчет попыток
    
    while True:
        count += 1
        random_number = (max_border + min_border) // 2 #
        
        if random_number == number:
            break 
        
        elif random_number > number:
            max_border = random_number
            
        else:
            min_border = random_number + 1
        
    return count

#print(guess_the_number(number=97)) # проверял работоспособность

def average_value (guess_the_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        average_value ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    list_numbers = [] #список для чисел
    np.random.seed(20) #установил, чтобы рандомное число у всех было 20
    random_array = np.random.randint(1, 101, size=1000)
    
    for num in random_array:
        list_numbers.append(guess_the_number (num)) 
        
    average = int(np.mean(list_numbers))
    print (f"Ваш алгоритм угадывает в среднем за: {average} попыток")
    return average

if __name__ == "__main__":
    # RUN
    average_value (guess_the_number)