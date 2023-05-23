"""
Módulo responsável por armazenar a classe Factory e seu construtor
"""
class Factory:
    def __init__(self, documento: str, tipo_documento: str) -> None:
        self.tipo_documento = str(tipo_documento)
        documento = str(documento)
        if self.tipo_documento.upper() == "CPF":
            if self.cpf_e_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento.upper() == "CNPJ":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")
    
    