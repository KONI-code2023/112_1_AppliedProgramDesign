def main():
  max_range = 100
  count = 0
  results = []
  
  for a in range(max_range + 1):
    for b in range(a, max_range + 1):
      for c in range(b, max_range + 1):
        for d in range(c, max_range + 1):
          if a**3 + b**3 + c**3 == d**3:
            if a < b < c < d:
              results.append((a, b, c, d))
              count += 1

  for result in results:
    print(f"({result[0]}, {result[1]}, {result[2]}, {result[3]})")
    
  print(f"共有 {count} 組")

if __name__ == '__main__':
    main()  