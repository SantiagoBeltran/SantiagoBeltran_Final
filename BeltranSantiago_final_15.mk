BeltranSantiago_final_15.pdf: datos.dat graficador.py
	python graficador.py

%.dat : a.out
	./a.out

a.out: solucion15.cpp
	g++ solucion15.cpp