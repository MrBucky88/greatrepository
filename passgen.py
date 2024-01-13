import random
chars = ["+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
print("Witaj w SuperHiperGigaMegaTeraUltra Password Generejtorze! :D")
howmany = int(input("Ile znaków ma mieć twoje hasło masło? "))
pasw = []
for i in range(howmany):
    rchar = random.choice(chars)
    print(rchar)
    pasw.append(rchar)
print("Twoje Wygenerowane hasło to: ", pasw)