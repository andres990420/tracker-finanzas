class Transaction:

    def __init__(self, transaction_id=None, user_id=None, transaction_type=None,
                 category_id=None, amount=None, transaction_date=None, text_description=None):

        self._transaction_id = transaction_id
        self._user_id = user_id
        self._transaction_type = transaction_type
        self._category_id = category_id
        self._amount = amount
        self._transaction_date = transaction_date
        self._text_description = text_description

    def __str__(self):
        return f''' Transaction id: {self._transaction_id}
                    User id: {self._user_id}
                    Transaction type: {self._transaction_type}
                    Category id: {self._category_id}
                    Amount: {self._amount}
                    Transaction date: {self._transaction_date}
                    Text Description: {self._text_description}
                '''
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self._transaction_type = transaction_type

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self._transaction_date = transaction_date

    @property
    def text_description(self):
        return self._text_description

    @text_description.setter
    def text_description(self, text_description):
        self._text_description = text_description