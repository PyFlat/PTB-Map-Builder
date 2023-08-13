import sys

from MainWindow import Ui_MainWindow
from CustomSyntaxHighlighter import CustomSyntaxHighlighter
from src.CustomTextEdit import CustomTextEdit
sys.dont_write_bytecode = True
from tkinter import *
from tkinter import messagebox, filedialog
from functools import partial
from PtbLoad import PtbLoad
from compiler import *
from compressor import *
import pathlib, os

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import src.KEYWORDS

# class Window():
#     def __init__(self, width, height):
#         self.master = Tk()
#         self.master.geometry(str(width)+"x"+str(height))
#         self.master.resizable(width=0, height=0)
# class MainDisplay():
#     def __init__(self, block_manager):
#         self.bm = block_manager
#         self.window = Window(580, 500)
#         self.master = self.window.master
#         self.top = None
#         self.active = True
#         self.w = Canvas(self.master, highlightthickness=0)
#         self.w.pack()
#         self.w.place(x=80, y=0, width=500, height=500)
#         self.path = str(pathlib.Path(__file__).parent.absolute()) + "/textures/"
#         self.files = os.listdir(self.path)
#         self.addpath = "textures/"
#         f = Button(self.master, bg = "blue", command=partial(self.bm.load_from_json))
#         f.place(x=15, y=430, width=20, height=20) 
#         l = Button(self.master, bg = "orange", command=partial(self.bm.set_texture, -1))
#         l.place(x=15, y=460, width=20, height=20)
#         l.bind("<Button-3>", lambda ev: self.bm.set_texture(-1, False))
#         c = Button(self.master, bg = "red", command=partial(self.bm.reset))
#         c.place(x=45, y=460, width=20, height=20)
#         editor = Button(self.master, text="Scripts", bg="black", fg="white", command=partial(Script_Editor, self.bm))
#         editor.place(x=15, y=370, width=50, height=20)
#         editor = Button(self.master, text="Texts", bg="black", fg="white", command=partial(Text_Editor, self.bm))
#         editor.place(x=15, y=340, width=50, height=20)
#         save = Button(self.master, bg = "green", command=partial(self.bm.save_to_file))
#         save.place(x=45, y=430, width=20, height=20)
#         self.bl = Button(self.master, bg="white", border = 0)
#         self.bl.place(x=15, y=400, width=20, height=20)
#         self.br = Button(self.master, bg="white", border = 0)
#         self.br.place(x=45, y=400, width=20, height=20)
#         self.load_images_background()
#         self.create_buttons()
#         self.master.protocol("WM_DELETE_WINDOW", self.on_close)
#     def load_images_background(self):
#         for i in range(0, len(self.files)):
#             self.bm.textures.append(PhotoImage(file=self.addpath + self.files[i]))
#         for i in range(23):
#             for j in range(23):
#                 if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
#                     self.w.create_image((i+1)*20+10, (j+1)*20+10, image = self.bm.textures[14])
#                 else:
#                     self.w.create_image((i+1)*20+10, (j+1)*20+10, image = self.bm.textures[15])
#     def create_buttons(self):
#         for i in range(len(self.bm.textures)-2):
#             l = Button(self.master, image=self.bm.textures[i], border=1,command=partial(self.bm.set_texture, i))
#             l.bind("<Button-3>", partial(self.bm.set_texture, i, False))
#             if i %2==0:
#                 x=15
#                 l.place(x=x, y=(i*20)+20, width=20, height=20)
#             else:
#                 x=45
#                 l.place(x=x, y=(i*20), width=20, height=20)
#             if i == 10:
#                 l.bind("<Shift-Button-1>", lambda ev: Enemy_Editor(True))
#     def place_bedrock(self):
#         self.bm.set_texture(1)
#         for i in range(25):
#             self.bm.place(i, 0)
#             self.bm.place(0,i)
#             self.bm.place(24,i)
#             self.bm.place(i, 24)
#         self.bm.set_texture(-1)
#     def bind_buttons(self):
#         self.master.bind("<space>", lambda ev: self.bm.start_move())
#         self.master.bind("<KeyRelease-space>", lambda ev: self.bm.stop_move())
#         self.master.bind("<Control-Button-1>", lambda ev: self.bm.update_line(start=True))
#         self.master.bind("<Control-Button-3>", lambda ev: self.bm.update_line(False, start=True))
#         self.master.bind("<Control-B1-Motion>", lambda ev: self.bm.update_line())
#         self.master.bind("<Control-B3-Motion>", lambda ev: self.bm.update_line(False))
#         self.master.bind("<Control-B1-KeyRelease>", lambda ev: self.bm.update_line(fin=True))
#         self.master.bind("<Control-B3-KeyRelease>", lambda ev: self.bm.update_line(False,fin=True))
#         self.master.bind("<Alt-Button-1>", lambda ev: self.bm.update_box(start=True))
#         self.master.bind("<Alt-Button-3>", lambda ev: self.bm.update_box(False, start=True))
#         self.master.bind("<Alt-B1-Motion>", lambda ev: self.bm.update_box())
#         self.master.bind("<Alt-B3-Motion>", lambda ev: self.bm.update_box(False))
#         self.master.bind("<ButtonRelease-1>", lambda ev: [self.bm.update_box(fin=True),self.bm.update_line(fin=True)])
#         self.master.bind("<ButtonRelease-3>", lambda ev: [self.bm.update_box(False,fin=True), self.bm.update_line(False,fin=True)])
#         self.master.bind("<Alt-B1-KeyRelease>", lambda ev: self.bm.update_box(fin=True))
#         self.master.bind("<Alt-B3-KeyRelease>", lambda ev: self.bm.update_box(False,fin=True))
#         self.master.bind("<B1-Motion>", lambda ev: self.bm.place(-1,-1, True))
#         self.master.bind("<B3-Motion>", lambda ev: self.bm.place(-1,-1, False))
#         self.master.bind("<ButtonPress-1>", lambda ev: [self.bm.save(),self.bm.place(-1,-1, True)])
#         self.master.bind("<ButtonPress-3>", lambda ev: [self.bm.save(),self.bm.place(-1,-1, False)])
#         self.master.bind("<Control-z>", lambda ev: self.bm.load())
#         self.master.bind("<Shift-Button-1>", lambda ev: [Enemy_Editor(False), self.bm.save()])
#         self.master.bind("<Control-B1-KeyPress>", lambda ev: self.bm.save())
#         self.master.bind("<Control-B3-KeyPress>", lambda ev: self.bm.save())
#         self.master.bind("<Alt-B1-KeyPress>", lambda ev: self.bm.save())
#         self.master.bind("<Alt-B3-KeyPress>", lambda ev: self.bm.save())
#     def update_frame(self):
#         if self.bm.get_texture() < 0:
#             self.bl.config(bg="white", image ="")
#         else:
#             self.bl.config(image=self.bm.textures[self.bm.get_texture()])
#         if self.bm.get_texture(False) < 0:
#             self.br.config(bg="white", image="")
#         else:
#             self.br.config(image=self.bm.textures[self.bm.get_texture(False)])
#     def mainloop(self):
#         while self.active:
#             for block in self.bm.update_list:
#                 block.move(1)
#             x, y = self.bm.get_pos()
#             self.master.title(f"PTB-Map-Builder | (x: {x}, y: {y})")
#             self.update_frame()
#             self.master.update()
#             self.master.update_idletasks()
#     def on_close(self):
#         self.active = False
#         self.master.quit()
#         self.master.destroy()
# class BlockManager():
#     def __init__(self):
#         self.update_list = []
#         self.texts = None
#         self.scripts = None
#         self.texture_left = -1
#         self.texture_right = -1
#         self.textures = []
#         self.blocks = [[None for i in range(25)] for j in range(25)]
#         self.last_blocks = []
#         self.enemy_damage = 1
#         self.enemy_health = 1
#         self.line_x = None
#         self.line_y = None
#         self.line_images = []
#         self.move_x_s = self.move_y_s = None
#         self.mouse_x = None
#         self.mouse_y = None
#         self.mobj = None
#         self.x_stable = None
#         self.check_x = True
#         self.check_y = True
#         self.box_x = None
#         self.box_y = None
#         self.comp = compiler()
#     def get_texture(self, side = True):
#         tex = self.texture_left if side else self.texture_right
#         return tex
#     def set_texture(self, tex, side = True, *args):
#         self.texture_left, self.texture_right = (tex, self.texture_right) if side else (self.texture_left, tex)
#     def reset(self):
#         self.texts = self.scripts = None
#         for i in range(23):
#             for j in range(23):
#                 if self.blocks[i+1][j+1] != None:
#                     self.delete(i+1, j+1)
#         self.set_texture(-1);self.set_texture(-1, False)
#     def delete(self, x, y, item = None):
#         if item is None: md.w.delete(self.blocks[x][y].obj); self.blocks[x][y] = None
#         else: md.w.delete(item)
#     def get_pos(self):
#         abs_x = md.master.winfo_pointerx() - md.master.winfo_rootx()
#         abs_y = md.master.winfo_pointery() - md.master.winfo_rooty()
#         self.num_x =abs_x//20-4
#         self.num_y = abs_y//20
#         return [self.num_x, self.num_y]

