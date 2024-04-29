from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    #sub_tipos = ()
    
    @staticmethod
    def mostrar_formatos():
        #pass
        print('formato video')
        for v in Video.SUB_TIPOS:
            print(f'-{v}')
            
        print('formato display')
        for d in Display.SUB_TIPOS:
            print(f'-{d}')
        
        print('formato social')
        for s in Social.SUB_TIPOS:
            print(f'-{s}')
    
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
    def __init__(self, alto, ancho, url_archivo, url_clic, sub_tipo):
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

        # if sub_tipo not in Anuncio.sub_tipos:
        #     print('Ese Subtipo no existe')
    
    #para el ancho
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
    
    #para el alto
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1
    
    #para el archivo url
    @property
    def url_archivo(self):
        return self.__url_archivo
        
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
    
    #para el url clic
    @property
    def url_clic(self):
        return self.__url_clic
        
    @url_clic.setter
    def url_archivo(self, url_clic):
        self.__url_clic = url_clic
    
    #para el subtipo
    @property
    def sub_tipo(self):
        return self.__sub_tipo
        
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        #pass
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS 
            or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS 
            or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError('El subtipo indicado no está permitido para este formato.')
        else:
            self.__sub_tipo = sub_tipo

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ["instream", "outstream"]
    
    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1,1,url_archivo, url_clic, sub_tipo)
        if sub_tipo not in Video.SUB_TIPOS:
            raise SubTipoInvalidoError(f'El sub tipo indicado {sub_tipo} no está permitido para este formato')
        self.__duracion = duracion if duracion > 0 else 5
    
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5
    
    def comprimir_anuncio(self):
        print('Compresion de video no implementada aún.')
    
    def redimensionar_anuncio(self):
        print('Recorte de video no implementado aún.')
    
    def mostrar_formatos():
        sub1, sub2 = Video.SUB_TIPOS
        return f'Los valores son {sub1} y {sub2}'

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    def __init__(self,ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        print ('Compresión de anuncios display no implementada aún')
        
    def redimensionar_anuncio(self):
        print ('Redimensionamiento de  no implementado aún')
    
    def mostrar_formatos():
        sub1, sub2 = Display.SUB_TIPOS
        return f'Los valores son {sub1} y {sub2}'

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self,ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        print ('Compresión de vídeo no implementada aún')
        
    def redimensionar_anuncio(self):
        print ('Recorte de vídeo no implementado aún')
    
    def mostrar_formatos():
        sub1, sub2 = Social.SUB_TIPOS
        return f'Los valores son {sub1} y {sub2}'