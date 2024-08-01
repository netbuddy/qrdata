from abc import ABC, abstractmethod

#基类
class Logger(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def log(self, msg):
        pass

class GUILogger(Logger):
    def __init__(self, qtextedit):
        super().__init__()
        self.qtextedit = qtextedit
    def log(self, msg):
        self.qtextedit.append(msg)

class CUILogger(Logger):
    def __init__(self):
        super().__init__()
    def log(self, msg):
        print(msg)