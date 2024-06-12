class User:
    def __init__(self, id, first_name, last_name, age, group):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.group = group

    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'age': self.age,
            'group': self.group
        }
