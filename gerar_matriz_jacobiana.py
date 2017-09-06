import json 

componentes = []
linhas = []
matriz_admitancia = []

filename_componente = "models/componentes.json"
filename_linhas = "models/linhas.json"

with open(filename_componente) as data_file:    
    componentes = json.load(data_file)

with open(filename_linhas) as data_file:    
    linhas = json.load(data_file)

for x in range(0,len(componentes)):
	matriz_admitancia.append([0 for x  in range(0,len(componentes))])
	pass
i = 0
j=0	
for componente in componentes:	
	if componente['R']+componente['X'] != 0:
		G = componente['R']/(componente['R']*componente['R'] + componente['X']*componente['X'])
		B = -componente['X']/(componente['X']*componente['X'] + componente['R']*componente['R'])
		pass		
		matriz_admitancia[i][j] = str(G) + " j"+str(B)
	i+=1
	j = i	
	pass


i = 0 
j=1		

for linha in linhas:
	
	if linha['R']+linha['X'] != 0:
		G = linha['R']/(linha['R']*linha['R'] + linha['X']*linha['X'])
		B = -linha['X']/(linha['X']*linha['X'] + linha['R']*linha['R'])
		pass
	
	matriz_admitancia[i][j] = str(G) + " j"+str(B)
	if j==len(componentes)-1  and i == len(componentes)-1:
		print(i,j)
		break
	else:
		if(j<len(componentes)-1 ):
			j+=1
		else:
			j=0
			i+=1	
		pass
		
	pass

print(matriz_admitancia)



