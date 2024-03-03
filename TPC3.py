import re

texto = """On35612=87=oFF233=
844,aduyoNajdi=56=OFF244=
"""
     

def somadorOnOff(texto):
    flag = 0
    soma = 0
    i = 0
    
    while texto and i< len(texto): 
        if re.match("(?i:on)", texto[i:i+2]):
            flag = 1
        elif re.match("(?i:off)", texto[i:i+3]):
            flag = 0
        elif re.match("=", texto[i]):
            print(soma)
        
        if re.match("[0-9]", texto[i]) and flag == 1:
            soma += int(texto[i]) 

        i +=1

    
