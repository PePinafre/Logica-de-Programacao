vetor = ["a", "b", "c", 1, 2, 3]
primerio = vetor[0]

sub_vetor = vetor[1:4]
#print(sub_vetor)

vetor.append("d")
#print(vetor)

vetor.extend([4,5])
#print(vetor)

vetor.remove("b")

del vetor[2]
#print(vetor)

vetor[0] = "JLR"
#print(vetor)

tamanho_vetor = len(vetor)
#print(vetor)
#print(tamanho_vetor)

matriculas = ["Ana", "Pedro", "Maria", "Matheus"]
matriculas.sort()
#print(matriculas)

novo_vetor = sorted(vetor)

for estudante in matriculas:
    print(estudante)

frase = "Python é muito bom! 😂"
palavras = frase.split()
print(palavras)

nova_frase = " ".join(palavras)
print(nova_frase)

#Operações matemáticas em vetores numericos 
vetor_numerico = [1, 2, 3, 4]
for i in range(len(vetor)):
    vetor[i] *=2
print(vetor_numerico)