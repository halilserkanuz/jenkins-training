class Library:
    def __init__(self):
        self.books = []
    def __len__(self):
        return len(self.books)


if __name__ == "__main__":
    library = Library()
    print(len(library)) # 0
    library.books.append("Book 1")
    print(len(library)) # 1