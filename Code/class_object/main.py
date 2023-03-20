class A:
    
    def __init__(self,f_name,l_name):
        print("Hello welcome to class A")
        self.f_name = f_name
        self.l_name = l_name
        
    def user(self,f_name,l_name):
        pass
    
    def user_details(self):
        print("User First Name :",self.f_name)
        print("User Last Name :",self.l_name)