class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList():
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo
        return 
    
    def inserir_meio(self, Novo_valor, index):
        if self.tamanho() > index:
            novo_no = No(Novo_valor)
            procurado = self.inicio
            cont = 0
            while procurado.get_proximo() is not None:
                if cont == index-1:
                    novo_no.set_proximo(procurado.get_proximo())
                    procurado.set_proximo(novo_no)
                    break
                    
                cont = cont + 1
                procurado = procurado.proximo
            return 
        

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)
        return 

#---------------------------------------------------
    def esta_vazio(self) -> bool:
        if self.inicio is None:
            return True
        else:
            return False

#---------------------------------------------------
    def remove(self, item):
        procurado1 = self.inicio
        if procurado1 is not None:
            if procurado1.valor == item:
                self.inicio = procurado1.proximo
                procurado1 = None
                return
            
            while procurado1 is not None:
                if procurado1.valor == item:
                    break
                memoria = procurado1
                procurado1 = procurado1.proximo
                
            if procurado1 == None:
                return
            memoria.proximo = procurado1.proximo
            procurado1 = None
        return 
                  
#---------------------------------------------------    
    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else:
            cont = 1
            aux = self.inicio
            while aux.get_proximo() is not None:
                cont = cont+1
                aux = aux.get_proximo()
                
            return cont

#----------------------------------------------------
    def limpa(self):
        while self.inicio is not None:
            A = self.inicio
            self.inicio = self.inicio.proximo
            A = None
        return
                
#----------------------------------------------------
    def procura(self, item) -> bool:
        procurado = self.inicio
        index=0
        while procurado:
            if procurado.valor == item:

                return True

            else:
                procurado = procurado.proximo
                index = index + 1

        return False
       

#------------------------------------------------------
    def indice_de(self, item):
        if self.tamanho() == 0:
            return -1
        
        else:
            procurado = self.inicio
            indice=0
            while procurado:
                if procurado.valor == item:
                
                    return indice

                procurado = procurado.proximo
                indice = indice + 1
        return -1

         

#-----------------------------------------------------
    def recupera_indice(self, index):
        if self.tamanho() > index:
            procurado = self.inicio
            cont = 0
            while procurado.get_proximo() is not None:
                if cont == index:
                    return procurado.valor
                
                cont = cont + 1
                procurado = procurado.proximo
            return procurado.valor
        
        return None
    

#----------------------------------------------------
    def transforma_em_lista(self):
        novaLista = []
        if self.inicio is None:
            return novaLista
        else:
            aux = self.inicio
            while aux is not None:
                novaLista.append(aux.valor)
                aux = aux.get_proximo()
        
        return novaLista
        




#-----------------------------------------------------
lista_ligada = LinkedList()
#inserir_inicio
#inserir_fim
#esta_vazio
#remove
#tamanho
#limpa
#procura
#indice_de (item)pequisa o index do item
#recupera_indice(index) retorna o valor do index
#tranforma_lista

#_____________________________________________________
#chama a funcao que adiciona valores
lista_ligada.inserir_inicio(10)
#lista_ligada.inserir_meio(x,y)
lista_ligada.inserir_fim(20)
lista_ligada.inserir_fim(30)
lista_ligada.inserir_fim(40)
lista_ligada.inserir_fim(50)

print("lista=", lista_ligada.transforma_em_lista())
lista_ligada.inserir_meio(15,1)
print("lista=", lista_ligada.transforma_em_lista())
lista_ligada.inserir_meio(25,3)
print("lista=", lista_ligada.transforma_em_lista())
lista_ligada.inserir_meio(35,5)
print("lista=", lista_ligada.transforma_em_lista())


#chama a funcao que apaga valores
lista_ligada.remove(99)
lista_ligada.limpa() #apaga a lista

# funcao que mensura os valores 
lista_ligada.tamanho()
lista_ligada.esta_vazio() 
lista_ligada.indice_de(20)
lista_ligada.recupera_indice(1)
lista_ligada.transforma_em_lista()


