from Chef import Chef

# if our Chinese Chef can do everything the regular chef can do, we can use inheritance
    # we could copy and paste from chef file, but that is a drag
    # inheritance makes this easier

class ChineseChef(Chef):

    # we can override inherited functions within our defined class!
    def make_special_dish(self):
        print("The chef prepares lo mein.")

    def make_fried_rice(self):
        print("The chef prepares fried rice.")

