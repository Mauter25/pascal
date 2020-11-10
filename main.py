class Pascal:
    def __init__(self, list):
        self.list = list

    def __setitem__(self, key, value):
        if len(self.list) >= key:
            self.list[key - 1] = value
        else:
            self.list.append(value)

    def __getitem__(self, item):
        if item > 0:
            return self.list[item-1]
        elif item > len(self.list):
            return KeyError
        elif item > len(self.list):
            return KeyError

    def __str__(self):
        return str(self.list)
