import yaml
from liquid import Liquid
from unidecode import unidecode

dictionary = 'dictionary.yaml'
template = 'dictionary.latex.liquid'

with open(dictionary) as f:
    df = yaml.full_load(f)
df = sorted(df, key = lambda s: unidecode(s['key'].casefold()))

for e in df:
    if not 'ety' in e.keys():
        e['ety'] = ''
    if not 'parts' in e.keys():
        e['parts'] = ''
    for item in e['definitions']:
        if 'tag' not in item.keys():
            item['tag'] = ''
        if 'ex' not in item.keys():
            item['ex'] = ''

with open(template) as f:
    liq = Liquid(f)

ret = liq.render(dictionary = df)
print(ret)
