from dataclasses import dataclass, field
@dataclass(order=True)
class Fruit:
    sort_index: int = field(init=False, repr=False)
    name: str
    weight: float

    def __post_init__(self):
        self.sort_index = -self.weight


f = Fruit('apple', 30)
f1 = Fruit('apple', 3)
f2 = Fruit('banana', 30)
f3 = Fruit('coconut', 2)
# f.name = 'banana'
print(f == f1)

l = [f3, f1, f2]
print(sorted(l))


