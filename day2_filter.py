'''
build push filter
proc(string)

main will build the chain : print filter - upper case filter - print filter - length filter (word <3 ) - print filter
classes:
- print filter
- upper case filter
- length filter
'''


class PrintFilter:
    def __init__(self):
        self.next = None

    def set_next_filter(self, next):
        self.next = next

    def process_string(self, string):
        self.print_string(string)
        return string

    def print_string(self, string):
        print(string)


class UpperCaseFilter(PrintFilter):
    def process_string(self, string):
        string = string.upper()
        return string
        
        
class LengthFilter(PrintFilter):
    def process_string(self, string):
        string = " ".join(word for word in string.split(" ") if len(word) > 3)
        return string


class FilterChain:
    def __init__(self):
        self.root_filter = None

    def add_filter(self, filter):
        if self.root_filter:
            f = self.root_filter
            aux = f
            while f:
                aux = f
                f = f.next
            aux.next = filter
        else:
            self.root_filter = filter

    def process(self, string):
        filter = self.root_filter
        while filter:
            string = filter.process_string(string)
            filter = filter.next


if __name__ == '__main__':
    upc = UpperCaseFilter()
    lf = LengthFilter()
    pf1 = PrintFilter()
    pf2 = PrintFilter()
    pf3 = PrintFilter()

    chain = FilterChain()
    chain.add_filter(pf1)
    chain.add_filter(upc)
    chain.add_filter(pf2)
    chain.add_filter(lf)
    chain.add_filter(pf3)

    chain.process("ana are mere")

    chain.process("ana are pere")




