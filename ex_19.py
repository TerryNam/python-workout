from fileinput import filename


def passwd_to_dict(filename):
    users = {} #key-value pair로 만들기 위해 
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')): # 주석 및 blank line제외 한 content만 처리하기 위해
                user_info = line.split(":")      # str(line)에서 원하는 부분만 뽑아내기 위해 split()메서드로 구분자(:)에 따라 쪼갬
                users[user_info[0]] = int(user_info[2])  #dict에 keyword,value 선언
    return users
    

print(passwd_to_dict('passwd.txt'))

