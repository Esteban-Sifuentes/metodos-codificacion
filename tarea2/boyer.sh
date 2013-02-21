morris=morris.dat
boyer=boyer.dat

##para ver si existen los archivos
##si es asi los borra
##agradecimiento a pedrito por
##esta parte de archivos

if [ -e $morris ]; then
	rm morris.dat
fi
if [ -e $boyer ]; then
	rm boyer.dat
fi


touch morris.dat
touch boyer.dat
rm repe.dat
touch grafica.dat
rm grafica.dat
touch grafica.dat
##no delcaramos mas varaibles ya que no ase falta
## la varaible dentro del for toma los valores despues de in
## en cada regreso

for PATRONES in 3 4 5 6 7 8 # cantidad de letras para los patrones
do
	for TEXTO in 10 20 30 40 50 60 70 80 # cantidad de letras para los
	do
		for REPETICIONES in 1 2 3 4 5
		do
			touch repe.dat
			res=`python Morris.py $TEXTO $PATRONES`
			echo $res
			echo $res >> repe.dat
		done
		res=`awk -f boyer.awk repe.dat`
		echo $res
		echo valor de res $res
		rm repe.dat
		echo $PATRONES $TEXTO $res >> grafica.dat ##pasamos datos al archivo final
	done
	echo '' >> grafica.dat
done
#echo '' >> grafica.dat
echo $PATRONES
gnuplot broyer.plot ##crear la imagen de la grafica
