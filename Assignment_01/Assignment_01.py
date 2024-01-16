# ======================
# file: Assignment_01.py
# author: KONI-code2023@github
# date: 2023-09-25
# ======================
def find_special_numbers(max_range: int) -> list:
    results = []
    for a in range(max_range + 1):
        for b in range(a, max_range + 1):
            for c in range(b, max_range + 1):
                for d in range(c, max_range + 1):
                    if a**3 + b**3 + c**3 == d**3:
                        if a < b < c < d:
                            results.append((a, b, c, d))
    return results


def print_results(results: list) -> None:
    for result in results:
        print(f"({result[0]}, {result[1]}, {result[2]}, {result[3]})")


def main() -> None:
    max_range = 100
    results = find_special_numbers(max_range)

    print_results(results)

    print(f"共有 {len(results)} 組")


if __name__ == "__main__":
    main()
