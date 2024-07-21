import getpass
def diary_app():
    username = input("Enter your username: ")
    secret_key = getpass.getpass(prompt="Enter secret key (include special characters, numbers): ")
    with open('credentials.txt', 'w') as file:
        file.write(username + '\n')
        file.write(secret_key + '\n')
    usernamelogin = input("Enter your username: ")
    secret_key_login = getpass.getpass(prompt="Enter secret key (include special characters, numbers): ")
    with open('credentials.txt', 'r') as files:
            s_username = files.readline().strip()
            s_secret_key = files.readline().strip()
            if usernamelogin == s_username and secret_key_login == s_secret_key:
                print("Welcome to Diary")
                mood = input("Enter your mood today: ")
                print("Enter about your day today (Press Enter twice to Finish The input): ")
                day = []
                while True:
                    line = input()
                    if line.strip() == "":
                        break
                    day.append(line)
                writing = "\n".join(day)
                with open('Diary.txt', 'w') as filed:
                    filed.write("Mood: " + mood + '\n')
                    filed.write("Diary: " + '\n' + writing + '\n')
                print("Diary written successfully")
            else:
                print("Invalid Credentials")
diary_app()
