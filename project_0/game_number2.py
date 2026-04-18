import numpy as np

def guess_the_number(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    
    max_border = 101 # Верхняя граница
    min_border = 1 # Нижняя
    count = 0 # Подсчет попыток
    
    while True:
        count += 1
        random_number = (max_border + min_border) // 2 # Объединяю две границы и делю на 2, для точки отсчета поиска
        
        if random_number == number:
            break 
        
        elif random_number > number: # Если число больше тчки отсчета, то присваиваю новую верхнуюю границу и таким образом ниже делаю
            max_border = random_number
            
        else:
            min_border = random_number + 1
        
    return count

#print(guess_the_number(number=97)) # Проверял работоспособность

def average_value (guess_the_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        average_value ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    list_numbers = [] # Список для чисел
    np.random.seed(20) # Установил, чтобы рандомное число у всех было 20
    random_array = np.random.randint(1, 101, size=1000)
    
    for num in random_array:
        list_numbers.append(guess_the_number (num)) 
        
    average = int(np.mean(list_numbers))
    print (f"Ваш алгоритм угадывает в среднем за: {average} попыток")
    return average

if __name__ == "__main__":
    # RUN
    average_value (guess_the_number)