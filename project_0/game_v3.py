import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:
    """Пытаемся найти ответ методом бисекции. Этот итерационный метод 
    ищет ноль функции, деля отрезок поиска пополам на каждом шаге.


    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # инициируем счетчик
    border = 100 # срединная точка
    width = border # ширина диапазона
    
    if number == border: # проверка на случай, ответ на самом краю полного диапазона
        count = 1
    
    while number != border:
       count += 1
       width = round(width / 2.0) # сужаем диапазон в два раза
       border += width * (number-border) // abs(number-border) # смещаем серединную точку на полдиапазона 
    # в сторону, определяемую знаком проверки. Вместо того, чтобы городить систему условий, 
    # я решил воспользоваться математическим оператором sgn().
    # К сожалению, я не разобрался, как его найти в Python, поэтому заявил его через старый добрый abs 

    return count



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)



def mean_count(random_predict) -> int:
    """Мне показалось странным, что для метрики скорости алгоритма 
    используется радномный прогон через большой массив случайных чисел,
    в то время как ее асимптотическое значение вычисляется очень легко через 
    матожидание. Поэтому я написал дополнительную функцию, которая делает это.
    В ней функции скармливаются все значения от 1 до 100 и вычисляется средне арифметическое

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    sum = 0 # инициирую сумму количества попыток для всех входных чисел
    
    for i in range(1, 100):
        sum += random_predict(i)    
    
    score = int(sum/100)

    print(f'Матожидание количества попыток вашего алгоритма равно {score}')
    return(score)    



#Run benchmarking to score effectiveness of all algorithms
#You can compare benchmarking based on random numbers with the exact one 
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for random_predict with mean_count: ', end='')
print(mean_count(random_predict))


print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for game_core_v2 with mean_count: ', end='')
print(mean_count(game_core_v2))


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

print('Run benchmarking for game_core_v3 with mean_count: ', end='')
print(mean_count(game_core_v3))