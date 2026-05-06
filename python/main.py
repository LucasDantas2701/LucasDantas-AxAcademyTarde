import os
import importlib.util

# Caminho correto da pasta modules
modules_dir = os.path.join(os.path.dirname(__file__), "src", "modules")

# Pede a letra ao usuário
letra = input("Digite a letra do módulo que deseja executar: ").upper()

for item in os.listdir(modules_dir):
    item_path = os.path.join(modules_dir, item)

    # Só pastas que começam com a letra
    if os.path.isdir(item_path) and item.upper().startswith(letra):
        main_file = os.path.join(item_path, "main.py")
        if os.path.exists(main_file):
            print(f"Executando {item}/main.py...")
            
            # Executa o main.py dinamicamente
            spec = importlib.util.spec_from_file_location(f"{item}.main", main_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)