import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pygame
import sys
from pygame.locals import *
from random import randint


def graficos(array):
    #grafico de pie
    df = pd.DataFrame({'Origin': array})
    plt.title('Grafico Pie Dardos al blanco',fontsize=15)
    plot = df['Origin'].value_counts().plot(kind='pie', autopct='%.2f',figsize=(6, 6))

    #grafico barras
    cant=len(array)
    df = pd.DataFrame({'Origin':array})
    plt.figure(figsize=(8,4))
    chart = sns.countplot(data = df,x='Origin', order = df['Origin'].value_counts().index)
    for p in chart.patches:
        height = p.get_height()
        chart.text(p.get_x()+p.get_width()/1.,
                height + 0.5,
                '{:1.0f}'.format(height),
                ha="right",rotation=0)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.title("Mirko's Dart Game -- Darts Thrown "+str(cant))
    plt.xlabel('Funcion de Perros')
    plt.ylabel('Cantidad de Perros')
    plt.show()

pygame.init()

#defino texto tablero dardos y ventana pygame
miFuente = pygame.font.Font(None,30)
miTexto= miFuente.render("100",0,(0,0,0))
miTexto1= miFuente.render("90",0,(0,0,0)) 
miTexto2= miFuente.render("80",0,(0,0,0)) 
miTexto3= miFuente.render("70",0,(0,0,0))
miTexto4= miFuente.render("60",0,(0,0,0))
miTexto5= miFuente.render("50",0,(0,0,0)) 
miTexto6= miFuente.render("40",0,(0,0,0)) 
miTexto7= miFuente.render("30",0,(0,0,0))
miTexto8= miFuente.render("20",0,(0,0,0)) 
miTexto9= miFuente.render("10",0,(0,0,0))  

ventana = pygame.display.set_mode((640,640))

pygame.display.set_caption("Mirko's Darts")

ventana.fill((185, 234, 243 ))

#dibujo circulos (radios)
pygame.draw.circle(ventana,(255,0,0),(320,320),320)
pygame.draw.circle(ventana,(255,255,255),(320,320),288) 
pygame.draw.circle(ventana,(255,0,0),(320,320),256)     
pygame.draw.circle(ventana,(255,255,255),(320,320),224)  
pygame.draw.circle(ventana,(255,0,0),(320,320),192)       
pygame.draw.circle(ventana,(255,255,255),(320,320),160)
pygame.draw.circle(ventana,(255,0,0),(320,320),128)    
pygame.draw.circle(ventana,(255,255,255),(320,320),96) 
pygame.draw.circle(ventana,(255,0,0),(320,320),64)     
pygame.draw.circle(ventana,(255,255,255),(320,320),32)  
ventana.blit(miTexto,(303,310))
ventana.blit(miTexto1,(310,265))
ventana.blit(miTexto2,(310,233))
ventana.blit(miTexto3,(310,200))
ventana.blit(miTexto4,(310,168))
ventana.blit(miTexto5,(310,136))
ventana.blit(miTexto6,(310,104))
ventana.blit(miTexto7,(310,73))
ventana.blit(miTexto8,(310,40))
ventana.blit(miTexto9,(310,7))

#defino array donde guardo resultados
totalDards= []

#apendeo las cordenadas y poner tope definido y graficar
arrayX = []
arrayY = []

cont=0

while True:
    #genero puntos aleatorios
    x=randint(0,640)
    y=randint(0,640)
    
    #si es menor al tope meto al array los resultados
    if (cont<1000):
        arrayX.append(x)
        arrayY.append(y)

        d = math.sqrt((x-320)**2+(y-320)**2)

        if(d<32):
            totalDards.append(100)
        if(d>32 and d<64):
            totalDards.append(90)
        if (d>64 and d<96):
            totalDards.append(80)
        if (d>96 and d<128):
            totalDards.append(70)
        if(d>128 and d<160):
            totalDards.append(60)
        if (d>160 and d<192):
            totalDards.append(50)
        if (d>192 and d<224):
            totalDards.append(40)
        if (d>224 and d<256):
            totalDards.append(30)
        if (d>256 and d<288):
            totalDards.append(20)
        if (d>288 and d<320):
            totalDards.append(10)
        if(d>320):   
            totalDards.append(0) 
    elif (cont>=1000):  #arecorro el array muestro los puntos definidos
        for i in range(len(arrayX)):
            pygame.draw.circle(ventana,(0,0,0),(arrayX[i],arrayY[i]),4)

    #eventos de la maquina 
    for evento in pygame.event.get():
        if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE) :
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN and evento.key == K_SPACE:
            graficos(totalDards)
    
    pygame.display.update()
    cont+=1
