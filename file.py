def print_names(filename):
   with open(filename, 'r') as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")
            if len(parts)>= 2: #Ensures at least last and first names
              last_name = parts[0]
              first_name = parts[1]
              print(first_name, last_name)
print_names("comma.csv")   

         


