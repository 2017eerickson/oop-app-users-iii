from users.User import User 
# from users import FreeUser
# 


def user_menu():
    choice = input("""  ---WELCOME--- \n 1. Create User \n 2. Post \n 3. View users \n 4. Update user \n 5. Delete user \n 6. Quit \n ---Choose (1-6)--- :
            """)
    while choice :
        match choice:
            case "1":
                new_user = User.create_user()
                print(new_user)
                user_menu()
            case "2":
                new_post = User.create_post()
                print(new_post)
                user_menu()
            case "3":
                view_users = User.users
                print(view_users)
                user_menu()
            case "4":
                update_users = User.users
                print(view_users)
                user_menu()
            case "6":
                choice = False
                return "---Goodbye---"

print(user_menu())