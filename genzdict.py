genzslang = {
    "LOL" : "odpowiedź na coś zabawnego",
    "CRINGE" : "coś dziwnego lub wstydliwego",
    "ROFL" : "odpowiedź na żart",
    "SHEESH" : "lekka dezaprobata",
    "CREEPY" : "straszny, złowieszczy",
    "AGGRO" : "stać się agresywnym/zły",
    "RANDOM" : "z angielskiego: 'losowy', osoba losowo napotkana",
    "REL" : "z angielskiego 'real', prawdziwe, słowo używane do przynania racji, tego że z sytuacją można się utożsamić",
    "ESSA" : "coś łatwego, prawdopodobnie z angielskiego 'easy' -> 'ez' -> 'essa', jaka piękna ewolucja słowa "
}

print("Witaj w programie: EpicPrimaCrissCrossAppleSauceGenZDictionary! ")
print("Pewnie nie raz spotkałeś się z sytuacją typu: ")
print("-------------------------------------")
print("Wnuczek: Hej Dziadku!")
print("Dziadek: Serwus Wnuczku!")
print("Wnuczek: Jak tam sheesh gitara na essie, w śpiulkolocie sigmy?")
print("Dziadek: No proszę ja Ciebie o czym ty mówisz?")
print("-------------------------------------")
print("Na pewno nie chcesz powtórki z tej sytuacji, nasz program Tobie w tym pomoże!")

for i in range(5):
    word = input("Wpisz słowo którego nie rozumiesz: ")
    
    if word in genzslang.keys():
        print(genzslang[word])
    
    else:
        print("Hmm wygląda na to że albo słowo które wpisałeś zostało wpisane małymi literkami, albo słowo nie zostało jeszcze wprowadzone do słownika!")
