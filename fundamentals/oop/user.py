class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, sep= '\n')
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print('User\'s already a member')
            return self
        else:
            self.is_rewards_member == True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print('insufficient funds')
        return self

# id1 = User('Tony', 'Stark', 'iamironman@starkin.com', 48)
# id1.display_info()
# id1.enroll()
# print(id1.spend_points(50))
user1 = User('Tony', 'Stark', 'iamironman@starkin.com', 48)
user1.display_info().enroll().spend_points(50)

user2= User('charles', 'Xavier', 'TomemyXmen@DOE.com', 59)
user2.display_info().enroll().spend_points(80)