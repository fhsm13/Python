# Tabela Hash sem tratamento de colisões
# Criado por: profa. Divani Barbosa Gavinier
# Curriculo Lattes: http://lattes.cnpq.br/8503400830635447

classe  Hash :

     def  __init__ ( self , tam ):
          self .tab = {}
          self .tam_max = tam

     def  funcaohash ( self , chave ):
          v =  int (chave)
          return v % self .tam_max

     def  cheia ( auto ):
          return  len ( self .tab) ==  self .tam_max

     def  imprime ( auto ):
          para eu em  auto .tab:
               print ( " Hash [ % d ] = "  % i, end = " " )
               imprimir ( auto .tab [i])

     def  apaga ( self , chave ):
          pos =  self .busca (chave)
          se pos ! =  - 1 :
               del  auto .tab [pos]
               print ( " -> Dado da posição % d apagado "  % pos)
          else :
               print ( " Item nao encontrado " )

     def  busca ( auto , chave ):
          pos =  self .funcaohash (chave)
          se  auto .tab.get (pos) ==  Nenhum : # se esta estratégia não existe
               retorno  - 1  # saida imediata
          se  auto .tab [pos] == chave:
               pos de retorno
          retorno  - 1

     def  insere ( self , item ):
          se  auto .cheia ():
               print ( " -> ATENÇÃO Tabela Hash CHEIA " )
               Retorna
          pos =  self .funcaohash (item)
          se  self .tab.get (pos) ==  Nenhum : # se posicao vazia
               self .tab [pos] = item
               print ( " -> Inserido HASH [ % d ] "  % pos)
          mais : # se posicao ocupada
               print ( " -> Ocorreu uma colisao na posicao % d "  % pos)
# fim Classe Hashlinear

tamanhoHash =  7
tab = Hash (tamanhoHash)
print ( " \ n ********************************************* ******* " )
print ( "       Tabela HASH Sem Colisões ( % d itens) "  % tamanhoHash)
print ( " *********************************************** ***** " )
para eu no  intervalo ( 0 , tamanhoHash, 1 ):
     print ( " \ n Inserindo elemento % d "  % (i +  1 )) ;
     item =  entrada ( " - Forneca valor numerico inteiro: " )
     tab.insere (item)
item =  input ( " \ n - Forneca valor numerico inteiro para buscar: " )
pos = tab.busca (item)
if pos ==  - 1 :
     print ( " Item nao encontrado " )
else :
     print ( " Item encontrado na posicao: " , pos)
item =  entrada ( " \ n - Forneca valor numerico inteiro para apagar: " )
tab.apaga (item)
print ( " \ n Imprimindo conteudo " )
tab.imprime ()
print ( " \ n " )