class Pilha:
  #criaçao de dicionario de relacoes
  #criaçao de pilha de camisas encontradas no decorrer da execuçao
  #criaçao de lista com os elementos
  #criaçao de lista com os pares de peças aprovados
  def __init__(self, pilha):
    self.relacoes = {'endrick':'new balance', 'neymar':'puma', 'cr7':'nike', 'messi':'adidas'}
    self.camisas_encontradas = []
    self.elementos = pilha.split('-')
    self.aprovados = []

#verificar se a pilha esta correta
#iterar por todos os elementos da pilha
#se o elemento for camisa, adicionar no conjunto de camisas encontradas
#se o elemento for chuteira, chamar funcao para conferir se há um par
#se nao houver par esta Incorreto
#ao termino das verificaçoes, resta conferir se há alguma camisa sobrando, 
#uma vez que todas as chuteiras já acharam seus pares
#se a lista de pares aprovados tiver os mesmos itens da pilha, entao esta correta
#se nao, incorreta
  def verificar_pilha(self):
    for elemento in self.elementos:
      if self.eh_camisa(elemento):
        self.camisas_encontradas.append(elemento)
      elif self.eh_chuteira(elemento):
        camisa_correspondente = self.encontrar_camisa(elemento)
        if camisa_correspondente is False:
          return "Incorreto"
    for aprovado in self.aprovados:
      self.elementos.remove(aprovado)
    if self.elementos == []:
      return "Correto"
    return "Incorreto"

#conferir se eh camisa
  def eh_camisa(self, elemento):
    return elemento.lower() in {'endrick', 'neymar', 'cr7', 'messi'}

#conferir se eh chuteira
  def eh_chuteira(self, elemento):
    return elemento.lower() in {'new balance', 'puma', 'nike', 'adidas'}

#comparar se a camisa no topo da pilha de camisas recebidas é equivalente a chuteira recebida
#se houver o par, remover camisa em questao da pilha, para ela nao fazer mais pares
#e adicionar o par na lista de aprovados
  def encontrar_camisa(self, chuteira):
    if not self.camisas_encontradas:
      return False
    topo = self.camisas_encontradas.pop()
    if self.relacoes[topo]==chuteira:
      self.aprovados.append(topo)
      self.aprovados.append(chuteira)
      return True
    return False
    
#receber entrada, criar obejto e printar a saída
entrada=input()
pilha=Pilha(entrada)
print(pilha.verificar_pilha())
