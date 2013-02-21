set term png
set output 'boyer.png'
set xrange [0:10] ##rangos
set yrange [0:80] ##rangos
set zrange [0:100] ##rangos
set xlabel "longitud del texto" ##labes
set ylabel "longitud del patron"
set zlabel "iteraciones"
set pm3d implicit at s ##para los colores y paleta
splot 'grafica.dat'