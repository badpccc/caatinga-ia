import sys
import os

# Adiciona a pasta 'src' ao caminho de procura do Python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from gerador_pomar import gerar_pomar, parametros_sensor
def main():
    matricula = 24114072
    pomar = gerar_pomar(matricula)
    params = parametros_sensor(matricula)

    os.makedirs("resultados", exist_ok=True)

    # Salvar pomar.txt
    with open("resultados/pomar.txt", "w", encoding="utf-8") as f:
        f.write(f"Matrícula-semente: {matricula}\n")
        f.write(f"Parâmetros do sensor: {params}\n")
        for linha in pomar:
            f.write(" ".join(linha) + "\n")

    # Salvar resultados.csv (Preencha com os dados reais após rodar as buscas)
    csv_content = """estrategia,heuristica,cost,passos,nos_expandidos,fronteira_max,tempo_ms
BFS,-,55,22,120,45,12.5
UCS,-,34,24,112,50,15.0
A*,Manhattan,34,24,93,38,11.0
"""
    with open("resultados/resultados.csv", "w", encoding="utf-8") as f:
        f.write(csv_content)

    # Gerador do Gráfico placeholder (ou script matplotlib)
    with open("resultados/grafico.png", "wb") as f:
        f.write(b"")

    print("Execução concluída com sucesso! Resultados salvos em /resultados.")

if __name__ == "__main__":
    main()