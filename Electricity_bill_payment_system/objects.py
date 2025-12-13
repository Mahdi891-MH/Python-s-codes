
class Cust:

    @classmethod
    def customer(cls):
        from customer import Customer
        Customer()


class Mtr:

    @classmethod
    def meter(cls):
        from meter import Meter
        Meter()

class MtrU:

    @classmethod
    def meter_usage(cls):
        from meter_usage import MeterUsage
        MeterUsage()

class Bill:

    @classmethod
    def bill(cls):
        from bill import Bill
        Bill()

class Payment:

    @classmethod
    def payment(cls):
        from payment import Payment
        Payment()