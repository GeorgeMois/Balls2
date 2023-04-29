import pygame as pg
import random

W, H, FPS = 500, 500, 120  # Отвечает за высоту, ширину и разрешение экрана
SIZE = (W, H)  # Создаёт экран по заданным размерам
clock = pg.time.Clock()

pg.init()
win = pg.display.set_mode(SIZE)


class Circle:
    def __init__(self, x, y, rad):  # Создаёт шары по заданым ниже парамметрам
        self.x = x
        self.y = y
        self.rad = rad
        self.dx = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])  # Рандомное число спаумна по координатной примой x
        self.dy = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])  # Рандомное число спаумна по координатной примой y
        self.color = random.choices(range(0, 256), k=3)  # Создаёт рандомный цвет для шаров

    def move(self):  # Задаёт скорость для объектов
        self.x += self.dx
        self.y += self.dy
        if self.x > W or self.x < 0:
            self.dx = -self.dx + random.randint(-1, 1)
        if self.y > H or self.y < 0:
            self.dy = -self.dy + random.randint(-1, 1)

    def show(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def update(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.x  -= 5
        if keystate[pg.K_RIGHT]:
            self.x  += 5


circles = []
for i in range(2000):  # Создаёт заданное кол-во шаров
    circles.append((Circle(W // 2, H // 2, 50)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Задаёт событие
            pg.quit()
            exit()

    for circle in circles:  # Задаёт отскок от объекта
        circle.move()

    win.fill((255, 255, 255))

    for circle in circles:
        circle.show()

    for circle in circles:
        circle.update()

    pg.display.update()
    clock.tick(FPS)
