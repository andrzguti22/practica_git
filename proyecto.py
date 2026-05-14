nombre_proyecto = 'MicroJobs'
descripcion = 'Plataforma tipo marketplace para intercambio de pequeños trabajos'
tecnologias = ['REACT', 'JAVASCRIPT', 'PYTHON', 'POSTGRES']
integrantes = ['Andrés Felipe Gutierrez']
funcionalidades = ['Login', 'Registro', 'Publicacion', 'Exploracion', 'Comunicacion']

def mostrar_info():
    print(f'Proyecto:  {nombre_proyecto}')
    print(f'Descripcion:   {descripcion}')
    print(f'Equipo:  {", ".join(integrantes)}')
    print(f'Tecnologias: {", ".join(tecnologias)}')
    print('Funcionalidades:')
    for f in funcionalidades:
        print(f'  -{f}')

mostrar_info()


