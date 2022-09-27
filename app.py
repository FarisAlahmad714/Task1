class User:
    def __init__(self , first_name , last_name , email ,age ,is_rewards_member= False  ):
        self.first_name = first_name
        self.last_name = last_name
        self.email =email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = 0

        # Have this method print all of the users' details on separate lines.
    def info(self):
        print(f"first_name:{self.first_name}")
        
user_fw = User('Faris' , 'Wayne' ,'f@w.com', 26 , True )
user_fw.info()



'''
     # adding the greeting method
        def enroll(self):
    	    print(f"Hello, my name is {self.name}")

     # adding the greeting method
            def spend_points(self, amount):
    	        print(f"Hello, my name is {self.name}")    
                '''