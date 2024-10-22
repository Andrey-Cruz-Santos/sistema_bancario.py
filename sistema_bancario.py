class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        else:
            return False

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero, titular, saldo_inicial=0):
        conta = Conta(numero, titular, saldo_inicial)
        self.contas.append(conta)
        return conta

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

# Exemplo de uso
banco = Banco()

# Criação de contas
conta1 = banco.criar_conta(1, 'Alice', 1000)
conta2 = banco.criar_conta(2, 'Bob', 500)

# Depósitos e Saques
conta1.depositar(200)
conta1.sacar(100)

# Transferências
conta1.transferir(300, conta2)

# Exibir saldos
print(f"Saldo da conta {conta1.numero} (titular: {conta1.titular}): {conta1.saldo}")
print(f"Saldo da conta {conta2.numero} (titular: {conta2.titular}): {conta2.saldo}")
