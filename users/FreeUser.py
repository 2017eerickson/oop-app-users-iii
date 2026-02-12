from users import User

class Free_user(User):
    
    stored_posts = []
    
    def create_post():
        if len(Free_user.stored_posts) > 2:
            return "Sorry non premium users are limited to two post"
        else:
            user_post = input("What would you like to post? :")
            Free_user.stored_posts.append(user_post)
            return Free_user.stored_posts
        
        
    