# Criado por @JonatasOSilva e @Raph4H

import random # Biblioteca para dar aleatoriedade para a matriz
import string # Bibliteca para o alfabeto, numeros e caracteres especiais

# Ilustração nome do programa
print('''\033[37m
##     ##  #######  ######## ##     ## ########     ###        ########  ##    ## 
###   ### ##     ##    ##    ##     ## ##     ##   ## ##       ##     ##  ##  ##  
#### #### ##     ##    ##    ##     ## ##     ##  ##   ##      ##     ##   ####   
## ### ## ##     ##    ##    ######### ########  ##     ##     ########     ##    
##     ## ##     ##    ##    ##     ## ##   ##   #########     ##           ##    
##     ## ##     ##    ##    ##     ## ##    ##  ##     ## ### ##           ##    
##     ##  #######     ##    ##     ## ##     ## ##     ## ### ##           ##    
\033[37m''')

# Cria uma lista com o alfabeto, números (0 a 9) e caracteres especiais (@,!,#...)
caracteres = list(string.ascii_letters + string.digits + string.punctuation + ' ' + 'àèìòùÀÈÌÒÙáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ')
# Remove caracteres que causam erro
caracteres.pop(85)
caracteres.pop(87)

# Cores
cor_vermelha = '\033[1;31m'
cor_amarela = '\033[1;33m'
cor_azul = '\033[1;34m'
cor_branca = '\033[1;37m'
cor_reset = '\033[m'

# Iniciando a matriz
matriz = []

# Cria a matriz
def criar_matriz():
    for i in range(len(caracteres)): 
        linha = [] 
        for j in range(len(caracteres)):
            # Adiciona as colunas na linha
            linha.append(caracteres[j])
        # Adiciona a linha a matriz
        matriz.append(linha)

# Faz o embaralhamento da matriz
def embaralhar_matriz(chave):
    random.seed(chave)
    for c in range(len(caracteres)):
        random.shuffle(matriz[c])
    
# Mostra na tela a matriz
def imprimir_matriz():
    for i in range(len(caracteres)): 
        for j in range(len(caracteres)): 
            print(matriz[i][j], end = " ")
        print()

# Deixa a chave do tamanho do texto
def chave_tam_texto(chave, texto):
    
    novachave = '' 
    cont2 = 0
    
    for cont in range(len(texto)):
        novachave += chave[cont2]
        cont2 += 1
        
        # Se o cont2 ultrapassar o tamanho da chave original ele volta pro inicio
        if cont2 >= len(chave):
            cont2 = 0

    return novachave

def criptografar(chave, textoclaro):

    textocifrado = ''

    # Embaralha a matriz de acordo com a chave
    embaralhar_matriz(chave)

    # Deixa a chave do tamanho do texto    
    novachave = chave_tam_texto(chave, textoclaro)
    
    # Criptografa o texto claro
    for contador in range(len(textoclaro)):
        textocifrado += matriz[caracteres.index(novachave[contador])][caracteres.index(textoclaro[contador])]

    # Imprime o texto cifrado
    print(f'{cor_branca}TEXTO CIFRADO: {cor_amarela}{textocifrado}{cor_reset}')

def descriptografar(chave, textocifrado):
    
    textoclaro = ''

    # Embaralha a matriz de acordo com a chave
    embaralhar_matriz(chave)
    
    # Deixa a chave do tamanho do texto
    novachave = chave_tam_texto(chave, textocifrado)

    # caracteres.index(chave) Mostra a posição da coluna/chave
    # matriz[caracteres.index(chave)] Mostra as colunas da linha
    # matriz[caracteres.index(chave)].index(textocifrado) Encontra o texto cifrado na linha
    # caracteres[matriz[caracteres.index(chave)].index(textocifrado)] Mostra o texto claro de acordo com o indice

    # Descriptografa o texto cifrado
    for cont in range (len(textocifrado)):
        textoclaro += caracteres[matriz[caracteres.index(novachave[cont])].index(textocifrado[cont])]
    
    # Imprime o texto claro
    print(f'{cor_branca}TEXTO CLARO: {cor_azul}{textoclaro}{cor_reset}')

def validacao_entrada (valor):
    
    # Converte a String em Lista
    valor = list(' '.join(valor.split()))

    valido = True

    # Verifica se há algum caractere inválido
    for c in range(len(valor)):
        if valor[c] not in caracteres:
            valido = False
            print(f'{cor_vermelha}ERRO! O CARACTERE "{valor[c]}" NÃO É PERMITIDO.')

    # Verifica se a entrada está vazia
    if not valor:
        valido = False
        print(f'{cor_vermelha}ERRO! ENTRE COM OS VALORES.{cor_reset}')

    return valido

def main():
    
    while True:

        # Limpa e cria a matriz
        matriz.clear()
        criar_matriz()

        # Escolha de criptografar, descriptografar ou sair
        opcao = str(input(f'{cor_branca}DIGITE {cor_amarela}1{cor_branca} PARA CRIPTOGRAFAR, {cor_azul}0{cor_branca} PARA DESCRIPTOGRAFAR OU {cor_vermelha}S{cor_branca} PARA SAIR: {cor_reset}')).upper()
        
        # O loop não permite que o usuário prossiga enquanto a entrada for diferente de 1, 0 ou S 
        while opcao != '1' and opcao != '0' and opcao != 'S':
            opcao = str(input(f'{cor_vermelha}ERRO!{cor_branca} DIGITE {cor_amarela}1{cor_branca} PARA CRIPTOGRAFAR, {cor_azul}0{cor_branca} PARA DESCRIPTOGRAFAR: OU {cor_vermelha}S{cor_branca} PARA SAIR: {cor_reset}')).upper()
        
        # Criptografia
        if opcao == '1':

            # O loop não permite que o usuário prossiga enquanto houver um caractere inválido ou se a entrada estiver vazia
            valido = False
            while valido == False:
                # Entrada da chave (senha) para que o texto criptografado
                chave = input(f'{cor_branca}DIGITE A CHAVE: {cor_reset}')
                valido = validacao_entrada(chave)

            # O loop não permite que o usuário prossiga enquanto houver um caractere inválido ou se a entrada estiver vazia
            valido = False
            while valido == False:
                # Entrada do texto claro para que possa ser criptografado
                textoclaro = input(f'{cor_branca}DIGITE O TEXTO CLARO: {cor_reset}')
                valido = validacao_entrada(textoclaro)
            
            # Chama a função passando os valores válidos
            criptografar(chave, textoclaro) 

        # Descriptografia
        elif opcao == '0':

            # O loop não permite que o usuário prossiga enquanto houver um caractere inválido ou se a entrada estiver vazia
            valido = False
            while valido == False:
                # Entrada da chave (senha) para que o texto seja descriptografado
                chave = input(f'{cor_branca}DIGITE A CHAVE: {cor_reset}')
                valido = validacao_entrada(chave)
            
            # O loop não permite que o usuário prossiga enquanto houver um caractere inválido ou se a entrada estiver vazia  
            valido = False
            while valido == False:
                # Entrada do texto cifrado para que possa ser descriptografado
                textocifrado = input(f'{cor_branca}DIGITE O TEXTO CIFRADO: {cor_reset}')
                valido = validacao_entrada(textocifrado)
        
            # Chama a função passando os valores válidos
            descriptografar(chave, textocifrado)

        # Encerra o programa
        elif opcao == 'S':
            break

main()
