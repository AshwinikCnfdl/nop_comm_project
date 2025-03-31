from abc import abstractmethod,ABC

class Shoppng_cart(ABC):
    @abstractmethod
    def serach(self):
        pass
    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def reg(self):
        pass

    @abstractmethod
    def cancle(self):
        pass

class Flipkart(Shoppng_cart):
    def serach(self):
        print("u can search a product ")

    def order(self):
        print("u can order")

    def login(self):
        print("u can login")


    def reg(self):
        print("u can reg")


    def cancle(self):
        print("u can cancel")

f = Flipkart()
f.serach()
f.order()
f.reg()
f.cancle()
