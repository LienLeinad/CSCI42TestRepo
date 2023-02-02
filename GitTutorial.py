"""
    Tutorial Python Script to showcase different methods of git workflow with collaborators
    Very basic tutorial on git add, git commit, git push, and git rebase

"""

class Page:
    num_words:int
    def __init__(self, num_words:int = 50):
        self.num_words = num_words
    

class Book:
    page:Page 

    def __init__(self):
        self.page = Page(100)

    def read(self):
        print(self.page.num_words)


class Encyclopedia(Book):
    num_reads:int
    def __init__(self, num_reads=1):
        self.page = Page(1000)
        self.num_reads = num_reads
    def read(self):
        print(self.page.num_words * 2)



def main():
    book = Book()
    encyclopedia = Encyclopedia(2)
    book.read()
    encyclopedia.read()


if __name__ == "__main__":
    main()
