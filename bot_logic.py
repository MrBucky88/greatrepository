import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coinflip(a, b):
    print("Siemka witaj, chcesz rzucić monetą?")
    urguess = a
    b = random.randint(1, 2) #1 orzeł 2 reszka
    if a == "orzeł" or 'orzel' and b == 1:
        print("Orzeł, trafiłeś!")
    elif a == 'orzeł' or 'orzel' and b == 2:
        print("Orzeł, niestety nie trafiłeś")
    if a == "reszka" and b == 1:
        print("Orzeł, niestety nie trafiłeś")
    elif a == 'reszka' and b == 2:
        print("Reszka, trafiłeś!")