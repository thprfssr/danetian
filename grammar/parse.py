import yaml
from liquid import Liquid
from unidecode import unidecode
import sys

dictionary = sys.argv[1]
template = sys.argv[2]

with open(dictionary) as f:
    df = yaml.full_load(f)

if not 'active' in df.keys():
    df['active'] = ''
elif not 'mediopassive' in df.keys():
    df['mediopassive'] = ''

with open(template) as f:
    liq = Liquid(f)

ret = liq.render(word = df)
print(ret)
