import json

# Configuração inicial
config = {
    "aulas_por_turma": 4,      # 1 aula por semana, 4 semanas no mês
    "num_turmas": 3,           # 3 turmas no mês
}

# Função para calcular ganhos
def calcular_ganhos(valor_hora_aula, horas_por_aula, valor_hora_supermodulo, horas_por_supermodulo,
                    valor_hora_workshop, horas_por_workshop, num_workshops, num_supermodulos):
    # Cálculo do ganho por turma
    valor_por_aula = valor_hora_aula * horas_por_aula
    ganho_turmas = config["num_turmas"] * config["aulas_por_turma"] * valor_por_aula
    
    # Cálculo do ganho por supermódulo
    valor_por_supermodulo = valor_hora_supermodulo * horas_por_supermodulo
    ganho_supermodulos = num_supermodulos * valor_por_supermodulo
    
    # Cálculo do ganho por workshop
    valor_por_workshop = valor_hora_workshop * horas_por_workshop
    ganho_workshops = num_workshops * valor_por_workshop
    
    # Cálculo do ganho total
    ganho_total = ganho_turmas + ganho_supermodulos + ganho_workshops
    
    return {
        "ganho_turmas": ganho_turmas,
        "ganho_supermodulos": ganho_supermodulos,
        "ganho_workshops": ganho_workshops,
        "ganho_total": ganho_total
    }

# Função para obter entrada do usuário com validação
def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

# Entrada de valores
valor_hora_aula = obter_float("Digite o valor recebido por hora-aula: ")
horas_por_aula = obter_float("Digite a duração de cada aula em horas: ")

valor_hora_supermodulo = obter_float("Digite o valor recebido por hora no supermódulo: ")
horas_por_supermodulo = obter_float("Digite a duração de cada supermódulo em horas: ")
num_supermodulos = int(obter_float("Quantos supermódulos você terá este mês? "))

valor_hora_workshop = obter_float("Digite o valor recebido por hora no workshop: ")
horas_por_workshop = obter_float("Digite a duração de cada workshop em horas: ")
num_workshops = int(obter_float("Quantos workshops você fará este mês? "))

# Cálculo de ganhos
ganhos = calcular_ganhos(valor_hora_aula, horas_por_aula, valor_hora_supermodulo, horas_por_supermodulo,
                         valor_hora_workshop, horas_por_workshop, num_workshops, num_supermodulos)

# Determinar a atividade mais rentável
# Comparar apenas os ganhos das atividades específicas
ganhos_atividade = {
    "turmas": ganhos["ganho_turmas"],
    "supermodulos": ganhos["ganho_supermodulos"],
    "workshops": ganhos["ganho_workshops"]
}

mais_rentavel = max(ganhos_atividade, key=ganhos_atividade.get)

# Exibição dos ganhos mensais
print("\nResumo dos ganhos mensais:")
print(json.dumps(ganhos, indent=4))

# Exibição da atividade mais rentável
valor_mais_rentavel = ganhos_atividade[mais_rentavel]
print(f"\nA atividade mais rentável é: {mais_rentavel} com ganho de: R${valor_mais_rentavel:.2f}")
