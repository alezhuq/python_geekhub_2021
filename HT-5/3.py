# 3. На основі попередньої функції створити наступний кусок кода:
#    а) створити список із парами ім'я/пароль різноманітних видів
#    (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#    перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)


class LenException(Exception):
    def __init__(self, message="the length of a username does not satisfy the conditions  3<= length <=50"):
        self.message = message


class NoNumberException(Exception):
    def __init__(self, message = "you have to write at least 1 number"):
        self.message = message


def user_validation(username, password:str):

    if not 3 <= len(username) <= 50:
        raise LenException("the length of a username does not satisfy the conditions  3<= length <=50")
    if len(password) < 8:
        raise LenException("the length of a password does not satisfy the conditions  password  >= 8")
    for i in password:
        if i.isdigit():
            break
    else:
        raise NoNumberException()
    print("OK")

def check_users():
    dataset_of_accounts = [
        {
            "Al1n04ka15": "i_like_cats",
            "login": "password1",
            "Groovy": "idkidkidk",
            "YaPasha": "322",
            "Crypto_investor": "H0DL_SH1B",
        }
    ]

    for nickname, passwrd in dataset_of_accounts[0].items():
        print("-------------------------")
        print("name - {} \npassword - {}".format(nickname, passwrd))
        try:
            user_validation(nickname, passwrd)

        except LenException as len_ex:
            print("problem with your nickname  or  password : ", len_ex.message)

        except NoNumberException as numb_ex:
            print("problem with password : ", numb_ex.message)



check_users()
