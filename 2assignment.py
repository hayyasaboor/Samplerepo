'''
GCIS123-607
HAYYA SABOOR, 434000367
DHEERAJ SHUIJUKUMAR, 433008033
SAMIYAH SIDDIQUI, 433001732
GROUP MANIFESTO:
HAYYA: Wrote Task 1 and Task 2 functions
DHEERAJ: Wrote Task 3 and Task 4 functions
SAMIYAH: Wrote main function, handled the debugging and testing of the code along with adding
comments and docstrings. 
All participated in discussion of the code and logic, did problem solving 
and reviewed the code.
'''
#-----------------------------------------------------------------------------------------------------------
# TASK 1
#-----------------------------------------------------------------------------------------------------------
import csv
def check_limit(borrowed):
    """
    Task 1: This function checks the no.of books borrowed by a student
    and returns if the student is within limit or has to a pay fine.
    """
    if borrowed < 0:
        return "Error: Invalid number of books"
    elif borrowed <= 3:
      return "Within limit"
    elif 3 < borrowed <= 6:
        return "Over limit: Fine $5"
    else:
        return "Over limit: Fine $10"
#-----------------------------------------------------------------------------------------------------------
# TASK 2
#-----------------------------------------------------------------------------------------------------------
def process_borrowers(filename):
    """
    This function reads a CSV file and checks the no.of books borrowed by each student, 
    their status and prints the name of the student and status. Also handles non-numeric values.
    """
    try:
        with open (filename, 'r') as f: #Open file for reading
            reader = csv.reader(f) #object reads the csv file row by row
            next(reader) #Skips header
            for line in reader: #Processes csv file line by line
                if len(line) != 2:
                    continue
                name, borrowed_str = line[0].strip(), line[1].strip() #Get the students name and the no.of books borrowed
                try:
                    borrowed = int(borrowed_str) #Convert to integer
                    status = check_limit(borrowed) #Get status by looking at the first function
                    if borrowed < 0:
                        print("Error: Invalid number of books for " + name) #Prints error message for invalid input
                    else:
                        print (name, ":", status) 
                except ValueError: #Handle non-numeric values for borrowed_books
                    print("Error: Non-Numeric value for", name)
    except FileNotFoundError:
        print("Error: File", filename, "not found")      
#-----------------------------------------------------------------------------------------
# TASK3 3
# ---------------------------------------------------------------------------------------           
def calculate_average_books(filename):  
    """
    This function calculates the average no.of books borrowed by students
    and handles non-numeric values and negative values
    """   
    try: 
        total_books = 0
        student_count = 0
        #Open CSV file and read line by line
        with open(filename, 'r') as f:
            reader = csv.reader(f) #Reads csv file
            next(reader)
            for line in reader:
                if len(line) != 2:
                    continue #Skips invalid lines
                borrowed_str = line[1].strip()     #Get no.of books borrowed            
                try:
                    borrowed = int(borrowed_str) #convert books into integers
                    if borrowed >= 0:
                        total_books += borrowed #incrementing total books
                        student_count += 1
                except ValueError:
                    continue #Skips non-numeric values
        #Calculate average
        if student_count > 0:
            avg = total_books / student_count    
            print("\nAverage no. of books borrowed:", round(avg, 2)) #Print average with 2 decimal places
        else:
            print("\nNo Valid Entries to Calculate the Average")    
    except FileNotFoundError:
        print("Error: File", filename, "not found")    
#-----------------------------------------------------------------------------------------------------------
# TASK 4
#-----------------------------------------------------------------------------------------------------------          
def count_over_limit(filename):
    """
    This function counts the no.of students who have borrowed more than  3 books
    and handles non-numeric values and negative values"""
    count = 0
    with open(filename, 'r') as f: #Open csv file in reading mode
        next(f) #Skips Header
        for line in f:
            line = line.strip().split(",") #Strips all whitespaces and the delimiter is ,
            if len(line) != 2:
                continue
            borrowed_str = line[1].strip()
            try:
                borrowed = int(borrowed_str)
                if borrowed > 3:
                    count += 1 
            except ValueError:
                continue
    print("Number of Students over limit:", count) 
     
#-----------------------------------------------------------------------------------------------------------
# TASK 5
#-----------------------------------------------------------------------------------------------------------           
def main():
    """Main function to run all tasks and prompts the user to add the filename.
    """
    while True: #Loop until valid filename is provided
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as f:
            #Call all the functions 
             process_borrowers(filename)
             calculate_average_books(filename)
             count_over_limit(filename)
            break
        except FileNotFoundError:
            print("Error: File", filename, "not found. Please try again.")
main()