from converter import CsvToJsonConverter

def main():
    csv_list = [
        "1,Aula 01.1 - Introdução ao curso.mp4,300",
        "2,Aula 02.1 - Instalação do software.mp4,420",
        "3,Aula 03.1 - Configurações iniciais.mp4,240"
    ]
    
    converter = CsvToJsonConverter(csv_list)
    
    json_result = converter.convert()
    
    output_file = "dados_aulas.json"
    
    with open(output_file, "w") as file:
        file.write(json_result)
    
    print(f"JSON salvo com sucesso no arquivo '{output_file}'")

if __name__ == "__main__":
    main()