from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class desktop(computer):
    def process(self):
        print("in process")
class programer:
    def work(self,com):
        print("solving bugs")
        com.process()
lap=laptop()
des=desktop()
pro=programer()
pro.work(des)
pro.work(lap)
