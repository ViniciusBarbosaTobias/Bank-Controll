from Client import Client
from Account import Account


class Main:
    pass

client = Client('Vinicius','1146184113','48024509822')
account = Account(client.get_name(),1222)

account.deposit(1000)
account.withdraw(400)
account.extract()
