from clcrypto import password_hash, generate_salt, check_password


class User:
    __ID_UNSAVED = -1

    def __init__(self):
        self.__id = User.__ID_UNSAVED
        self.__email = None
        self.__unique = None
        self.__username = None
        self.__hashed_password = None

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    def set_password(self, password):
        self.__hashed_password = password_hash(password, generate_salt())

    def is_password_correct(self, candidate):
        return check_password(candidate, self.__hashed_password)


u = User()

u.email = "zajebioza@gmail.com"
u.username = "blaBla"
u.set_password("qwerty")

print(u.email)
print(u.username)
print(u.is_password_correct("qwerty"))
# print(u.is_password_correct("qwertfsffsfsy"))




