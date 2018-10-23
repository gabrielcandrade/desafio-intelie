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

def validacaoAtributos(facts, schemas):
        i = 0
        for fact in facts:
                for schema in schemas: 
                        if schema[0] != fact[1]:
                                i+=1
        if i == len(facts):
                print("Iguais")
        else:
                print("Algum atributo diferente do schema")

def exclusaoDosInativos(facts, schemas):
        for fact in facts:
                if fact[-1] == False:
                        facts.remove(fact)

def sobrescreverValor(facts, schemas):
        factsAux = facts
        for fact in facts:
                for factAux in factsAux:
                        if fact[0] == factAux[0]:
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

        for fact in facts:
                for factAux in factsAux:
                        if fact[0] == factAux[0]:
                                if fact[1] == factAux[1]:
                                        if fact[2] != factAux[2]:
                                                if fact[3] == factAux[3]:
                                                        for schema in schemas:
                                                                if schema[2] == 'one' and fact[1] == schema[0]:
                                                                        facts.remove(fact)

        for fact in facts:
                for factAux in factsAux:
                        for schema in schemas:
                                if fact == factAux:
                                        if fact[1] == schema[0]:
                                                print (fact)
        

validacaoAtributos(facts, schemas)
sobrescreverValor(facts, schemas)
