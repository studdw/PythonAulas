alunos = int(input("Digite o numero de alunos na turma: "))

i = 1
soma = 0
alunosabaixo = 0
alunosacima = 0

while i <= alunos:
    nota = float(input("Digite a nota do aluno: "))
    if nota <= 5 and nota >= 0:
        alunosabaixo = alunosabaixo + 1
    else:
        alunosacima = alunosacima + 1
    
    soma = soma + nota
    i = i + 1
media = soma / alunos

print(f"A media da turma é: {media}")
print(f"O numero de alunos com nota abaixo de 5 é: {alunosabaixo}")
print(f"O numero de alunos com nota acima de 5 é: {alunosacima}")