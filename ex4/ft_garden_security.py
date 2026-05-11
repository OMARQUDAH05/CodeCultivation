class plant:
    def __init__(
        self, name: str, height: float, age_d: int, g_rate: float = 0.8
    ) -> None:
        self.__name = name
        self.__height = height
        self.__age_d = age_d
        self.__g_rate = g_rate

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age_d} days old")

    def grow(self, nod: int) -> None:
        self.__height += self.__g_rate * nod

    def age(self, nod: int) -> None:
        self.__age_d += nod

    def set_height(self, height: float) -> None:
        if (height > 0):
            self.__height = height
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


def main():
    print("=== Garden Security System ===")
    p1 = plant("Rose", 15, 10)
    print("Plant created: ", end="")
    p1.show()
    print()
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-12)
    p1.set_age(-2)
    print("")
    print("Current state: ", end="")
    p1.show()


if __name__ == "__main__":
    main()
