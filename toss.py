def start():
    import random

    def cointoss():
        rand_i = random.randint(0, 1)
        outcomes = ["Heads", "Tails"]
        return outcomes[rand_i]


    t1 = cointoss()
    print(t1)
start()

def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()

restart_and_exit()

xyz_pro_plus = 1

while (xyz_pro_plus < 2):
    restart_and_exit()

