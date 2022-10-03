class LimitGroupError(Exception):

    def __init__(self, value=None, msg=None):
        super().__init__()
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'Current Limit in Group = {self.value}\n{self.msg}'
