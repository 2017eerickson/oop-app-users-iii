class User: 
    
    posted = []
    users = {
        "ericka" : { "name": "Ericka",
                    "email": "eerickson2017@gmail.com",  
                    "license": "4ff545",
                    "posts" : ["merry christmas", "my coding school started", "I got a SWE job!"]  
        }
    }
    
    def __init__(self, name, email, license, post):
        self.name = name
        self.email = email
        self.license = license
        self.license = post
        
    def __repr__(self):
        return      
     
    @classmethod   
    def create_user(cls):
        new_user = {
            "name" : input("Please enter a name: \n"),
            "email" : input("Please enter an email: \n "),
            "license" : input("Please enter your license number: \n"),
            }
        cls.users.append(new_user)
        return new_user 
    
    def create_post():
        user = input("What is your username?: ")
        if user in User.users :
            user_post = input("What would you like to post? :")
            User.posted.append(user_post)
            return f" user {user} :posted {user_post}"
        else:
            return print("User not found , please create a user first. ")
            
           
    @property
    def email(self, email_val):
        self._email = email_val
    
    @email.setter
    def email(self, email_val):
        if "@" in email_val:
            self._email = email_val
        else:
            raise Exception("Invalid email")


    