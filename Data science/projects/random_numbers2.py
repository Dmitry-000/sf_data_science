import numpy as np
def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): загадываем число

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count +=1
        predict_nomber = np.random.randint (1, 101)
        if number == predict_nomber:
            break
    return count 


print(f'Количество попыток: {random_predict()}')



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    
    np.random.seed(1) # фиксируем сид для воспроизводимости
    # число, которое задаёт начальную точку для алгоритма генерации псевдослучайных чисел.
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    # size Простыми словами: он говорит функции, сколько именно чисел нужно сгенерировать и как их расположить.

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    # np.mean(count_ls): Функция из библиотеки NumPy складывает все элементы массива и делит сумму на их количество.

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__': #активировать эту часть, чтобы если потребуется импортировать код он не активирвался сразу
    ruscore_game(random_predict)
    
    
#score_game(random_predict)