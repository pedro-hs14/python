var = input('Digite alguma coisa: ')

tipo = type(var)
print('A classe de {} é: {}'.format(var, tipo))
print('O valor digitado é numérico? {}.'.format(var.isnumeric()))
print('O valor digitado é alfanumérico? {}.'.format(var.isalnum()))
print('O valor digitado possui apenas letras? {}.'.format(var.isalpha()))
print('O valor digitado está totalmente minúsculo? {}.'.format(var.islower()))
print('O valor digitado está totalmente maiúsculo? {}.'.format(var.isupper()))
print('O valor digitado possui a primeira letra maiúscula? {}.'.format(var.istitle()))


