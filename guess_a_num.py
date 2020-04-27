from random import randint

num = 100 #int(input("Where do you want your guess to end: "))
counter = 0
u_guess = 0
C_guess = randint(1, num)

while u_guess != C_guess:
    u_guess = int(input("Guess a number between 1 and %d: " % num))
    counter += 1
    if C_guess == u_guess:
        print("%d You guessed it" % u_guess)
    elif u_guess < C_guess:
        print("%d is Lower" % u_guess)
    else:
        print("%d is Higher" % u_guess)
    
    
print("\nYou guessed it in %d guess(es)" % counter)
