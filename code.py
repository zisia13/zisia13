class Me():

    discord = "zisia13"

    def __init__(self):

        self.name = "zisia13"

    def __str__(self):

        return f"My name is: {self.name}" 
    
    @classmethod
    def contact(cls):

        return cls.discord
    
    @staticmethod
    def get_age() -> int:

        return 19

