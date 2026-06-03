# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Digite o nome do aluno(a)")
nt01 = float(input("Informe a primeira nota"))
nt02 = float(input("informe a segunda nota"))
nt03 = float(input("informe a terceira nota"))

media = (nt01 + nt02 + nt03) / 3

print("|_____________________________________________|")
print("|SISTEMA DE PROVAS                            |")
print("|                                             |")
print("|_____________________________________________|")
print("|Nome do Aluno(a)",nome)
print("|Nota da primeira prova: ",nt01)
print("|Nota da sgunda prova: ",nt02)
print("|Nota da terceira prova: ",nt03)
print("|                                             |")
print("|_____________________________________________|")
print("|Aluno(a): ",nome)
print("|Média: ",media)

if media >= 5:
    print("|Aprovado(a)")

elif media < 5:
    print("|Reprovado(a)")