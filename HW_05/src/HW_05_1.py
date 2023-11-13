def main():
    while True:
        a = int(input())
        b = int(input())
        if a <= b:
            break

    output = []

    for i in range(a, b+1):
        if i % 4 == 0 or i % 9 == 0:
            output.append(i)
            
    print(f"{output}，共有{len(output)}個，總和為{sum(output)}")

if __name__ == '__main__':
        main() 