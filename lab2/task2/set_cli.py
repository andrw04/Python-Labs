import re
import os


class CLI:
    users = []
    current_user = None

    @classmethod
    def interface(cls):
        us_name = ''
        while not us_name.isalnum():
            us_name = input('Input username: ')
        cls.load(us_name)

        while(True):
            command = input(f'{cls.current_user.name}$ ')
            operation, args = cls.parse_command(command)

            match(operation):
                case 'add':
                    cls.current_user.add(*args)
                case 'remove':
                    cls.current_user.remove(*args)
                case 'find':
                    result = cls.current_user.find(*args)
                    if result:
                        for element in result:
                            print(element)
                    else:
                        print('No such elements')
                case 'list':
                    print(*cls.current_user.list())
                case 'grep':
                    if len(args) == 1:
                        result = cls.current_user.grep(*args)
                        if result:
                            for i in result:
                                print(i)
                        else:
                            print('No such elements')
                case 'save':
                    cls.save()
                case 'load':
                    if len(args) == 1:
                        cls.load(*args)
                case 'switch':
                    if len(args) == 1:
                         cls.switch(*args)
                         op = input('Do you want to load the container? [y/n]: ').strip().lower()
                         if op == 'y':
                             cls.load(cls.current_user.name)
                    else:
                        print('Incorrect command!')
                case 'exit':
                    op = input('Do you want to save all user containers? [y/n]: ').strip().lower()
                    if op == 'y':
                        for user in cls.users:
                            cls.current_user = user
                            cls.save()
                    return

    @staticmethod
    def parse_command(command):
        command = command.split()
        if not command:
            return None, None
        operation = command[0]
        args = command[1:]

        return operation, args
        

    @classmethod
    def switch(cls, username):
        for user in cls.users:
            if user.name == username:
                cls.current_user = user

        if cls.current_user == None or cls.current_user.name != username:
            print(f'Created new user {username}')
            cls.create_user(username)
            cls.current_user = cls.users[-1]

    
    @classmethod
    def save(cls):
        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        data_path = os.path.join(path, 'data')
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        if cls.current_user != None:
            data_path = os.path.join(data_path, f'{cls.current_user.name}.txt')

            with open(data_path,'w+') as file:
                for line in cls.current_user.container:
                    file.write(line + '\n')


    @classmethod
    def load(cls, username):
        if not cls.users:
            cls.create_user(username)

        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        file_path = os.path.join(path, 'data',f'{username}.txt')

        if os.path.exists(file_path):
            user_exist = False
            temp_user = None
            for user in cls.users:
                if user.name == username:
                    temp_user = user
                    user_exist = True
                    break

            if not user_exist:
                cls.switch(username)
                temp_user = cls.current_user

            with open(file_path, 'r') as file:
                    text = file.readlines()
                    for string in text:
                        temp_user.add(string.strip())
                    print('Data successfully loaded')
        else:
            print('Data not found')

            

    @classmethod
    def create_user(cls, username):
        cls.users.append(UserContainer(username))
        cls.current_user = cls.users[-1]



class UserContainer:
    def __init__(self, username=None):
        self.username = username
        self.container = set()

    @property
    def name(self):
        return self.username

    def add(self, *key):
        for i in key:
            self.container.add(i)

    def remove(self, *key):
        for i in key:
            if i in self.container:
                self.container.remove(i)

    def find(self, *key):
        key_set = set(key)
        res = self.container & key_set
        return res

    def list(self):
        return self.container.copy()

    def grep(self, key):
        result = []
        for item in self.container:
            if re.match(key, item):
                result.append(item)
        
        return result


def main():
    CLI.interface()


if __name__ == "__main__":
    main()
