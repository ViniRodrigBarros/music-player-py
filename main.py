import pygame
def playSong():
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    pygame.event.wait()
    input()
def pauseSong():
    pygame.mixer.music.pause()

def unpauseSong():
    pygame.mixer.music.unpause()

while True:
    print("Selecione a opção: ")
    print("[0] - selecionar musica:")
    print("[1] - Play :")
    print("[2] - pausar:")
    print("[3] - despausar:")
    opção = int(input())
    if opção == 1:
        playSong()
    if opção == 2:
        pauseSong()
    if opção == 3:
        unpauseSong()
    if opção == 0:
        print("selecione a musica:")
        musica = input()
        musica = musica + ".mp3"

