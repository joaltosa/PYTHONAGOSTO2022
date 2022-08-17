# Cálculo de las taices de la ecuación cuadrática
A = float (input ( ' Ingrese el valor de A  ' ) )
B = float (input ( ' Ingrese el valor de B  ' ) )
C = float (input ( ' Ingrese el valor de C  ' ) )

# Cálculo del discriminante

disc =  B ** 2 - 4 * A * C

print ( )
# Análisis discriminante

if disc > 0:
    print ( ' Tiene 2 raíces reales diferentes ' )
elif disc == 0:
    print (' Tiene dos raíces iguales ' )
else:
    print ( ' Tiene dos raíces complejas diferentes' )
print ( )
# Cálculo de las raíces

print ( ' x1 = ' ,   ( - B + disc ** ( 1 / 2 ) ) / ( 2 * A )  ) 
print ( ' x2 = ' ,   ( - B - disc ** ( 1 / 2 ) ) / ( 2 * A )  )
print ( )