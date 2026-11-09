# classe 
# usanso dois _ fica private / somente um _ fica public
class Pessoa:
    def __init__(self, nome,idade,cpf,telefone,email):
        self.__nome = nome 
        self.__idade = idade 
        self.__cpf = cpf 
        self.__telefome = telefone
        self.__email = email

    # metodos set e get no python sempre se inicia pelo get
    # 1. O GETTER (Leitura)
    @property #envia o dado
    def nome(self):
        return self.__nome

    # 2. O SETTER (Escrita)
    @nome.setter # pega o dado
    def nome(self,nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf        

    @property
    def telefone(self):
        return self.__telefome
        
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone  

    @property
    def email(self):
        return self.__email
            
    @email.setter
    def email(self,email):
        self.__email = email