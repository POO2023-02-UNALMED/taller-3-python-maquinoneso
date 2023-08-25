class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.estado=estado
        self.marca=marca
        self.canal=1
        self.volumen=1
        self.precio=500
        self.control = None
        TV.numTV+=1

    def setControl(self, control):
        self.control=control

    def getControl(self):
        return self.control

    def setMarca(self, Newmarca):
        self.marca = Newmarca
    
    def getMarca(self):
        return self.marca
    
    def getCanal(self):
        return self.canal
    
    def setCanal(self, Numcanal):
        self.canal=Numcanal

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, NewPrecio):
        self.precio=NewPrecio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self,Newvol):
        self.volumen=Newvol

    def getnumTV(self):
        return TV.numTV
    
    def setNumTV(value):
        TV.numTV = value

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True and self.canal < 120:
            self.canal += 1
        else:
            None

    def canalDown(self):
        if self.estado == True and self.canal > 1:
            self.canal -= 1
        else:
            None

    def volumenUp(self):
        if self.estado == False or self.volumen == 7:
            None
        else:
            self.volumen += 1

    def volumenDown(self):
        if self.estado == False or self.volumen == 1:
            None
        else:
            self.volumen -= 1