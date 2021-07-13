import yaml

filename = 'inflection.yaml'

def load_file(filename):
    with open(filename) as F:
        try:
            df = yaml.safe_load(F)
        except yaml.YAMLError as exc:
            print(exc)
    return df

df = load_file(filename)



def inflect(root, declension):
    endings = df[declension]
    inflected = endings.copy()
    for number in endings.keys():
        for case in endings[number].keys():
            inflected[number][case] = root + endings[number][case]
    return inflected

print(inflect('ben', 'I'))
