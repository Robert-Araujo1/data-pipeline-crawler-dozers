import papermill as pm
import os

# Etapas do pipeline
def run_pipeline():
    print("🔁 Iniciando pipeline...")
    os.makedirs("output", exist_ok=True)
    
    etapas = [
        ("01_extract.ipynb", "01_extract_output.ipynb"),
        ("02_transform.ipynb", "02_transform_output.ipynb"),
        ("03_load.ipynb", "03_load_output.ipynb"),
        ("04_analyze.ipynb", "04_analyze_output.ipynb"),
    ]

    for input_nb, output_nb in etapas:
        print(f"📒 Executando {input_nb}...")
        pm.execute_notebook(
            "notebooks/" + input_nb,
            "output/" + output_nb
        )

    print("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
