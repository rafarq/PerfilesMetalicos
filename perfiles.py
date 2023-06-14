import argparse
import json
import pandas as pd

def main(perfil, valor):
    with open('perfiles.json') as file:
        data = json.load(file)
        
    for key in data:
        for p in data[key]:
            if p['Perfil'].lower() == perfil.lower():
                df = pd.DataFrame(p, index=[0])
                if valor:
                    if valor in df.columns:
                        print(f"El valor de {valor} para el perfil {perfil} es: {df[valor][0]}")
                    else:
                        print(f"No se encontró el valor {valor} para el perfil {perfil}")
                else:
                    print(df)
                return
                
    print(f"No se encontró el perfil {perfil}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buscar perfiles y sus valores")
    parser.add_argument('-perfil', type=str, help='Nombre del perfil a buscar')
    parser.add_argument('-valor', type=str, help='Valor específico a buscar en el perfil')
    args = parser.parse_args()
    main(args.perfil, args.valor)
