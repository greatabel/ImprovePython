cur_user = None
login_hook = None


def set_login_hook(hook):
    print('set_login_hook')
    global login_hook
    login_hook = hook


def login(username, password):
    if username is not None and password is not None:
        global login_hook
        if login_hook != None:
            login_hook(username)

        global cur_user
        cur_user = username
        return True
    else:
        return False


def logout():
    global cur_user
    cur_user = None


if __name__ == "__main__":
    login("abel", "1234")
    print('start# cur_user=', cur_user)
    logout()
    print('end  # cur_user=', cur_user)