#open the file
numbers_file = open('numbers.txt', 'r')

#create a list
all_numbers_list = []

#read every line
for line in numbers_file:

    #strip
    real_number = int(line.strip)
    all_numbers_list.append(real_number)

#open 2 files
even_numbers_file = open('even_numbers.txt', 'w')
odd_numbers_file = open('odd_numbers.txt', 'w')

#decide where each number goes
for current_number in all_numbers_list:
    if current_number % 2 == 0:
        even_numbers_file.write(str(current_number) + '\n')
    else:
        odd_numbers_file.write(current_number)

#close
even_numbers_file.close()
odd_numbers_file.close()