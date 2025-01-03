# frenpy

`frenpy` est une bibliothèque permettant d'exécuter des scripts Python écrits en français.

## Installation

Pour installer la bibliothèque, utilisez pip :

```sh
pip install frenpy
```

## Importation

Pour importer la bibliothèque dans votre script Python :

```python
import frenpy
```

## Fonctionnalités

### Compiler un fichier `.frenpy` en `.py`

La fonction `compile_frenpy` permet de transformer un fichier `.frenpy` en code Python.

```python
data_compiled = frenpy.compile_frenpy(filepath)
```

### Charger et exécuter un fichier compilé `.frenpy` ou `.py`

La fonction `load` permet de charger et d'exécuter un fichier `.frenpy` ou `.py`.

```python
frenpy.load(filepath)
```

### Exécuter des fichiers `.py` ou `.frenpy` de manière interactive

La fonction `main_function` permet de lancer des fichiers `.py` ou `.frenpy` de manière interactive.

```python
frenpy.main_function()
```

## Syntaxe des fichiers `.frenpy`

Les fichiers `.frenpy` sont des scripts Python écrits en français. Voici la liste des mots-clés traduits :

```py
def => définir
import => importer
print => afficher
if => si
else => sinon
while True => répéter à l'infini
round => arrondir
os.system("cls") => nouvelle écran
break => stopper
time.sleep => attendre
input => saisir
in => dans la
retourner => return
et => and
ou => or
non => not
vrai => True
faux => False
pour => for
tant que => while
essayer => try
except => except
avec => with
classe => class
importer comme => import as
depuis => from
lever => raise
continuer => continue
passer => pass
supprimer => del
global => global
lambda => lambda
assurer => assert
ranger => sort
longueur => len
ouvrir => open
liste => list
dictionnaire => dict
ensemble => set
tuple => tuple
enumerer => enumerate
toutes => all
n'importe lequel => any
plage => range
type => type
frpy_info => affiche la version actuel
frpy_scc=True => sauvegarde la version compilée
frpy_debug=true => active le debug
```

***Tout les mots commençant par frpy ne sont pas transformable en python car ils n'ont pas de traduction littéral**


## Exemple

Voici un exemple de fichier `.frenpy` :

```py
# importations :
importer os
importer time

# configuration de frenpy :
frpy_debug=True
frpy_scc=True

# test de la fonction :
afficher("--- version de frpy ---")
frpy_info
afficher("-----------------------")
attendre(3)
afficher("Bonjour, ce texte est un exemple")

# test interaction
question = saisir("es-tu riche ?")
si "oui" dans la question :
    afficher("tu es riche !")
si "non" dans la question:
    afficher("tu n'es pas riche !")
```

## Contributeurs 

<a href="https://github.com/slohwnix/frenpy/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=slohwnix/frenpy" />
</a>
