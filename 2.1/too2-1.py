'''
[17] Poes
Küsi kasutajalt iga toote kohta eraldi:
> Kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.

- Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
- Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).

Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
'''

# Import just the uniform function from the library called "random"
from random import uniform
# Import just the datetime function from the library called "datetime"
from datetime import datetime
# To halt the program execution in case we have an error
import sys 

# Initialize date and save it into the variable that we can later format both into day and time
tana = datetime.now()
# For the pretty purposes to imitate how checks actually look in real life
offset = 49
delimiter = "-" * offset

# String that allows us to output different error message
# that ValueError exception catches depending on where we're in the program
# Default value: "start"
program_part = "start"
# Conditional check against these values in list to save up on a variable call overhead
choices_variant = ["yes", "ye", 'y', "nah", "no", 'n']
# Also we'll use another trick for the final receipt of the purchase.. Cause why not? 
# Python is cursed enough to allow str + str without explicitly using concat-equivalent function
receipt_str = f"""\nSinu tšekk:
  _  __    _   _   _ ____  _    _   _ ____        
 | |/ /   / \ | | | |  _ \| |  | | | / ___|   _   
 | ' /   / _ \| | | | |_) | |  | | | \___ \ _| |_ 
 | . \  / ___ \ |_| |  __/| |__| |_| |___) |_   _|
 |_|\_\/_/   \_\___/|_|   |_____\___/|____/  |_|

    Sinu igapäevane E-kauplus, mugav ja odav!\n
Kuupäev: {tana.strftime("%d.%m.%Y")}       |\t      Kell: {tana.strftime("%H:%M")}
{delimiter}
   TOODE:\t\tHIND:\t\tSUMMA:
"""

# Products manually written out cause we haven't yet learned what arrays nor dictionaries are :(
# if only i could write a proper dictionary + while + for loops, i'm tired of being THAT handicapped in my writing abilities
# this is pure shitcode. 
# But if you're new to the programming scene you can learn a lot from my code here, depends on YOU though.
piim_str = "piim"
sai_str = "sai"
leib_str = "leib"
porgand_str = "porgand"
tomat_str = "tomat"
kurk_str = "kurk"

piim_hind = round(uniform(0.5, 3), 2)
sai_hind = round(uniform(0.5, 3), 2)
leib_hind = round(uniform(0.5, 3), 2)
porgand_hind = round(uniform(0.5, 3), 2)
tomat_hind = round(uniform(0.5, 3), 2)
kurk_hind = round(uniform(0.5, 3), 2)

# Final value that we get from all of our purchases
final_hind = 0

# At least the output gonna be pretty with all those 
# - \t (aka. tab delimiter that just inserts space, your tab key on the keyboard does the same ascii escape symbol each time underneath all abstractions btw).
# - \n (aka. new line delimiter that just writes characters on the next line).
# f""" """ - an f-string format + """ """ triple quotation marks that allows
# us to write multiline string in one print() function call instead of pain.
print(f"""---- ÜLESANNE [17]: POES -----\n\n---MEIE KATALOOG:------------------------------
\tTOODE:\t\tHIND:
\t{piim_str.upper()}\t\t{piim_hind} €
\t{sai_str.upper()}\t\t{sai_hind} €
\t{leib_str.upper()}\t\t{leib_hind} €
\t{porgand_str.upper()}\t\t{porgand_hind} €
\t{tomat_str.upper()}\t\t{tomat_hind} €
\t{kurk_str.upper()}\t\t{kurk_hind} €
""")

