from pygame import mixer

mixer.init()
caminho = ('Pyhton\\Exercicios_Curso_Em_Video\\'
           'ex021\\OpeningBombingMission.mp3')
mixer.music.load(caminho)
mixer.music.play()
parar = input('Aperte Enter para parar.')
