def escolhe_taxi(tf1, vqr1, tf2, vqr2):
    #convert string inputs to floats
    f_tf1 = float(tf1.replace(',', '.'))
    f_vqr1 = float(vqr1.replace(',', '.'))
    f_tf2 = float(tf2.replace(',', '.'))
    f_vqr2 = float(vqr2.replace(',', '.'))
    
    # handle identical pricing structures
    if f_tf1 == f_tf2 and f_vqr1 == f_vqr2:
      return "Tanto faz"
    
    # if equal, the one with the lower fixed fee is always cheaper
    if f_vqr1 == f_vqr2:
        return "Empresa 1" if f_tf1 < f_tf2 else "Empresa 2"
    
    # intersection of y1 = f_vqr1*x + f_tf1 and y2 = f_vqr2*x + f_tf2
    n = (f_tf2 - f_tf1) / (f_vqr1 - f_vqr2)
    formatado = round(n, 2)

    #if the intersection occurs at or before distance 0, one company is always cheaper
    if n <= 0:
      return "Empresa 1" if f_vqr1 < f_vqr2 else "Empresa 2"
    
    # choose which company starts cheaper and which becomes cheaper after the break-even point
    if f_tf1 < f_tf2:
        xpto, ypto = "1", "2"
    else:
        xpto, ypto = "2", "1"

    return f"Empresa {xpto} quando a distância < {formatado}, Tanto faz quando a distância = {formatado}, Empresa {ypto} quando a distância > {formatado}"