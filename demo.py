from campana import Campaña
from error import SubTipoInvalidoError

c = Campaña('ricomida', '2024-03-15', '2024-03-24')
try:
    c.crear_video( 'https://...', 'https://...','instream', 3)
except SubTipoInvalidoError as e:
    arch = open('error.log', 'a')
    print(f'Error al agregar un video {e}')
    arch.write(f'Error al agregar un video {e}\n')
    arch.close()
try:
    c.crear_display(20,20 ,'https://www.archivo.com' ,' https://www.archivo.com','native')
except SubTipoInvalidoError as e:
    arch = open('error.log', 'a')
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}\n')
    arch.close()
try:
    c.crear_social(10,20,'https://www.discordia.gg' ,' https://www.discordia.gg', 'facebook')
except SubTipoInvalidoError as e:
    arch = open('error.log', 'a')
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}\n')
    arch.close()
#imprimir detalle de la campaña
print(c)

