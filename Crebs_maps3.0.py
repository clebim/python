
from tkinter import *
from datetime import datetime

cidades = ('uberlandia', 'capinopolis', 'ituiutaba', 'centralina', 'itumbiara', 'tupaciguara',
'monte alegre de minas', 'douradinhos', 'araguari', 'cascalho rico', 'indianopolis', 'grupiara',
'estrela do sul', 'romaria', 'sao juliana')

grafico = {'capinopolis': {'ituiutaba':30, 'centralina':40},
'ituiutaba': {'capinopolis':30, 'monte alegre de minas':85, 'douradinhos':90},
'centralina':{'itumbiara':20, 'monte alegre de minas':75, 'capinopolis':40},
'itumbiara': {'tupaciguara':55, 'centralina': 20},
'tupaciguara':{'itumbiara':55, 'monte alegre de minas':44, 'uberlandia':60},
'monte alegre de minas': {'centralina':75, 'tupaciguara':44, 'uberlandia':60, 'douradinhos':28, 'ituiutaba':90},
'douradinhos': {'monte alegre de minas':28, 'uberlandia':63, 'ituiutaba':90},
'uberlandia': {'tupaciguara':60, 'monte alegre de minas':60, 'douradinhos':63, 'araguari':30, 'romaria':78, 'indianopolis':45},
'araguari':{'uberlandia':30, 'cascalho rico':28, 'estrela do sul':34},
'cascalho rico':{'araguari':28, 'grupiara':32},
'indianopolis': {'uberlandia':45, 'sao juliana':40},
'grupiara': {'cascalho rico':32, 'estrela do sul':38},
'estrela do sul': {'grupiara':38, 'araguari':34, 'romaria':27},
'romaria': {'estrela do sul':27, 'uberlandia':78, 'sao juliana':28},
'sao juliana': {'indianopolis':40, 'romaria':28}}


def dijkstra(começo, objetivo):
    menor_distancia = {}
    antecessor = {}
    nonao_visitado = {'capinopolis': {'ituiutaba':30, 'centralina':40},
    'ituiutaba': {'capinopolis':30, 'monte alegre de minas':85, 'douradinhos':90},
    'centralina':{'itumbiara':20, 'monte alegre de minas':75, 'capinopolis':40},
    'itumbiara': {'tupaciguara':55, 'centralina': 20},
    'tupaciguara':{'itumbiara':55, 'monte alegre de minas':44, 'uberlandia':60},
    'monte alegre de minas': {'centralina':75, 'tupaciguara':44, 'uberlandia':60, 'douradinhos':28, 'ituiutaba':90},
    'douradinhos': {'monte alegre de minas':28, 'uberlandia':63, 'ituiutaba':90},
    'uberlandia': {'tupaciguara':60, 'monte alegre de minas':60, 'douradinhos':63, 'araguari':30, 'romaria':78, 'indianopolis':45},
    'araguari':{'uberlandia':30, 'cascalho rico':28, 'estrela do sul':34},
    'cascalho rico':{'araguari':28, 'grupiara':32},
    'indianopolis': {'uberlandia':45, 'sao juliana':40},
    'grupiara': {'cascalho rico':32, 'estrela do sul':38},
    'estrela do sul': {'grupiara':38, 'araguari':34, 'romaria':27},
    'romaria': {'estrela do sul':27, 'uberlandia':78, 'sao juliana':28},
    'sao juliana': {'indianopolis':40, 'romaria':28}}
    infinito = 9999999
    caminho = []
    for no in nonao_visitado:
        menor_distancia[no] = infinito
    menor_distancia[começo] = 0    

    while nonao_visitado:
        nomin = None
        for no in nonao_visitado:
            if nomin is None:
                nomin = no
            elif menor_distancia[no] < menor_distancia[nomin]:
                nomin = no

        for nofilho, peso in grafico[nomin].items():
            if peso + menor_distancia[nomin] < menor_distancia[nofilho]:
                menor_distancia[nofilho] = peso + menor_distancia[nomin]
                antecessor[nofilho] = nomin
        nonao_visitado.pop(nomin)
    no_atual = objetivo
    while no_atual != começo:
        try:
            caminho.insert(0,no_atual)
            no_atual = antecessor[no_atual]
        except KeyError:
            print('caminho nao alcançavel')
            break
    caminho.insert(0,começo)
    if menor_distancia[objetivo] != infinito:
        listaux = []
        listaux.append(menor_distancia[objetivo])
        listaux.append(caminho)
        return listaux

def argumento(cidades, origem, destino, grafico):
    origem = origem.lower()
    destino = destino.lower()
    if origem in cidades:
        if destino in cidades:
            # chama dijkstra
            distancia = dijkstra(origem, destino)
            lbldistancia["text"] = ('Distancia: ' + str(distancia[0]))
            #lblcaminho["text"] = ('Caminho: ' + str(distancia[1]))
            mapa_menor_caminho(distancia)
        else:
            lbldistancia["text"] = ('Argumento invalido,\ntente novamente.')   
    else:
        lbldistancia["text"] = ('Argumento invalido,\ntente novamente.')

def btclick():
    origem = entrada1.get()
    destino = entrada2.get()
    argumento(cidades, origem, destino, grafico)   

def mapa_menor_caminho(caminho):
    from PIL import Image, ImageDraw
    posiçoes = {'capinopolis': (35,141), 'ituiutaba' : (78,252), 'itumbiara': (162,30), 'centralina': (169,102),
    'tupaciguara': (346,102), 'monte alegre de minas': (285,214), 'douradinhos': (361,277), 'uberlandia': (504,225),
    'araguari': (535,121), 'indianopolis': (637,269), 'cascalho rico': (650,96), 'grupiara': (707,63),
    'estrela do sul': (718,159), 'romaria': (763,125), 'sao juliana': (741,330)}
    locais = caminho[1]
    lista = []
    for x, y in posiçoes.items():
        if x in locais:
            lista.append(y)    
    novo_mapa = Image.open('mapa.png')
    draw = ImageDraw.Draw(novo_mapa)
    draw.line(lista, fill='blue', width=2) 
    novo_mapa.save('novo_mapa.png')
    mapa["file"] = ("novo_mapa.png")
            

#Criando interface
janela = Tk()

janela.geometry("798x500+200+100")
janela.title("Crebs Maps")
janela["background"] = "white"


mapa = PhotoImage(file="mapa.png")
lblimagem = Label(janela, image=mapa, bg='white')
lblimagem.place(x=0, y=0)

#origem
lblorigem = Label(janela, font=('times new roman', 15), text='Origem: ', bg='white')
lblorigem.place(x=0 , y=400)
#destino
lbldestino = Label(janela, font=('times new roman', 15), text='Destino: ', bg='white')
lbldestino.place(x=0,y=420)

#entrada origem
entrada1 = Entry(janela, width=22, bg='white')
entrada1.place(x=80,y=400)
#entrada destino
entrada2 = Entry(janela, width=22, bg='white')
entrada2.place(x=80,y=420)


#botao para procurar
botao = Button(janela, text='Procurar', font=('times new roman',10), width=10, command=btclick)
botao.place(x=0,y=450)
botao.configure(background='white')
botao.configure(activebackground='white')

#distancia
lbldistancia = Label(janela, font=('times new roman', 15), text='', bg='white')
lbldistancia.place(x=250, y=400)
#lblcaminho = Label(janela, font=('times new roman', 15), text='', bg='white', width=500, height=80)
#lblcaminho.place(x=250, y=420)

janela.mainloop()



