class User:
    def __init__(self , first_name , last_name , email ,age  ):
        self.first_name = first_name
        self.last_name = last_name
        self.email =email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else:
            print('You are already member')
    def display_info(self):
        print('Points:' , self.gold_card_points)
    def remove_points(self , amnt):
        if self.gold_card_points >= amnt :
            self.gold_card_points -= amnt
        else:
            print('Not enough Points')
    
        
user_fw = User('Faris' , 'Wayne' ,'f@w.com', 26  )
user_lw = User('Larry' , 'Wayne' ,'l@w.com', 66  )

user_fw.enroll()
user_fw.remove_points(50)
user_fw.remove_points(500)
user_fw.display_info()
user_lw.enroll()

print('User1')
print(user_fw.is_rewards_member)

print('User2')
print(user_lw.is_rewards_member)