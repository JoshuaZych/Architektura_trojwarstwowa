from models.User import User


class UserService:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self):
        return [user.to_dict() for user in self.users]

    def get_user_by_id(self, user_id):
        user = next((u for u in self.users if u.id == user_id), None)
        return user.to_dict() if user else None

    def create_user(self, user_data):
        new_user = User(self.next_id, user_data['firstName'], user_data['lastName'], user_data['age'],
                        user_data['group'])
        self.users.append(new_user)
        self.next_id += 1
        return new_user.to_dict()

    def update_user(self, user_id, updates):
        user = next((u for u in self.users if u.id == user_id), None)
        if not user:
            return None
        if 'firstName' in updates:
            user.first_name = updates['firstName']
        if 'lastName' in updates:
            user.last_name = updates['lastName']
        if 'age' in updates:
            user.age = updates['age']
        if 'group' in updates:
            user.group = updates['group']
        return user.to_dict()

    def delete_user(self, user_id):
        user = next((u for u in self.users if u.id == user_id), None)
        if not user:
            return False
        self.users.remove(user)
        return True
