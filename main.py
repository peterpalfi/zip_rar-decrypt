import zoperations
import itertools
import time

def bruteforce(zfile, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    numType = "1234567890"
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            print(letter)
            if zoperations.extractable(zfile, letter) == True:
                end = time.time()
                distance = end - start
                return (attempts, distance, letter)

#stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
#numType = "1234567890"
