cur_user = None

def login(username, password):
    if username is not None and password is not None:
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