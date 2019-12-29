import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    print(data)