#     def place(self, x, y, dire = True):
#         num_x, num_y = self.get_pos()
#         if x >= 0:
#             num_x = x
#         if y >= 0:
#             num_y = y
#         if (num_x > 23 or num_x < 1 or num_y < 1 or num_y > 23) and not (num_x == x and num_y== y): return
#         if self.blocks[num_x][num_y]:self.delete(num_x, num_y)
#         texture = self.get_texture(dire)
#         if texture == 0:
#             for i, j in [(i, j) for i in range(25) for j in range(25) if self.blocks[i][j] and self.blocks[i][j].texture == 0]:
#                 self.delete(i, j)
#         elif texture < 0:
#             return
#         if self.blocks[num_x][num_y]:
#             self.delete(num_x, num_y)
#         b = Block(num_x * 20 + 10, num_y * 20 + 10, dire)
#         self.blocks[num_x][num_y] = b
#         del b

#     def start_move(self):
#         x,y = self.get_pos()
#         if self.move_x_s == None or self.move_y_s == None:
#             self.move_x_s = x
#             self.move_y_s = y
#         else:
#             if self.mobj == None:
#                 if self.blocks[self.move_x_s][self.move_y_s] != None:
#                     tex = self.blocks[self.move_x_s][self.move_y_s].get_block()
#                     self.mobj = md.w.create_image(x*20+10,y*20+10,image=self.textures[tex])
#             else:
#                 md.w.moveto(self.mobj,x*20,y*20)
#     def stop_move(self):
#         x,y = self.get_pos()
#         b = self.blocks[self.move_x_s][self.move_y_s]
#         if b == None:
#             self.move_x_s = None
#             self.move_x_s = None
#             md.w.delete(self.mobj)
#             self.mobj = None
#             return
#         if x > 23 or x < 1 or y < 1 or y > 23:
#             return
#         oblock = self.blocks[self.move_x_s][self.move_y_s]
#         otex = self.get_texture()
#         ntex = oblock.get_block()
#         self.delete(self.move_x_s, self.move_y_s)
#         enemy = oblock.get_enemy()
#         self.set_texture(ntex)
#         self.place(-1,-1)
#         if enemy != None:
#             self.blocks[x][y].health = enemy[0]
#             self.blocks[x][y].damage = enemy[1]
#         self.set_texture(otex, True)
#         self.move_x_s = None
#         self.move_x_s = None
#         md.w.delete(self.mobj)
#         self.mobj = None

