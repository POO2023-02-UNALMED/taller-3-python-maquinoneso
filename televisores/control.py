class Control:
    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv
    
    def setTv(self, NewTv):
        self.tv = NewTv

    def enlazar(self, televisor):
        self.tv = televisor
        televisor.control = self

    def turnOn(self):
        return self.tv.turnOn()
    
    def turnOff(self):
        return self.tv.turnOff()
    
    def setCanal(self, int):
        return self.tv.setCanal(int)
    
    def canalUp(self):
        return self.tv.canalUp()
    
    def canalDown(self):
        return self.tv.canalDown()
    
    def volumenUp(self):
        return self.tv.volumenUp()
    
    def volumenDown(self):
        return self.tv.volumenDown()
    
    def setVolumen(self,value):
        return self.tv.setVolumen(value)