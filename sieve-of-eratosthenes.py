# Python 2.x
# rvisharma - rvisharma91@gmail.com

# Sieve of Eratosthenes

import time
results = [1]
n = int(input('Enter n '))
t1 = time.time()
numbers = [x for x in range(2,n)]
while len(numbers) > 0:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]
    #print (results)
t2 = time.time()
print round(t2-t1, 4), 'seconds'
inp = raw_input('''Press P followed bt ENTER to print the prime numbers,
                to exit Press Enter ''')
if inp.lower() == 'p':
    print results