#     def update_box(self, dire=True, fin=False, start=False):
#         if start and self.get_texture(dire) != 0:
#             self.box_x, self.box_y = self.get_pos()
#         if self.box_x == None or self.box_y == None:
#             return
#         x,y = self.get_pos()
#         difference_x = x-self.box_x
#         difference_y = y-self.box_y
#         if self.box_x == x and self.box_y == y:
#             return
#         while len(self.line_images) > 0:
#             md.w.delete(self.line_images.pop(0))
#         difference_x = 1 if difference_x == 0 else difference_x
#         difference_y = 1 if difference_y == 0 else difference_y
#         stepx = int(difference_x/abs(difference_x))
#         stepy = int(difference_y/abs(difference_y))
#         for i in range(self.box_x, x+stepx, stepx):
#             for j in range(self.box_y, y+stepy, stepy):
#                 if i <= 0 or i >= 24 or j <= 0 or j >= 24:
#                     break
#                 if fin:
#                     self.place(i, j, dire)
#                 else:
#                     texture = self.get_texture(dire)
#                     if texture == -1:
#                         is_even = (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)
#                         texture = 14 if is_even else 15
#                     self.line_images.append(md.w.create_image(i * 20 + 10, j * 20 + 10, image=self.textures[texture]))
#         if fin:
#             self.box_x = self.box_y = None
#     def update_line(self, dire=True, fin=False, start=False):
#         if start and self.get_texture(dire) != 0:
#             self.line_x,self.line_y = self.get_pos()
#             self.update_line(dire, fin)
#         if self.line_x == None or self.line_y == None: return
#         x,y = self.get_pos()
#         difference_x = x-self.line_x
#         difference_y = y-self.line_y
#         if self.line_x == x and self.line_y == y: return 
#         elif (x != self.line_x and self.x_stable == None) or (self.check_x and self.x_stable != None):
#             self.check_y, self.x_stable, difference, line, xy = False, False, difference_x, self.line_x, x
#         elif (y != self.line_y and self.x_stable == None) or (self.check_y and self.x_stable != None):
#             self.check_x, self.x_stable, difference, line, xy = False, True, difference_y, self.line_y, y
#         while len(self.line_images) > 0:
#             md.w.delete(self.line_images.pop(0))
#         difference = 1 if difference == 0 else difference
#         step = int(difference/abs(difference))
#         if xy + step - line == 1:
#             self.x_stable, self.check_x, self.check_y = None, True, True
#             self.update_line(dire, fin)
#             return
#         for i in range(line, xy+step, step):
#             x = self.line_x if self.x_stable else i
#             y = i if self.x_stable else self.line_y
#             if x <= 0 or x >= 24 or y <= 0 or y >= 24:
#                 break
#             elif fin:
#                 self.place(x, y, dire)
#             else:
#                 texture = self.get_texture(dire)
#                 if texture == -1:
#                     is_even = (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0)
#                     texture = 14 if is_even else 15
#                 self.line_images.append(md.w.create_image(x * 20 + 10, y * 20 + 10, image=self.textures[texture]))
#         if fin:
#             self.x_stable = self.line_x = None
#             self.check_x = self.check_y = True
#     def save(self):
#         self.last_blocks = []
#         for x in range(len(self.blocks)):
#             temp = []
#             for elem in self.blocks[x]:
#                 temp.append(elem)
#             self.last_blocks.append(temp)
#         self.last_texture = self.get_texture()
#     def load(self):
#         self.reset()
#         for i in range(25):
#             for j in range(25):
#                 if self.last_blocks[i][j]:
#                     self.set_texture(self.last_blocks[i][j].texture)
#                     self.place(i,j)
#                     if self.get_texture() == 10:
#                         self.blocks[i][j].damage = self.last_blocks[i][j].damage
#                         self.blocks[i][j].health = self.last_blocks[i][j].health
#         self.set_texture(self.last_texture)
#     def get_path(self, fileopen = False):
#         if fileopen:
#             path = filedialog.askopenfilename(title="Choose a PTB or JSON file to load", initialdir="~/Downloads/", filetypes = [("PTB save files", "*.ptb"),("*Old* json save files","*.json")])
#         else:
#             path = filedialog.asksaveasfilename(defaultextension=".ptb", title="Choose a Place to Save your Map", initialdir="~/Downloads/", filetypes = [("PTB save files", "*.ptb")])
#         if path == None or ((path[-4:] == ".ptb") or ((path[-5:] == ".json") and fileopen)):
#             return path
#         elif path == "":
#             return None
#         messagebox.showerror("Error", "False File Format")
#         return None
#     def load_from_json(self):
#         path = self.get_path(fileopen = True)
#         if path == None:
#             return
#         self.reset()
#         if path[-4:] == ".ptb":
#             out = ptbload.load_ptb(path)
#             self.scripts = self.comp.decompile(out[1])
#         elif path[-5:] == ".json":
#             out = jsonload.load_json(path)
#         new_blocks = out[0]
#         self.texts = out[2]
#         for i in range(25):
#             for j in range(25):
#                 if new_blocks[i][j] == None:
#                     self.blocks[i][j] = None
#                 elif isinstance(new_blocks[i][j], list):
#                     block = new_blocks[i][j]
#                     self.set_texture(block[0])
#                     self.place(i,j)
#                     self.blocks[i][j].health = block[1]
#                     self.blocks[i][j].damage = block[2]
#                 else:
#                     self.set_texture(new_blocks[i][j])
#                     self.place(i,j)
#         self.set_texture(-1, True)
#     def get_json_block_data(self):
#         block_list = []
#         for i in range(25):
#             temp = []
#             for j in range(25):
#                 block = self.blocks[i][j]
#                 texture = block.texture if block != None else None
#                 ids = {4: 450, 5: 700, 6: 900, 7: 20, 8: 150, 9: 55, 11: 80, 12: 0, 13: 260}
#                 if block is None:
#                     temp.append({"id": -1, "objectData": {}})
#                 elif texture == 10:
#                     health, mode = block.get_enemy()
#                     temp.append({"id": 6, "objectData": {"health": health, "id2": mode, "id1": 1}})
#                 elif texture in ids:
#                     start = ids[texture]
#                     temp.append({"id": 5, "objectData": {"start": start, "fin": start}})
#                 elif texture == 3:
#                     temp.append({"id": 3, "objectData": {}})
#                 elif texture == 2:
#                     temp.append({"id": 4, "objectData": {}})
#                 elif texture == 1:
#                     temp.append({"id": 0, "objectData": {}})
#                 elif texture == 0:
#                     temp.append({"id": 2, "objectData": {}})
#             block_list.append(temp)
#         return block_list
#     def check_for_player(self):
#         for i in range(25):
#             for j in range(25):
#                 if self.blocks[i][j] and self.blocks[i][j].texture == 0: return True
#         return False
#     def get_info(self):
#         dict = {
#                 "enemys": {
#                     "damage": [],
#                     "no-damage": []
#                 },
#                 "items": {
#                     "bombs": 0,
#                     "exp": 0,
#                     "dynamite": 0,
#                     "time_bombs": 0,
#                     "nukes": 0,
#                     "health": 0,
#                     "damage": 0,
#                 },
#                 "blocks": 0
#                 }
#         for row in self.blocks:
#             for block in row:
#                 if not block: continue
#                 match block.texture:
#                     case 10: dict["enemys"]["no-damage" if block.damage == 2 else "damage"].append(block.health)
#                     case 3: dict["blocks"] += 1
#                     case 4: dict["items"]["bombs"] += 1
#                     case 5: dict["items"]["exp"] += 1
#                     case 7: dict["items"]["dynamite"] += 1
#                     case 8: dict["items"]["time_bombs"] += 1
#                     case 9: dict["items"]["health"] += 1
#                     case 11: dict["items"]["damage"] += 1
#                     case 12: dict["items"]["nukes"] += 1
#         return dict
    
