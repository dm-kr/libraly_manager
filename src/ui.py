def draw_menu() -> None:
    menu = [
        "Добавить книгу",
        "Удалить книгу",
        "Поиск книг",
        "Вывести список книг",
        "Изменить статус книги",
        "Выйти"
    ]
    v_wall: str = chr(0x2551)
    h_wall: str = chr(0x2550)
    corners: str = [chr(0x2554), chr(0x2557), chr(0x255D), chr(0x255A)]
    print(corners[0] + h_wall * 30 + corners[1])
    print(f"{v_wall}Добро пожаловать в библиотеку!{v_wall}")
    for i, action in enumerate(menu, start=1):
        left_border: str = v_wall
        right_border = f"{" " * (26 - len(action))}{v_wall}"
        print(f"{left_border}{i} - {action}{right_border}")
    print(corners[3] + h_wall * 30 + corners[2])
