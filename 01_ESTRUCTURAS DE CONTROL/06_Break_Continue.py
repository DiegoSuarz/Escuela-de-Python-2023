c = 0

while c <10:
    c += 1
    print(c)

    if c == 5:
        #print("Termina el bucle")
        #break #temina el bucle en la iteraccion #5
        
        print("Continue activado")
        continue #salta a la siguiente iteraccion
    print('iteraccion numero', c)   
else:  #no se ejecuta else ya que while no se ha terminado por causa del break
    print('Fin de While')
