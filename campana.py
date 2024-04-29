from anuncio import Video, Display, Social
from error import ClassLargoExtendido

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino):
        if len(nombre) > 250:
            raise ClassLargoExtendido(f'Nombre invalido, sobrepasa 250 caracteres')
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value):
        self.__fecha_termino = value

    def __str__(self):
        print(f'Nombre de la Campaña: {self.__nombre}')
        num_videos = 0
        num_display = 0
        num_social = 0
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                num_videos += 1
            if isinstance(anuncio, Display):
                num_display += 1
            if isinstance(anuncio, Social):
                num_social += 1
        return f'Anuncios: {num_videos} Video, {num_display} Display, {num_social} Social'
    
    def crear_video(self, sub_tipo, url_archivo, url_clic, duracion):
        v = Video(sub_tipo, url_archivo, url_clic, duracion)
        self.__anuncios.append(v)
    
    def crear_display(self, ancho, alto, url_archivo, url_click , sub_tipo):
        d = Display(ancho, alto, url_archivo, url_click, sub_tipo)
        self.__anuncios.append(d)
    
    def crear_social(self, ancho, alto, url_archivo, url_click ,sub_tipo):
        s = Social(ancho, alto, url_archivo, url_click, sub_tipo)
        self.__anuncios.append(s)
    