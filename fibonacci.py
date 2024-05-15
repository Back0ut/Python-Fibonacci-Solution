class fibonacci_solution():
    def __init__(self, length: int):
        self.length = length
        self.ans = [0, 1]

        for n in range(0, length+1):
            (self.ans).append(self.ans[-1] + self.ans[-2])

if __name__ == '__main__':
    given_length = input('Length: ')

    try:
        int(given_length)
    except:
        print('Error! Length must be number')

    fibonacci = fibonacci_solution(given_length)
    print(fibonacci.ans)
