
import sys

try:

    import time
    import os
    import re

except ModuleNotFoundError:

    import pip
    pip.main(['install', 'time', 'os', 're'])

except:

    print(f"Erreur inattendue lors de l'importation des modules\ndétail {str(ImportError)}", file=sys.stderr)
    exit()


frpy_version = "1.0.0"


def read(fichier: str)-> str|None:

    try:

        with open(fichier, 'r', encoding='utf-8') as f:
            return f.read()

    except Exception as err:

        print(f"Erreur lors de la lecture du fichier '{fichier}'\ndétail {str(err)}", file=sys.stderr)
        return None


def save_current(fichier: str, content: str)-> None:
    
    try:
        
        with open(fichier, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Le fichier {fichier} a été sauvegardé !")
    
    except Exception as err:
        
        print(f"Erreur lors de l'enregistrement\ndétail : {str(err)}", file=sys.stderr)
        exit()


def main_function()-> None:
    
    try:
        
        print("_____")
        print("| frenpy compiled executor")
        
        repeat: bool = True
        
        while repeat:
            repeat = not load(input("Quelle fichier éxécuter ? "))
        
    except KeyboardInterrupt:
        exit()
        
    except Exception as err:
        print(f"Erreur :\ndétail : {str(err)}", file=sys.stderr)


def load(file: str)-> bool:
    
    try:
        
        content:str|None = read(file)
        
        if content:
            
            if file.endswith(".py"):
                exec(content)
                return True
            
            elif file.endswith(".frenpy"):
                
                compiled: str = compile_frenpy(file)
                
                if compiled:
                    
                    if compiled in "frpy_debug=True":
                        print("Code source :\n", content)
                        print("Code compilé :\n", compiled)
                    
                    if "frpy_scc=True" in content:
                        save_current("compiled.py", compiled)
                    
                    exec(compiled)
                    return True
            
            elif file == "":
                print("Erreur : vous n'avez choisi aucun fichier", file=sys.stderr)
            
            else:
                print("Erreur : fichier non supporté", file=sys.stderr)
    
    except Exception as err:
        print(f"Erreur :\ndétail : {str(err)}", file=sys.stderr)
    
    return False


def compile_frenpy(file: str)-> str|None:

    data = read(file)

    if data is None:
        return

    try:

        data = re.sub(r'(?<!")\bdéfinir\b(?!")', 'def', data)
        data = re.sub(r'(?<!")\bpour\b(?!")', 'for', data)
        data = re.sub(r'(?<!")\bimporter\b(?!")', 'import', data)
        data = re.sub(r'(?<!")\bafficher\b(?!")', 'print', data)
        data = re.sub(r'(?<!")\bsi\b(?!")', 'if', data)
        data = re.sub(r'(?<!")\bou sinon\b(?!")', 'elif', data)
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
        data = re.sub(r'(?<!")\bfrpy_debug=True\b(?!")', '', data)
        data = re.sub(r'(?<!")\bfrpy_debug=False\b(?!")', '', data)
        
        return data

    except Exception as err:
        
        print(f"Erreur lors de l'étape de compilation :\ndétail : {str(err)}", file=sys.stderr)
        exit()


if __name__ == "__main__":
    main_function()
