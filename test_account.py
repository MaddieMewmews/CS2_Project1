from account import *
from pytest import *

class Test:
    def setup_method(self):
        self.p1 = Account("Dave Strider")
        self.p2 = Account("John Egbert")

    def test_init(self):
        assert self.p1.get_name() == "Dave Strider"
        assert self.p2.get_name() == "John Egbert"

    def test_deposit(self):
        assert self.p1.deposit(427) is True
        assert self.p1.get_balance() == 427.0
        assert self.p2.deposit(413) is True
        assert self.p2.get_balance() == 413.0

        assert self.p1.deposit(-345) is False
        assert self.p2.deposit(0) is False

    def test_withdraw(self):
        # persist deposits from previous test
        self.test_deposit()

        assert self.p1.withdraw(64) is True
        assert self.p1.get_balance() == 363.0
        assert self.p2.withdraw(80) is True
        assert self.p2.get_balance() == 333.0

        assert self.p1.withdraw(428) is False
        assert self.p2.withdraw(0) is False
        assert self.p1.withdraw(-3) is False
