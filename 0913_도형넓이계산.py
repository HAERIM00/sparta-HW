class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f"{self.width*self.height}"

    def square(self):
        return f"{self.width * self.height}"

    def triangle(self):
        return f"{self.width*self.height*0.5}"

    def circle(self):
        return f"{((self.width*0.5)**2)*3.14}"

area = Area(10,20)
print(area.square())
print(area.triangle())
print(area.circle())