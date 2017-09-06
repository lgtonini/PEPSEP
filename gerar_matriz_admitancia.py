import json 

filename = "models/componentes.json"

with open(filename) as data_file:    
    componentes = json.load(data_file)
 		
        for componente in componentes:
	G,B = None
	if componente['R'] != 0:
		G = 1/componente['R']
		pass
	if componente['X'] != 0:
		B = 1/componente['X']
		pass
	print(G,B)
	pass

input() 	 	
