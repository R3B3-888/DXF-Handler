class City:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def set_path(self, root_path):
        self.path = root_path + "/" + self.name + "/"

    def get_path(self):
        return self.path

    
