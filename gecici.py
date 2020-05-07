from bs4 import BeautifulSoup

def magic(number):
    return int(''.join(str(i) for i in number))

r = open("asdfaf.txt","r")
listeler = []
for i in r:
    liste = list()
    for j in i:
        if(j.isdigit()):
            j = int(j)
            liste.append(j)
    liste = magic(liste)
    listeler.append(liste)
