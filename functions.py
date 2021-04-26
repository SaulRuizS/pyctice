def division_module():
    result, a, b = 0, 0, 0
    a = int(input("Please enter an integer number: "))
    b = int(input("Please enter another integer number: "))
    result = (a % b)
    if result == a:
        print("There is not residue")
    else:    
        print("The residue of the operation is:", result)
#When a function is created there should be to lines of space 
#from the next part of the code     
division_module()

#--------MODULES EXAMPLE--------   

from utils import find_max

numbers = [41, 78, 62, 150, 35, 94]
print(find_max(numbers))