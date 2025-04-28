class Database:
    def __init__(self):
        self.users = set()
    def user_exist(self, name):
        return name in self.users
    
    def save_user(self, name):
        self.users.add(name)