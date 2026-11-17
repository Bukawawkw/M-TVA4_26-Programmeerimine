# Import only specific modules used in the project
# because using * for the entirety of math module is a bad practice
# and not an idiomatic way of python writing
from math import sqrt, pi
import sys

# Separate parts that do the formula calculations and 
# printing out of the results for the ease of the code flow
# and well my eyes don't hurt as much now looking at this code :)
print("Ruudu karakteristikud")
try:
    a = float(input("Sisesta ruudu külje pikkus => ")) # Added up float wrapper here
# Which allows us to have floating point values without wrapping basically everything 
# with the float wrapper
except ValueError:
    print("Sisestatud andmed ei sobi! Palun proovige uuesti.\n")
    sys.exit(1) # Better to halt the programm execution cause we can't use while loops like a regular humans yet..

# Made all of the letters used in the formulas lower-case
# while also fixing all of the spacings for the idiomatic Python way of writing it
s = a ** 2
p = 4 * a
di = a * sqrt(2) # Initially missed letter 't' but importing just the module specific functions that we need
# allows us to just use it "directly" at this point

# Also refactor the way it prints out values by using f-string format for the print function
print(f"Ruudu pindala {s}")
print(f"Ruudu ümbermõõt {p}")
print(f"Ruudu diagonaal {round(di, 2)}\n") # Add up '\n' operator to separate the next part of the programm on the next line


# Basically same as the previous one:
# - Spacing
# - Float wrapper
# - Formulas
# - The code flow
# In addition also removed redundant "empty print()" called in several places
print("Ristküliku karakteristikud")
try:
    b = float(input("Sisesta ristküliku 1. külje pikkus => "))
    c = float(input("Sisesta ristküliku 2. külje pikkus => "))
except ValueError:
    print("Sisestatud andmed ei sobi! Palun proovige uuesti.\n")
    sys.exit(1) 

s = b * c
p = 2 * (b + c) # Missed * multiplying operator here, unfortunately math rules doesn't apply here for the interpreter of Python
di = sqrt((b ** 2) + (c ** 2)) # Fixed formula missing extra * indicating exponent math operator ( ** )

print(f"Ristküliku pindala {s}")
print(f"Ristküliku ümbermõõt {p}")
print(f"Ristküliku diagonaal {round(di, 1)}\n") # Missed rounding parametr that i added up here 
# to match the example console output provided in the task


# Same as the two were previously done
print("Ringi karakteristikud")
try:
    r = float(input("Sisesta ringi raadiusi pikkus => "))
except ValueError:
    print("Sisestatud andmed ei sobi! Palun proovige uuesti.\n")
    sys.exit(1) 

d = 2 * r
s = pi * (r ** 2) # Yet another missing exponent operator here and also pi isn't a function but a constant value
c = 2 * pi * r # Missing * multiplying operator here once again

print(f"Ringi läbimõõt {d}")
print(f"Ringi pindala {round(s, 2)}") # Lacked parametr for how many values after the coma
print(f"Ringjoone pikkus {round(c, 2)}") # Here too
