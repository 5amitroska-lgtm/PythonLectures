# #------------------------------------------------------
# # ULOHA 1
# #-------------------------------------------------------

print("Kolko mas rokov?")
try:
    vek_kupujuceho=abs(int(input()))
except(ValueError):
    print("Nezadal si spravny vek, skus to znovu")
    try:
        vek_kupujuceho=abs(int(input()))
    except(ValueError):
        print("Nesplnil si podmienky")
        exit()

print("Kolko penazi mas na ucte?")
try:
    zostatok_na_ucte = float(input())
except(ValueError):
    print("Nezadal si ciselny zostatok, skus to znovu:")
    try:
        zostatok_na_ucte = float(input())
    except(ValueError):
        print("Nesplnil si podmienky")
        exit()

print("Kolko stoji pivo?")

try:
    cena_piva = abs(float(input()))
except(ValueError):
    print("Cena piva musi byt ciselna hodnota. Skus to znovu")
    try:
        cena_piva = abs(float(input()))
    except(ValueError):
        print("Nesplnil si podmienky")
        exit()

if vek_kupujuceho>=18:
    if zostatok_na_ucte>=cena_piva:
        print(f"Mozes si kupit pivo, tvoj zostatok na ucte je: {zostatok_na_ucte-cena_piva}Kč")
    else:
        print("Nemozes si kupit pivo, nemas dostatok penazi na ucte.")
else:
    print("Nemozes si kupit pivo, nie si plnolety.")


#-----------------------------------------
#metoda na input premennej BOOLEAN
#-----------------------------------------
def read_bool(prompt):
    value = input(prompt).strip().lower()
    if value in ("true", "t", "yes", "y", "1","ano", "a","jo"):
        return True
    if value in ("false", "f", "no", "n", "0","nie","n","ne"):
        return False
    else:
        print("Nespravny datovy typ, napis ano alebo nie")
        value = input(prompt).strip().lower()
        if value in ("true", "t", "yes", "y", "1", "ano", "a", "jo"):
            return True
        if value in ("false", "f", "no", "n", "0", "nie", "n", "ne"):
            return False
        else:
            exit()
#------------------------------------------------------
# ULOHA 2
#-------------------------------------------------------

cena_listka=45
je_zamestnanec=False
minimalny_vek_zamestnanca=18
maximalny_vek_zamstnanca=65
#-----------------------------------------------------------------------
#OTAZKA NA TO CI JE ZAMESTNANEC SA PUSTI IBA PRE ZADANU VEKOVU KATEGORIU
#JE POTREBNE VYPLNIT MAXIMALNY A MINIMALNY VEK ZAMESTNANCA
#-----------------------------------------------------------------------
def vek():
    print("Kolko mas rokov?")
    try:
        vek_kupujuceho=abs(int(input()))
        return vek_kupujuceho
    except(ValueError):
        print("Nezadal si spravny vek, skus to znovu:")
        try:
            vek_kupujuceho=abs(int(input()))
            return vek_kupujuceho
        except(ValueError):
            print("Nesplnil si podmienky, restartuj program.")
            exit()

vek_kupujuceho=vek()
bezna_cena=cena_listka
cena_zamestnanec=cena_listka
#na to ci je zamestnanec sa opytame iba tych, ktori by zamestnancami byt mohli

if vek_kupujuceho>=minimalny_vek_zamestnanca and vek_kupujuceho<=maximalny_vek_zamstnanca:
    je_zamestnanec = read_bool("Si zamestnanec elektrickovej sluzby?")
else:
    je_zamestnanec= False

#vypocet ceny podla veku
if vek_kupujuceho<12:
    if je_zamestnanec:
        cena_zamestnanec=cena_listka*0.2
    else:
        bezna_cena=0
    vysledna_cena=min(cena_zamestnanec,bezna_cena)
elif vek_kupujuceho<18:
    if je_zamestnanec:
        cena_zamestnanec=cena_listka*0.2
    else:
        bezna_cena=cena_listka*0.5
    vysledna_cena= min(bezna_cena,cena_zamestnanec)
elif vek_kupujuceho<55 and je_zamestnanec:
    vysledna_cena=cena_listka*0.2
elif vek_kupujuceho<=65 and je_zamestnanec:
    vysledna_cena=0
elif vek_kupujuceho<=65 and je_zamestnanec==False:
    vysledna_cena=cena_listka
else:
    if je_zamestnanec:
        cena_zamestnanec=cena_listka*0.2
    else:
        bezna_cena=cena_listka*0.7
    vysledna_cena=round(min(bezna_cena,cena_zamestnanec),2)

print(f"Cena listka je: {vysledna_cena} Kc")

