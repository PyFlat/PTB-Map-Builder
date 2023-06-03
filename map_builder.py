from tkinter import *
from tkinter import messagebox
from functools import partial
from jsonload import *
from compiler import *
from compressor import *
import pathlib, os,easygui

class Window():
    def __init__(self, width, height):
        self.master = Tk()
        self.master.geometry(str(width)+"x"+str(height))
        self.master.resizable(width=0, height=0)
class MainDisplay():
    def __init__(self, block_manager):
        self.bm = block_manager
        self.window = Window(580, 500)
        self.master = self.window.master
        self.top = None
        self.active = True
        self.w = Canvas(self.master, highlightthickness=0)
        self.w.pack()
        self.w.place(x=80, y=0, width=500, height=500)
        self.path = str(pathlib.Path(__file__).parent.absolute()) + "/textures/"
        self.files = os.listdir(self.path)
        self.addpath = "textures/"
        f = Button(self.master, bg = "blue", command=partial(self.bm.load_from_json))
        f.place(x=15, y=430, width=20, height=20) 
        l = Button(self.master, bg = "orange", command=partial(self.bm.set_texture, -1))
        l.place(x=15, y=460, width=20, height=20)
        l.bind("<Button-3>", lambda ev: self.bm.set_texture(-1, False))
        c = Button(self.master, bg = "red", command=partial(self.bm.reset))
        c.place(x=45, y=460, width=20, height=20)
        editor = Button(self.master, text="Scripts", bg="black", fg="white", command=partial(Script_Editor, self.bm))
        editor.place(x=15, y=370, width=50, height=20)
        editor = Button(self.master, text="Texts", bg="black", fg="white", command=partial(Text_Editor, self.bm))
        editor.place(x=15, y=340, width=50, height=20)
        save = Button(self.master, bg = "green", command=partial(self.bm.save_to_file))
        save.place(x=45, y=430, width=20, height=20)
        self.bl = Button(self.master, bg="white", border = 0)
        self.bl.place(x=15, y=400, width=20, height=20)
        self.br = Button(self.master, bg="white", border = 0)
        self.br.place(x=45, y=400, width=20, height=20)
        self.load_images_background()
        self.create_buttons()
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
    def load_images_background(self):
        for i in range(0, len(self.files)):
            self.bm.textures.append(PhotoImage(file=self.addpath + self.files[i]))
        for i in range(23):
            for j in range(23):
                if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                    self.w.create_image((i+1)*20+10, (j+1)*20+10, image = self.bm.textures[14])
                else:
                    self.w.create_image((i+1)*20+10, (j+1)*20+10, image = self.bm.textures[15])
    def create_buttons(self):
        for i in range(len(self.bm.textures)-2):
            l = Button(self.master, image=self.bm.textures[i], border=1,command=partial(self.bm.set_texture, i))
            l.bind("<Button-3>", partial(self.bm.set_texture, i, False))
            if i %2==0:
                x=15
                l.place(x=x, y=(i*20)+20, width=20, height=20)
            else:
                x=45
                l.place(x=x, y=(i*20), width=20, height=20)
            if i == 10:
                l.bind("<Shift-Button-1>", lambda ev: Enemy_Editor(True))
    def place_bedrock(self):
        self.bm.set_texture(1)
        for i in range(25):
            self.bm.place(i, 0)
            self.bm.place(0,i)
            self.bm.place(24,i)
            self.bm.place(i, 24)
        self.bm.set_texture(-1)
    def bind_buttons(self):
        self.master.bind("<space>", lambda ev: self.bm.start_move())
        self.master.bind("<KeyRelease-space>", lambda ev: self.bm.stop_move())
        self.master.bind("<Control-Button-1>", lambda ev: self.bm.update_line(start=True))
        self.master.bind("<Control-Button-3>", lambda ev: self.bm.update_line(False, start=True))
        self.master.bind("<Control-B1-Motion>", lambda ev: self.bm.update_line())
        self.master.bind("<Control-B3-Motion>", lambda ev: self.bm.update_line(False))
        self.master.bind("<Control-B1-KeyRelease>", lambda ev: self.bm.update_line(fin=True))
        self.master.bind("<Control-B3-KeyRelease>", lambda ev: self.bm.update_line(False,fin=True))
        self.master.bind("<Alt-Button-1>", lambda ev: self.bm.update_box(start=True))
        self.master.bind("<Alt-Button-3>", lambda ev: self.bm.update_box(False, start=True))
        self.master.bind("<Alt-B1-Motion>", lambda ev: self.bm.update_box())
        self.master.bind("<Alt-B3-Motion>", lambda ev: self.bm.update_box(False))
        self.master.bind("<ButtonRelease-1>", lambda ev: [self.bm.update_box(fin=True),self.bm.update_line(fin=True)])
        self.master.bind("<ButtonRelease-3>", lambda ev: [self.bm.update_box(False,fin=True), self.bm.update_line(False,fin=True)])
        self.master.bind("<Alt-B1-KeyRelease>", lambda ev: self.bm.update_box(fin=True))
        self.master.bind("<Alt-B3-KeyRelease>", lambda ev: self.bm.update_box(False,fin=True))
        self.master.bind("<B1-Motion>", lambda ev: self.bm.place(-1,-1, True))
        self.master.bind("<B3-Motion>", lambda ev: self.bm.place(-1,-1, False))
        self.master.bind("<ButtonPress-1>", lambda ev: [self.bm.save(),self.bm.place(-1,-1, True)])
        self.master.bind("<ButtonPress-3>", lambda ev: [self.bm.save(),self.bm.place(-1,-1, False)])
        self.master.bind("<Control-z>", lambda ev: self.bm.load())
        self.master.bind("<Shift-Button-1>", lambda ev: [Enemy_Editor(False), self.bm.save()])
        self.master.bind("<Control-B1-KeyPress>", lambda ev: self.bm.save())
        self.master.bind("<Control-B3-KeyPress>", lambda ev: self.bm.save())
        self.master.bind("<Alt-B1-KeyPress>", lambda ev: self.bm.save())
        self.master.bind("<Alt-B3-KeyPress>", lambda ev: self.bm.save())
        self.master.bind("k", lambda ev: print(self.bm.get_pos()))
    def update_frame(self):
        if self.bm.get_texture() < 0:
            self.bl.config(bg="white", image ="")
        else:
            self.bl.config(image=self.bm.textures[self.bm.get_texture()])
        if self.bm.get_texture(False) < 0:
            self.br.config(bg="white", image="")
        else:
            self.br.config(image=self.bm.textures[self.bm.get_texture(False)])
    def mainloop(self):
        while self.active:
            for block in self.bm.update_list:
                block.move(1)
            x, y = self.bm.get_pos()
            self.master.title(f"PTB-Map-Builder | (x: {x}, y: {y})")
            self.update_frame()
            self.master.update()
            self.master.update_idletasks()
    def on_close(self):
        self.active = False
        self.master.quit()
        self.master.destroy()
