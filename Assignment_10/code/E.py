# ======================
# file: Assignment_06.py
# author: KONI-code2023@github
# date: 2023-11-27
# ======================
class TrainTickets:
    def __init__(self) -> None:
        self.rows = []
        self.columns = ["A", "B", "C", "D", "E"]
        self.tickets = []
        self.init_tickets()

    def init_tickets(self) -> None:
        for i in range(1, 11):
            if i == (20 / 2):
                self.rows.append(i)
            else:
                self.rows.append(i)
                self.rows.append(20 - i)

        for row in self.rows:
            for col in self.columns:
                if row % 2 == 0 and col in ("B", "E"):
                    self.tickets.append(str(row) + col)
                elif row % 2 != 0 and col in ("A", "C", "D"):
                    self.tickets.append(str(row) + col)

    def purchase_tickets(self) -> None:
        while self.tickets:
            try:
                num = int(input("購買張數 (1-4)："))
                if 0 < num <= 4:
                    if len(self.tickets) < num:
                        print(f"剩餘票數不足，目前剩餘 {len(self.tickets)} 張票")
                    else:
                        print(f"已完成購買")
                        for _ in range(num):
                            print(self.tickets.pop(0), end=" ")
                        print()
                else:
                    print("每人每次限購 1~4 張票")
            except ValueError:
                print("請輸入正確購買票數")

        print("本車廂所有座位已售完")


def main() -> None:
    tt = TrainTickets()
    tt.purchase_tickets()


if __name__ == "__main__":
    main()
