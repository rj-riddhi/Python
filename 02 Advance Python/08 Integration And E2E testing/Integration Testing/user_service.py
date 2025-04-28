# Testing in software development is crucial to ensure the reliability of an application. 
# Two key testing strategies are: 
#     1. Integration Testing – Verifies that multiple components or modules work together as expected. 
    # 2. End-to-End (E2E) Testing – Tests the entire application flow, simulating real user interactions. 

# What is Integration Testing? 
#     - It tests interactions between different modules or services. 
#     - Ensures that components work together correctly. 
#     - Typically uses databases, APIs, or external dependencies. 

class UserService:
    def __init__(self, database):
        self.database = database

    def create_user(self, username):
        if self.database.user_exist(username):
            return f"User with the name {username} is exist"
        else:
            self.database.save_user(username)
            return f"User with the name {username} created!!!"