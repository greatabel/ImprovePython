import i6hook_login_module


def my_login_hook(username):
    print('#'*5, username , '*'*10)



if __name__ == "__main__":
    i6hook_login_module.set_login_hook(my_login_hook)
    i6hook_login_module.login("abel", "1234")
    print('start# cur_user=', i6hook_login_module.cur_user)
    i6hook_login_module.logout()
    print('end  # cur_user=', i6hook_login_module.cur_user)