#     def save_to_file(self):
#         if not self.check_for_player(): messagebox.showerror("ERROR", "Player is missing"); return
#         path = self.get_path()
#         if path == None:
#             return
#         block_list = self.get_json_block_data()
#         info = self.get_info()
#         World = {"world":block_list}
#         if self.scripts != None:
#             script = self.comp.compile(self.scripts)
#         else:
#             script = None
#         if self.texts != None:
#             texts = self.texts[:-1]
#         else:
#             texts = None
#         com = compressor()
#         com.insert_normal(World, script, texts)
#         com.compress()
#         com.save(path)
# class Script_Editor():
#     running = False
#     def __init__(self, blocks):
#         self.bm = blocks
#         self.current_word = ""
#         self.autocomplete_list = []
#         self.autocomplete_index = 0
#         if Script_Editor.running: return
#         Script_Editor.running = True
#         self.window = Window(600, 600)
#         self.window.master.config(bg="#3c3c3c")
#         self.window.master.title("Scripts")
#         self.textfeld = Text(self.window.master, relief="flat", font="Calibri 20", bg="#1f1f1f", fg="white", insertbackground="white", undo=True)
#         self.textfeld.place(x=25, y=25, height=525, width=550)
#         self.textfeld.bind("<KeyRelease>", self.highlight_syntax)
#         self.textfeld.bind("<Control-BackSpace>", self.delete_whole_word)
#         self.textfeld.bind("<Tab>", self.on_tab_press)
#         self.textfeld.bind("<Down>", self.on_down_press)
#         self.textfeld.bind("<Up>", self.on_up_press)
#         if self.bm.scripts != None:
#             self.textfeld.insert("1.0",self.bm.scripts)
#         self.highlight_syntax()
#         self.submit = Button(self.window.master,relief="flat", text="Submit",bg="orange",fg="white", font="Calibri 20", activeforeground="orange", activebackground="white", border = 0, command=lambda:[self.compile_text(),self.destroy()])
#         self.submit.place(x=200, y=560, height=30, width=200)
#         self.window.master.protocol("WM_DELETE_WINDOW", self.destroy)
        
        
#     def check_autofill(self, event):
#         if event:
#             if event.keysym == "BackSpace":
#                 return
#         self.update_autocomplete_list()
#         if self.autocomplete_list:
#             if len(event.keysym) == 1:
#                 self.show_autocomplete_text()

