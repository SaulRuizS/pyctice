def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

#--------MODULES EXAMPLE--------   

#from utils import find_max             *This line calls an especific function from the module, if is not required just use "import"
#numbers = [41, 78, 62, 150, 35, 94]
#print(find_max(numbers))