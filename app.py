# Defina tuplas para representar os dados de 3 alunos
# Matrícula, nome e email

aluno1 = (20221, 'Maria Joaquina', 'mariajoaquina@gmail.com')
aluno2 = (20222, 'João Gabriel', 'joaogabriel@gmail.com')
aluno3 = (20223, 'Miguel Oliveira', 'migueloliveira@gmail.com')

# Crie uma lista para representar os alunos matriculados na disciplina

lista_alunos = list()
lista_alunos.append(aluno1)
lista_alunos.append(aluno2)
lista_alunos.append(aluno3)

# Crie uma lista de 4 notas para cada aluno

notas_aluno1 = [6, 9, 8, 7]
notas_aluno2 = [8 , 7.9, 4, 3]
notas_aluno3 = [10 , 10, 5, 7.7]

# Crie uma tupla que represente um aluno e suas notas

aluno1_notas = (aluno1, notas_aluno1)
aluno2_notas = (aluno2, notas_aluno2)
aluno3_notas = (aluno3, notas_aluno3)

# Crie uma lista que represente os alunos e as notas da disciplina

lista_notas_alunos = list()
lista_notas_alunos.append(aluno1_notas)
lista_notas_alunos.append(aluno2_notas)
lista_notas_alunos.append(aluno3_notas)

# Imprima os alunos com suas respectivas notas

for aluno in lista_notas_alunos:
  print(f'Nome: {aluno[0][1]}, notas: {aluno[1]}')
