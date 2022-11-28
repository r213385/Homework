def ask_password():
    for i in range(1,3):
        pfrol = input()
        if pfrol == 'password':
            print('пароль принят')
            break
        elif i == 3:
            print('пароль не принят')
            return