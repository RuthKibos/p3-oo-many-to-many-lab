class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name
        self._contracts = []  # Initialize an empty list for contracts
        Author.all.append(self)

    def add_contract(self, contract):
        self._contracts.append(contract)

    def get_contracts(self):
        return self._contracts

    def get_books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        book.add_contract(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        self.title = title
        self._contracts = []  # Initialize an empty list for contracts
        Book.all.append(self)

    def add_contract(self, contract):
        self._contracts.append(contract)

    def get_contracts(self):
        return self._contracts

    def get_authors(self):
        return [contract.author for contract in self._contracts]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        # Add contract to the author's and book's list of contracts
        author.add_contract(self)
        book.add_contract(self)