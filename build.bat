del dist
python -m build
py -m twine upload --repository testpypi dist/*