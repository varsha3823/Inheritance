class InstagramAccount:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            if self._private_reels:
                for reel in self._private_reels:
                    print(reel)
            else:
                print("No private reels available")
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            if self.__archived_reels:
                for reel in self.__archived_reels:
                    print(reel)
            else:
                print("No archived reels available")
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Incorrect Password"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")


account = InstagramAccount("my_account", "1234")

account.add_private_reel("Vacation Reel")
account.add_private_reel("Birthday Reel")

account.add_archived_reel("Old Trip")
account.add_archived_reel("College Days")

print("Private Reels (Follower):")
account.display_private_reels(True)

print("\nPrivate Reels (Non-Follower):")
account.display_private_reels(False)

print("\nArchived Reels (Correct Password):")
account.display_archived_reels("1234")

print("\nArchived Reels (Wrong Password):")
account.display_archived_reels("0000")

print("\nUpdating Password:")
account.set_password("1234", "5678")

print("\nArchived Reels After Password Change:")
account.display_archived_reels("5678")
