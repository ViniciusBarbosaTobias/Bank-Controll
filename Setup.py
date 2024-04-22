from Client import Client
from Account import Account


class Main:
    pass

client = Client('adm','114444-2222','111222333-44')
account = Account(client.get_name(),1222)

account.deposit(1000)
account.withdraw(400)
account.extract()
