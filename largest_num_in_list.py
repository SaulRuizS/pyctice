#A very simple program for finding the largest and lowest number in a list (also my version)

numbers = [660, 254, 88, 1242, 1001]

index1 = 0
index2 = 0
largest = numbers[index1]
lowest = numbers[index2]

for num in numbers:               ### REALLY IMPORTANT NOTE: In lists the "item" or in this case "num" 
    if numbers[index1] > largest: ### represents the element of the list in the actual iteration
        largest = numbers[index1] ### so it is not necesary at all an "index" variable just use "num"
    index1 += 1                   ### instead of the whole list name

for num in numbers:
    if numbers[index2] < lowest:
        lowest = numbers[index2]
    index2 += 1    
 
print(largest, "is the largest number in the list\nAnd ", lowest, "is the lowest")

#But for a simpliest way, it is this one: (also the version from a course in YouTube :v)

nums = [32, 5460, 12, 654, 23, 7]

max = nums[0]

for numb in nums:
    if numb > max:
        max = numb

print(max, "is the largest number in other list case")