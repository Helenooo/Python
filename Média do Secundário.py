from math import *

print("Média do Secundário (10º e 11º anos)")
print()

#10º ano
print("Insere a tua nota final do 10º ano a cada uma destas disciplinas:")
print()
fqA10 = input("Física e Química A: ")
print()
bg10 = input("Biologia e Geologia: ")
print()
matA10 = input("Matemática A: ")
print()
pt10 = input("Português: ")
print()
ing10 = input("Inglês: ")
print()
fil10 = input("Filosofia: ")
print()
edf10 = input("Educação Física: ")

#11º ano
print()
print("Insere a tua nota final do 11º ano a cada uma destas disciplinas:")
print()
fqA11 = input("Física e Química A: ")
print()
bg11 = input("Biologia e Geologia: ")
print()
matA11 = input("Matemática A: ")
print()
pt11 = input("Português: ")
print()
ing11 = input("Inglês: ")
print()
fil11 = input("Filosofia: ")
print()
edf11 = input("Educação Física: ")

#Média de 10º
med10 = (float(fqA10) + float(bg10) + float(matA10) + float(pt10) + float(ing10) + float(fil10) +
float(edf10)) / 7

#Média de 11º
med11 = (float(fqA11) + float(bg11) + float(matA11) + float(pt11) + float(ing11) + float(fil11) +
float(edf11)) / 7

#Média de cada disciplina
fqA = (float(fqA10) + float(fqA11)) / 2

bg = (float(bg10) + float(bg11)) / 2

matA = (float(matA10) + float(matA11)) / 2

pt = (float(pt10) + float(pt11)) / 2

ing = (float(ing10) + float(ing11)) / 2

fil = (float(fil10) + float(fil11)) / 2

edf = (float(edf10) + float(edf11)) / 2

#Média do Secundário Final
medSec = (ceil(fqA) + ceil(bg) + ceil(matA) + ceil(pt) + ceil(ing) + ceil(fil) + ceil(edf)) / 7

def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n

print()
print("Média do 10º ano: " +str((truncate(med10, 1)) * 10))
print("Média do 11º ano: " +str((truncate(med11, 1)) * 10))
print()
print("Média do Secundário: " +str((truncate(medSec, 1)) * 10))
