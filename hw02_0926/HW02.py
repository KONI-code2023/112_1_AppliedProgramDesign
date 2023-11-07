import numpy as np

def main():
  n = []
  num = 0

  while num >= 0:
    n.append(num)
    num = float(input())
    
  n.pop(0)

  print(f"輸入數字:{n}，平均值={round(np.mean(n), 2)}，中位數={round(np.median(n), 2)}，"
        f"變異數={round(np.var(n), 2)}，標準差{round(np.std(n), 2)}")

if __name__ == "__main__":
  try:
    main()
  except:
    pass