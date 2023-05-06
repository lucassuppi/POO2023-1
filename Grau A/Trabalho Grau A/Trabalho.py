import os, time, random
from objects import User, CSVHandler, UserSticker


class UI:
    @staticmethod
    def main_menu():
        UI.clear_screen()
        
        while True:
            print('Album Menu')
            print('1. New Album')
            print('2. Access Album')
            print('3. Exit')
            
            choice = int(input('Enter your choice (1-3): '))
            
            match (choice):
                case 1:
                    user_username = input('Enter your username: ')
                    user_password = input('Enter your password: ')
                    if not User.register(user_username, user_password):
                        print("Username is taken!")
                        continue
                    
                    print("Successfully registered!")
                    UI.wait()
                    
                    UI.manage_album_screen(User(user_username))
                   
                case 2:
                    user_username = input('Enter your username: ')
                    user_password = input('Enter your password: ')
                    
                    if not User.verify_login(user_username, user_password):
                        print("Username or password is incorrect")
                        UI.wait()
                        continue
                    
                    print("Successfully logged in!")
                    UI.wait()
                    
                    UI.clear_screen()
                    UI.manage_album_screen(User(user_username))
                    
                case 3:
                    break
                
            print()
            
            UI.clear_screen()
            
    @staticmethod
    def manage_album_screen(user: User):
        while True:
            print('Manage Album Screen')
            print('1. View Album Description')
            print('2. Manage the Collection')
            print('3. Open sticker pack')
            print('4. Back to previous menu')
            
            choice = int(input('Enter your choice (1-4): '))

            match choice:
                case 1:
                    pass
                case 2:
                    print('Your sticker collection: ')
                    for sticker in user.get_collection().values():
                        print(sticker)
                    time.sleep(10)
                    
                case 3:
                    stickers = [*CSVHandler.get_all_stickers()]
                    pack = [random.choice(stickers) for _ in range(3)]
                    
                    print('Your new stickers: ')
                    for csvsticker in pack:
                        user_sticker = UserSticker.from_csvsticker(csvsticker)
                        
                        user.add_sticker_to_collection(user_sticker)
                        CSVHandler.add_usersticker(user.get_username(), user_sticker)
                        
                        print(csvsticker)
                        
                    time.sleep(10)
                    
                case 4:
                    break
            print()
            UI.clear_screen()
            
    def clear_screen():
        os.system('cls')
    
    def wait():
        time.sleep(1)
    
if __name__ == "__main__":
    UI.main_menu()
