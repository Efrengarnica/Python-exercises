#Duración de otros cursos y el mio
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5
#Duracion de crudos
crudo_promedio=5
crudo_dalto=3.5

#Diferencias de duración

diferencia_con_min=100-(dalto_curso/otros_cursos_min *100)
diferencia_con_max=100-((dalto_curso*1000//otros_cursos_max)/10)
diferencia_con_promedio=100-(dalto_curso/otros_cursos_promedio *100)
print(f'El curso dura un {diferencia_con_min} % menos que el más rápido')
print(f'El curso dura un {diferencia_con_max} % menos que el más lento')
print(f'El curso dura un {diferencia_con_promedio} % menos que el promedio')

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio= 100 - otros_cursos_promedio * 1000// crudo_promedio/10
print(f'El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
tiempo_vacio_dalto=100 - dalto_curso * 1000// crudo_dalto/10
print(f'El curso elimina un {tiempo_vacio_dalto}% de tiempo vacio')

#Mostrando diferencias sin los cursos duraran 10 hrs
print(f'Ver 10 hrs de este curso equivale a ver {otros_cursos_promedio*100//dalto_curso /10} hrs de otros cursos')



