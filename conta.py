class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é de {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print("O valor de {} não é permitido para saque".format(valor))

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)
    

    # GET n SET
    # GET -->  Listar/Pegar valores de um atributo da classe
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    # SET --> Alterar/Configurar valores de um atributo da classe

    def set_limite(self, limite):
        self.__limite = limite
        