try:
    piim_soov = input(f"[{piim_str.capitalize()}: {str(piim_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not piim_soov.isalpha() or piim_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if piim_soov == "yes" or piim_soov == 'y':
        piim_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if piim_soov.isdigit(): piim_soov = int(piim_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif piim_soov.isalpha():
            program_part = "amount"
            raise ValueError

        # Now we can continue with the digit check against it being a NULL value
        if piim_soov > 0:
            receipt_str += f"   {piim_str.upper()}   \t\t{piim_hind} €\t\t{round(piim_hind * piim_soov, 2)} € [x{piim_soov}]\n"
            final_hind += piim_hind * piim_soov
            print(f"{piim_str.capitalize()} have been added to your cart!\n")
        else:
            program_part = "null"
            raise ValueError
    
    sai_soov = input(f"[{sai_str.capitalize()}: {str(sai_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not sai_soov.isalpha() or sai_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if sai_soov == "yes" or sai_soov == 'y':
        sai_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if sai_soov.isdigit(): sai_soov = int(sai_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif sai_soov.isalpha():
            program_part = "amount"
            raise ValueError

        if sai_soov > 0:
            receipt_str += f"   {sai_str.upper()}    \t\t{sai_hind} €\t\t{round(sai_hind * sai_soov, 2)} € [x{sai_soov}]\n"
            final_hind += sai_hind * sai_soov
            print(f"{sai_str.capitalize()} have been added to your cart!\n") 
        else:
            program_part = "null"
            raise ValueError

    leib_soov = input(f"[{leib_str.capitalize()}: {str(leib_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not leib_soov.isalpha() or leib_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if leib_soov == "yes" or leib_soov == 'y':
        leib_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if leib_soov.isdigit(): leib_soov = int(leib_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif leib_soov.isalpha():
            program_part = "amount"
            raise ValueError
        
        if leib_soov > 0:
            receipt_str += f"   {leib_str.upper()}    \t\t{leib_hind} €\t\t{round(leib_hind * leib_soov, 2)} € [x{leib_soov}]\n"
            final_hind += leib_hind * leib_soov
            print(f"{leib_str.capitalize()} have been added to your cart!\n") 
        else:
            program_part = "null"
            raise ValueError

    porgand_soov = input(f"[{porgand_str.capitalize()}: {str(porgand_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not porgand_soov.isalpha() or porgand_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if porgand_soov == "yes" or porgand_soov == 'y':
        porgand_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if porgand_soov.isdigit(): porgand_soov = int(porgand_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif porgand_soov.isalpha():
            program_part = "amount"
            raise ValueError
        
        if porgand_soov > 0:
            receipt_str += f"   {porgand_str.upper()}    \t\t{porgand_hind} €\t\t{round(porgand_hind * porgand_soov, 2)} € [x{porgand_soov}]\n"
            final_hind += porgand_hind * porgand_soov
            print(f"{porgand_str.capitalize()} have been added to your cart!\n") 
        else:
            program_part = "null"
            raise ValueError

    tomat_soov = input(f"[{tomat_str.capitalize()}: {str(tomat_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not tomat_soov.isalpha() or tomat_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if tomat_soov == "yes" or tomat_soov == 'y':
        tomat_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if tomat_soov.isdigit(): tomat_soov = int(tomat_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif tomat_soov.isalpha():
            program_part = "amount"
            raise ValueError
        
        if tomat_soov > 0:
            receipt_str += f"   {tomat_str.upper()}    \t\t{tomat_hind} €\t\t{round(tomat_hind * tomat_soov, 2)} € [x{tomat_soov}]\n"
            final_hind += tomat_hind * tomat_soov
            print(f"{tomat_str.capitalize()} have been added to your cart!\n") 
        else:
            program_part = "null"
            raise ValueError

    kurk_soov = input(f"[{kurk_str.capitalize()}: {str(kurk_hind) + "€"}] OSTA?\n[Y/N]: ").lower()
    # Check against whether input value is an alphabet and if it's not one then just call ValueError
    if not kurk_soov.isalpha() or kurk_soov not in choices_variant:
        raise ValueError

    # Now we can continue with out purchase logic
    if kurk_soov == "yes" or kurk_soov == 'y':
        kurk_soov = input("Kui palju?: ")
        # Here comes foolproof checks to exclude any wrong input from the user whatsoever
        # if it's a proper digit then we can wrap it as int and continue with the program as it is
        if kurk_soov.isdigit(): kurk_soov = int(kurk_soov)
        # Otherwise if it's some kind of character instead of a digit we raise a ValueError
        elif kurk_soov.isalpha():
            program_part = "amount"
            raise ValueError
        
        if kurk_soov > 0:
            receipt_str += f"   {kurk_str.upper()}    \t\t{kurk_hind} €\t\t{round(kurk_hind * kurk_soov, 2)} € [x{kurk_soov}]\n"
            final_hind += kurk_hind * kurk_soov
            print(f"{kurk_str.capitalize()} have been added to your cart!\n") 
        else:
            program_part = "null"
            raise ValueError
    
    # If the user bought anything at all then we can safely print out the final tsekk
    if final_hind > 0:
        receipt_str += f"{delimiter}\n           KOGUS:\t\t\t{round(final_hind, 2)} €\n{delimiter}\n\n\t\tAitäh ostmise eest!\n\n"
        print(receipt_str)
    else:
        print("\nHead aega! Ootame teid tagasi!\n")

except ValueError:
    if program_part == "start":
        print(f"Sisestatud valik ei ole õige, sobivaid valikud on: {choices_variant}\nPalun proovige uuesti!\n") 
    elif program_part == "null":
        print("Sisestatud andmed ei ole õiged! Arv peab olema rohkem kui 0! Palun proovige uuesti!\n")
    elif program_part == "amount":
        print("Sisestatud andmed ei ole õiged! Siin sobivad ainult täisarvud. Palun proovige uuest!\n")

    # After all of those checks we just safely halt the program execution
    # because it caught an error somewhere from the wrong user input
    sys.exit(1)

