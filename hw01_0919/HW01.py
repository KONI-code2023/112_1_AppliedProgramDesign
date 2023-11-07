def main():
  RANGE = 100
  count = 0
  results = []
  for a in range(RANGE + 1):
    for b in range(a, RANGE + 1):
      for c in range(b, RANGE + 1):
        for d in range(c, RANGE + 1):
          if a**3 + b**3 + c**3 == d**3:
            if a < b < c < d:
              results.append((a, b, c, d))
              count += 1
  for i in results:
    print(f"({i[0]}, {i[1]}, {i[2]}, {i[3]})")
  print(f"總共{count}組")

if __name__ == '__main__':
    main()  