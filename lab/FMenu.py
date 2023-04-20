import os

import keyboard


class FMenu:
    def __init__(self, src="../data/"):
        self.file_list = None
        self.src = src
        self._update_list()
        self.choice_id = 0
        self.choice_status = False
        keyboard.add_hotkey('Escape', lambda: print("script stopped"))
        keyboard.add_hotkey('Return', lambda: self._key_react("enter"))
        keyboard.add_hotkey('Down', lambda: self._key_react("next"))
        keyboard.add_hotkey('Up', lambda: self._key_react("last"))

    def choose_file(self, test=False):
        if not test:
            self._render_menu()
        file_src = self.src + self.file_list[self.choice_id]
        print("chosen file: ", file_src)
        file = open(file_src, mode="r")

        # TODO: here reading logic
        a, b, e = None, None, None
        mass = []
        for line in file.readlines():
            mass = line.split()
            if len(mass) == 3:
                a, b, e = float(mass[0]), float(mass[1]), float(mass[2])
                break
        # END
        file.close()
        keyboard.unhook_all_hotkeys()
        return a, b, e

    def _render_menu(self):
        while not self.choice_status:
            fid = 0
            os.system("cls")  # clear console
            print(self.src)
            for file in self.file_list:  # print the list
                print(">" if (fid == self.choice_id) else " ", end=" ")
                print(file)
                fid += 1
            keyboard.read_key()

    def _update_list(self):
        self.file_list = os.listdir(self.src)

    def _key_react(self, cmd):
        os.system("cls")
        if cmd == "enter":
            keyboard.unhook_all_hotkeys()
            self.choice_status = True
            return
        elif cmd == "next":
            if self.choice_id < len(self.file_list) - 1:
                self.choice_id += 1

        elif cmd == "last":
            if self.choice_id > 0:
                self.choice_id -= 1
