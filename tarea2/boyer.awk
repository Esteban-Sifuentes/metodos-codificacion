#!/usr/bin/awk -f
BEGIN {
    suma = 0.0 ##suma de porcentaje de exito
    cont = 0 ##la cantidad de estos porcentaje
}
{
    suma = suma +  $1 ##sumamos uno por uno
    cont = cont + 1 ##contamos cuantos son
}
END {
    print suma/cont ##sacamos el promedio
}