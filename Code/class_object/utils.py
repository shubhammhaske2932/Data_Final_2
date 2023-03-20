from main import A

A_obj = A("Shubham", "Mhaske")


class B():
    def B1(self):
        print("B1 function from class B")
        
    def B2(self):
        print("B2 function from class B")
        
    def B3(self):
        print("B3 function from class B")
        return A_obj.user_details()

B_obj = B()
B_obj.B3()