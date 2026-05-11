class plant:
    class counter_system:
        def __init__(self):
            self.__show_c = 0
            self.__grow_c = 0
            self.__age_dc = 0
        def get_grow_c(self) -> int:
            return (__grow_c)
        def get_age_c(self) -> int:
            return(__age_dc)
        def get_show_c(self):
            return(self.__show_c)
        
        def setshow_c(self) -> None:
            self.__show_c += 1
        
        def setgrow_c(self) -> None:
            self.__grow_c += 1
        def setage_dc(sef) -> None:
            self.__age_dc += 1

    def __init__(
        self, name: str, height: float, age_d: int, g_rate: float = 0.8
    ) -> None:
        self.__name = name
        self.__height = height
        self.__age_d = age_d
        self.__g_rate = g_rate
        self.counter_system1 = self.counter_system()

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age_d} days old")
        self.counter_system1.setshow_c()

    def grow(self, nod: int) -> None:
        self.__height += self.__g_rate * nod
        self.counter_system1.setgrow_c()

    def age(self, nod: int) -> None:
        self.__age_d += nod
        self.counter_system1.setage_dc()


    def set_height(self, height: float) -> None:
        if (height > 0):
            self.__hpythoneight = height
            print(f"Height updated: {self.__height}cm")
        else:
            print(f"{self.__name}: Error, height can’t be negative")
            print("Height update rejected")

    def get_heghit(self) -> float:
        return (self.__height)

    def set_age(self, age_d: int) -> None:
        if (age_d > 0):
            self.__age_d = age_d
            print(f"Age updated: {self.__age_d} days")
        else:
            print(f"{self.__name}: Error, age can’t be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return (self.__age_d)

    @staticmethod
    def more_than_year(age_d: int) -> bool:
        if (age > 365):
            return True
        return False

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)
    
        


class flower(plant):
    def __init__(
        self, name: str, height: float, age_d: int, g_rate: float = 0.8, color: str
    ):
        super().__init__(name, height, age_d)
        self.color = color
        self.bloomed = 0

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self.bloomed):
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")
    
    def grow(self, nod: int) -> None:
        super().grow()

    def age(self, nod: int) -> None:
        super().age()


class seeds(flower):
    def __init__(
        self, name: str, height: float, age_d: int,
        g_rate: float = 0.8, color: str, num_seed: int
    ):
        super().__init__()
        self.num_seed = num_seed

    def grow(self, nod: int) -> None:
        super().grow()

    def age(self, nod: int) -> None:
        super().age()
    
    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.num_seed}")


class tree(plant):
        class counter_system:
        def __init__(self):
            self.__show_c = 0
            self.__grow_c = 0
            self.__age_dc = 0
            self.__shade_c = 0
        def get_grow_c(self) -> int:
            return (self.__grow_c)
        def get_age_c(self) -> int:
            return(self.__age_dc)
        def get_show_c(self):
        
        def setshow_c(self) -> None:
            self.__show_c += 1
        
        def setgrow_c(self) -> None:
            self.__grow_c += 1
        def setage_dc(sef) -> None:
            self.__age_dc += 1
        def setshade_c(self) ->None:
            self.__shade_c += 1
        def get_shade_c() -> int:
            return ()
    def __init__(
        self, name: str, height: float, age_d: int,
        g_rate: float = 0.8, trunk_diameter: float
    ):
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of 200.0cm long and" 
             f"{self.trunk_diameter}cm wide.")


class vegtable(plant):
    def __init__(
        self, name: str, height: float, g_rate: float = 0.8,
        age_d: int, harvest_season: str, nutritional_value: int
    ):
        super().__init__(name, height, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_and_age(self, nod: int) ->None:
        super().grow(nod)
        super().age(nod)
        self.nutritional_value += nod
    
    def show(self) ->None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")



def main() -> None:
    f1 = flower("Rose", 15, 10, "red")
    t1 = tree("Oak", 200, 365, 5)
    v1 = vegtable("Tomato", 5, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f1.show()
    f1.bloom()
    f1.show()
    print()
    print("=== Tree")
    t1.show()
    t1.produce_shade()
    print()
    print("=== Vegetable")
    v1.show()
    v1.grow_and_age(20)
    v1.show()


if __name__ == "__main__":
    main()
