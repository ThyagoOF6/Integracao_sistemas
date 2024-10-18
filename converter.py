class CsvToJsonConverter:
    def __init__(self, csv_list: list[str]):
        self.csv_list = csv_list

    def convert(self) -> str:
        result = []
        
        for line in self.csv_list:
            id, title, duration = line.split(",")
            title = title[6:].replace(".mp4", "")
            
            lesson_data = {
                "id": id.strip(),
                "titulo": title.strip(),
                "duracao": int(duration.strip())
            }
            
            result.append(lesson_data)
        
        json_result = "[\n"
        for i, entry in enumerate(result):
            json_result += "    {\n"
            json_result += f'        "id": "{entry["id"]}",\n'
            json_result += f'        "titulo": "{entry["titulo"]}",\n'
            json_result += f'        "duracao": {entry["duracao"]}\n'
            json_result += "    }"
            if i < len(result) - 1:
                json_result += ",\n"
            else:
                json_result += "\n"
        json_result += "]"
        
        return json_result