nome=[]
nota=[]
sexo=[]
def cadastrar(a, n, s):
    nome.append(a)
    nota.append(n)
    sexo.append(s)
def lista():
    for c in range(0,len(nome)):
        print("\n Aluno: {} nota: {} sexo: {}\n".format(nome[c],float(nota[c]),sexo[c]))
    print(input("Pressione enter para prosseguir"))
#def consultar(n):
    #l=nome.index(n)
    #print
def listaM():
    for c in range(len(nome)):
        if nota[c] > 8:
            print(nome[c], nota[c], sexo[c])
def listaP():
    for c in range(len(nome)):
        if nota[c] <5 :
            print(nome[c], nota[c], sexo[c])
def alterar(n):
     l=nome.index(n)
     nota[l]=float(input("Inf. nova nota: "))
     print(nome[l], nota[l], sexo[l])
def remover(n):
     l=nome.index(n)
     print("Aluno",nome[l],"removido")
     del(nome[l])
     del(nota[l])
     del(sexo[l])
while True:
    print("""
1. Cadastrar aluno
2. Listar alunos
3. Consultar aluno
4. Lista dos melhores alunos
5. Lista dos piores alunos
6. Alterar nota de alunos
7. Remover alunos
8. Sair
""")
    m=int(input(">>> "))
    if m == 1:
        a=input("Inf. o nome do aluno: ")
        n=input("Inf. a nota: ")
        #while (n.isalpha or n.isalnum):
        #n=input("""Valor inválido, tente novamente
#Inf. a nota: """)
        s=input("Inf. o sexo {masculino/feminino}: ")
        while(s!="masculino" and s!="feminino"):
                s=input("""Sexo inválido, tente novamente
                        
Inf. o Sexo {masculino/feminino}: """)                        
        cadastrar(a, n, s)
        #break
    if m==2:
        lista()