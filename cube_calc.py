class Cube:
    def __init__(self, value):
        self.value = value
        
    def cube_calc(self):
        cube = self.value * self.value * self.value
        return f'Cube value is: {cube}'
    

cube = Cube(6).cube_calc()
print(cube)