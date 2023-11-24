class Cola:
    def __init__(self):
        self.array=[0]

    def push(self, valor_to_input):
        self.array.append(valor_to_input)

    def pop(self):
        self.array.pop()


if __name__ == "__main__":
    c1 = Cola()
    for _ in range(10):
        c1.push("macia")

        c1.pop()