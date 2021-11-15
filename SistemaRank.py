#SISTEMA DE RANK
#HELLO WORLD!! :)
#Fiz baseado no q eu sei

#15/nov/21
import json
class rank:
	def brickApart():
		a = '''{"1":{"pontos":"0","nome":"A"},"2":{"pontos":"150","nome":"B"},"3":{"pontos":"2","nome":"C"}}''' #json
		b = json.loads(a) #carregar json
		dados = b
		rank = [] #array vazia
		for key, value in dados.items():
			rank.append((value["nome"], int(value['pontos']))) #converter em array
		rank = sorted(rank, key=lambda r: r[1], reverse=True) #organizar por ordem decresente
		i =0
		p = 1 # posical do rank
		while (i < 10):
			try:
				dd = rank[i]  #carregar dados 
				print(str(p)+" - "+str(dd[0])+":"+str(dd[1])) 
				p=p+1
				i=i+1
			except:
				break
rank.brickApart()