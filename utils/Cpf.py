from .Factory import Factory  

from validate_docbr import CPF

class Cpf(Factory):
    def cpf_e_Valido(self, cpf: str):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError(
                "Quantidade de dígitos inválida!"
            )

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        if self.tipo_documento.upper() == 'CPF':
            return self.format_cpf()
    