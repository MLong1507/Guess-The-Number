from random import randint
score=7500
number=randint(1,1000)
while True:
    print(f"Score:{score}")
    while True:
        try:
            answer=int(input("Choose a number from 1 to 1000:"))
            if 1<=answer<=1000:
                break
            else:
                print("It's invalid, try again!")
        except ValueError:
            print("Value error happend, try again!")
    if score>=10000:
        print("Congratulations! You win the game!")
        break
    elif number==answer:
        times=randint(1,7)
        score+=answer*times
        number=randint(1,1000)
        if times>1:
            print(f"You got it! x{times} score")
        else:
            print("You got it!")
    else:
        score-=answer
        if score<=0:
            print(f"""Score:{score}
You lose""")
            break
        else:
            if number>answer:
                print("Greater")
            else:
                print("Less")