#     def on_tab_press(self, event):
#         if self.autocomplete_list:
#             self.remove_autocomplete_text()
#             cursor_position = float(self.textfeld.index(INSERT))
#             start = cursor_position-(len(self.current_word)/10)
#             if start < 1: start = 1.0
#             end = start+len(self.autocomplete_list[self.autocomplete_index])/10
#             self.textfeld.mark_set(INSERT, end)
#             return "break"

#     def on_down_press(self, event):
#         if self.autocomplete_list:
#             self.autocomplete_index = (self.autocomplete_index + 1) % len(self.autocomplete_list)
#             self.show_autocomplete_text()

#     def on_up_press(self, event):
#         if self.autocomplete_list:
#             self.autocomplete_index = (self.autocomplete_index - 1) % len(self.autocomplete_list)
#             self.show_autocomplete_text()

#     def update_autocomplete_list(self):
#         current_word = self.get_current_word()
#         if current_word != self.current_word and len(current_word)>0:
#             self.current_word = current_word
#             self.autocomplete_list = self.get_autocomplete_list(self.current_word)

#     def get_current_word(self):
#         cursor_position = self.textfeld.index(INSERT)
#         line, col = map(int, cursor_position.split('.'))
#         current_line_text = self.textfeld.get(f"{line}.0", f"{line}.end")
#         words = current_line_text.split()
#         if words:
#             current_word = words[min(col - 1, len(words) - 1)]
#             return current_word
#         return ""

#     def get_autocomplete_list(self, partial_word):
#         autocomplete_list = []
#         for keyword_set in self.keywords:
#             for keyword in keyword_set["keywords"]:
#                 if keyword.startswith(partial_word):
#                     autocomplete_list.append(keyword)
#         return autocomplete_list

#     def show_autocomplete_text(self):
#         if self.autocomplete_list:
#             cursor_position = self.textfeld.index(INSERT)
#             options_text = self.autocomplete_list[self.autocomplete_index][len(self.current_word):]
#             self.textfeld.insert(INSERT, options_text)
#             self.textfeld.tag_add("sel", "insert - %dc" % len(options_text), INSERT)
#             self.textfeld.mark_set(INSERT, cursor_position)

#     def remove_autocomplete_text(self):
#         self.textfeld.tag_remove("sel", "1.0", "end")

        
#     def highlight_syntax(self, event=None):
#         self.keywords = [
#             {"keywords" : ['on_init', 'on_collect', 'on_step', 'on_explode', "on_destroy", "on_tick"],
#             "color": "#dcdcaa",
#             "name": "trigger"
#             },
#             {"keywords" : ['@', "end", "win", "loose", "add", "subtract", "multiply", "divide", "set", "reset", "store", "set_item", "drawImage", "drawRect", "clear", "compare", "jump", "setFlag", "tp", "jumpRelative", "createMemory", "loadToMemory", "loadFromMemory", "randomNumber", "loadFromPointer"],
#             "color": "#2667ca",
#             "name": "commands"
#             },
#             {"keywords" : ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
#             "color": "#a7ce9b",
#             "name": "number"
#             },
#             {"keywords" : ['=>', "="],
#             "color": "#9cdcfe",
#             "name": "variables"
#             },
#             {"keywords": ["player.health", "player.bombs", "player.range", "player.dynamite", "player.timed_bombs", "player.damage", "player.nukes",],
#             "color": "#c3602d",
#             "name": "player_set"}
#         ]
#         #self.check_autofill(event)
#         self.remove_all_highlights(event)
#         for key in self.keywords:
#             self.apply_highlight(key["name"], key["keywords"], key["color"])

#     def remove_all_highlights(self, event=None):
#         if event and "Shift" in event.keysym:
#             return
#         for tag in self.textfeld.tag_names():
#             if tag != "sel":
#                 self.textfeld.tag_remove(tag, '1.0', END)

#     def apply_highlight(self, name, keywords, color):
#         self.textfeld.tag_configure(name, foreground=color)
#         for keyword in keywords:
#             start = '1.0'
#             while True:
#                 pos = self.textfeld.search(keyword, start, stopindex=END)
#                 if not pos:
#                     break
#                 next_char = self.textfeld.get(f'{pos}+{len(keyword)}c')
#                 if next_char == " " or next_char == "\n":
#                     end = f'{pos}+{len(keyword)}c'
#                     self.textfeld.tag_add(name, pos, end)
#                 start = f'{pos}+1c'
                
#     def delete_whole_word(self, event):
#         cursor_position = self.textfeld.index(INSERT)

#         start_index = self.textfeld.search(r'\s', cursor_position, backwards=True, regexp=True, stopindex="1.0")
#         if not start_index:
#             start_index = "1.0"
#         self.textfeld.delete(start_index, cursor_position)

#     def apply_highlight(self, name, keywords, color):
#         self.textfeld.tag_configure(name, foreground=color)
#         for keyword in keywords:
#             start = '1.0'
#             while True:
#                 pos = self.textfeld.search(keyword, start, stopindex=END)
#                 if not pos:
#                     break
#                 next_char = self.textfeld.get(f'{pos}+{len(keyword)}c')
#                 if next_char == " " or next_char == "\n":
#                     end = f'{pos}+{len(keyword)}c'
#                     self.textfeld.tag_add(name, pos, end)
#                 start = f'{pos}+1c'
                

#     def compile_text(self):
#         self.bm.scripts = self.textfeld.get("1.0",END)
#         try: 
#             self.bm.comp.compile(self.bm.scripts)
#         except compilerError as e:
#             line, x, y = e.get()
#             print(line, x,y)
#     def destroy(self):
#         self.window.master.destroy()
#         self.window.master.quit()
#         Script_Editor.running = False
        
