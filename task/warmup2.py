def check_lowercase_and_uppercase(sentence):
    number_of_UpperCase = 0
    number_of_LowerCase = 0
    for index in sentence:
        if index.isupper():
            number_of_UpperCase += 1
        if index.islower():
            number_of_LowerCase += 1
    return {'UPPERCASE', number_of_UpperCase, 'LOWERCASE', number_of_LowerCase}




def one_line(sentence):
    return {'upperCase': len(list(filter(lambda x: x.isupper(), sentence))),
            'lowerCase': len(list(filter(lambda a: a.islower(), sentence)))}


print(one_line('hello World'))
