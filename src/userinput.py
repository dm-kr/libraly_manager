
def get_number_from_user(text: str = "Введите число: ", allow_empty=False) -> str:
    user_input: str = input(text).strip()
    if allow_empty == True and user_input == "":
        return user_input
    try:
        int(user_input)
    except ValueError:
        print("Некорректный ввод!")
        user_input = get_number_from_user(text=text)
    return user_input


def get_user_action():
    pass
