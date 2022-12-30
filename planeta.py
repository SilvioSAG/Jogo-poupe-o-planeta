#Aqui está um exemplo de como o jogo "Poupe o planeta" poderia ser implementado em Python. Observe que este é apenas um exemplo e pode haver várias maneiras de implementar essa ideia:

# Definimos as variáveis que armazenarão os valores do jogo
dinheiro = 1000
satisfacao_populacao = 50
poluicao = 0

# Criamos uma função para exibir o status atual do jogo
def exibe_status():
  print("Dinheiro: $" + str(dinheiro))
  print("Satisfação da população: " + str(satisfacao_populacao) + "%")
  print("Poluição: " + str(poluicao) + " toneladas")

# Exibimos o status inicial do jogo
exibe_status()

# Criamos um laço de repetição para simular o passar dos anos
for ano in range(1, 11):
  print("Ano " + str(ano))
  
  # Pedimos para o usuário tomar uma decisão sobre o que fazer neste ano
  decisao = input("O que você gostaria de fazer? (investir em sustentabilidade/aumentar produção/ignorar problemas): ")
  
  # Verificamos a decisão do usuário e atualizamos as variáveis de acordo
  if decisao == "investir em sustentabilidade":
    dinheiro -= 500
    satisfacao_populacao += 10
    poluicao -= 10
  elif decisao == "aumentar producao":
    dinheiro += 500
    satisfacao_populacao -= 10
    poluicao += 20
  elif decisao == "ignorar problemas":
    satisfacao_populacao -= 5
    poluicao += 10
    
  # Exibimos o status atualizado do jogo
  exibe_status()
  #Neste exemplo, usamos três variáveis para armazenar o dinheiro, a satisfação da população e a poluição. Criamos uma função para exibir o status atual do jogo e um laço de repetição para simular o passar dos anos. A cada ano, solicitamos ao usuário que tome uma decisão sobre o que fazer e, de acordo com sua escolha, atualizamos as variáveis e exibimos o status atualizado do jogo.



