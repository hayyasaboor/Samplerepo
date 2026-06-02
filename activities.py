def make_list(a_sequence):
    new_list = []
    for item in a_sequence:
        print("List after Appending: ", new_list)
    return new_list   
def main():
    result= make_list(range(5))
    print ("Final list Returned: ", result)
if __name__ == "__main__":
   main()   