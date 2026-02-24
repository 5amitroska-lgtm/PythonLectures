numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.

for number in numbers:
    if(number>=0):
        print(number)

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
i=0
if len(names)>0:
    while True:
        if(names[i]== 'Alice'):
            break
        print(names[i])
        i+=1

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0

novy_list= [a for a in random_codes if "0" in a]
print(novy_list)

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
iterator=0
pocet_rovnakych=0
atualny_znak=None
vysledny_zoznam=[]
for string in random_codes:
    iterator=0
    aktualny_znak=None
    pocet_rovnakych=0
    for letter in string:
        if iterator > 0:
            if aktualny_znak==letter:
                pocet_rovnakych+=1
                if pocet_rovnakych>1:
                    vysledny_zoznam.append(string)
            else:
                pocet_rovnakych=0
        aktualny_znak=letter
        iterator+=1
print(vysledny_zoznam)





