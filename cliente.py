class Cliente:
    
   def __init__(self, nome):
       self.nome = nome

    # Criamos uma propriedade para o atributo "nome" da classe "Cliente"
   @property
   def nome(self): 
       return self.nome.title()