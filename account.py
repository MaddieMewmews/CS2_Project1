class Account:
    def __init__(self, name) -> None:
        """
        Initialization function for Account class
        :param name: account name
        """
        self.__account_name = f"{name}"
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        '''
        Function to deposit money into account
        :param amount: Amount to add to account balance
        :return: Success boolean
        '''
        if (amount <= 0):
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount) -> bool:
        '''
        Function to withdraw money from account
        :param amount: Amount to subtract to account balance
        :return: Success boolean
        '''
        if (amount <= 0) or (amount > self.__account_balance):
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to return account balance value
        :return: Balance value guaranteed as float
        """
        return float(self.__account_balance)

    def get_name(self) -> str:
        """
        Method to return the account name as string
        :return: Account name value
        """
        return self.__account_name
