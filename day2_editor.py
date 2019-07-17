'''
text editor -> apply command
commands -> insert(poz), overwrite(poz)
implement undo, redo
'''


class Command:
    def __init__(self, pos, string):
        self.pos = pos
        self.string = string


class Overwrite(Command):
    def __init__(self, pos, string):
        super().__init__(pos, string)
        self.replaced = ""

    def execute(self, text):
        l = len(self.string)
        self.replaced = text[self.pos:l+1]
        text = text[:self.pos] + self.string + text[self.pos+l:]
        return text

    def revert(self, text):
        l = len(self.string)
        text = text[0:self.pos] + self.replaced +  text[self.pos + l:]
        return text


class Insert(Command):

    def execute(self, text):
        text = text[0:self.pos] + self.string + text[self.pos:]
        return text

    def revert(self, text):
        l = len(self.string)
        text = text[0:self.pos] + text[self.pos + l:]
        return text


class EditorText:
    def __init__(self, text):
        self.actions = {}
        self.text = text

    def set_text(self, text):
        self.text = text

    def insert(self, pos, string):
        self.clean()
        i = Insert(pos - 1, string)
        self.text = i.execute(self.text)
        self.actions[i] = True

    def overwrite(self, pos, string):
        self.clean()
        o = Overwrite(pos - 1, string)
        self.text = o.execute(self.text)
        self.actions[o] = True

    def get_last_active_command(self):
        active_cmd = [key for key in self.actions.keys() if self.actions[key]]
        if len(active_cmd) != 0:
            return active_cmd[-1]
        return None

    def get_first_inactive_command(self):
        inactive_cmd = [key for key in self.actions.keys() if not self.actions[key]]
        if len(inactive_cmd) != 0:
            return inactive_cmd[0]
        return None

    def undo(self):
        action = self.get_last_active_command()

        if action:
            self.text = action.revert(self.text)
            self.actions[action] = False
        else:
            print("Cannot undo anymore!")

    def redo(self):
        action = self.get_first_inactive_command()

        if action:
            self.text = action.execute(self.text)
            self.actions[action] = True
        else:
            print("Cannot redo anymore!")

    def clean(self):
        keys_list = [key for key in self.actions.keys() if self.actions[key] == False]

        for key in keys_list:
            del self.actions[key]

    def display(self):
        print(self.text)


if __name__ == '__main__':
    editor = EditorText("bla bla blu")

    editor.display()
    editor.insert(5, "casa")
    editor.display()
    editor.overwrite(2, "pom")
    editor.display()

    editor.undo()
    editor.display()

    editor.undo()
    editor.display()

    editor.redo()
    editor.display()

    editor.insert(5, "casa")
    editor.display()

    editor.undo()
    editor.display()

    editor.undo()
    editor.display()

    editor.undo()


