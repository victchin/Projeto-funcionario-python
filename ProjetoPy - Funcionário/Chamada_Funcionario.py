from Objeto_Funcionario import *

# Instânciação do objeto
funcionario = Funcionario("Matheus", "matheus@NãoSeiOQueDizer.com")

# Adiciona o mês do cadastro
funcionario.cadastro_hora("Janeiro", 300)
funcionario.cadastro_hora("Fevereiro", 200)

# Adiciona o valor ganho por hora trabalhada
funcionario.cadastro_salario_hora("Janeiro", 30)
funcionario.cadastro_salario_hora("Fevereiro", 30)

print(funcionario)
# Calcular o salário de Janeiro e de Fevereiro desse funcionario
print(f"Calculo do salário ganho em janeiro: {funcionario.calcular_salario('Janeiro')}")
print(f"Calculo do salário ganho em Fevereiro: {funcionario.calcular_salario('Fevereiro')}")

funcionario.__repr__()

# SAÍDA
# Funcionário: Matheus,
# Email: matheus@NãoSeiOQueDizer.com,
# Horas/Mês: {'Janeiro': 300, 'Fevereiro': 200},
# Salário-hora: {'Janeiro': 30, 'Fevereiro': 30}
# Calculo do salário ganho em janeiro: 9000
# Calculo do salário ganho em Fevereiro: 6000
