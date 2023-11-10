import matplotlib.pyplot as plt

path = '..\\data\\snow-white.txt'

def main():
    c = {}
    f = open(path)
    txt = f.read().lower()                          #全部轉成小寫
    f.close()
    txt = "".join(filter(str.isalpha, txt))         #只留a~z
    #print(txt)

    for i in sorted(txt):
        c[i] = txt.count(i)
    print(c)

    plt.bar(list(c.keys()), c.values())
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except:
        pass