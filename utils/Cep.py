class Cep:
    def __init__(self, cep: str) -> None:
        self.cep = str(cep)
        if self.validate_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP invalido!")
    
    def __str__(self) -> str:
        return self.format_cep()
    
    def validate_cep(self, cep: str) -> bool:
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self) -> str:
        return f"{self.cep[:5]}-{self.cep[5:]}"