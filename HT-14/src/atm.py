# Переписати останню версію банкомата з використанням ООП.

from pathlib import Path
from datetime import datetime
import sqlite3
import requests
from abc import ABC, abstractmethod


def pretty_print(func):
    # custom decorator for output
    def wrapper(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)

    return wrapper


class Person(ABC):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def view_balance(self):
        return NotImplemented

    @abstractmethod
    def money_in(self, amount, conector):
        return NotImplemented

    @abstractmethod
    def money_out(self, amount, conector):
        return NotImplemented

    @staticmethod
    def validation(username: str, password: str, conector):
        with conector.con:
            all_users = conector.cur.execute("SELECT username, password, is_incasator FROM users").fetchall()

        for user_line in all_users:
            try:
                name, secur, status = user_line
            except Exception:
                print("invalid data")
                return None

            if name == username and secur == password:
                if status:
                    return Incasator(username, password)
                else:
                    return User(username, password)
        else:
            return None

    @staticmethod
    @pretty_print
    def show_curr_exchange_table():
        try:
            request = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
            request.raise_for_status()
        except:
            print("something is wrong with request")
            return
        currency_list = request.json()
        for temp_dict in currency_list:
            print(
                f"{temp_dict['ccy']}/{temp_dict['base_ccy']} : buy : {temp_dict['buy']}, sale : {temp_dict['sale']}\n")


