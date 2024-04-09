from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
lap=laptop()
lap.process()
# now we created a method for laptop it does not show error