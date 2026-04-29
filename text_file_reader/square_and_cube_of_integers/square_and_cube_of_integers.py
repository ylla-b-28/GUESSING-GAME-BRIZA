def process_integers():
    with open("integers.txt", "r") as source, \
         open("double.txt", "w") as double_out, \
         open("triple.txt", "w") as triple_out:

      for line in source:
         if line.strip():
            number = int(line.strip())
         if number % 2 == 0:
            double_out.write(f"{val**2}\n")
         else:
           triple_out.write(f"{val**3}\n")

process_integers()
