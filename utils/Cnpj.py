from .Factory import Factory

from validate_docbr import CNPJ

class Cnpj(Factory):
    def cnpj_e_valido(self, cnpj: str) -> bool:
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError(
                "Quantidade de dígitos inválida!"
            )
        
    def format_cnpj(self) -> None:
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self) -> str:
        if self.tipo_documento.upper() == 'CNPJ':
            return self.format_cnpj()
    