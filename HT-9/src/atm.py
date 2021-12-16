# Перепишіть програму-банкомат на використання бази даних для збереження всих даних.
# Використовувати БД sqlite3 та натівний Python.
# Дока з прикладами: https://docs.python.org/3/library/sqlite3.html
# Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/
# Для уніфікації перевірки, в базі повинні бути 3 користувача:
#   ім'я: user1, пароль: user1
#   ім'я: user2, пароль: user2
#   ім'я: admin, пароль: admin (у цього коритувача - права інкасатора)


from pathlib import Path
from datetime import datetime
import sqlite3


def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
    except sqlite3.Error as e:
        print(e)

    return con


def validation(username: str, password: str, con, cur):
    with con:
        all_users = cur.execute("SELECT username, password, is_incasator FROM users").fetchall()

    for user_line in all_users:
        try:
            name, secur, status = user_line
        except Exception:
            print("invalid data")
            return "out"

        if name == username and secur == password:
            if status:
                return "worker"
            return "no"


def im_trying_to_give_you_money(nominals: dict, value: int, con, cur):
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

        with con:
            cur.execute('UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
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


def money_in(username: str, amount: int, con, cur):
    if amount <= 0:
        print("incorrect value")
        return

    balance = cur.execute("SELECT balance FROM users_balance WHERE user = ?", (username,)).fetchone()[0]
    total_dinero = amount + int(balance)
    transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}
    transaction_string = str(cur.execute("SELECT transactions FROM users_transactions WHERE user = ?",
                                         (username,)).fetchone()[0])
    transaction_string += str(transaction_dict)
    with con:
        cur.execute("UPDATE users_balance SET balance = ? WHERE user = ?", (total_dinero, username))
        cur.execute("UPDATE users_transactions SET transactions = ? WHERE user = ?", (transaction_string, username))


def money_out(username: str, amount: int, con, cur):
    if amount <= 0:
        print("incorrect value")
        return

    balance = cur.execute("SELECT balance FROM users_balance WHERE user = ?", (username,)).fetchone()[0]
    total_dinero = int(balance) - amount

    if total_dinero < 0:
        print("can't perform the operation")
        return
    else:
        a = cur.execute("PRAGMA table_info(atm);").fetchall()
        b = cur.execute("SELECT * FROM atm").fetchone()
        nominals = {a[i][1]: b[i] for i in range(len(a))}
        if im_trying_to_give_you_money(nominals, amount, con, cur):
            transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}

            transaction_string = str(cur.execute("SELECT transactions FROM users_transactions WHERE user = ?",
                                                 (username,)).fetchone()[0])
            transaction_string += str(transaction_dict)

            with con:
                cur.execute("UPDATE users_balance SET balance = ? WHERE user = ?", (total_dinero, username))
                cur.execute("UPDATE users_transactions SET transactions = ? WHERE user = ?",
                            (transaction_string, username))

            print("operation good")
        else:
            print("can't do it rn, sry")


def cash_out(con, cur):
    a = cur.execute("PRAGMA table_info(atm);").fetchall()
    b = cur.execute("SELECT * FROM atm").fetchone()
    nominals = {a[i][1]: b[i] for i in range(len(a))}
    for i in nominals.keys():
        nominals[i] = 0
    with con:
        cur.execute('UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
                    tuple(i for i in nominals.values()))
    print("operation good")


def cash_in(nominal: int, amount: int, con, cur):
    a = cur.execute("PRAGMA table_info(atm);").fetchall()
    b = cur.execute("SELECT * FROM atm").fetchone()
    nominals = {a[i][1]: b[i] for i in range(len(a))}
    if not (str(nominal) in nominals.keys()):
        print("i don't hold such type of nominal")
        return
    if amount <= 0:
        print("dont scam me okei?")
        return
    else:
        nominals[str(nominal)] += amount
        with con:
            cur.execute('UPDATE atm SET "10" = ?, "20" = ?, "50" = ?, "100" = ?, "200" = ?, "500" = ?, "1000" = ?',
                        tuple(i for i in nominals.values()))
        print("operation good")


def view_balance(username: str, cur):
    # shows the current balance of a user
    balance = cur.execute("SELECT balance FROM users_balance WHERE user = ?", (username,)).fetchone()[0]
    print(balance)


def view_atm(cur):
    a = cur.execute("PRAGMA table_info(atm);").fetchall()
    b = cur.execute("SELECT * FROM atm").fetchone()
    nominals = {a[i][1]: b[i] for i in range(len(a))}
    print(nominals)


