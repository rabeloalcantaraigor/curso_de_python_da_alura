from abc import ABCMeta, abstractmethod
import array as arr
from tkinter.filedialog import SaveFileDialog # evitar de usar o array
import numpy as np
from functools import total_ordering

# class ContaCorrente:
    
#     def __init__(self, codigo):
#         self.codigo = codigo
#         self.saldo = 0
        
#     def deposita(self, valor):
#         self.saldo += valor
    
#     def __str__(self):
#         return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"
    
class Conta(metaclass=ABCMeta):
    
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod
    def passa_o_mes(self):
        pass
    
    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"
    
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2
    
class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
        
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        
        return self._codigo < outro._codigo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"
        
    
# conta_do_gui = ContaCorrente(15)
# print(conta_do_gui)

# conta_do_gui.deposita(500)
# print(conta_do_gui)

# conta_da_dani = ContaCorrente(47685)
# conta_da_dani.deposita(1000)
# print(conta_da_dani)

# contas = [conta_do_gui, conta_da_dani]
# for conta in contas:
#     print(conta)
    
# contas = [conta_do_gui, conta_da_dani, conta_do_gui]

# print(contas[0])

# conta_do_gui.deposita(100)

# print(contas[0])

# print(contas[2])

# print(Conta(88))

# conta16 = ContaCorrente(16)
# conta16.deposita(1000)
# conta16.passa_o_mes()
# print(conta16)

# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)
# conta17.passa_o_mes()
# print(conta17)

# contas = [conta16, conta17]

# for conta in contas:
#     conta.passa_o_mes() # ducking typing
#     print(conta)

# # arr.array('d', [1, 3.5], 'igor')
# numeros=np.array([1,3.5])

# conta1 = ContaSalario(37)
# print(conta1)

# conta2 = ContaSalario(37)
# print(conta2)

# print(conta1 == conta2)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme < conta_da_daniela)

for conta in sorted(contas):
    print(conta)
    
print(conta_do_guilherme <= conta_da_daniela)
print(conta_do_guilherme <= conta_do_paulo)
print(conta_do_guilherme < conta_do_guilherme)
print(conta_do_guilherme == conta_do_guilherme)
print(conta_do_guilherme <= conta_do_guilherme)