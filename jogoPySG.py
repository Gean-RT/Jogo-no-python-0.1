from PySimpleGUI import PySimpleGUI as sg
from time import sleep
from random import randint

cor = 'SystemDefault'
sg.theme(cor)
tela_jogo = [
[sg.Output(size=(15,5),key='tela')],
[sg.Button('esquerda',size=(6,1))]  + [sg.Button('direita',size=(5,1))],
[sg.Button('baixo',size=(6,1))] + [sg.Button('cima',size=(5,1))],
#[sg.Output(size=(15,5),key='config')]
]

layoutInicial = [
[sg.Button('Iniciar',size=(8,2))],
[sg.CloseButton('Sair',size=(8,2))],
]

#janelas 
inicio = sg.Window('Inicio',layoutInicial)
janela = sg.Window('jogo',tela_jogo)

#Janela em 'format' de function
def tela_jogo():
	posD1 = ' '
	posD2 = ''
	posX = 1
	while True:
		eventos, valores = janela.read()
		if eventos == sg.WINDOW_CLOSED:
			break
		
		#obejetivo
		if len(posD2) == 0:
			NPM = randint(1,136)
			mal = (' '*(NPM)+'-')
			
		if len(mal) == len(posD2):
				NPM = randint(10,110)
				mal = (' '*(NPM)+'-')
		#janela['config'].update(f'Mal: POS.{len(mal)}\nBom: POS.{len(posD2)}')
					
		#colunas
			#1
		if posX == 1:
			if len(posD1[1:]) < 31:
				if eventos == 'direita':
					posD1 += ' '
					posD2 = posD1 + '>'
					janela['tela'].update(posD2[:]+mal[len(posD2):])
			if len(posD1) > 1:
				if eventos == 'esquerda':
						posD1 = posD1[1:]
						posD2 = posD1 + '<'
						janela['tela'].update(posD2[:]+mal[len(posD2):])
			#2
		if posX == 2:
			if 31 < len(posD1[1:]) < 65:
				if eventos == 'direita':
					posD1 += ' '
					posD2 = posD1 + '>'
					janela['tela'].update(posD2[:]+mal[len(posD2):])
			if len(posD1) > 35:
				if eventos == 'esquerda':
						posD1 = posD1[1:]
						posD2 = posD1 + '<'
						janela['tela'].update(posD2[:]+mal[len(posD2):])
			#3
		if posX == 3:
			if 65 < len(posD1[1:]) < 99:
				if eventos == 'direita':
					posD1 += ' '
					posD2 = posD1 + '>'
					janela['tela'].update(posD2[:]+mal[len(posD2):])
			if len(posD1) > 69:
				if eventos == 'esquerda':
						posD1 = posD1[1:]
						posD2 = posD1 + '<'
						janela['tela'].update(posD2[:]+mal[len(posD2):])
			#4
		if posX == 4:
			if 99 < len(posD1[1:]) < 133:
				if eventos == 'direita':
					posD1 += ' '
					posD2 = posD1 + '>'
					janela['tela'].update(posD2[:]+mal[len(posD2):])
			if len(posD1) > 103:
				if eventos == 'esquerda':
						posD1 = posD1[1:]
						posD2 = posD1 + '<'
						janela['tela'].update(posD2[:]+mal[len(posD2):])
			#5
		if posX == 5:
			if 133 < len(posD1[1:]) < 167:
				if eventos == 'direita':
					posD1 += ' '
					posD2 = posD1 + '>'
					janela['tela'].update(posD2[:]+mal[len(posD2):])
			if len(posD1) > 137:
				if eventos == 'esquerda':
						posD1 = posD1[1:]
						posD2 = posD1 + '<'
						janela['tela'].update(posD2[:]+mal[len(posD2):])
						
			#posiçãoXY
		if posX < 5:
			if eventos == 'baixo':
				posD1 = posD1 + (' '*34)
				posD2 = posD1 + 'ˌ'
				janela['tela'].update(posD2[:]+mal[len(posD2):])
				posX += 1
		if posX > 1:
			if eventos == 'cima':
				posD1 = posD1[34:]
				posD2 = posD1 + 'ˡ'
				janela['tela'].update(posD2[:]+mal[len(posD2):])
				posX -= 1
		
		
			
	janela.close()


#programa que vai iniciar tudo

while True:
	events,values = inicio.read()
	if events == sg.WINDOW_CLOSED:
		break
	if events == "Iniciar":
		#jogo
		tela_jogo()
		#...
inicio.close()