# class Text_Editor():
#     running = False
#     def __init__(self, blocks):
#         self.bm = blocks
#         if Text_Editor.running: return
#         Text_Editor.running = True
#         self.window = Window(600, 600)
#         self.window.master.config(bg="#3c3c3c")
#         self.window.master.title("Texts")
#         self.textfeld = Text(self.window.master, relief="flat", font="Calibri 20")
#         self.textfeld.place(x=25, y=25, height=525, width=550)
#         if self.bm.texts != None:
#             text = self.bm.texts
#             text = "\n".join(text)
#             self.textfeld.insert("1.0",text)
#         self.submit = Button(self.window.master,relief="flat", text="Submit",bg="orange",fg="white", font="Calibri 20", activeforeground="orange", activebackground="white", border = 0, command=lambda:[self.destroy()])
#         self.submit.place(x=200, y=560, height=30, width=200)
#         self.window.master.protocol("WM_DELETE_WINDOW", self.destroy)
#     def destroy(self):
#         self.bm.texts = self.textfeld.get("1.0",END)
#         self.window.master.destroy()
#         self.window.master.quit()
#         Text_Editor.running = False
# class Enemy_Editor():
#     running = False
#     def __init__(self, gen):
#         self.general = gen
#         self.pos_x, self.pos_y = bm.get_pos()
#         self.block = bm.blocks[self.pos_x][self.pos_y]
#         if ((self.block == None or self.block.edit == False) and (self.general == False)) or Enemy_Editor.running:
#             return
#         Enemy_Editor.running = True
#         self.enem_win = Window(250, 150)
#         self.enem_win.master.protocol("WM_DELETE_WINDOW", partial(self.destroy, self.enem_win))
#         self.l1 = Label(self.enem_win.master, text="Health:", justify="center", font="Calibri 15")
#         self.l1.place(x=0, y=0, width=250)
#         self.e1 = Entry(self.enem_win.master)
#         self.e1.place(x=0,y=35,width=250)
#         self.l2 = Label(self.enem_win.master, text="Damage:", justify="center", font="Calibri 15")
#         self.l2.place(x=0, y=60, width=250)
#         self.var = IntVar(self.enem_win.master)
#         self.b1 = Button(self.enem_win.master, text="Save", font="Calibri 15", command=lambda:[self.set_value()])
#         self.b1.place(x=0, y=125, width= 250, height=25)
#         self.radio_1  = Radiobutton(self.enem_win.master, text="OFF", variable=self.var, value=1)
#         self.radio_1.place(x=0, y=95, width=125)
#         self.radio_2 = Radiobutton(self.enem_win.master, text="ON", variable=self.var, value=2)
#         self.radio_2.place(x=125, y=95, width=125)
#         if not self.general:
#             self.var.set(self.block.damage)
#             self.set_health(self.block.health)
#         else:
#             self.var.set(bm.enemy_damage)
#             self.set_health(bm.enemy_health)
#     def set_health(self, health):
#         self.e1.delete(1)
#         self.e1.insert(1, health)
#     def set_value(self):
#         health = self.e1.get()
#         if not health.isdigit() or int(health) <= 0:
#             health = 1
#         else:
#             health = int(health)
#         if self.general:
#             bm.enemy_damage = self.var.get()
#             bm.enemy_health = health
#         else:
#             bm.blocks[self.pos_x][self.pos_y].damage = self.var.get()
#             bm.blocks[self.pos_x][self.pos_y].health = health
#         self.destroy()
#     def destroy(self, *args):
#         Enemy_Editor.running = False
#         self.enem_win.master.destroy()
        
