
import re


class Emails(list):

    def __init__(self, data):
       
        cleaned = self.validate(data)
        super().__init__(cleaned)
        self.data = cleaned

    @staticmethod
    def validate(items):
        
        if not all(isinstance(i, str) for i in items):
            raise ValueError("All items must be strings")

        pattern = r"^[^@]+@[^@]+\.[^@]+$"
        
        for email in items:
            if not re.match(pattern, email):
                raise ValueError(f"Invalid email: {email}")

        unique = list(dict.fromkeys(items))

        return unique

    def __repr__(self):
        return f"Emails({list(self)})"

    def __str__(self):
        return ", ".join(self)
