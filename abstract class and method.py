from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
com=computer()
com.process()

# for abstract class we can not able to creat object it show error