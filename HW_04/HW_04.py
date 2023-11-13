import sys

def fib(k):
    if k == 0:
       return [0]
    if k == 1:
        return [1]
    fibs = [0, 1]
    for i in range(1, k):
        fibs.append(fibs[-1] + fibs[-2])
        if fibs[-1] > sys.maxsize:
            return "overflow"
    return fibs

def main():
    k = int(input())
    print(f"F({k}) = {fib(k)}")

if __name__ == "__main__":
    main()