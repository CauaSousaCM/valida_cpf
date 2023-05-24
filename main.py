from utils.Telefone import Telefone
from utils.Cnpj import Cnpj
from utils.Cpf import Cpf
from utils.Datas import Data

telefone = Telefone("5585985670102")
cnpj = Cnpj("12345678910112", "cnpj")
cpf = Cpf("12561263611", "cpf")
data = Data()

print(telefone)
print(cnpj) # invalido!
print(cpf) # invalido!
print(data)
