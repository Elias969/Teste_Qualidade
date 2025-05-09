def calcular_imc(peso, altura):
 if altura <= 0:
    raise ValueError('A altura deve ser maior que zero')
 return round(peso / (altura ** 2), 2)