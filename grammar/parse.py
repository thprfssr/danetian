import yaml
from liquid import Liquid
from unidecode import unidecode
import sys

dictionary = sys.argv[1]
template = sys.argv[2]

with open(dictionary) as f:
    df = yaml.full_load(f)

active = None
mediopassive = None
if 'active' in df.keys():
    active = df['active']
if 'mediopassive' in df.keys():
    mediopassive = df['mediopassive']

with open(template) as f:
    liq = Liquid(f)

ret = liq.render(active = active, mediopassive = mediopassive)
print(ret)
