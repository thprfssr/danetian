import yaml

with open('inflections.yaml') as file:
    INFLECTIONS = yaml.full_load(file)

def append_noun_ending(root, noun_class, case_and_number):
    return root + INFLECTIONS['nouns'][noun_class][case_and_number]
