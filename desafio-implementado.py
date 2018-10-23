#Autor: Gabriel de Carvalho Andrade
#Empresa: Intelie

# Argumento de entrada de dados (dado na questao)

facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]

schemas = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]

# Validacao de atributos ao schema, caso tenha algum atributo de facts que
#nao corresponde ao que schemas, ele avisa que existe atributos incompativeis.

def validacaoAtributos(facts, schemas):
        i = 0
        for fact in facts:      # Percorre toda a lista de facts
                for schema in schemas:          # Percorrendo tambem a lista de schemas 
                        if schema[0] != fact[1]:        # Quando encontra algum atributo no schema, ele soma +1
                                i+=1
        if i == len(facts):                             # Se a quantidade de i for igual ao tamanho de facts, todos os facts foram encontrados.
                print("Iguais")
        else:
                print("Algum atributo diferente do schema")     # Caso contrário, ele possui divergência

def sobrescreverValor(facts, schemas):
        # Apaga os atributos que forem invalidados através da flag "False"
        
        factsAux = facts        # Cria uma copia de facts, porque ele não pode percorrer a própria lista, decidi percorrer uma igual.
        for fact in facts:      # Percorre toda a lista de facts
                for factAux in factsAux:        # Percorre toda a lista de facts copiada
                        if fact[0] == factAux[0]:       # Aqui ele fará a validacao se tiver algum False e um True, ele apaga as duas informacoes de ambas as listas.
                                if fact[1] == factAux[1]:
                                        if fact[2] == factAux[2]:
                                                if fact[3] != factAux[3]:
                                                        if fact[3] == True:
                                                                facts.remove(fact)
                                                        if factAux[3] == True:
                                                                factsAux.remove(factAux)
                                                        if fact[3] == False:
                                                                facts.remove(fact)
                                                        if factAux[3] == False:
                                                                factsAux.remove(factAux)
        # Sobrescreve os parâmetros
        
        for fact in facts:      # Percorre toda a lista de facts
                for factAux in factsAux:        # Percorre toda a lista de facts
                        if fact[0] == factAux[0]:       # Aqui ele vai procurar conteudos diferentes de atribuitos iguais para fazer a sobreposicao. Caso positivo, ele apaga o anterior.
                                if fact[1] == factAux[1]:
                                        if fact[2] != factAux[2]:
                                                if fact[3] == factAux[3]:
                                                        for schema in schemas:
                                                                if schema[2] == 'one' and fact[1] == schema[0]:
                                                                        facts.remove(fact)
                                                                        
        # Percorre todos os itens e mostra apenas os conteudos que sao iguais para ambas.
        
        for fact in facts: # Percorre toda a lista de facts
                for factAux in factsAux:        # Percorre toda a lista de facts
                        for schema in schemas:  # Valida novamente todos os facts nas schemas dadas para imprimir a quantidade correta.
                                if fact == factAux:
                                        if fact[1] == schema[0]:
                                                print (fact)    # Imprime na tela os dados da lista.
        

validacaoAtributos(facts, schemas)
sobrescreverValor(facts, schemas)
input()
