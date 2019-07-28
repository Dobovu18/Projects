
def C2F():
    celsius = eval(input("What is the temperature in Celsius? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is %.2f degrees fahrenheit" %fahrenheit)


def countdown(n):
    if(not isinstance(n, int)):
        print("Countdown must have an integer input")
    elif(n < 0):
        while(n < 0):
            print(-n)
            n += 1
    elif(n > 0):
        while(n > 0):
            print(n)
            n -= 1
                

