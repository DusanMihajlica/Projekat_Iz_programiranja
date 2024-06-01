from libary import Libary
from book import Book
libary = Libary()

unos = input("Sta zelite da radite (1-Za dodavanje knjige, 2-Za brisanje knjige, 3-Za prikaz svih knjiga, 4-Za menjanje informacija o knjigama)")
if unos =="1":
    while True:
        print("Napisi informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        book = Book(naziv, autor, god_izdanja, zanr)
        libary.dodaj_knjigu(book)
        code = input("Ako zelite da prekinete upis knjiga pritisnite x ako ne bilo sta drugo")
        if code == "x":
            break
    
    with open("fajl.txt", "a") as file:
        for object in libary.lista_objekata:
            file.write(object.display_info() + "\n")

elif unos == "2":
    print("Napisi informacije o knjizi koju zelite da izbrisete.")
    naziv = input("Naziv: ")
    autor = input("Autor: ")
    god_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    book = Book(naziv, autor, god_izdanja, zanr)
    with open("fajl.txt", "r") as file:
        lines = file.readlines()
    with open("fajl.txt", "w") as file:
        for line in lines:
            if line.strip() != book.display_info().strip():
                file.write(line)