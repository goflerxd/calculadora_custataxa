# Faça um programa com uma função chamada somaimposto. 
# A função possui dois parâmetros formais: taxa, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
#Curso Python - CVT Beberibe 

print('>> Calculadora do preço real e com adição de impostos do produto')

def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo real do produto: '))
print('Valor do produto com imposto:', somaImposto(t,c))

print(">>> Obrigado por usar nossa aplicação! <<<")
input('Digite ENTER para encerar o programa')