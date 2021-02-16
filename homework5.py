#1)Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при этом из каждой строки должно быть удалено только четное количество таких слов.
#
#2)Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.
#
#3) Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
#
#4)Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит ip адрес, время 
#и название дня недели (например, 139.18.150.126 23:12:44 sunday). Создайте новый текстовый файл, который 
#бы содержал список ip без повторений из первого файла. Для каждого ip укажите количество посещений, 
#наиболее популярный день недели. Последней строкой в файле добавьте наиболее популярный отрезок времени 
#в сутках длиной один час в целом для сайта.
import csv
from datetime import *

if __name__ == '__main__':
    #----------------------------------------------------------------------------------#
    # 1
    #----------------------------------------------------------------------------------#
    new_lines = []
    with open(r'.\homework5_data\1.txt', 'r', encoding='utf-8') as f:
        for line in f:
            unwanted_words = [unwanted_word for unwanted_word in line.split() if 3 <= len(unwanted_word.strip('.,?!()\'')) <= 5]
            unwanted_word_count = len(unwanted_words)
            unwanted_word_count = unwanted_word_count if unwanted_word_count % 2 == 0 else unwanted_word_count - 1
            clean_line = line
            for i in range(unwanted_word_count):
                clean_line = clean_line.replace(unwanted_words[i] + ' ', '', 1)
            new_lines.append(clean_line)

    with open(r'.\homework5_data\1.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    #----------------------------------------------------------------------------------#
    # 2
    #----------------------------------------------------------------------------------#
    file_path = r'.\homework5_data\2_input.txt'
    required_phones = []

    with open(r'.\homework5_data\2_input.txt', 'r', encoding='utf-8') as f:
        required_phones = [line.split()[2] + '\n' for line in f if line.split()[1][0] in ['С', 'К']]

    with open(r'.\homework5_data\2_output.txt', 'w', encoding='utf-8') as f:
        f.writelines(required_phones)

    #----------------------------------------------------------------------------------#
    # 3
    #----------------------------------------------------------------------------------#
    file_path = r'.\homework5_data\3.txt'
    new_lines = []

    with open(file_path, 'r', encoding='utf-8') as f:
        current_lines = [string for string in f]
        max_len = len(max(current_lines, key=len))
        new_lines = [string.rjust(max_len, ' ') for string in current_lines]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    #----------------------------------------------------------------------------------#
    # 4
    #----------------------------------------------------------------------------------#
    input_file_path = r'.\homework5_data\4_input.csv'
    output_file_path = r'.\homework5_data\4_output.txt'
    output_data = []
    
    with open(input_file_path, newline='', encoding='utf-8') as csvfive:
        reader = csv.DictReader(csvfive)
        input_data = list(reader)
        unique_ip = set([row['ip'] for row in input_data])
        for ip in unique_ip:
            day_list = [row['day'] for row in input_data if row['ip'] == ip]
            visits_count = len(day_list)
            most_popular_day = max(day_list, key=day_list.count)
            output_data.append(f'{ip} {visits_count} {most_popular_day}\n')
        
        times = []
        time_list = [datetime.strptime(row['time'], "%H:%M:%S") for row in input_data]
        for visit_time in time_list:
            start = visit_time.time()
            end = (visit_time + timedelta(hours=1)).time()
            visits_count = len([row for row in time_list if start <= row.time() < end])
            times.append((start, end, visits_count))
        popular_time = max(times, key=lambda el : el[2])
        output_data.append(f'Самый популярный период времени: {popular_time[0]} - {popular_time[1]}')
        
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.writelines(output_data)
            