class Utils():
    def get_abs_path(relative_path):
        base_path = getattr(sys,'_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_path, relative_path).replace("\\", "/")
        return path

class MainWindow(QMainWindow):
    coord_signal = Signal(int, int)
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow() # Setup the Ui from the Designer
        self.ui.setupUi(self)
        
        self.connect_menu()
        
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.prev_page_btn.setDisabled(True)
        
        self.setStyleSheet(open(Utils.get_abs_path("style.qss"), "r").read())
        
        self.textures = self.load_textures() # Load All Textures
        
        self.blocks = [[None for i in range(25)] for j in range(25)]
        
        self.texture_left = 0
        self.texture_right = 0
        
        self.enemy_damage = 1
        self.enemy_health = 1
        
        self.player = None
        
        self.scripts = None
        self.texts = None
        
        self.comp = compiler()
        
        self.build_background() # Create The Grass Background
        
        self.build_border() # Create the Endstone Border
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_title) # Update the title to the current mouse pos
        self.timer.start(10)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_current_block)
        self.timer2.start(25)
        self.drawing = False
        self.ui.imagePainter.mousePressEvent = self.mouse_click_event # Bind the Mouse Click
        self.ui.imagePainter.mouseMoveEvent = self.mouseMove # Bind Mouse Move
        self.ui.imagePainter.mouseReleaseEvent = self.mouseRelease # Bind Mouse Release
        
        for i in range(len(self.textures)-1):
            button = getattr(self.ui, f"block_button_{i}")
            idx = -1 if i == len(self.textures)-2 else i
            button.mousePressEvent = lambda event=False, index=idx: self.set_textures(event=event, idx=index)
            
        self.ui.block_button_15.clicked.connect(self.reset_all)
        
        
        self.ui.prev_page_btn.clicked.connect(lambda: self.previous_page())
        self.ui.next_page_btn.clicked.connect(lambda: self.next_page())
        shortcut = QShortcut(QKeySequence("Ctrl+Shift+E"), self)
        shortcut.activated.connect(lambda: self.set_textures(None, -1, True))
        
        shortcut = QShortcut(QKeySequence("Ctrl+1"), self)
        shortcut.activated.connect(lambda: self.switch_to_page(0))
        shortcut = QShortcut(QKeySequence("Ctrl+2"), self)
        shortcut.activated.connect(lambda: self.switch_to_page(1))
        shortcut = QShortcut(QKeySequence("Ctrl+3"), self)
        shortcut.activated.connect(lambda: self.switch_to_page(2))
        
        self.show()

        
    def switch_to_page(self, page_index):
        if 0 <= page_index < self.ui.stackedWidget_2.count():
            self.ui.stackedWidget_2.setCurrentIndex(page_index)
            self.update_button_states()

    def previous_page(self):
        current_index = self.ui.stackedWidget_2.currentIndex()
        if current_index > 0:
            self.ui.stackedWidget_2.setCurrentIndex(current_index - 1)
        self.update_button_states()

    def next_page(self):
        current_index = self.ui.stackedWidget_2.currentIndex()
        if current_index < self.ui.stackedWidget_2.count() - 1:
            self.ui.stackedWidget_2.setCurrentIndex(current_index + 1)
        self.update_button_states()

    def update_button_states(self):
        current_index = self.ui.stackedWidget_2.currentIndex()
        self.ui.prev_page_btn.setEnabled(current_index > 0)
        self.ui.next_page_btn.setEnabled(current_index < self.ui.stackedWidget_2.count() - 1)

    def update_current_block(self):
        self.ui.current_left_block.setPixmap(QPixmap(self.textures[self.texture_left]))

    def place(self, x, y, texture_idx, god_mode=False, damage=None, health=None):
        if not god_mode:
            if x <= 0 or x >= 24 or y <= 0 or y >= 24:
                return
        if texture_idx == 0: self.check_for_existing_player()
        if self.blocks[x][y]: self.remove(x,y)
        if texture_idx == -1: return
        block_id = self.ui.imagePainter.add_image(self.textures[texture_idx], x*20, y*20)
        damage = damage if damage is not None else self.enemy_damage
        health = health if health is not None else self.enemy_health
        self.blocks[x][y] = Block(x,y,texture_idx, block_id, damage, health) if texture_idx not in (14,15) else None
        if texture_idx == 0: self.player = self.blocks[x][y]

    def reset_all(self):
        for x in range(1,24):
            for y in range(1,24):
                if self.blocks[x][y]:
                    self.remove(x,y)

    def connect_menu(self):
        self.ui.actionOpen.triggered.connect(lambda: self.load_map_file())
        self.ui.actionSave.triggered.connect(lambda: self.save_map_file())
        self.ui.actionEdit_Scripts.triggered.connect(lambda: ScriptEditor(self))

    def remove(self, x, y):
        id = self.blocks[x][y].id
        if self.blocks[x][y].get_block() == 0: self.player = None
        self.ui.imagePainter.remove_image(id)
        self.blocks[x][y] = None
        
    def check_for_existing_player(self):
        if not self.player: return
        x,y = self.player.x, self.player.y
        self.remove(x,y)

    def build_border(self):
        for i in range(25):
            self.place(i, 0, 1, True)
            self.place(0, i, 1, True)
            self.place(24, i, 1, True)
            self.place(i, 24, 1, True)

    def build_background(self):
        for x in range(1,24):
            for y in range(1,24):
                if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
                    self.place(x, y, 14, True)
                else:
                    self.place(x, y, 15, True)

    def load_textures(self):
        textures = []
        self.files = os.listdir(str(pathlib.Path(__file__).parent.absolute()) + "/textures/")
        for file in self.files:
            textures.append(Utils.get_abs_path(f"textures/{file}"))
        return textures
    
    def set_textures(self, event, idx, side=None):
        if event is not None:
            side = True if event.button() == Qt.LeftButton else False
        if side: self.texture_left = idx
        else: self.texture_right = idx
    
    def update_title(self):
        x,y = self.get_pos()
        self.setWindowTitle(f"PTB-Map-Builder | (x: {x}, y: {y})")
    
    def get_pos(self):
        pos = self.get_mouse_position()
        posx = pos.x() // 20
        posy = pos.y() // 20
        return (posx, posy)
    
    def get_mouse_position(self):
        cursor_pos = QCursor.pos()
        target_pos = self.ui.imagePainter.mapFromGlobal(cursor_pos)
        return target_pos
    
    def mouse_click_event(self, event):
        self.drawing = True
        b, p = event.button(), self.get_pos()
        self.current_texture = self.texture_left if b == Qt.LeftButton else self.texture_right
        self.place(p[0], p[1], self.current_texture)
        
    def mouseMove(self, event):
        if self.drawing:
            p = self.get_pos()
            self.place(p[0], p[1], self.current_texture)

    def mouseRelease(self, event):
        self.drawing = False
        self.current_texture = None
        
    def load_map_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Load a PTB Map", "", "*.ptb")
        if not file_name: return
        self.reset_all()
        out = PtbLoad.load_ptb(file_name)
        #self.scripts = self.comp.decompile(out[1])
        loaded_blocks = out[0]
        self.texts = out[2]
        for i, row in enumerate(loaded_blocks):
            for j, block_data in enumerate(row):
                if block_data is None: self.blocks[i][j] = None
                elif isinstance(block_data, list): self.place(i, j, *block_data)
                else: self.place(i, j, block_data)

    def save_map_file(self):
        if self.player is None: return
        file_name, _ = QFileDialog.getSaveFileName(self, "Save a PTB Map", "", "*.ptb")
        if not file_name: return
        block_list, info = self.get_combined_info()
        world = {"world":block_list}
        script = self.comp.compile(self.scripts) if not self.scripts is None else None
        print(script)
        texts = self.texts[:-1] if not self.texts is None else None
        com = compressor()
        com.insert_normal(world, script, texts)
        com.compress()
        com.save(file_name)

    def get_combined_info(self):
        block_list = []
        ids = {4: 450, 5: 700, 6: 900, 7: 20, 8: 150, 9: 55, 11: 80, 12: 0, 13: 260}
        item_keys= {4: "bombs", 5: "exp", 7: "dynamite", 8: "time_bombs", 9: "health", 11: "damage", 12: "nukes"}
        info = {
            "enemys": {"damage": [], "no-damage": []},
            "items": {"bombs": 0, "exp": 0, "dynamite": 0, "time_bombs": 0, "nukes": 0, "health": 0, "damage": 0},
            "blocks": 0
        }

        for i in range(25):
            temp = []
            for j in range(25):
                block = self.blocks[i][j]
                if not block:
                    temp.append({"id": -1, "objectData": {}})
                    continue
                print(block.texture)
                if block.texture == 10:
                    health, mode = block.get_enemy()
                    block_info = {"id": 6, "objectData": {"health": health, "id2": mode, "id1": 1}}
                    info["enemys"]["no-damage" if block.damage == 2 else "damage"].append(health)
                elif block.texture in ids:
                    start = ids[block.texture]
                    block_info = {"id": 5, "objectData": {"start": start, "fin": start}}
                    if block.texture in item_keys: 
                        item_key = item_keys[block.texture] 
                        info["items"][item_key] += 1
                elif block.texture == 3:
                    block_info = {"id": 3, "objectData": {}}
                    info["blocks"] += 1
                elif block.texture == 2:
                    block_info = {"id": 4, "objectData": {}}
                elif block.texture == 1:
                    block_info = {"id": 0, "objectData": {}}
                elif block.texture == 0:
                    block_info = {"id": 2, "objectData": {}}
                else:
                    print(block.texture)
                
                temp.append(block_info)
            block_list.append(temp)
    
        return block_list, info

    def pick_coords(self):
        for i in range(len(self.textures)+1):
            button = getattr(self.ui, f"block_button_{i}")
            button.setEnabled(False)
        self.menuBar().setEnabled(False)
        self.ui.next_page_btn.setEnabled(False)
        self.ui.imagePainter.mousePressEvent = lambda event: self.get_coords_on_mouse_click()
    
    def get_coords_on_mouse_click(self):
        x,y = self.get_pos()
        self.coord_signal.emit(x,y)
        self.ui.imagePainter.mousePressEvent = self.mouse_click_event
        for i in range(len(self.textures)+1):
            button = getattr(self.ui, f"block_button_{i}")
            button.setEnabled(True)
        self.menuBar().setEnabled(True)
        self.ui.next_page_btn.setEnabled(True)
        
