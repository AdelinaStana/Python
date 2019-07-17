''' construim proxy virtual
app care tine in obiect setarile programului nume setare - val setare

 proxy     ===========> Setari - string : string
                               - string : string
- set(string, string)
- get(string)
- clone()
- commit()
- rollback()

- recursiv
'''

import copy


class Settings:
    def __init__(self):
        self.attrib = {}

    def set_attrib(self, name, val):
        self.attrib[name] = val

    def get_attrib(self, name):
        if name in self.attrib.keys():
            return self.attrib[name]

    def print(self):
        print(self.attrib)


class Proxy:
    def __init__(self):
        self.current_settings = Settings()
        self.orig_settings = []
        self.clone_command = False

    def set(self, name, val):
        if self.clone_command:
            copy_of_settings = copy.deepcopy(self.current_settings)
            self.orig_settings.append(copy_of_settings)
            self.clone_command = False
        self.current_settings.set_attrib(name, val)

    def get(self, name):
        attrib = self.current_settings.get_attrib(name)
        print(attrib)

    def clone(self):
        self.clone_command = True

    def commit(self):
        if len(self.orig_settings) != 0:
            del self.orig_settings[-1]

    def rollback(self):
        if len(self.orig_settings) != 0:
            self.current_settings = self.orig_settings[-1]
            del self.orig_settings[-1]

    def print_state(self):
        self.current_settings.print()


def main():
    proxy = Proxy()

    proxy.set("attrib1", "1")
    proxy.set("attrib2", "2")
    proxy.print_state()

    proxy.clone()
    proxy.set("attrib3", "3")
    proxy.print_state()

    proxy.clone()
    proxy.set("attrib4", "4")
    proxy.rollback()

    proxy.set("attrib1", "5")
    proxy.commit()
    proxy.print_state()


if __name__ == "__main__":
    main()










