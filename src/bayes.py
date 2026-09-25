from gerador_pomar import parametros_sensor

def calcular_bayes(matricula: int):
    params = parametros_sensor(matricula)
    prev = params["prevalencia"]
    sens = params["sensibilidade"]
    tfp = params["taxa_falso_positivo"]
    talhoes = params["talhoes_por_semana"]

    # P(Sensitivo | Infestado) = sens
    # P(Sensitivo | Nao Infestado) = tfp
    # P(Infestado) = prev
    # P(Nao Infestado) = 1 - prev
    
    p_sensor_pos = (sens * prev) + (tfp * (1 - prev))
    p_inf_dado_pos = (sens * prev) / p_sensor_pos if p_sensor_pos > 0 else 0

    print(f"Parâmetros do Sensor para {matricula}: {params}")
    print(f"(a) P(infestado | sensor positivo) = {p_inf_dado_pos:.4f}")
    
    falsos_por_100 = (1 - p_inf_dado_pos) * 100
    print(f"(b) A cada 100 alertas, cerca de {falsos_por_100:.2f} serão falsos.")

    # Alertas falsos semanais
    # Total de alertas gerados ou proporção de falsos positivos sobre talhões sadios
    sadios = talhoes * (1 - prev)
    total_falsos_positivos = sadios * tfp
    horas_perdidas = (total_falsos_positivos * 12) / 60
    print(f"(c) Alertas falsos semanais: {total_falsos_positivos:.1f} | Horas gastas: {horas_perdidas:.1f}h")

if __name__ == "__main__":
    calcular_bayes(24114072)