import os

frpy_version = "2"

try:
    import time
    import os
    import re
    import json
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'time', 'os', 're', 'json'])
except:
    print("erreur inattendue : " + str(ImportError))
    exit()

def recup_donnee_fichier(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier} : {e}")
        return None
    
def save_actual_file(fichier_name, content):
    try:
        with open(fichier_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Le fichier {fichier_name} a été sauvegardé !")
    except Exception as errors:
        print("Erreur lors de l'enregistrement : " + str(errors))
        exit()

def main_function():
    try:
        print("_____")
        print("| frenpy compiled executor")
        File_toexecute = input("quelle fichier éxécuter ? ")
        if File_toexecute.endswith(".py"):
            with open(File_toexecute, 'r', encoding='utf-8') as file:
                exec(file.read())
        elif File_toexecute.endswith(".frenpy"):
            data_code = recup_donnee_fichier(File_toexecute)
            compiled_code = compile_frenpy(File_toexecute)
            if compiled_code:
                if "frpy_debug=True" in compiled_code:
                    print("Code compilé :\n", compiled_code)
                    print("Code source :\n", data_code)
                if "frpy_scc=True" in data_code:
                    save_actual_file("compiled.py", compiled_code)
                exec(compiled_code)
        elif File_toexecute == "":
            print("erreur : vous n'avez choisi aucun fichier")
        else:
            print("erreur : fichier non supporté")
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print("erreur : " + str(error))

def load(File_toexec):
    try:
        data_code = recup_donnee_fichier(File_toexec)
        if data_code:
            if File_toexec.endswith(".py"):
                exec(data_code)
            elif File_toexec.endswith(".frenpy"):
                compiled_code = compile_frenpy(File_toexec)
                if compiled_code:
                    if compiled_code in "frpy_debug=True":
                        print("Code compilé :\n", compiled_code)
                        print("Code source :\n", data_code) 
                    if "frpy_scc=True" in data_code:
                        save_actual_file("compiled.py", compiled_code)
                    elif compiled_code in "frpy_debug=False":
                        pass
                    else:
                        pass
                    exec(compiled_code)
            elif File_toexec == "":
                print("erreur : vous n'avez choisi aucun fichier")
            else:
                print("erreur : fichier non supporté")
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print("erreur : " + str(error))

def load_replacement_words(json_file):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, json_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier JSON {json_file} : {e}")
        return {}

def get_words_frenpy():
    try:
        replacement_words = load_replacement_words('words.json')
        return list(replacement_words.keys())
    except Exception as e:
        print(f"Erreur lors de la récupération des mots : {e}")
        return []

def compile_frenpy(file_to_compile):
    import re
    data = recup_donnee_fichier(file_to_compile)
    if data is None:
        return None
    try:
        replacement_words = load_replacement_words('words.json')
        for fr_word, py_word in replacement_words.items():
            
            if data in "frpy_info":
                data = re.sub(rf'(?<!")\b{fr_word}\b(?!")', f'print("version actuelle : {frpy_version}")', data)
            data = re.sub(rf'(?<!")\b{fr_word}\b(?!")', py_word, data)
        return data
    except Exception as errors:
        print("-Erreur lors de l'étape de compilation")
        print("-Echec : " + str(errors))
        exit()

if __name__ == "__main__":
    main_function()
