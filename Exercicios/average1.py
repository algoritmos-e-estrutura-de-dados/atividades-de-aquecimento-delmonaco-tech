import numbers


a = input("insira os numeros : ")
b = [float(num) for num in a.split()]
 
total = 0
for x in numbers:
    total = total + x
print("media dos ", numbers, " e ", total / len(numbers))