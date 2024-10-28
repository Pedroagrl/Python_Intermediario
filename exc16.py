def donwload():
    tamanho = float(input('Tamanho do arquivo(MB): '))
    velocidade = float(input('Velocidade da internet(Mbps):'))
    MBps = velocidade / 8
    tempo = tamanho / MBps
    tempo_min = tempo/60
    print(f'O tempo aproximado de donwload é {tempo_min:.2f} minutos')
donwload()