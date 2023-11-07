def main():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))
        if a <= b:
            break

    output = []

    for i in range(a, b+1):
        if i % 4 == 0 or i % 9 == 0:
            output.append(i)
            
    print(f"輸入：{a}, {b}，輸出：{output}，共有{len(output)}個，總和為{sum(output)}。")

if __name__ == '__main__':
    try:
        main() 
    except:
        pass