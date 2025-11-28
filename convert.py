import re
import json
import ast

def convert_ruby_hash_to_json(input_filepath, output_filepath="task1_valid.json"):
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            ruby_data_string = f.read()

        temp_string = ruby_data_string.replace('=>', ':')

        python_like_data = re.sub(r':(\w+):', r'"\1":', temp_string)

        data_list = ast.literal_eval(python_like_data)

        valid_json_string = json.dumps(data_list, ensure_ascii=False, indent=4)

        with open(output_filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(valid_json_string)

        print("good")
        

    except Exception as e:
        print(f"error: {e}")

convert_ruby_hash_to_json("task1_d.json")