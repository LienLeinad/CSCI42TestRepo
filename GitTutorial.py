"""
    Tutorial Python Script to showcase different methods of git workflow with collaborators
    Very basic tutorial on git add, git commit, git push, and git rebase

"""
import abc
class Reader(abc.ABC):
    @abc.abstractmethod
    def get_num_words(self) -> int:
        """ returns num words attribute"""
        

class Page(Reader):
    word_num:int
    def __init__(self, num_words:int = 50):
        self.word_num = num_words
        
    def get_num_words(self):
        return self.word_num

class Book:
    page:Page 
    def __init__(self):
        self.page = Page(100)

    def read(self) -> int:
        print(self.page.get_num_words())


class Encyclopedia(Book):
    num_reads:int
    def __init__(self, num_reads=1):
        self.page = Page(1000)
        self.num_reads = num_reads
    def read(self):
        print(self.page.get_num_words() * 2)



def main():
    book = Book()
    encyclopedia = Encyclopedia(2)
    book.read()
    encyclopedia.read()


if __name__ == "__main__":
    main()
