n = 15
number = 1
print('Fizzbuzz is counting up to' + " " + str(n))
while number <= n:

    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print ('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
    number +=1