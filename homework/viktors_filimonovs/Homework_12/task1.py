# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. 
# В букете цветы пусть хранятся в списке. Это будет список объектов.

# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

class Flowers():
    def __init__(self, name, color, price, freshnes, dlinna_steblja, lifetime):
        self.name = name
        self.color = color
        self.price = price
        self.freshnes = freshnes
        self.dlinna_steblja = dlinna_steblja
        self.lifetime = lifetime

    def __str__(self):
        return (f"{self.name}({self.color}), Price: {self.price}, "
                f"Freshness: {self.freshnes}, Length: {self.dlinna_steblja}, "
                f"Life Time: {self.lifetime} days")


class Sunflower(Flowers):
    def __init__(self, color, price, freshnes, dlinna_steblja):
        super().__init__("Sunflower", color, price, freshnes,
                         dlinna_steblja, 8)


class Rododendron(Flowers):
    def __init__(self, color, price, freshnes, dlinna_steblja,):
        super().__init__("Rododendron", color, price, freshnes,
                         dlinna_steblja, 12)


class Rose(Flowers):
    def __init__(self, color, price, freshnes, dlinna_steblja,):
        super().__init__("Rose", color, price, freshnes,
                         dlinna_steblja, 13)


class Lilly(Flowers):
    def __init__(self, color, price, freshnes, dlinna_steblja,):
        super().__init__("Lilly", color, price, freshnes,
                         dlinna_steblja, 4)


class Buket():
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if len(self.flowers) == 0:
            return "Bouquet is empty"
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by(self, attribute):
        self.flowers.sort(
            key=lambda flower: getattr(flower, attribute),
            reverse=True
        )

    def search_by_lifespan(self, min_lifespan):
        return [flower for flower in self.flowers
                if flower.lifetime >= min_lifespan]

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)


sunflower1 = Sunflower("Yellow", 16, 10, 65)
rodedendron1 = Rododendron("Purpure", 12, 5, 38)
rodedendron2 = Rododendron("Wiolet", 10, 6, 38)
roze1 = Rose("White", 36, 9, 125)
roze2 = Rose("Red", 36, 4, 125)
lilly1 = Lilly("White", 46, 8, 135)
lilly2 = Lilly("Red", 40, 9, 135)
lilly3 = Lilly("Black", 25, 5, 45)


bouquet = Buket()
bouquet.add_flowers(lilly1)
bouquet.add_flowers(lilly2)
bouquet.add_flowers(lilly1)
bouquet.add_flowers(roze1)
bouquet.add_flowers(rodedendron2)
bouquet.add_flowers(sunflower1)

print("bouquet Contains: ")
print(bouquet)
print(f"\n Price: {bouquet.total_price()}p")
print(f"\n Average life time: {bouquet.average_lifespan()} days")
bouquet.sort_by("freshnes")
print("\n bouquet after short by freshnes :")
print(bouquet)
print("\n The oldest flowers: ")
for flower in bouquet.search_by_lifespan(7):
    print(flower)
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.()
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
