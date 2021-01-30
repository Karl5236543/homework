import pprint


if __name__ == "__main__":
    #---------------------------------------------------------------------------#
    # 1
    #---------------------------------------------------------------------------#
    result_dict = {}
    for key in range(11):
        result_dict[key] = key * key
    print(f'1:\t{result_dict}')

    #---------------------------------------------------------------------------#
    # 2
    #---------------------------------------------------------------------------#
    result_list = [ number for number in range(101) if number % 2 == 0]
    print(f'2:\t{result_list}')

    #---------------------------------------------------------------------------#
    # 3
    #---------------------------------------------------------------------------#
    old_string = 'произвольная строка'
    vowels = ('а','о','у','ы','э','и')
    result_string = old_string
    for ch in old_string:
        if ch not in vowels:
            result_string = result_string.replace(ch,'a')
    print(f'3:\t{old_string} --> {result_string}')

    #---------------------------------------------------------------------------#
    # 4.1
    #---------------------------------------------------------------------------#
    numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 2, 32, 76, 3, 10, 0, 1]
    unique_numbers = list(set(numbers))
    print(f'4.1:\t{unique_numbers}')

    #---------------------------------------------------------------------------#
    # 4.2
    #---------------------------------------------------------------------------#
    numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 2, 32, 76, 3, 10, 0, 1]
    max_numbers = []
    unique_numbers = set(numbers)
    for _ in range(3):
        max_num =  max(unique_numbers)
        unique_numbers.remove(max_num)
        max_numbers.append(max_num)
    print(f'4.2:\t{max_numbers}')

    #---------------------------------------------------------------------------#
    # 4.3
    #---------------------------------------------------------------------------#
    numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 2, 32, 76, 3, 10, 0, 1]
    min_number = min(numbers)
    index = numbers.index(min_number)
    print(f'4.3:\t{index}')

    #---------------------------------------------------------------------------#
    # 4.4
    #---------------------------------------------------------------------------#
    numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 2, 32, 76, 3, 10, 0, 1]
    print(f'4.4:\tinverted numbers --> {numbers[::-1]}')

    #---------------------------------------------------------------------------#
    # 5
    #---------------------------------------------------------------------------#
    dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
    dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }
    shared_keys = list(set(dict_one.keys()).intersection(set(dict_two.keys())))
    print(f'5:\t{shared_keys}')

    #---------------------------------------------------------------------------#
    # 6.1
    #---------------------------------------------------------------------------#
    data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

    data.sort(key = lambda el : el['age'])
    print('6.1:')
    pprint.pprint(data)

    #---------------------------------------------------------------------------#
    # 6.2
    #---------------------------------------------------------------------------#
    cities = [row['city'] for row in data]
    unique_sities = set(cities)
    result = {}
    for city in unique_sities:
        result[city] = [row for row in data if row['city'] == city]
    print('6.2:')
    pprint.pprint(result)

    #---------------------------------------------------------------------------#
    # 7
    #---------------------------------------------------------------------------#
    def most_frequent(list_var):
        str_counts = []
        unique_str_list = list(set(list_var))
        for string in unique_str_list:
            str_counts.append({
                    'string': string.lower(),
                    'count': list_var.count(string.lower())
                })
        return sorted(str_counts, key = lambda el : el['count'])[-1]['string']
    
    list_var = 'В начале июля, в чрезвычайно жаркое время, под вечер, один молодой человек вышел из своей каморки, которую нанимал от жильцов в С — м переулке, на улицу и медленно, как бы в нерешимости, отправился к К — ну мосту.'.split()
    most_frequent_str = most_frequent(list_var)
    print(f'7:\nlist_var: {list_var}\nРезультат: {most_frequent_str}')
    
    #---------------------------------------------------------------------------#
    # 8
    #---------------------------------------------------------------------------#
    input_number = 123123010012
    number_str = str(input_number)
    sum = 0
    for number in number_str:
        sum += int(number)
    print(f'8:\t{input_number} --> {sum}')

    #---------------------------------------------------------------------------#
    # 9
    #---------------------------------------------------------------------------#
    def some_function(array:list, n):
        if len(array) <= n:
            return -1
        return array[n]**n
    
    print(f'9:\tsome_function([1,2,3,6,7],4) --> {some_function([1,2,3,6,7],4)}')
    print(f'\tsome_function([1,2,3,6,7],5) --> {some_function([1,2,3,6,7],5)}')

    #---------------------------------------------------------------------------#
    # 10
    #---------------------------------------------------------------------------#
    word_list = "12 dawd d 212 dwa 13 daw".split()
    count = 0
    is_three_words = False
    for word in word_list:
        if word.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            is_three_words = True
            break
    print(f'10:\t{word_list} --> {is_three_words}')
    
