#Dein Name
# MIT Lisence

name = input("Bitte geben Sie ihren Namen an: ")
age = input("Bitte geben Sie ihr Alter an: ")
filmname = input("Bitte geben Sie den Gewünschten Filmname an: ")

if age < "18" :
    print(f'Der Film {filmname} hat eine Altersbegrenzung. Du({name}) bist zu jung({age})')
    
elif age >= "18" :
    print(f'Der Film {filmname} ist für Sie({name}) freigegeben')
