import pygame
import os
os.listdir("musicas")
lista = []
for i in os.listdir("musicas"):
    lista.append(i)
def playSong():
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    pygame.event.wait()
def pauseSong():
    pygame.mixer.music.pause()

def unpauseSong():
    pygame.mixer.music.unpause()
cont=0
while True:
    print("Selecione a opção: ")
    print("[1] - Play :")
    print("[2] - pausar:")
    print("[3] - despausar:")
    print("[4] - proxima musica:")
    print("[5] - musica anterior:")
    opção = int(input())
    musica = "musicas\\"+lista[cont]
    if opção == 1:
        playSong()
    if opção == 2:
        pauseSong()
    if opção == 3:
        unpauseSong()
    if opção == 4:
        cont+=1
        if(cont>=len(lista)-1):
            cont=len(lista)-1
        musica = "musicas\\" + lista[cont]
        playSong()
    if opção == 5:
       cont=cont-1
       musica = "musicas\\" + lista[cont]
       playSong()
       if(cont<0):
           cont=0


