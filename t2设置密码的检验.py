def check_password(password):
    if len(password) < 8:
        return "密码太短,至少8位！"
    for char in password:
        a = False
        b = False
        if char.isspace():
            return "密码不能包含空格！"
    a = any(char.isdigit() for char in password)
    b = any(char.isalpha() for char in password)
    if not (a and b):
        return "密码必须包含数字和字母！"
    if not a:
        return "密码必须包含数字！"
    if not b:
        return "密码必须包含字母！"
    return "密码符合要求！"
print(check_password(input("请输入密码：")))
input("按回车键退出")