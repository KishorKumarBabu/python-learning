from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    pass
lap=laptop()
lap.process()

# if we create a class laptop it as no method and it inherits computer so it access the process of computer so it is a abstract class so we cannot able to create a object it show an error