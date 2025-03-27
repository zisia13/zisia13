class Me():

    discord = "zisia13"

    def __init__(self) -> None:

        self.name = "zisia13"

    def __str__(self) -> str:

        return f"My name is: {self.name}" 
    
    @classmethod
    def contact(cls) -> str:

        return cls.discord
    
    @staticmethod
    def get_age() -> int:

        return 19

