class plant:
    class counter_system:
        def __init__(self) -> None:
            self.__show_c = 0
            self.__grow_c = 0
            self.__age_dc = 0

        def get_grow_c(self) -> int:
            return self.__grow_c

        def get_age_c(self) -> int:
            return self.__age_dc

        def get_show_c(self) -> int:
            return self.__show_c

        def setshow_c(self) -> None:
            self.__show_c += 1

        def setgrow_c(self) -> None:
            self.__grow_c += 1

        def setage_dc(self) -> None:
            self.__age_dc += 1

    def __init__(
        self, name: str, height: float, age_d: int, g_rate: float = 0.8
    ) -> None:
        self.__name = name
        self.__height = height
        self.__age_d = age_d
        self.__g_rate = g_rate
        self.cs1 = self.counter_system()

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age_d} days old")
        self.cs1.setshow_c()

    def grow(self, nod: int) -> None:
        self.__height += self.__g_rate * nod
        self.cs1.setgrow_c()

    def age(self, nod: int) -> None:
        self.__age_d += nod
        self.cs1.setage_dc()

    def set_height(self, height: float) -> None:
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm")
        else:
            print(f"{self.__name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self.__height

    def set_age(self, age_d: int) -> None:
        if age_d > 0:
            self.__age_d = age_d
            print(f"Age updated: {self.__age_d} days")
        else:
            print(f"{self.__name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self.__age_d

    @staticmethod
    def more_than_year(age_d: int) -> bool:
        if age_d > 365:
            return True
        return False

    @classmethod
    def anonymous(cls) -> 'plant':
        return cls("Unknown plant", 0.0, 0)


class flower(plant):
    def __init__(
        self, name: str, height: float, age_d: int,
        color: str, g_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age_d, g_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color:  {self.color}")
        if self.bloomed:
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")

    def grow(self, nod: int) -> None:
        super().grow(nod)

    def age(self, nod: int) -> None:
        super().age(nod)


class seeds(flower):
    def __init__(
        self, name: str, height: float, age_d: int, color: str,
        num_seed: int, g_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age_d, color, g_rate)
        self.num_seed = num_seed

    def grow(self, nod: int) -> None:
        super().grow(nod)

    def bloom(self) -> None:
        super().bloom()
        self.num_seed += 42

    def age(self, nod: int) -> None:
        super().age(nod)

    def show(self) -> None:
        super().show()
        print(f"Seeds:  {self.num_seed}")


class tree(plant):
    class counter_system(plant.counter_system):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_c = 0

        def setshade_c(self) -> None:
            self.__shade_c += 1

        def get_shade_c(self) -> int:
            return self.__shade_c

    def __init__(
        self, name: str, height: float, age_d: int, trunk_diameter: float,
        g_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age_d, g_rate)
        self.trunk_diameter = trunk_diameter

        self.cs_tree = self.counter_system()
        self.cs1 = self.cs_tree

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter:  {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree Oak now produces a shade of {self.get_height():.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
        )
        self.cs_tree.setshade_c()


class vegtable(plant):
    def __init__(
        self, name: str, height: float, age_d: int, harvest_season: str,
        nutritional_value: int, g_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age_d, g_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_and_age(self, nod: int) -> None:
        super().grow(nod)
        super().age(nod)
        self.nutritional_value += nod

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def statistics_p(ob: plant) -> None:
    print(
        f"Stats:  {ob.cs1.get_grow_c()} grow, {ob.cs1.get_age_c()} "
        f"age, {ob.cs1.get_show_c()} show"
    )


def statistics_t(ob: tree) -> None:
    print(
        f"Stats:  {ob.cs_tree.get_grow_c()} grow, {ob.cs_tree.get_age_c()} "
        f"age, {ob.cs_tree.get_show_c()} show"
    )
    print(f"{ob.cs_tree.get_shade_c()} shade")


def main() -> None:
    f1 = flower("Rose", 15.0, 10, "red", 8.0)
    t1 = tree("Oak", 200.0, 365, 5.0)
    v1 = seeds("Sunflower", 80.0, 45, "yellow", 0, 30.0)
    p1 = plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year?  -> {plant.more_than_year(30)}")
    print(f"Is 400 days more than a year?  -> {plant.more_than_year(400)}")
    print()

    print("=== Flower")
    f1.show()
    print("[statistics for Rose]")
    statistics_p(f1)
    print("[asking the rose to grow and bloom]")
    f1.grow(1)
    f1.bloom()
    f1.show()
    print("[statistics for Rose]")
    statistics_p(f1)
    print()

    print("=== Tree")
    t1.show()
    print("[statistics for Oak]")
    statistics_t(t1)
    print("[asking the oak to produce shade]")
    t1.produce_shade()
    print("[statistics for Oak]")
    statistics_t(t1)
    print()

    print("=== Seed")
    v1.show()
    print("[make sunflower grow, age and bloom]")
    v1.grow(1)
    v1.age(20)
    v1.bloom()
    v1.show()
    print("[statistics for Sunflower]")
    statistics_p(v1)
    print()

    print("=== Anonymous")
    p1.show()
    print("[statistics for Unknown plant]")
    statistics_p(p1)


if __name__ == "__main__":
    main()
