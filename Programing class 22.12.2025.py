# trabalhamos com classes tendo quatro pilares, polimorfia, abstração, encapsulamento e herança.
# encapsulamento = boneco russo, um dentro do outro. padroes de privacidade com base na quantidade de '_'
from hmac import new

class contaBancaria():
    def __init__(self,nome, cpf, idade, email, telefone, valor):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.valor = valor

    # fazer o saque, deposito e mostrar dados

    def saque(self):
        saque = int(input('quanto você quer sacar?: '))
        if saque > self.valor:
            print("Valor de saque indisponível")
        else:
            self.valor = self.valor - saque
            print("Valor de saque realizado com sucesso")
            print(self.valor)

    def deposito(self):
        deposito = int(input('quanto você quer depositar?: '))
        self.valor = deposito+self.valor

    def mostrardados(self):
        print(self.nome,self.cpf,self.idade,self.email,self.telefone,self.valor)

    def showvalue(self):
        print(self.valor)

conta1 = contaBancaria('Tenshi', '12345678910', 24, 'tenshikisekishiro@gmail.com', '61991234567', 6300)
while True:
    question1 = input('você deseja fazer um saque (1), deposito (2), ver o saldo disponível (3) ou ver dados de usuario (4)? ')
    if question1 == '1':
        conta1.saque()
    if question1 == '2':
        conta1.deposito()
    if question1 == '3':
        conta1.showvalue()
    if question1 == '4':
        print(conta1.nome,conta1.cpf,conta1.idade, conta1.email, conta1.telefone)
    outraacao = input('deseja realizar outra ação? (y/n)')
    if outraacao == 'n':
        break
