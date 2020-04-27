# import re
# from datetime import datetime

# def parse_user_data(line):
#     return tuple(re.split(" |@", line))


# print(parse_user_data(('John Doe john.doe@example.com')))


# def compare_lists(dir_a, dir_b):
#     """
#     {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
#     """
#     removed = sorted(list(set(dir_a)-set(dir_b)))
#     added = sorted(list(set(dir_b)-set(dir_a)))

#     return{"removed": removed, "added": added}




# print(compare_lists(dir_a=['hello.py', 'readme.txt'],
#                     dir_b=['readme.txt', 'install.txt', 'hello2.py']))




# def print_log(message, process_id, timestamp, level=2):
    # return(timestamp + " [" + str(process_id) + "] [" + ['TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR'][
    #     level] + "] " + message)




# def biggest_rectangle(rectangles):
#     return max(rectangles, key=lambda r: r[0] * r[1])

# print(biggest_rectangle([(2, 4), (3, 3), (4, 2)]))