class BlockManager():
    def __init__(self):
        self.update_list = []
        self.texts = None
        self.scripts = None
        self.texture_left = -1
        self.texture_right = -1
        self.textures = []
        self.blocks = [[None for i in range(25)] for j in range(25)]
        self.last_blocks = []
        self.enemy_damage = 1
        self.enemy_health = 1
        self.line_x = None
        self.line_y = None
        self.line_images = []
        self.move_x_s = None
        self.move_y_s = None
        self.mouse_x = None
        self.mouse_y = None
        self.mobj = None
        self.x_stable = None
        self.check_x = True
        self.check_y = True
        self.box_x = None
        self.box_y = None
        self.comp = compiler()
    def get_texture(self, side = True):
        tex = self.texture_left if side else self.texture_right; return tex
    def set_texture(self, tex, side = True, *args):
        self.texture_left, self.texture_right = (tex, self.texture_right) if side else (self.texture_left, tex)
    def reset(self):
        self.texts = self.scripts = None
        for i in range(23):
            for j in range(23):
                if self.blocks[i+1][j+1] != None:
                    self.delete(i+1, j+1)
        self.set_texture(-1);self.set_texture(-1, False)
    def delete(self, x, y, item = None):
        if item is None: md.w.delete(self.blocks[x][y].obj); self.blocks[x][y] = None
        else: md.w.delete(item)
    def get_pos(self):
        abs_x = md.master.winfo_pointerx() - md.master.winfo_rootx()
        abs_y = md.master.winfo_pointery() - md.master.winfo_rooty()
        abs_x_r = round(abs_x, -1) - 80
        abs_y_r = round(abs_y, -1)
        abs_x_r += 10 if abs_x_r % 20 == 0 else 0
        abs_y_r += 10 if abs_y_r % 20 == 0 else 0
        self.num_x = round((abs_x_r - 10) / 20)
        self.num_y = round((abs_y_r - 10) / 20)
        return [self.num_x, self.num_y]

    def place(self, x, y, dire = True):
        num_x, num_y = self.get_pos()
        if x >= 0:
            num_x = x
        if y >= 0:
            num_y = y
        if (num_x > 23 or num_x < 1 or num_y < 1 or num_y > 23) and not (num_x == x and num_y== y): return
        if self.blocks[num_x][num_y]:self.delete(num_x, num_y)
        texture = self.get_texture(dire)
        if texture == 0:
            for i, j in [(i, j) for i in range(25) for j in range(25) if self.blocks[i][j] and self.blocks[i][j].texture == 0]:
                self.delete(i, j)
        elif texture < 0:
            return
        if self.blocks[num_x][num_y]:
            self.delete(num_x, num_y)
        b = Block(num_x * 20 + 10, num_y * 20 + 10, dire)
        self.blocks[num_x][num_y] = b
        del b

    def start_move(self):
        x,y = self.get_pos()
        if self.move_x_s == None or self.move_y_s == None:
            self.move_x_s = x
            self.move_y_s = y
        else:
            if self.mobj == None:
                if self.blocks[self.move_x_s][self.move_y_s] != None:
                    tex = self.blocks[self.move_x_s][self.move_y_s].get_block()
                    self.mobj = md.w.create_image(x*20+10,y*20+10,image=self.textures[tex])
            else:
                md.w.moveto(self.mobj,x*20,y*20)
    def stop_move(self):
        x,y = self.get_pos()
        b = self.blocks[self.move_x_s][self.move_y_s]
        if b == None:
            self.move_x_s = None
            self.move_x_s = None
            md.w.delete(self.mobj)
            self.mobj = None
            return
        if x > 23 or x < 1 or y < 1 or y > 23:
            return
        oblock = self.blocks[self.move_x_s][self.move_y_s]
        otex = self.get_texture()
        ntex = oblock.get_block()
        self.delete(self.move_x_s, self.move_y_s)
        enemy = oblock.get_enemy()
        self.set_texture(ntex)
        self.place(-1,-1)
        if enemy != None:
            self.blocks[x][y].health = enemy[0]
            self.blocks[x][y].damage = enemy[1]
        self.set_texture(otex, True)
        self.move_x_s = None
        self.move_x_s = None
        md.w.delete(self.mobj)
        self.mobj = None

    def update_box(self, dire=True, fin=False, start=False):
        if start and self.get_texture(dire) != 0:
            self.box_x, self.box_y = self.get_pos()
        if self.box_x == None or self.box_y == None:
            return
        x,y = self.get_pos()
        difference_x = x-self.box_x
        difference_y = y-self.box_y
        if self.box_x == x and self.box_y == y:
            return
        while len(self.line_images) > 0:
            md.w.delete(self.line_images.pop(0))
        difference_x = 1 if difference_x == 0 else difference_x
        difference_y = 1 if difference_y == 0 else difference_y
        stepx = int(difference_x/abs(difference_x))
        stepy = int(difference_y/abs(difference_y))
        for i in range(self.box_x, x+stepx, stepx):
            for j in range(self.box_y, y+stepy, stepy):
                if i <= 0 or i >= 24 or j <= 0 or j >= 24:
                    break
                if fin:
                    self.place(i, j, dire)
                else:
                    texture = self.get_texture(dire)
                    if texture == -1:
                        is_even = (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)
                        texture = 14 if is_even else 15
                    self.line_images.append(md.w.create_image(i * 20 + 10, j * 20 + 10, image=self.textures[texture]))
        if fin:
            self.box_x = self.box_y = None
    def update_line(self, dire=True, fin=False, start=False):
        if start and self.get_texture(dire) != 0:
            self.line_x,self.line_y = self.get_pos()
            self.update_line(dire, fin)
        if self.line_x == None or self.line_y == None: return
        x,y = self.get_pos()
        difference_x = x-self.line_x
        difference_y = y-self.line_y
        if self.line_x == x and self.line_y == y: return 
        elif (x != self.line_x and self.x_stable == None) or (self.check_x and self.x_stable != None):
            self.check_y, self.x_stable, difference, line, xy = False, False, difference_x, self.line_x, x
        elif (y != self.line_y and self.x_stable == None) or (self.check_y and self.x_stable != None):
            self.check_x, self.x_stable, difference, line, xy = False, True, difference_y, self.line_y, y
        while len(self.line_images) > 0:
            md.w.delete(self.line_images.pop(0))
        difference = 1 if difference == 0 else difference
        step = int(difference/abs(difference))
        if xy + step - line == 1:
            self.x_stable, self.check_x, self.check_y = None, True, True
            self.update_line(dire, fin)
            return
        for i in range(line, xy+step, step):
            x = self.line_x if self.x_stable else i
            y = i if self.x_stable else self.line_y
            if x <= 0 or x >= 24 or y <= 0 or y >= 24:
                break
            elif fin:
                self.place(x, y, dire)
            else:
                texture = self.get_texture(dire)
                if texture == -1:
                    is_even = (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0)
                    texture = 14 if is_even else 15
                self.line_images.append(md.w.create_image(x * 20 + 10, y * 20 + 10, image=self.textures[texture]))
        if fin:
            self.x_stable = self.line_x = None
            self.check_x = self.check_y = True
    def save(self):
        self.last_blocks = []
        for x in range(len(self.blocks)):
            temp = []
            for elem in self.blocks[x]:
                temp.append(elem)
            self.last_blocks.append(temp)
        self.last_texture = self.get_texture()
    def load(self):
        self.reset()
        for i in range(25):
            for j in range(25):
                if self.last_blocks[i][j]:
                    self.set_texture(self.last_blocks[i][j].texture)
                    self.place(i,j)
                    if self.get_texture() == 10:
                        self.blocks[i][j].damage = self.last_blocks[i][j].damage
                        self.blocks[i][j].health = self.last_blocks[i][j].health
        self.set_texture(self.last_texture)
    def get_path(self, fileopen = False):
        if fileopen:
            path = easygui.fileopenbox(msg="Choose a PTB or JSON file to load", default="~/Downloads/", filetypes = ["*.ptb", "*.json"])
        else:
            path = easygui.filesavebox(msg="Choose a Place to Save your Map", default="~/Downloads/*.ptb")
            if path[-4:] != ".ptb":
                path += ".ptb"
        if path == None or ((path[-4:] == ".ptb") or ((path[-5:] == ".json") and fileopen)):
            return path
        messagebox.showerror("Error", "False File Format")
        return None
    def load_from_json(self):
        path = self.get_path(fileopen = True)
        if path == None:
            return
        self.reset()
        if path[-4:] == ".ptb":
            out = ptbload.load_ptb(path)
            self.scripts = self.comp.decompile(out[1])
        elif path[-5:] == ".json":
            out = jsonload.load_json(path)
        new_blocks = out[0]
        self.texts = out[2]
        for i in range(25):
            for j in range(25):
                if new_blocks[i][j] == None:
                    self.blocks[i][j] = None
                elif isinstance(new_blocks[i][j], list):
                    block = new_blocks[i][j]
                    self.set_texture(block[0])
                    self.place(i,j)
                    self.blocks[i][j].health = block[1]
                    self.blocks[i][j].damage = block[2]
                else:
                    self.set_texture(new_blocks[i][j])
                    self.place(i,j)
        self.set_texture(-1, True)
    def get_json_block_data(self):
        block_list = []
        for i in range(25):
            temp = []
            for j in range(25):
                if self.blocks[i][j] == None:
                    temp.append({"id":-1,"objectData":{}})
                elif self.blocks[i][j].texture == 10:
                    health, mode = self.blocks[i][j].get_enemy()
                    temp.append({"id":6,"objectData":{"health":health,"id2":mode,"id1":1}})
                elif self.blocks[i][j].texture == 9:
                    temp.append({"id":5,"objectData":{"start":55,"fin":55}})
                elif self.blocks[i][j].texture == 8:
                    temp.append({"id":5,"objectData":{"start":150,"fin":150}})
                elif self.blocks[i][j].texture == 7:
                    temp.append({"id":5,"objectData":{"start":20,"fin":20}})
                elif self.blocks[i][j].texture == 6:
                    temp.append({"id":5,"objectData":{"start":900,"fin":900}})
                elif self.blocks[i][j].texture == 5:
                    temp.append({"id":5,"objectData":{"start":700,"fin":700}})
                elif self.blocks[i][j].texture == 4:
                    temp.append({"id":5,"objectData":{"start":450,"fin":450}})
                elif self.blocks[i][j].texture == 11:
                    temp.append({"id":5,"objectData":{"start":80,"fin":80}})
                elif self.blocks[i][j].texture == 12:
                    temp.append({"id":5,"objectData":{"start":0,"fin":0}})
                elif self.blocks[i][j].texture == 13:
                    temp.append({"id":5,"objectData":{"start":260,"fin":260}})
                elif self.blocks[i][j].texture == 3:
                    temp.append({"id":3,"objectData":{}})
                elif self.blocks[i][j].texture == 2:
                    temp.append({"id":4,"objectData":{}})
                elif self.blocks[i][j].texture == 1:
                    temp.append({"id":0,"objectData":{}})
                elif self.blocks[i][j].texture == 0:
                    temp.append({"id":2,"objectData":{}})
            block_list.append(temp)
        return block_list
    def save_to_file(self):
        path = self.get_path()
        if path == None:
            return
        block_list = self.get_json_block_data()
        World = {"world":block_list}
        if self.scripts != None:
            script = self.comp.compile(self.scripts)
        else:
            script = None
        if self.texts != None:
            texts = self.texts[:-1]
        else:
            texts = None
        com = compressor()
        com.insert_normal(World, script, texts)
        com.compress()
        com.save(path)
