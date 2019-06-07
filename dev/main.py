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

def nouns_to_bidix():
    c = 0
    with open('nouns.txt', 'r') as d:
        with open('nouns_bidix.txt', 'a+') as f:
            for line in d:
                line = line.split()

                #cl7
                if 'VII-VIII-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl7"/></r></p></e>\n'
                        f.write(out)
                
                #cl1
                if 'I-II-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl1"/></r></p></e>\n'
                        f.write(out)

                #cl1a
                if 'Ia-II-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl1a"/></r></p></e>\n'
                        f.write(out)

                #cl3
                if 'III-IV-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl3"/></r></p></e>\n'
                        f.write(out)

                #cl5
                if 'V-VI-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl5"/></r></p></e>\n'
                        f.write(out)


                #cl9
                if 'IX-X-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl9"/></r></p></e>\n'
                        f.write(out)

                #cl11
                if 'XI-VI-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl11"/></r></p></e>\n'
                        f.write(out)

                #cl14
                if 'XIV-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.lower().replace('"', '').replace(',', '') + '<s n="n"/></l><r>' + line[0].split(':')[0] + '<s n="n"/><s n="cl14"/></r></p></e>\n'
                        f.write(out)

                #proper nouns
                if 'Anthroponym-Suffix' in line or 'Toponym-Suffix' in line or 'MiscProper-Suffix' in line:
                    for word in line[4:]: # words with multiple translations
                        out = '<e><p><l>' + word.replace('"', '').replace(',', '') + '<s n="np"/></l><r>' + line[0].split(':')[0] + '<s n="np"/></r></p></e>\n'
                        f.write(out)

                

    print(c,'lines added')


def verbs_to_bidix():
    with open('verbs.txt', 'r') as d:
        with open('verbs_bidix.txt', 'a+') as f:
            for line in d:
                line = line.split()

                for word in line[5:]:
                    out = '<e><p><l>' + word.lower().replace(',','').replace('"', '') + '<s n="vblex"/></l><r>' + line[0].split(':')[0] + '<s n="vblex"/></r></p></e>\n'
                    f.write(out)

verbs_to_bidix()

    


    
                
            
