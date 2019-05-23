punto15.pdf : python DelgadoMaria_final_15.py punto15.dat
	python DelgadoMaria_final_15.py
    
DelgadoMaria_final_15.py : g++ DelgadoMaria_final_15.cpp punto15.dat
	g++ DelgadoMaria_final_15.cpp
	./a.out 