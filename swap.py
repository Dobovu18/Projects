n = 18
m = 100

print("n is %d and m is %d" %(n, m))
print("Swapping...")
n, m = m, n

print("n is now %d and m is now %d" %(n, m))


score1, score2 = eval(input("Enter your two marks from the Python test separated by commas: "))
average = (score1 + score2)/2
print("Your overall grade is %.2f" % average)


#Using recursion to create a fibonacci sequence
def fib(n):
    if(not isinstance(n, int)):
        print("Sequences only take positive INTEGER values")
        return None
    elif(n < 1):
        print("Sequence only takes POSITIVE integer values")
    elif(n == 1 or n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 31):
    print("The %dth term is: %r" %(i, fib(i)))


#Note that when calculating terms beyond n = 30 the program seems to run slowly, recursion seems to be inefficient

def fib3(n):
    if n == 0 or n == 1: return n
    x, y = 0, 1
    for i in range(n - 1):
        x, y = y, x + y
    return y

for i in range(0, 31):
    print("The %dth term is: %r" %(i, fib3(i)))





