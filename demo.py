from campana import Campaña
from error import SubTipoInvalidoError

arch = open('error.log', 'a')
c = Campaña('ricomida', '2024-03-15', '2024-03-24')
try:
    c.crear_video('instream', 'https://...', 'https://...', 3)
except SubTipoInvalidoError as e:
    print(f'Error al agregar un video {e}')
    arch.write(f'Error al agregar un video {e}')
#imprimir detalle de la campaña
print(c)

arch.close()