class Block():
    def __init__(self, x, y, dire):
        self.w = md.w
        self.x = x
        self.y = y
        self.health = bm.enemy_health
        self.damage = bm.enemy_damage
        self.texture = bm.get_texture(dire)
        self.obj = self.w.create_image(self.x, self.y, image = bm.textures[self.texture])
        if self.texture == 10:
            self.edit = True
        else:
            self.edit = False
    def move(self, x, y):
        self.w.moveto(self.obj, x=x,y=y) 
    def get_block(self):
        return self.texture
    def get_enemy(self):
        if self.texture == 10:
            return (self.health, self.damage)
class Script_Editor():
    running = False
    def __init__(self, blocks):
        self.bm = blocks
        if Script_Editor.running:
            return
        Script_Editor.running = True
        self.window = Window(600, 600)
        self.window.master.config(bg="#3c3c3c")
        self.window.master.title("Scripts")
        self.textfeld = Text(self.window.master, relief="flat", font="Calibri 20")
        self.textfeld.place(x=25, y=25, height=525, width=550)
        if self.bm.scripts != None:
            self.textfeld.insert("1.0",self.bm.scripts)
        self.submit = Button(self.window.master,relief="flat", text="Submit",bg="orange",fg="white", font="Calibri 20", activeforeground="orange", activebackground="white", border = 0, command=lambda:[self.compile_text(),self.destroy()])
        self.submit.place(x=200, y=560, height=30, width=200)
        self.window.master.protocol("WM_DELETE_WINDOW", self.destroy)
    def compile_text(self):
        self.bm.scripts = self.textfeld.get("1.0",END)
    def destroy(self):
        self.window.master.destroy()
        self.window.master.quit()
        Script_Editor.running = False
