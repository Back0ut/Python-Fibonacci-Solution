class fibonacci_solution():
    def __init__(self, length: int):
        self.length = length
        self.ans = [0, 1]

        for n in range(0, length+1):
            (self.ans).append(self.ans[-1] + self.ans[-2])

fibonacci = fibonacci_solution(5)
print(fibonacci.ans)