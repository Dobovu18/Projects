"""
A file about the Collatz conjecture
"""

def sequence(n):
    if (not isinstance(n, int)):
        print("Please enter a positive integer.")
        return 0
    #Determining the next term in the sequence for a given n
    elif n == 1: return 0
    elif n % 2 == 0: return n // 2
    else: return 3*n + 1

def collatz(n):
    sequenceList = []
    #Creating a list of terms in the sequence 
    if sequence(n) == 0: return sequenceList
    else:
        sequenceList.append(n)
        while sequence(n) != 0:
            n = sequence(n)
            sequenceList.append(n)

    return sequenceList
    
    


print(collatz(1209109320903223103))
