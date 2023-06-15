import argparse
import json
import pandas as pd

def main(perfil, valor):
    with open('perfiles.json') as file:
        data = json.load(file)
    
    if perfil in data:
        df = pd.DataFrame(data[perfil])
        if valor:
            if valor in df.columns:
                print(df[[valor]])
            else:
                print(f"No se encontró el valor {valor} en los perfiles {perfil}")
        else:
            print(df)
        return
                
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
    with open('perfiles.json') as file:
        data = json.load(file)
    parser = argparse.ArgumentParser(description="Busca perfiles metálicos para la construcción y sus valores.", epilog=f"Autor: Rafael Antonio Roa Hernández\nrafaroah@me.com\nVersión 1.0", formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument('-perfil', type=str, help='Nombre del perfil a buscar', default=None)
    parser.add_argument('-valor', type=str, help='Valor específico a buscar en el perfil', default=None)
    args = parser.parse_args()

    print(parser.description)
    print("Autor: Rafael Antonio Roa Hernández")
    print("rafaroah@me.com")
    print("Versión 1.0")

    if args.perfil is None:
        print(f"Perfiles disponibles en el fichero json: {', '.join(data.keys())}")
        args.perfil = input("Introduce el nombre del perfil a buscar: ")
    if args.valor is None:
        args.valor = input("Introduce el valor específico a buscar en el perfil (presiona enter si no buscas un valor específico): ")
    
    main(args.perfil, args.valor)
