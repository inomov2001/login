import os
import sys


class User:
    def __init__(self, user_file_name="file.txt"):
        os.system("clear")
        self.login = None
        self.password = None
        self.file_name = user_file_name
        self.all_users = []
        self.initial_page()

    def initial_page(self):
        enter_sys = input(self.welcome_msg()).strip()

        while not self.file_empty() and enter_sys not in ["1", "2", "3"]:
            os.system("clear")
            print("Invalid input! ")
            enter_sys = input(self.welcome_msg()).strip()

        while self.file_empty() and enter_sys not in ["1", "2"]:
            os.system("clear")
            print("Invalid input! ")
            enter_sys = input(self.welcome_msg()).strip()

        if enter_sys == "1":
            self.register()
        elif not self.file_empty() and enter_sys == "2":
            self.log_in()
        else:
            sys.exit()

    def register(self):
        self.get_all_users()
        print("Register part not written yet! ")

    def log_in(self):
        if self.user_logged_in():
            print("You are already logged in!")
            return
        os.system("cls")
        tmp_login = input("Your login: ").strip()
        tmp_password = input("YOur password: ").strip()

        while not self.login_is_correct(tmp_login) or not self.password_is_correct(tmp_password):
            os.system("cls")
            self.wrong_log_pass_msg()
            tmp_login = input("Your login: ").strip()
            tmp_password = input("YOur password: ").strip()

        self.get_all_users()
        if self.user_exists(tmp_login, tmp_password):
            print("You are logged in successfully")
            self.login = tmp_login
            self.password = tmp_password
        else:
            os.system("csl")
            print("This user does not exists")
            self.all_users.clear()
            self.initial_page()
        os.system("clear")
        

    def log_out(self):
        self.login = self.password = None
        self.all_users.clear()
        self.initial_page()

    def update_login(self):
        pass

    def update_password(self):
        pass

    def delete_account(self):
        pass

    def welcome_msg(self):
        if self.file_empty():
            return """
            Please select one of the options below:

            [1] Register
            [2] Exit
            """
        else:
            return """
            Please select one of the options below:

            [1] Register
            [2] Login
            [3] Exit
            """

    @staticmethod
    def login_is_correct(login_: str):
        return len(login_) > 2 and login_.isalnum()

    @staticmethod
    def password_is_correct(password_: str):
        return len(password_) > 5

    @staticmethod
    def wrong_log_pass_msg():
        print("Login or password is invalid!")
        print("Login should contain at least 3 characters, [a-z] and/or ]0-9]")
        print("Password should contain at least 6 characters")

    def file_empty(self):
        with open(self.file_name) as file:
            text = file.read()
        return text == ""

    def get_all_users(self):
        with open(self.file_name) as file:
            users = file.read()
            for row in users.split():
                self.all_users.append(
                    {
                        "login": row.split("|")[0].split("=")[1],
                        "password": row.split("|")[1].split("=")[1]
                    }
                )

    def show_all_users(self):
        [print(user_) for user_ in self.all_users]

    def user_exists(self, login_: str, password_: str):
        for user__ in self.all_users:
            if user__["login"] == login_ and user__["password"] == password_:
                return True
        return False

    def user_logged_in(self):
        return self.login is not None and self.password is not None


person = User()
