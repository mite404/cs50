def meow(n: int) -> None:
    return "meow\n" * n


number: int = int(input("How many mow mows? "))
meows: str = meow(number)
print(meows, end="")

