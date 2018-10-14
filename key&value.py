def namelist(names):
    result = ''
    if names is [] or None :
        return ''
    if len(names) == 1:
        return names[0]['name']

    else :
        for i in range(len(names)-1) :
            result = result + names[i]['name'] + ', '
        result = result[:-2] + ' & '
        result = result + names[-1]['name']
        return result


print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))