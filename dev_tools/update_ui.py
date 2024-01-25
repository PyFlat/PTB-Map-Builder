import os
main_win  = open("mainwindow_ui.py", "r").read()
new = main_win[main_win.find("self.actionSave ="):]


main_win_new = open("../src/MainWindow.py", "r+").read()
old = main_win_new[:main_win_new.find("self.actionSave")]
open("../src/MainWindow.py", "w").write(old+new)

os.remove("mainwindow_ui.py")
