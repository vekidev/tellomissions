import pygame, sys

class TestTello:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.virtdrone = pygame.Vector2()  # [0,0]
        self.target = pygame.Vector2()
        self.angle = 0

    def connect(self):
        pass

    def takeoff(self):
        pass

    def land(self):
        pygame.quit()
        sys.exit()

    def move_forward(self, distance):
        self.virtdrone.x += math.sin(self.angle) * distance
        self.virtdrone.y += math.cos(self.angle) * distance

    def move_backward(self, distance):
        self.virtdrone.x += math.sin(self.angle) * distance
        self.virtdrone.y += math.cos(self.angle) * distance

    def rotate_clockwise(self, angle):
        self.angle += math.radians(angle)

    def rotate_counter_clockwise(self, angle):
        self.angle -= math.radians(angle)

# Inicijalizacija pygame modula
pygame.init()

# Postavljanje veličine ekrana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Putanja Drona")

# Boje
WHITE = (255, 255, 255)


# Funkcija za crtanje prave linije
def draw_line(start, end):
    pygame.draw.line(screen, WHITE, start, end, 2)
    pygame.display.flip()  # Ažuriranje ekrana nakon crtanja linije


# Funkcija za crtanje putanje na osnovu datih koordinata
def draw_path(path_coordinates):
    # Pronalaženje maksimalnih i minimalnih vrednosti za x i y koordinate
    min_x = min(coord[0] for coord in path_coordinates)
    max_x = max(coord[0] for coord in path_coordinates)
    min_y = min(coord[1] for coord in path_coordinates)
    max_y = max(coord[1] for coord in path_coordinates)

    # Računanje centra ekrana
    center_x = width // 2
    center_y = height // 2

    # Računanje offseta za x i y koordinate
    offset_x = center_x - (max_x - min_x) // 2 - min_x
    offset_y = center_y - (max_y - min_y) // 2 - min_y

    # Prilagođavanje koordinata putanje na centar ekrana
    centered_coordinates = [(coord[0] + offset_x, coord[1] + offset_y) for coord in path_coordinates]

    # Crta putanju linijama
    for i in range(len(centered_coordinates) - 1):
        draw_line(centered_coordinates[i], centered_coordinates[i + 1])


# Koordinate putanje
path_coordinates = [(0, 0),  # Početna tačka
                    (0, 50),  # Prva tačka nakon prvog pomeranja napred
                    (-35.36, 85.36),  # Druga tačka nakon rotacije levo 45 stepeni
                    (0, 121.36),  # Treća tačka nakon drugog pomeranja napred
                    (35.36, 85.36),  # Četvrta tačka nakon ponovne rotacije desno 45 stepeni
                    (85.36, 121.36),  # Peta tačka nakon trećeg pomeranja napred
                    (85.36, 171.36),  # Šesta tačka nakon rotacije levo 90 stepeni
                    (135.36, 171.36),  # Sedma tačka nakon četvrtog pomeranja napred
                    (135.36, 221.36),  # Osma tačka nakon ponovne rotacije levo 90 stepeni
                    (185.36, 221.36),  # Deveta tačka nakon petog pomeranja napred
                    (185.36, 171.36),  # Deseta tačka nakon ponovne rotacije desno 90 stepeni
                    (135.36, 171.36),  # Jedanaesta tačka nakon šestog pomeranja napred
                    (135.36, 71.36),  # Dvanaesta tačka nakon rotacije levo 90 stepeni
                    (135.36, -28.64),  # Trinaesta tačka nakon sedmog pomeranja napred
                    (85.36, -28.64),  # Četrnaesta tačka nakon ponovne rotacije levo 90 stepeni
                    (85.36, 21.36),  # Petnaesta tačka nakon osmog pomeranja napred
                    (135.36, 21.36),  # Šesnaesta tačka nakon ponovne rotacije desno 90 stepeni
                    (135.36, 71.36),  # Sedamnaesta tačka nakon devetog pomeranja napred
                    (170.36, 71.36),  # Osamnaesta tačka nakon ponovne rotacije desno 45 stepeni
                    (135, 36),  # Devetnaesta tačka nakon desetog pomeranja napred
                    (170.36, 71.36)]  # Krajnja tačka

# Crta putanju
draw_path(path_coordinates)

# Prikazuje prozor i čeka zatvaranje
pygame.display.update()  # Prikazuje prozor nakon crtanja putanje
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
