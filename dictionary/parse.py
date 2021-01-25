import yaml
from liquid import Liquid
from unidecode import unidecode

dictionary = 'dictionary.yaml'
template = 'dictionary.latex.liquid'

with open(dictionary) as f:
    df = yaml.full_load(f)
keys = sorted(df, key = lambda s: unidecode(s.casefold()))

for e in df:
    if not 'ety' in df[e].keys():
        df[e]['ety'] = ''
    if not 'parts' in df[e].keys():
        df[e]['parts'] = ''

with open(template) as f:
    liq = Liquid(f)

ret = liq.render(dictionary = df, keys = keys)
print(ret)
