class Funcionario:
    def __init__(self, nome, email):
        # Atributos
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    # Adicionar o mês em que o funcionário trabalhou,
    # atribuir ao mês as horas trabalhadas
    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    # Adicionar ao mês o valor ganho pelo período de
    # trabalho desse funcionário
    def cadastro_salario_hora(self, mes, valor):
        if(mes not in self.salario_hora):
            self.salario_hora[mes] = valor

    # Calculo das horas trabalhadas do mês pelo salário
    # ganho por período
    def calcular_salario(self, mes):
        if(mes not in self.horas) or (mes not in self.salario_hora):
            print("Mês Inexistente!!")
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):
        # Saída
        return f"Funcionário: {self.nome}," \
               f" \nEmail: {self.email}," \
               f" \nHoras/Mês: {self.horas}," \
               f" \nSalário-hora: {self.salario_hora}"
