import yaml

filename = 'proto-danetian.yaml'

def load_file(filename):
    with open(filename) as F:
        try:
            lexicon = yaml.safe_load(F)
        except yaml.YAMLError as exc:
            print(exc)
    return lexicon

def filter_class(lexicon, c):
    filtered = []
    for e in lexicon:
        if 'class' in e.keys() and e['class'] == c:
            filtered.append(e)
    return filtered


df = load_file(filename)
df = filter_class(df, 'U') + filter_class(df, 'III-i')
for e in df:
    if 'inflection' in e.keys():
        lemma = e['key']
        cls = e['class']
        e = e['inflection']
        if 'singular' in e.keys():
            nom_s, acc_s, gen_s, abl_s, dat_s, loc_s, ins_s = e['singular'].values()
        else:
            nom_s, acc_s, gen_s, abl_s, dat_s, loc_s, ins_s = ['']*7
        if 'plural' in e.keys():
            nom_p, acc_p, gen_p, abl_p, dat_p, loc_p, ins_p = e['plural'].values()
        else:
            nom_p, acc_p, gen_p, abl_p, dat_p, loc_p, ins_p = ['']*7

        print(r'\begin{tabular}{l|ll}')
        print(r'\toprule')
        print(r'\multicolumn{3}{c}{', lemma, '(' + cls + ')', r'} \\')
        print(r'\midrule')
        print(r'~ & singular & plural \\')
        print(r'\midrule')

        print('nom &', nom_s, '&', nom_p, r'\\')
        print('acc &', acc_s, '&', acc_p, r'\\')
        print('gen &', gen_s, '&', gen_p, r'\\')
        print('abl &', abl_s, '&', abl_p, r'\\')
        print('dat &', dat_s, '&', dat_p, r'\\')
        print('loc &', loc_s, '&', loc_p, r'\\')
        print('ins &', ins_s, '&', ins_p, r'\\')

        print(r'\bottomrule')
        print(r'\end{tabular}')
        print(r'\\\\\\')
        print('\n\n')
