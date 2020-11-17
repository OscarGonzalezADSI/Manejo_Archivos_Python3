import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'fondo.png'
destino = ruta + 'dir1/fondo.png'

if os.path.exists(origen):
    with open(origen, 'rb') as forigen:
        with open(destino, 'wb') as fdestino:
            shutil.copyfileobj(forigen, fdestino)
            print("Archivo copiado")
            pausa = input("")

# -------------------------------------------------------------------------------

# fuente:
# https://python-para-impacientes.blogspot.com/2015/10/copiar-mover-y-borrar.html

# -------------------------------------------------------------------------------