class Error(Exception):
    pass

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

class ClassLargoExtendido(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje