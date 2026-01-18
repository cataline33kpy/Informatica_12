import random
teme = {
    "Matematica": [
        ("Cat face 5 + 7?", "12"),
        ("Cat face 9 * 9?", "81"),
        ("Cat face 100 / 4?", "25"),
        ("Radacina patrata din 16?", "4"),
        ("Cat face 10 - 3?", "7"),
        ("Cat face 8 * 8?", "64"),
        ("Cat face 5 la puterea 2?", "25"),
        ("Cat face 12 + 11?", "23"),
        ("Cat face 9 + 1?", "10"),
        ("Cat face 7 * 6?", "42"),
    ],
    "Geografie": [
        ("Capitala Frantei?", "Paris"),
        ("Cel mai mare ocean?", "Pacific"),
        ("Capitala Romaniei?", "Bucuresti"),
        ("Cel mai lung fluviu din Europa?", "Dunarea"),
        ("Cea mai mare tara?", "Rusia"),
        ("Capitala Italiei?", "Roma"),
        ("Cea mai mica tara?", "Vatican"),
        ("Cel mai mare continent?", "Asia"),
        ("Capitala Spaniei?", "Madrid"),
        ("Capitala Germaniei?", "Berlin"),
    ],
    "Istorie": [
        ("In ce an a inceput al Doilea Razboi Mondial?", "1939"),
        ("Cine a fost primul presedinte al Romaniei?", "Nicolae Ceausescu"),
        ("Unde s-a semnat Tratatul de la Versailles?", "Versailles"),
        ("Cine a descoperit America?", "Cristofor Columb"),
        ("Care a fost capitala Imperiului Roman?", "Roma"),
        ("In ce an s-a Revolutia Franceza?", "1789"),
        ("Cine a fost Alexandru cel Mare?", "Conducator macedonean"),
        ("Ce imperiu a cazut in 1453?", "Imperiul Bizantin"),
        ("Cine a fost regina Angliei in timpul 'Epocii de Aur'?", "Elisabeta I"),
        ("Care a fost cauza principala a Primului Razboi Mondial?", "Asasinarea arhiducelui Franz Ferdinand"),
    ],
    "Sport": [
        ("Cati jucatori are o echipa de fotbal?", "11"),
        ("In ce tara s-au nascut Jocurile Olimpice?", "Grecia"),
        ("Ce sport practica Serena Williams?", "Tenis"),
        ("Care este durata unui meci de baschet?", "48 minute"),
        ("Cine detine recordul mondial la 100m sprint?", "Usain Bolt"),
        ("Ce sport se joaca cu o minge ovala?", "Rugby"),
        ("Cate puncte valoreaza un cos in baschet?", "2"),
        ("Care este numele faimosului ciclist spaniol?", "Alberto Contador"),
        ("In ce an s-au desfasurat primele Jocuri Olimpice moderne?", "1896"),
        ("Ce sport practica Lionel Messi?", "Fotbal"),
    ],
    "IT": [
        ("Ce inseamna CPU?", "Unitate centrala de procesare"),
        ("Ce limbaj de programare foloseste print()?", "Python"),
        ("Ce inseamna HTML?", "Limbaj de marcare a hipertextului"),
        ("Ce sistem de operare foloseste Android?", "Linux"),
        ("Ce este un browser?", "Program pentru navigarea pe internet"),
        ("Ce inseamna RAM?", "Memorie cu acces aleator"),
        ("Ce companie a creat Windows?", "Microsoft"),
        ("Ce este un virus informatic?", "Program malitios"),
        ("Ce limbaj foloseste Java?", "Java"),
        ("Ce este un IP?", "Adresa internet"),
    ],
}

tema = random.choice(list(teme.keys()))
print(f"Tema aleasa: {tema}\n")
intrebari=teme[tema]
scor=0
for i, (intrebare, raspuns_corect) in enumerate(intrebari, start=1):
    raspuns = input(f"Intrebarea {i}: {intrebare}")
    if raspuns.strip().lower()==raspuns_corect.lower():
        print("Corect!\n")
        scor += 1
    else:
        print(f"Gresit! Raspunsul corect era: {raspuns_corect}\n")

print(f"Scor final: {scor}/{len(intrebari)}")