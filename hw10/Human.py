class Human:
 
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        print(f'Hello {self.name.title()}')

    @classmethod
    def info(cls):
        print('Species is Homosapiens')
    
    @staticmethod
    def arbitrary_message():
        print(f'You are so funny')



