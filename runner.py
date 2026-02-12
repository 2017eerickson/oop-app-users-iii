from users.User import User 
# from users import FreeUser
# 


def user_menu():
    choice = input("""  ---WELCOME--- \n 1. Create User \n 2. Post \n 3. View users \n 4. Update user \n 5. Delete user \n 6. Quit \n ---Please choose an option (1-6)--- :
            """)
    while choice != "6":
        match choice:
            case "1":
                new_user = User.create_user()
                return new_user
            case "2":
                new_post = User.create_post()
                return new_post
            case "3":
                view_users = User.users()
                print(view_users)

print(user_menu())