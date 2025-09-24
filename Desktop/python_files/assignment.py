# HAYYA SABOOR UID:434000376
def triangle_type_checker(A, B, C):
    """Determine the type of traingle given its sides A, B, C"""
    if A <= 0 or B <= 0 or C <= 0:  #for negative or zero sides
        return "invalid"
    if A == B == C:                 #for all sides equal
        return "equilateral" 
    elif A == B or B == C or A ==C: #for two sides equal
        return "isosceles"
    else:                           #for no sides equal
        return "scalene"
def main():
    """Main function to have user enter inputs and to call triangle_type_checker"""
    side_A = int(input("Enter Value of Side A: "))
    side_B = int(input("Enter Value of Side B: "))
    side_C = int(input("Enter Value of Side C: "))
    print(triangle_type_checker(side_A, side_B, side_C))
main()    
    
