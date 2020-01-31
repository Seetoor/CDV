class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def wspolrzedne(self):
        return "x={}, y={}, z={}".format(self.x, self.y, self.z)
        
    def modul(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
    
    def zwieksz(self, x, y, z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        
    def zmniejsz(self, x, y, z):
        self.x = self.x - x
        self.y = self.y - y
        self.y = self.z - z
        
    def mnozenie(self,a):
        self.x = self.x * a
        self.y = self.y * a
        self.z = self.z * a
    
    def iloczyn_skalarny(self, x, y, z):
        return self.x * x + self.y * y + self.z * z
    
    def iloczyn_wektorowy(self, x, y, z):
        x = self.y * z - self.z * y
        y = self.z * x - self.x * z
        z = self.x * y - self.y * x
        
        return x, y, z
    
    def wektor_przeciwny(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z