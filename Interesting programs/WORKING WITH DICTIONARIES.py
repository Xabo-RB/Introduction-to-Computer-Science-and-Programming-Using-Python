animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    ls = []
    for x in aDict.values():
        ls += x
    number = len(ls)
    return number


def biggest(aDict):
    #HALLA EL VALOR MÁS GRANDE DEL DICCIONARIO Y SU KEY CORRESPONDIENTE
    
    key_list = list(aDict.keys())
    val_list = list(aDict.values())
    
    # print key with val the maximum
    indexMax = max(val_list)
    position = val_list.index(indexMax)
    
    return key_list[position]

def biggest(aDict):
    #HALLA LA POSICIÓN DEL DICCIONARIO DONDE HAY UNA LISTA MÁS GRANDE, ES DECIR
    #CON MÁS ELEMENTOS DENTRO DE LA LISTA Y SI FUERA NINGUNO DEVUELVE NONE
    
    key_lngst_val = None
    klv_len = 0
    for k in aDict:
       if len(aDict[k]) >= klv_len:
            key_lngst_val = k
            klv_len = len(aDict[k])
    return key_lngst_val