def start():
    # main function, runs all mentioned above

    create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY NOT NULL,
                            password TEXT NOT NULL,
                            is_incasator INTEGER NOT NULL DEFAULT FALSE
                            ); """

    create_user_transactions_table = """CREATE TABLE IF NOT EXISTS users_transactions(
                                        user TEXT NOT NULL,
                                        transactions BLOB,
                                        FOREIGN KEY(user) references users(username)
                                        );"""

    create_user_balance_table = """CREATE TABLE IF NOT EXISTS users_balance(
                                   user TEXT NOT NULL,
                                   balance INTEGER NOT NULL,
                                   FOREIGN KEY(user) references users(username)
                                   );"""

    create_atm_table = """CREATE TABLE IF NOT EXISTS atm(
                          "10" INTEGER NOT NULL,
                          "20" INTEGER NOT NULL,
                          "50" INTEGER NOT NULL,
                          "100" INTEGER NOT NULL,
                          "200" INTEGER NOT NULL,
                          "500" INTEGER NOT NULL,
                          "1000" INTEGER NOT NULL
                          );"""

    con = create_connection(Path(__file__).parent.parent / "data" / "users.db")

    cur = con.cursor()
    with con:
        cur.execute(create_user_table)
        cur.execute(create_user_transactions_table)
        cur.execute(create_user_balance_table)
        cur.execute(create_atm_table)

    users_list = [["user1", "user1", 0],
                  ["user2", "user2", 0],
                  ["admin", "admin", 1]]

    atm_status = {"10": 0, "20": 62, "50": 16, "100": 0, "200": 15, "500": 10, "1000": 0}
    balance_dict = {"user1": 1237, "user2": 909, "admin": 999999}
    for user in users_list:
        # check if user exist
        exist = cur.execute("SELECT rowid FROM users WHERE username = ?", (user[0],)).fetchone()
        if not exist:
            with con:
                cur.execute("INSERT INTO users(username, password, is_incasator) VALUES (?,?,?)",
                            (user[0], user[1], user[2],))
        # check if balance exist
        exist = cur.execute(f"SELECT rowid FROM users_balance WHERE user = ?", (user[0],)).fetchone()
        if not exist:
            with con:
                cur.execute("INSERT INTO users_balance(user, balance) VALUES (?,?)",
                            (user[0], balance_dict[user[0]]))

        # check if transactions exist
        exist = cur.execute(f"SELECT rowid FROM users_transactions WHERE user = ?", (user[0],)).fetchone()
        if not exist:
            with con:
                cur.execute("INSERT INTO users_transactions(user, transactions) VALUES (?,?)",
                            (user[0], balance_dict[user[0]]))

    exist = cur.execute("SELECT * FROM atm").fetchone()

    if not exist:
        with con:
            cur.execute('INSERT INTO atm("10", "20", "50", "100", "200", "500", "1000") VALUES (?, ?, ?, ?, ?, ?, ?)',
                        tuple((i for i in atm_status.values())))

        # now all tables are created

    ok = True

    while ok:
        username, password = input("enter your username and password(ex.:antoxaMC mypasswrd) : ").split(sep=" ")
        valid_res = validation(username, password, con, cur)
        if valid_res == "out":
            print("bad username or password")
            break
        elif valid_res == "no":
            flag = True
            while flag:
                choice = int(input(
                    '''Actions:\n1.view balance\n2. money in\n3. money out\n4. exit\n(example : 1) : '''
                ))
                if choice == 1:
                    view_balance(username, cur)
                elif choice == 2:
                    amount = int(input("input your sum :"))
                    money_in(username, amount, con, cur)
                elif choice == 3:
                    amount = int(input("input your sum (but with plus) :"))
                    money_out(username, amount, con, cur)
                elif choice == 4:
                    flag = False
        elif valid_res == "worker":
            flag = True
            while flag:
                choice = int(input(
                    '''Actions:\n1.view atm\n2. cash in\n3. cash out\n4. exit\n(example : 1) : '''
                ))
                if choice == 1:
                    view_atm(cur)
                elif choice == 2:
                    nominal = int(input("input your nominal :"))
                    amount = int(input("input your amount :"))
                    cash_in(nominal, amount, con, cur)
                elif choice == 3:
                    cash_out(con, cur)
                elif choice == 4:
                    flag = False
        else:
            print("bad uname/password")
        answer = input("continue?(y/n) : ")
        if answer == "n":
            ok = False


if __name__ == "__main__":
    start()
