frpy_version = "1"

try:
    import time
    import os
    import re
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'time', 'os', 're'])
except:
    print("erreur inattendue : " + str(ImportError))
    exit()
def recup_donnee_fichier(fichier):
    try:
        with open(f"./{fichier}", 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier} : {e}")
        return None

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

def compile_frenpy(file_to_compile):
    import re
    data = recup_donnee_fichier(file_to_compile)
    if data is None:
        return None
    try:
        data = re.sub(r'(?<!")\bimporter\b(?!")', 'import', data)
        data = re.sub(r'(?<!")\bafficher\b(?!")', 'print', data)
        data = re.sub(r'(?<!")\bsi\b(?!")', 'if', data)
        data = re.sub(r'(?<!")\bsinon\b(?!")', 'else', data)
        data = re.sub(r'(?<!")\brépéter à l\'infini\b(?!")', 'while True', data)
        data = re.sub(r'(?<!")\barrondir\b(?!")', 'round', data)
        data = re.sub(r'(?<!")\bnouvelle_écran\b(?!")', 'os.system("cls")', data)
        data = re.sub(r'(?<!")\bfrpy_info\b(?!")', f'print("version actuelle : {frpy_version}")', data)
        data = re.sub(r'(?<!")\bstopper\b(?!")', 'break', data)
        data = re.sub(r'(?<!")\battendre\b(?!")', 'time.sleep', data)
        data = re.sub(r'(?<!")\bsaisir\b(?!")', 'input', data)
        data = re.sub(r'(?<!")\bdans la\b(?!")', 'in', data)
        data = re.sub(r'(?<!")\bfrpy_scc=True\b(?!")', '', data)
        return data
    except Exception as errors:
        print("-Erreur lors de l'étape de compilation")
        print("-Echec : " + str(errors))
        exit()

if __name__ == "__main__":
    main_function()
