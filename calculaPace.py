# -- encoding: utf-8 - 
from datetime import date, time, datetime 
distancia = float(input('Digite a distância (em km): ')) 
tempo_data = str(input('Digite seu tempo (hh:mm:ss): ')) 
hora = int(tempo_data.split(':')[0]) 
minuto = int(tempo_data.split(':')[1]) 
segundo = int(tempo_data.split(':')[2]) 
tempo_em_minutos = float((hora * 60) + (minuto) + segundo / 60) 
pace_str = str(tempo_em_minutos / distancia) 
pace_int = tempo_em_minutos / distancia 
min_inteiro = int(pace_str.split('.')[0]) 
min_fracao = float(pace_int - min_inteiro) 
min_fracao = float(min_fracao * 0.6) 
pace = round((min_inteiro + min_fracao),2) 
print('Distância: {} km'.format(distancia), ' | Tempo: {}'.format(tempo_data), ' | Pace Médio: {} min/km'.format(pace).replace('.',':'))