class User(Person):

    def __init__(self, username, password):
        super().__init__(username, password)

    @pretty_print
    def view_balance(self, conector):
        # shows the current balance of a user
        balance = conector.cur.execute("SELECT balance FROM users_balance WHERE user = ?",
                                       (self.username,)).fetchone()[0]
        print(balance)

    @pretty_print
    def money_in(self, amount: int, conector):
        if amount <= 0:
            print("incorrect value")
            return

        balance = conector.cur.execute("SELECT balance FROM users_balance WHERE user = ?",
                                       (self.username,)).fetchone()[0]
        total_dinero = amount + int(balance)
        transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}
        transaction_string = str(conector.cur.execute("SELECT transactions FROM users_transactions WHERE user = ?",
                                                      (self.username,)).fetchone()[0])
        transaction_string += str(transaction_dict)
        with conector.con:
            conector.cur.execute("UPDATE users_balance SET balance = ? WHERE user = ?", (total_dinero, self.username))
            conector.cur.execute("UPDATE users_transactions SET transactions = ? WHERE user = ?",
                                 (transaction_string, self.username))
        print("transaction good")

    @pretty_print
    def money_out(self, conector):
        amount = int(input("input your sum (but with plus) :"))
        if amount <= 0:
            print("incorrect value")
            return

        balance = conector.cur.execute("SELECT balance FROM users_balance WHERE user = ?",
                                       (self.username,)).fetchone()[0]
        total_dinero = int(balance) - amount

        if total_dinero < 0:
            print("can't perform the operation")
            return
        else:
            a = conector.cur.execute("PRAGMA table_info(atm);").fetchall()
            b = conector.cur.execute("SELECT * FROM atm").fetchone()
            nominals = {a[i][1]: b[i] for i in range(len(a))}
            if User.im_trying_to_give_you_money(nominals, amount, conector):
                transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}

                transaction_string = str(
                    conector.cur.execute("SELECT transactions FROM users_transactions WHERE user = ?",
                                         (self.username,)).fetchone()[0])
                transaction_string += str(transaction_dict)

                with conector.con:
                    conector.cur.execute("UPDATE users_balance SET balance = ? WHERE user = ?",
                                         (total_dinero, self.username))
                    conector.cur.execute("UPDATE users_transactions SET transactions = ? WHERE user = ?",
                                         (transaction_string, self.username))

                print("operation good")
            else:
                print("can't do it rn, sry")

    @staticmethod
    def im_trying_to_give_you_money(nominals: dict, value: int, conector):
        temp_value = value
        thousands = (temp_value // 1000) * 1000
        temp_value -= thousands
        hundreds = (temp_value // 100) * 100
        temp_value -= hundreds
        tens = (temp_value // 10) * 10
        ones = temp_value - tens
        xcept_dict = {i: 0 for i in nominals.keys()}
        final_dict = {i: 0 for i in nominals.keys()}
        # ex : 367
        if ones:
            print("i can't do this")
            return False
        # if thousands != 0 and {"1000", n}
        if thousands:
            temp_thousands = thousands
            while temp_thousands - 1000 >= 0 and nominals["1000"] > 0:
                temp_thousands = temp_thousands - 1000
                xcept_dict["1000"] += 1
                final_dict["1000"] += 1
                nominals["1000"] -= 1
            thousands = temp_thousands
        # if thousands != 0 and {"1000", 0}

        if thousands:
            temp_thousands = thousands
            while temp_thousands - 500 >= 0 and nominals["500"] > 0:
                temp_thousands = temp_thousands - 500
                final_dict["500"] += 1
                nominals["500"] -= 1
            thousands = temp_thousands
        # if there're thousands still
        if thousands:
            hundreds += thousands
            thousands = 0

        # if hundreds
        if hundreds:
            counter = 0
            arr = [i for i in reversed(nominals.keys()) if int(i) // 100 and not int(i) // 1000]  # [500, 200, 100]
            for _ in arr:
                ok = False
                temp_hundreds = hundreds
                for j in arr[counter:]:  # counter 1 will eliminate "500" from arr in case of fail
                    while temp_hundreds - int(j) >= 0 and nominals[j] > 0:
                        temp_hundreds = temp_hundreds - int(j)
                        xcept_dict[j] += 1
                        nominals[j] -= 1
                if temp_hundreds == 0:
                    hundreds = 0
                    for n in arr:
                        if xcept_dict[n] > 0:
                            final_dict[n] += xcept_dict[n]
                            xcept_dict[n] = 0
                    ok = True
                    break
                else:
                    for n in arr:
                        if xcept_dict[n] > 0:
                            nominals[n] += xcept_dict[n]
                            xcept_dict[n] = 0
                counter += 1
                if ok:
                    break

        if hundreds:
            temp_hundreds = hundreds
            while temp_hundreds - 50 >= 0 and nominals["50"] > 0:
                temp_hundreds = temp_hundreds - 50
                final_dict["50"] += 1
                nominals["50"] -= 1
            hundreds = temp_hundreds
        if hundreds:
            tens += hundreds
            hundreds = 0

        if tens:
            counter = 0
            arr = [i for i in reversed(nominals.keys()) if int(i) // 10 and not int(i) // 100]  # [50, 20, 10]
            for _ in arr:
                ok = False
                temp_tens = tens
                for j in arr[counter:]:
                    while temp_tens - int(j) >= 0 and nominals[j] > 0:
                        temp_tens = temp_tens - int(j)
                        xcept_dict[j] += 1
                        nominals[j] -= 1
                if temp_tens == 0:
                    tens = 0
                    ok = True
                    for n in arr:
                        if xcept_dict[n] > 0:
                            final_dict[n] += xcept_dict[n]
                            xcept_dict[n] = 0
                    break
                else:
                    for n in arr:
                        if xcept_dict[n] > 0:
                            nominals[n] += xcept_dict[n]
                            xcept_dict[n] = 0
                counter += 1
                if ok:
                    break
        if not (tens or hundreds or thousands):

            with conector.con:
                conector.cur.execute(
                    'UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
                    tuple(i for i in nominals.values()))

            if final_dict['10']:
                print(f"{final_dict['10']} of nominal 10 ", end="\t")
            if final_dict['20']:
                print(f"{final_dict['20']} of nominal 20 ", end="\t")
            if final_dict['50']:
                print(f"{final_dict['50']} of nominal 50 ", end="\t")
            if final_dict['100']:
                print(f"{final_dict['100']} of nominal 100 ", end="\t")
            if final_dict['200']:
                print(f"{final_dict['200']} of nominal 200 ", end="\t")
            if final_dict['500']:
                print(f"{final_dict['500']} of nominal 500 ", end="\t")
            if final_dict['1000']:
                print(f"{final_dict['1000']} of nominal 1000 ", end="\t")
            print("")
            return True
        else:
            for i in nominals.keys():
                if xcept_dict[i] > 0:
                    nominals[i] += xcept_dict[i]
            return False


class Incasator(Person):

    def __init__(self, username, password):
        super().__init__(username, password)

    @pretty_print
    def view_balance(self, conector):
        a = conector.cur.execute("PRAGMA table_info(atm);").fetchall()
        b = conector.cur.execute("SELECT * FROM atm").fetchone()
        nominals = {a[i][1]: b[i] for i in range(len(a))}
        print(nominals)

    @pretty_print
    def money_in(self, amount: int, conector):
        nominal = int(input("input your nominal :"))
        a = conector.cur.execute("PRAGMA table_info(atm);").fetchall()
        b = conector.cur.execute("SELECT * FROM atm").fetchone()
        nominals = {a[i][1]: b[i] for i in range(len(a))}
        if not (str(nominal) in nominals.keys()):
            print("i don't hold such type of nominal")
            return
        if amount <= 0:
            print("don\'t scam me okay?")
            return
        else:
            nominals[str(nominal)] += amount
            with conector.con:
                conector.cur.execute(
                    'UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
                    tuple(i for i in nominals.values()))
            print("operation good")

    @pretty_print
    def money_out(self, conector):
        a = conector.cur.execute("PRAGMA table_info(atm);").fetchall()
        b = conector.cur.execute("SELECT * FROM atm").fetchone()
        nominals = {a[i][1]: b[i] for i in range(len(a))}
        for i in nominals.keys():
            nominals[i] = 0
        with conector.con:
            conector.cur.execute(
                'UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
                tuple(i for i in nominals.values()))
        print("operation good")


class DataBaseConnector(object):

    def __init__(self, db_file):
        self.db_file = db_file
        self.con = None
        try:
            self.con = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)
            exit(1)
        self.cur = self.con.cursor()

    def create_user_tb(self):
        with self.con:
            self.cur.execute(""" CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY NOT NULL,
                            password TEXT NOT NULL,
                            is_incasator INTEGER NOT NULL DEFAULT FALSE
                            ); """)

    def create_user_transactions_tb(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users_transactions(
                                        user TEXT NOT NULL,
                                        transactions BLOB,
                                        FOREIGN KEY(user) references users(username)
                                        );""")

    def create_user_balance_tb(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users_balance(
                                   user TEXT NOT NULL,
                                   balance INTEGER NOT NULL,
                                   FOREIGN KEY(user) references users(username)
                                   );""")

    def create_atm_tb(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS atm(
                          "10" INTEGER NOT NULL,
                          "20" INTEGER NOT NULL,
                          "50" INTEGER NOT NULL,
                          "100" INTEGER NOT NULL,
                          "200" INTEGER NOT NULL,
                          "500" INTEGER NOT NULL,
                          "1000" INTEGER NOT NULL
                          );""")

    def fill_up_db(self, users_list, atm_status, balance_dict):
        for user in users_list:
            # check if user exist
            exist = self.cur.execute("SELECT rowid FROM users WHERE username = ?", (user.username,)).fetchone()
            if not exist:
                with self.con:
                    self.cur.execute("INSERT INTO users(username, password, is_incasator) VALUES (?,?,?)",
                                     (user.username, user.password, isinstance(user, Incasator),))
            # check if balance exist
            exist = self.cur.execute(f"SELECT rowid FROM users_balance WHERE user = ?", (user.username,)).fetchone()
            if not exist:
                with self.con:
                    self.cur.execute("INSERT INTO users_balance(user, balance) VALUES (?,?)",
                                     (user.username, balance_dict[user.username]))

            # check if transactions exist
            exist = self.cur.execute(f"SELECT rowid FROM users_transactions WHERE user = ?",
                                     (user.username,)).fetchone()
            if not exist:
                with self.con:
                    self.cur.execute("INSERT INTO users_transactions(user, transactions) VALUES (?,?)",
                                     (user.username, balance_dict[user.username]))

        exist = self.cur.execute("SELECT * FROM atm").fetchone()
        if not exist:
            with self.con:
                self.cur.execute(
                    'INSERT INTO atm("10", "20", "50", "100", "200", "500", "1000") VALUES (?, ?, ?, ?, ?, ?, ?)',
                    tuple((i for i in atm_status.values())))


def start():
    # main function, runs all mentioned above

    conector = DataBaseConnector(Path(__file__).parent.parent / "data" / "users.db")

    with conector.con:
        conector.create_user_tb()
        conector.create_user_balance_tb()
        conector.create_user_transactions_tb()
        conector.create_atm_tb()

    users_info_list = [["user1", "user1", 0],
                       ["user2", "user2", 0],
                       ["admin", "admin", 1]]

    users_list = []
    for info in users_info_list:
        if info[-1]:
            users_list.append(Incasator(info[0], info[1]))
        else:
            users_list.append(User(info[0], info[1]))

    atm_status = {"10": 0, "20": 62, "50": 16, "100": 0, "200": 15, "500": 10, "1000": 0}
    balance_dict = {"user1": 1237, "user2": 909, "admin": 999999}

    conector.fill_up_db(users_list, atm_status, balance_dict)

    # now all tables are created

    ok = True
    user_show_actions = '''Actions:
    1.view balance 
    2. money in
    3. money out
    4. show current exchange table
    0. exit\n(example : 1) : '''
    while ok:
        username, password = input("enter your username and password(ex.:antoxaMC mypasswrd) : ").split(sep=" ")
        valid_person = Person.validation(username, password, conector)
        if not valid_person:
            print("bad username or password")
            break
        else:
            flag = True
            while flag:
                try:
                    choice = int(input(user_show_actions))
                except ValueError:
                    choice = ""
                if choice == 1:
                    valid_person.view_balance(conector)
                elif choice == 2:
                    amount = int(input("input your amount :"))
                    valid_person.money_in(amount, conector)
                elif choice == 3:
                    valid_person.money_out(conector)
                elif choice == 4:
                    Person.show_curr_exchange_table()
                elif choice == 0:
                    flag = False
                else:
                    print("choose something...")
        answer = input("continue?(y/n) : ")
        if answer == "n":
            ok = False


if __name__ == "__main__":
    start()
