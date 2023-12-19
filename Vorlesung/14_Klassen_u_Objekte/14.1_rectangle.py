class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.__top_left = top_left
        self.__bottom_right = bottom_right
    
    def compute_area(self):
        width = abs(self.__bottom_right[0] - self.__top_left[0])
        height = abs(self.__bottom_right[1] - self.__top_left[1])
        return width * height

    def print_area(self):
        print(f"Das Rechteck hat eine Fläche von {self.compute_area()} Quadratpixeln.")

#Erweiterung______________________________________________________________________________________________________________________________________________________
    def print_coordinates(self):
        print(f'Koordinaten für Links oben: {self.__top_left} | Koordinaten für Rechts unten: {self.__bottom_right}')

    def move_obj(self, delta_x, delta_y):
        self.__top_left[0] += delta_x
        self.__top_left[1] += delta_y
        self.__bottom_right[0] += delta_x
        self.__bottom_right[1] += delta_y
#_________________________________________________________________________________________________________________________________________________________________



#Objekt erzeugung
rectangle = Rectangle([100, 200], [200, 300])

#Ausgabe Test
rectangle.print_coordinates()
rectangle.move_obj(40, 40)
rectangle.print_coordinates()
rectangle.print_area()