class Text_Editor():
    running = False
    def __init__(self, blocks):
        self.bm = blocks
        if Text_Editor.running:
            return
        Text_Editor.running = True
        self.window = Window(600, 600)
        self.window.master.config(bg="#3c3c3c")
        self.window.master.title("Texts")
        self.textfeld = Text(self.window.master, relief="flat", font="Calibri 20")
        self.textfeld.place(x=25, y=25, height=525, width=550)
        if self.bm.texts != None:
            text = self.bm.texts
            text = "\n".join(text)
            self.textfeld.insert("1.0",text)
        self.submit = Button(self.window.master,relief="flat", text="Submit",bg="orange",fg="white", font="Calibri 20", activeforeground="orange", activebackground="white", border = 0, command=lambda:[self.destroy()])
        self.submit.place(x=200, y=560, height=30, width=200)
        self.window.master.protocol("WM_DELETE_WINDOW", self.destroy)
    def destroy(self):
        self.bm.texts = self.textfeld.get("1.0",END)
        self.window.master.destroy()
        self.window.master.quit()
        Text_Editor.running = False
class Enemy_Editor():
    running = False
    def __init__(self, gen):
        self.general = gen
        self.pos_x, self.pos_y = bm.get_pos()
        self.block = bm.blocks[self.pos_x][self.pos_y]
        if ((self.block == None or self.block.edit == False) and (self.general == False)) or Enemy_Editor.running:
            return
        Enemy_Editor.running = True
        self.enem_win = Window(250, 150)
        self.enem_win.master.protocol("WM_DELETE_WINDOW", partial(self.destroy, self.enem_win))
        self.l1 = Label(self.enem_win.master, text="Health:", justify="center", font="Calibri 15")
        self.l1.place(x=0, y=0, width=250)
        self.e1 = Entry(self.enem_win.master)
        self.e1.place(x=0,y=35,width=250)
        self.l2 = Label(self.enem_win.master, text="Damage:", justify="center", font="Calibri 15")
        self.l2.place(x=0, y=60, width=250)
        self.var = IntVar(self.enem_win.master)
        self.b1 = Button(self.enem_win.master, text="Save", font="Calibri 15", command=lambda:[self.set_value()])
        self.b1.place(x=0, y=125, width= 250, height=25)
        self.radio_1  = Radiobutton(self.enem_win.master, text="OFF", variable=self.var, value=1)
        self.radio_1.place(x=0, y=95, width=125)
        self.radio_2 = Radiobutton(self.enem_win.master, text="ON", variable=self.var, value=2)
        self.radio_2.place(x=125, y=95, width=125)
        if not self.general:
            self.var.set(self.block.damage)
            self.set_health(self.block.health)
        else:
            self.var.set(bm.enemy_damage)
            self.set_health(bm.enemy_health)
    def set_health(self, health):
        self.e1.delete(1)
        self.e1.insert(1, health)
    def set_value(self):
        health = self.e1.get()
        if not health.isdigit() or int(health) <= 0:
            health = 1
        else:
            health = int(health)
        if self.general:
            bm.enemy_damage = self.var.get()
            bm.enemy_health = health
        else:
            bm.blocks[self.pos_x][self.pos_y].damage = self.var.get()
            bm.blocks[self.pos_x][self.pos_y].health = health
        self.destroy()
    def destroy(self, *args):
        Enemy_Editor.running = False
        self.enem_win.master.destroy()
        
bm = BlockManager()
md = MainDisplay(bm)
md.place_bedrock()
md.bind_buttons()
md.mainloop()
