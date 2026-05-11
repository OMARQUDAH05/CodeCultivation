class plant:
    def __init__(
        self, name: str, height: float, age_d: int, g_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_d = age_d
        self.g_rate = g_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_d} days old")

    def grow(self) -> None:
        self.height += self.g_rate

    def age(self) -> None:
        self.age_d += 1


def main() -> None:
    p1 = plant("Rose", 25, 30, 0.8)
    week = 7
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1, week + 1):
        print(f"=== Day {i} ===")
        p1.grow()
        p1.age()
        p1.show()
    print(f"Growth this week: {week * p1.g_rate:.1f}")


if __name__ == "__main__":
    main()
