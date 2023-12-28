class TrainTickets:
    def __init__(self):
        self.rows = []
        self.columns = ['A', 'B', 'C', 'D', 'E']
        self.tickets = []
        self.initialize_tickets()

    def initialize_tickets(self):
        for i in range(1, 11):
            if i == (20 / 2):
                self.rows.append(i)
            else:
                self.rows.append(i)
                self.rows.append(20 - i)

        for row in self.rows:
            for column in self.columns:
                if row % 2 == 0 and column in ('B', 'E'):
                    self.tickets.append(str(row) + column)
                elif row % 2 != 0 and column in ('A', 'C', 'D'):
                    self.tickets.append(str(row) + column)

    def purchase_tickets(self):
        while self.tickets:
            try:
                num = int(input("請輸入購買張數 (1-4)："))
                if 0 < num <= 4:
                    if len(self.tickets) < num:
                        print(f"剩餘票數不足，目前剩餘{len(self.tickets)}張票")
                    else:
                        for _ in range(num):
                            print(self.tickets.pop(0), end=' ')
                        print()
                else:
                    print("每人每次限購 1~4 張票")
            except ValueError as err:
                print("請輸入正確購買票數")

def main():
    train_tickets = TrainTickets()
    train_tickets.purchase_tickets()

if __name__ == "__main__":
    main()
