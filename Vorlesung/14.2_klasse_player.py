class Player:
    def __init__(self, name, points = 0):
        self.__name = name
        self.__points = points
        print('Player: Konstruktor wurde aufgerufen.')
    
    def print_info(self):
        print(f'Der name des Spielers ist {self.__name} und hat derzeit {self.__points} Punkte.')

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points
    
    def add_points(self, points):
        self.__points += points
        return self.__points

    def __del__(self):
        print('Player: Destruktor wurde aufgerufen.')



# Objekterzeugung
player = Player("Max") 

# Zugriff auf öffentliche Methoden
player.print_info()

# Zugriff auf private Methoden (mit Klammern)
print(f'Name: {player.get_name()} | Punkte: {player.get_points()}')

# Punkteaktualisierung
scored_points = player.add_points(50)
print(f'Der Spieler {player.get_name()} hat jetzt {scored_points} Punkte erreicht.')