class Block():
    def __init__(self, x,y,texture_id, block_id, damage, health):
        self.x = x
        self.y = y
        self.texture = texture_id
        self.id = block_id
        self.health = damage if texture_id == 10 else None
        self.damage = health if texture_id == 10 else None
        self.edit = True if self.texture == 10 else False
    def get_block(self):
        return self.texture
    def get_enemy(self):
        if self.texture == 10:
            return (self.health, self.damage)

class ScriptEditor(QDialog):
    def __init__(self, parent:MainWindow):
        super().__init__(parent=parent)
        self.parent = parent
        self.setWindowTitle("Custom Dialog")
        self.setFixedSize(500, 575)  # Set the window dimensions
        
        layout = QVBoxLayout()
        
        layout.setMenuBar(self.create_menu())

        self.text_edit = CustomTextEdit(self.get_keywords())
        CustomSyntaxHighlighter(self.text_edit.document())
        layout.addWidget(self.text_edit)

        compile_btn = QPushButton("OK")
        compile_btn.setObjectName("script_compile_dialog_btn")
        compile_btn.clicked.connect(self.accept)
        layout.addWidget(compile_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.exec()
    
    def get_keywords(self):
        ret = []
        for keywordlist in src.KEYWORDS.keywords:
            for keyword in keywordlist["keywords"]:
                ret.append(keyword)
        return ret
    
    def create_menu(self):
        menu = QMenuBar(self)
        
        tool_menu = QMenu(menu)
        tool_menu.setTitle("Tools")
        pick_coords_action = QAction(self)
        pick_coords_action.setText("Pick Coordinates")
        pick_coords_action.setShortcut("Ctrl+Shift+C")
        pick_coords_action.triggered.connect(lambda: self.pick_coordinates())
        tool_menu.addAction(pick_coords_action)
        menu.addMenu(tool_menu)
        return menu
    
    def pick_coordinates(self):
        self.hide()
        self.parent.pick_coords()
        self.parent.coord_signal.connect(self.insert_coords)
    def insert_coords(self, x, y):
        self.show()
        cursor = self.text_edit.textCursor()
        cursor.insertText(f"{x} {y}")
        self.parent.coord_signal.disconnect()

if __name__ == "__main__":
    app = QApplication([])
    md = MainWindow()
    sys.exit(app.exec())
