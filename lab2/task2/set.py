import re
import os


class CLI:
    user = None

    @classmethod
    def interface(cls):
        username = ''

        while not username.isalnum():
            username = input('Input username: ')
        cls.user = UserContainer(username)

        while(True):
            command = input(f'{cls.user.name}$ ')
            operation, args = cls.parse_command(command)

            match(operation):
                case 'add':
                    cls.user.add(*args)
                case 'remove':
                    cls.user.remove(*args)
                case 'find':
                    result = cls.user.find(*args)
                    if result:
                        print('Found elements:')
                        for element in result:
                            print(element)
                    else:
                        print('No such elements')
                case 'list':
                    lst = cls.user.list()
                    if lst:
                        print(*lst)
                    else:
                        print('Empty list')
                case 'grep':
                    if len(args) == 1:
                        result = cls.user.grep(*args)
                        if result:
                            print('All matches:')
                            for i in result:
                                print(i)
                        else:
                            print('No such elements')
                case 'save':
                    cls.user.save()
                case 'load':
                    cls.user.load()
                case 'switch':
                    if len(args) == 1:
                        cls.user.switch(*args)
                case 'exit':
                    del cls.user
                    return


    @staticmethod
    def parse_command(command):
        command = command.split()
        if not command:
            return None, None
        operation = command[0]
        args = command[1:]

        return operation, args



class UserContainer:
    def __init__(self, username=None):
        self.username = username
        self.container = set()

        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        data_path = os.path.join(path, 'data', f'{username}.txt')

        if os.path.exists(data_path):
            op = input(f'Do you want to load user: {username}?[y/n]: ').lower()
            if op == 'y':
                self.load()
                return

    def __del__(self):
        op = input('Do you want to save current user?[y/n]: ').lower()
        if op == 'y':
            self.save()


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
    
    def save(self):
        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        data_path = os.path.join(path, 'data')
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        data_path = os.path.join(data_path, f'{self.username}.txt')

        with open(data_path,'w+') as file:
            for line in self.container:
                file.write(line + '\n')

    def load(self):
        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        data_path = os.path.join(path, 'data', f'{self.username}.txt')

        if os.path.exists(data_path):

            with open(data_path, 'r') as file:
                text = file.readlines()

                for string in text:
                    self.add(string.strip())

        else:
            print(f'Username {self.username} not found!')

    def switch(self, username):
        abs_file_path = os.path.abspath(__file__)
        path, file_name = os.path.split(abs_file_path)
        data_path = os.path.join(path, 'data', f'{username}.txt')
        if self.username != username:
            op = input('Do you want to save current user?[y/n]: ').lower()

            if op == 'y':
                self.save()
                
            self.container.clear()

            self.username = username

            if os.path.exists(data_path):
                op = input(f'Do you want to load user: {username}?[y/n]: ').lower()

                if op == 'y':
                    self.username = username
                    self.load()


if __name__ == "__main__":
    CLI.interface()

