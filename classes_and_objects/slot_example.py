import random

class SlotMachine:
    def __init__(self):
        self.icons = ["🍒", "🔔", "🍫", "7️⃣"]

    def spin(self):
        return [random.choice(self.icons) for _ in range(3)]

class CasinoGame:
    def __init__(self, id):
        self.user_account_id = id
        self.slot_machine = SlotMachine()
        self.balance = 0
        self.lost_money_balance = 0


    def start(self):
        print("------ Welcome to Monaco Casino ------")
        self.balance = int(input('Enter the amount to start your balance:'))
        self.play_game()

    def play_game(self):
        while self.balance > 0:
            print(f"\nCurrent balance: {self.balance}")
            bet_amount = int(input("Enter the bet amount: "))

            if bet_amount <= self.balance:
                self.balance -= bet_amount
                self.lost_money_balance += bet_amount
                icons = self.slot_machine.spin()

                if self.user_account_id == '12345' and self.lost_money_balance >= 50000:

                    profit = bet_amount * 10
                    self.balance += profit
                    print(f"Spinning...{list(icons[0] * 3)}")
                    print(f"Congratulations! Jackpot! {profit:.2f} Euro!")
                    print(f"Real - Spinning...{' '.join(icons)}")
                    continue

                print(f"Spinning...{' '.join(icons)}")
                if self.check_jackpot(icons):
                    profit = bet_amount * 10
                    self.balance += profit
                    print(f"Congratulations! Jackpot! {profit:.2f} Euro!")
                elif icons[0] == icons[1] or icons[1] == icons[2]:
                    profit = bet_amount * 2
                    self.balance += profit
                    print(f"Congratulations! You win {profit:.2f} Euro!")
                else:
                    print("Better luck next time!")
            else:
                print("Insufficient balance!")
                break

    def check_jackpot(self, icons):
        return all(icon == icons[0] for icon in icons)


casino = CasinoGame('12345')
casino.start()