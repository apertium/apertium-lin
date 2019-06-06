import re

def calculate_duplicates():
    with open('e_bi_dr.txt', 'r') as d:
        o_list = []
        for line in d:
            o_list.append(line.strip())
        print(len(o_list)-len(list(set(o_list))), 'duplicates')
        print(set([x for x in o_list if o_list.count(x) > 1]))

def nouns():
    with open('nouns_2.txt', 'r') as d:
        with open('nouns.txt', 'a+') as f :
            for word in d:
                out = word.strip() + ':' + word.strip().replace('mo', '') + ' III-IV5-Suffix ; ! ""' + '\n'
                f.write(out)

def get_nouns_pl():
    # getting nouns that have a known plural form
    
    c = 0
    
    with open('../../lin_resources/eng_lin_dic.txt') as d:
        with open('../../lin_resources/nouns_pl.txt', 'a+') as f:
            for line in d:
                if re.search(r'\bpl\b', line):
                    f.write(line)
                    c += 1

    print(c, 'nouns found')

def classify_nouns():
    c = 0
    mo_ba_class = []
    ba_class = []
    mo_mi_class = []
    li_ma_class = []
    e_bi_class = []
    lo_ma_class = []
    no_class = []

    with open('../../lin_resources/nouns_pl.txt', 'r') as d:
        for line in d:
            line = line.split()

            i = 0
            while i < len(line):
                if re.search(r'\bpl\b', line[i]):
                #if 'pl' in line[i]:
                    # mo_ba
                    if line[i-1].startswith('mo') and line[i+1].startswith('ba'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        mo_ba_class.append(word)
                    #mo_mi
                    elif line[i-1].startswith('mo') and line[i+1].startswith('mi'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        mo_mi_class.append(word)
                    #li_ma
                    elif line[i-1].startswith('li') and line[i+1].startswith('ma'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        li_ma_class.append(word)
                    #e_bi
                    elif line[i-1].startswith('e') and line[i+1].startswith('bi'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        e_bi_class.append(word)
                    #lo_ma
                    elif line[i-1].startswith('lo') and line[i+1].startswith('ma'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        lo_ma_class.append(word)
                    #ba
                    elif line[i+1].startswith('ba'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        ba_class.append(word)
                    else:
                        no_class.append(line)
                i += 1
    with open('e_bi.txt', 'a+') as f:
        with open('e_bi_dr.txt', 'a+') as o:
            for word in e_bi_class:
                out = ''.join(word).replace('.', ',').replace(';', ',')+'\n'
                f.write(out)
                o.write(out.split(',')[0]+'\n')
    
    print('e_bi:', len(e_bi_class))

def yo():
    with open('nouns.txt', 'r') as d:
        with open('li_ma_dr.txt', 'a') as f:
            for word in d:
                if word.startswith('li'):
                    f.write(word.split(':')[0]+'\n')

def nouns_final():
    c=0
    with open('e_bi_dr.txt', 'r') as d:
        with open('e_bi_final.txt', 'a+') as o:
            with open('e_bi.txt', 'r') as f:
                for line in d:
                    c+=1
                    print(f.readline().strip())
                    out = line.strip() + ':' + line.strip()[1:]+ ' V-VI-Suffix ; ! ""\n'
                    o.write(out)
    print(c, 'words')

nouns_final()




    
                
            
