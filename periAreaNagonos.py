# Perimetro y área de los n-agonos
numlad = int ( input ( ' Escriba el número de lados de la figura ' ) )
lado = float (input ( ' Ingrese el valor del lado ' ) )
apotem = float ( input ( ' Escriba el valor de la apotema ' ) )

perim = numlad * lado

area = perim * apotem / 2

print ( 'El perímetro es ' , perim , ' y el área es ' , area)