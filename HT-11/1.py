# Сайт для виконання завдання: https://jsonplaceholder.typicode.com
# Написати програму, яка буде робити наступне:
# 1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів
#    (ID, ім'я, нікнейм)

# 2. Запропонувати обрати користувача (ввести ID)

# 3. Розробити наступну менюшку (із вкладеними пунктами):

#    1. Повна інформація про користувача

#    2. Пости:
#       - перелік постів користувача (ID та заголовок)
#       - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)

#    3. ТУДУшка:
#       - список невиконаних задач
#       - список виконаних задач

#    4. Вивести URL рандомної картинки


import requests
import time
import random


def give_dict_request(url: str):
    # takes an url and returns json if request was successful, else None :
    try:
        user_request = requests.get(url)
        time.sleep(0.5)
        user_request.raise_for_status()
    except:
        print("request fail")
        return
    return user_request.json()


def give_dict_user(url: str, user_id: int):
    # takes an url and returns json for certain user(for .../users )if request was successful, else None :
    try:
        user_request = requests.get(url)
        time.sleep(0.5)
        user_request.raise_for_status()
    except:
        print("request fail")
        return
    a = None
    for user in user_request.json():
        if user.get("id", 0) == user_id:
            a = user
    return a


def users_brief_info():
    # 1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів
    #    (ID, ім'я, нікнейм) :

    placeholder_users = 'https://jsonplaceholder.typicode.com/users'

    user_info_dict = give_dict_request(placeholder_users)

    for user in user_info_dict:
        print(f"ID : {user.get('id')}\nName :{user.get('name')}\nNickname :{user.get('username')}", end="\n\n")


def choose_user_id():
    placeholder_users = 'https://jsonplaceholder.typicode.com/users'
    try:
        input_id = int(input("input your id : "))
    except ValueError:
        print("can't understand your id :(")
        return
    user = give_dict_user(placeholder_users, input_id)
    print(f"ID : {user.get('id')}\nName :{user.get('name')}\nNickname :{user.get('username')}", end="\n\n")
    return input_id


def usr(user_id):
    placeholder_users = 'https://jsonplaceholder.typicode.com/users'

    # 1. Повна інформація про користувача

    user = give_dict_user(placeholder_users, user_id)

    print(f"ID : {user.get('id')}\nName :{user.get('name')}\nNickname : {user.get('username')}\n"
          f"address : {user['address'].get('street')} street, {user['address'].get('suite')}, "
          f"{user['address'].get('city')},\nzipcode : {user['address'].get('zipcode')}\n"
          f"geolocation : lat : {user['address']['geo'].get('lat')}, lng : {user['address']['geo'].get('lng')}\n"
          f"Contacts : phone : {user.get('phone')}, website : {user.get('website')}\n"
          f"Company : {user['company'].get('name')}, catch phrase : {user['company'].get('catchPhrase')}, "
          f"bs : {user['company'].get('bs')}\n\n"
          )

    # 2. Пости:


def posts(input_id):
    placeholder_posts = 'https://jsonplaceholder.typicode.com/posts'
    placeholder_comments = 'https://jsonplaceholder.typicode.com/comments'
    posts = give_dict_request(placeholder_posts)


    # перелік постів користувача (ID та заголовок)
    for post_info in posts:
        if post_info.get("userId", 0) == input_id:
            print(f"id : {post_info.get('id')},title : {post_info.get('title')}")

    # інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)

    comments = give_dict_request(placeholder_comments)
    try:
        input_post_id = int(input("input your post id : "))
    except ValueError:
        print("can't understand your id :(")
        return
    for post_info in posts:
        if post_info.get("id", 0) == input_post_id:
            number_of_comments = 0
            comments_id_list = []
            for comment_info in comments:
                if comment_info.get("postId") == input_post_id:
                    number_of_comments += 1
                    comments_id_list.append(comment_info.get("id"))
            print(f"id : {post_info.get('id')}\ntitle : {post_info.get('title')}\n"
                  f"body : {post_info.get('body')}\n{number_of_comments=}\n"
                  f"all comments id's : {comments_id_list}")


def todo(input_id):
    #    3. ТУДУшка:
    placeholder_todos = 'https://jsonplaceholder.typicode.com/todos'
    todos = give_dict_request(placeholder_todos)
    completed_list = []
    unfinished_list = []
    for todo_dict in todos:
        if todo_dict.get("userId") == input_id:
            if todo_dict.get("completed"):
                completed_list.append(todo_dict)
            else:
                unfinished_list.append(todo_dict)
    print("\n**************\n"
          "completed tasks"
          "\n**************\n")
    for task in completed_list:
        print(f"id :{task.get('id')}, title : {task.get('title')}")
    print("\n****************\n"
          "unfinished tasks"
          "\n****************\n")
    for task in unfinished_list:
        print(f"id :{task.get('id')}, title : {task.get('title')}")


def photo():
    # 4. Вивести URL рандомної картинки
    placeholder_photos = 'https://jsonplaceholder.typicode.com/photos'
    photos = give_dict_request(placeholder_photos)
    random_number = random.randint(0, len(photos))
    print("your url : ", photos[random_number].get('url'))


def main():
    print("short info about users : ")
    users_brief_info()
    print("choose 1 user (1 to 10): ")
    user_id = choose_user_id()
    ok = 1
    while ok:
        try:
            command = int(input("Actions : 1.full user info\n2.get post\n3.print todos\n4.random photo url\n"
                                "print your command : "))
        except ValueError:
            print("can't understand your input :(")
            break

        if command == 1:
            usr(user_id)
        elif command == 2:
            posts(user_id)
        elif command == 3:
            todo(user_id)
        elif command == 4:
            photo()
        else:
            ok = 0


if __name__ == "__main__":
    main()