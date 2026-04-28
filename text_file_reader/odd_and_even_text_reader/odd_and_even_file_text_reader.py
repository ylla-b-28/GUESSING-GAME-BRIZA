class OddEvenNumberSorter:

    def __init__(self, target_file):
        self.target_file = target_file
        self.even_results = "even.txt"
        self.odd_results = "odd.txt"

    def sort_the_numbers(self):
        try:
            with open(self.target_file, "r") as file_to_read:
                lines_from_file = file_to_read.readlines()

            with open(self.even_results, "w") as even_file, open(self.odd_results, "w") as odd_file:
                for line in lines_from_file:
                    single_number = int(line.strip())

                    if single_number % 2 == 0:
                        even_file.write(str(number_value) + '\n')
                    else:
                        odd_file.write(str(number_value) + '\n')

            print("Successfully sorted the numbers into even.txt and odd.txt!")

        except FileNotFoundError:
            print("The file numbers.txt was not found. Please make it first.")

if __name__ == "__main__":
    my_sorter = OddEvenNumberSorter("numbers.txt")
    my_sorter.sort_the_numbers()