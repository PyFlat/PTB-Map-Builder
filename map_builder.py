from tkinter import *
import pathlib
import os
import time
from functools import partial
import json
from tkinter import ttk
import copy
from jsonload import *

class Display():
    def __init__(self):
        self.master = Tk()
        self.master.geometry('580x500')
        self.master.resizable(width = 0, height=0)
        self.master.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
        self.top = None
        self.w = Canvas(self.master, bg="white")
        self.w.pack()
        self.w.place(x=80, y=0, width=500, height=500)
        self.path = str(pathlib.Path(__file__).parent.absolute()) + "/textures/"
        self.files = os.listdir(self.path)
        self.addpath = "textures/"
        self.kreuz = PhotoImage(file="tools/kreuz.png")
        for i in range(0, len(self.files)):
            bm.textures.append(PhotoImage(file=self.addpath + self.files[i]))
        for i in range(25):
            self.w.create_line(20*i, 0,20*i, 500)
            self.w.create_line(0, 20*i, 500, 20*i)
        for i in range(len(bm.textures)):
            l = Button(self.master, image=bm.textures[i], border=1,command=partial(bm.set_texture, i))
            if i %2==0:
                x=15
                l.place(x=x, y=(i*20)+20, width=20, height=20)
            else:
                x=45
                l.place(x=x, y=(i*20), width=20, height=20)
                
        self.move = Button(self.master, image = self.kreuz, border = 1, command=partial(bm.set_texture, "move"),state="disabled")
        self.move.place(x=15, y=400, width=20, height=20)
        l = Button(self.master, bg = "orange", command=partial(bm.set_texture, "white"))
        l.place(x=15, y=460, width=20, height=20)
        c = Button(self.master, bg = "red", command=partial(bm.set_texture, "clear"))
        c.place(x=45, y=460, width=20, height=20)
        save = Button(self.master, bg = "green", command=partial(bm.to_json))
        save.place(x=45, y=430, width=20, height=20)
        if isinstance(bm.texture, str):
            self.ci = Button(self.master, bg="white", border = 1)
        else:
            self.ci = Button(self.master, image=bm.textures[bm.texture], border = 1)
        self.ci.place(x=15, y=430, width=20, height=20)

    def update_frame(self):
        if isinstance(bm.texture, str):
            try:
                self.ci.config(bg="white", image ="")
            except TclError:
                pass
        else:
            try:
                self.ci.config(image=bm.textures[bm.texture])
            except TclError:
                pass
class window():
    def __init__(self, width, height):
        self.master = Tk()
        self.master.geometry(str(width)+"x"+str(height))
        self.master.resizable(width=0, height=0)
        self.master.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
class Blocks():
    update_list = []
    def __init__(self):
        self.texture = "white"
        self.textures = []
        self.blocks = []
        self.block = False
        self.last_blocks = []
        temp = []
        for j in range(25):
            for i in range(25):
                temp.append(None)
            self.blocks.append(temp)
            temp = []
    def set_texture(self, tex):
        if tex == "clear":
            for i in range(23):
                for j in range(23):
                    if self.blocks[i+1][j+1] != None:
                        self.delete(self.blocks[i+1][j+1].obj)
                        self.blocks[i+1][j+1] = None
        self.texture = tex
        
    def delete(self, item):
        d.w.delete(item)
    def get_pos(self):
        abs_x = d.master.winfo_pointerx() - d.master.winfo_rootx()
        abs_y = d.master.winfo_pointery() - d.master.winfo_rooty()
        abs_x_r = round(abs_x, -1)-80
        abs_y_r = round(abs_y, -1)
        if abs_x_r % 20 == 0:
            abs_x_r += 10
        if abs_y_r % 20 ==0:
            abs_y_r += 10
        num_x = round((abs_x_r-10)/20)
        num_y = round((abs_y_r-10)/20)
        return [num_x, num_y]
    def place(self, x, y):
        if (x or y) < 0:
            num_x = self.get_pos()[0]
            num_y = self.get_pos()[1]
            if  num_x > 23 or num_y > 23 or num_x < 1 or num_y < 1:
                return 
        else:
            num_x = x
            num_y = y
        
        if self.texture == "move" and self.blocks[num_x][num_y] != None:
            Blocks.update_list.append(self.blocks[num_x][num_y])
            self.block = True
            return
        if self.block == True:
            if self.blocks[num_x][num_y] != None:
                self.delete(self.blocks[num_x][num_y].obj)
                self.blocks[num_x][num_y] = None
            self.set_texture(Blocks.update_list[0].texture)
            b = Block(num_x*20+10, num_y*20+10)
            self.blocks[num_x][num_y] = b
            self.block = False
            Blocks.update_list = []
            return
        if self.texture == "clear" or self.texture == "white":
            if self.blocks[num_x][num_y] == None:
                return
            self.delete(self.blocks[num_x][num_y].obj)
            self.blocks[num_x][num_y] = None
            return
        for i in range(25):
            for j in range(25):
                if (self.blocks[i][j] != None) and (self.blocks[i][j].texture == 0) and self.texture == 0:
                    self.delete(self.blocks[i][j].obj)
                    self.blocks[i][j] = None
        if self.blocks[num_x][num_y] != None:
            self.delete(self.blocks[num_x][num_y].obj)
            self.blocks[num_x][num_y] = None
        b = Block(num_x*20+10, num_y*20+10)
        self.blocks[num_x][num_y] = b
        del b

    def save(self):
        if self.texture != "clear" or "white":
            self.last_blocks = copy.deepcopy(self.blocks)
            self.last_texture = self.texture
    def load(self):
        self.set_texture("clear")
        for i in range(25):
            for j in range(25):
                if self.last_blocks[i][j] == None:
                    self.blocks[i][j] = None
                else:
                    self.set_texture(self.last_blocks[i][j].texture)
                    b = Block(i*20+10, j*20+10)
                    if self.texture == 12:
                        b.damage = self.last_blocks[i][j].damage
                        b.health = self.last_blocks[i][j].health
                    self.blocks[i][j] = b
        self.set_texture(self.last_texture)
    def load_from_json(self):
        self.set_texture("clear")
        jsonload.load_json()
        new_blocks = jsonload.get_json()
        for i in range(25):
            for j in range(25):
                if new_blocks[i][j] == None:
                    self.blocks[i][j] = None
                elif isinstance(new_blocks[i][j], list):
                    self.set_texture(new_blocks[i][j][0])
                    b = Block(i*20+10, j*20+10)
                    b.damage = new_blocks[i][j][2]
                    b.health = new_blocks[i][j][1]
                    self.blocks[i][j] = b
                else:
                    self.set_texture(new_blocks[i][j])
                    b = Block(i*20+10, j*20+10)
                    self.blocks[i][j] = b
    def to_json(self):
        block_list = []
        scripts = []
        texts = []
        for i in range(25):
            temp = []
            for j in range(25):
                if self.blocks[i][j] == None:
                    temp.append({"id":-1,"objectData":{}})
                elif self.blocks[i][j].texture == 12:
                    health, mode = self.blocks[i][j].get_enemy()
                    temp.append({"id":6,"objectData":{"health":health,"id2":mode,"extra1":0,"extra2":0}})
                elif self.blocks[i][j].texture == 11:
                    temp.append({"id":5,"objectData":{"start":30,"fin":59}})
                elif self.blocks[i][j].texture == 10:
                    temp.append({"id":5,"objectData":{"start":950,"fin":1000}})
                elif self.blocks[i][j].texture == 9:
                    temp.append({"id":5,"objectData":{"start":60,"fin":299}})
                elif self.blocks[i][j].texture == 8:
                    temp.append({"id":5,"objectData":{"start":0,"fin":29}})
                elif self.blocks[i][j].texture == 7:
                    temp.append({"id":5,"objectData":{"start":800,"fin":949}})
                elif self.blocks[i][j].texture == 6:
                    temp.append({"id":5,"objectData":{"start":550,"fin":799}})
                elif self.blocks[i][j].texture == 5:
                    temp.append({"id":5,"objectData":{"start":300,"fin":449}})
                elif self.blocks[i][j].texture == 4:
                    temp.append({"id":3,"objectData":{}})
                elif self.blocks[i][j].texture == 3:
                    temp.append({"id":4,"objectData":{}})
                elif self.blocks[i][j].texture == 2:
                    temp.append({"id":-1,"objectData":{}})
                elif self.blocks[i][j].texture == 1:
                    temp.append({"id":0,"objectData":{}})
                elif self.blocks[i][j].texture == 0:
                    temp.append({"id":2,"objectData":{}})
                    
            block_list.append(temp)
            temp = []
        Data = {"world":block_list,"scripts":scripts,"texts":texts}
        file = open("temp" + ".json", "w")
        file.write(json.dumps(Data))
        file.close()
class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pix_x = round((self.x-10)/20)
        self.pix_y = round((self.y-10)/20)
        self.health = 1
        self.damage = 1
        self.texture = bm.texture
        self.obj = d.w.create_image(self.x, self.y, image = bm.textures[self.texture])
        d.w.lower(self.obj)
        if self.texture > 11:
            self.edit = True
        else:
            self.edit = False
    def move(self, pos):
        d.w.moveto(self.obj, bm.get_pos()[0]*20, bm.get_pos()[1]*20)
    def get_block(self):
        return self.texture
    def get_enemy(self):
        if self.texture == 12:
            return (self.health, self.damage)
class enemy_win():
    exists = False
    def __init__(self):
        self.pos_x = bm.get_pos()[0]
        self.pos_y = bm.get_pos()[1]
        self.block = bm.blocks[self.pos_x][self.pos_y]
        if self.block == None or self.block.edit == False or enemy_win.exists == True:
            return
        self.enem_win = window(250, 150)
        enemy_win.exists = True
        self.l1 = Label(self.enem_win.master, text="Health", justify="center", font="Calibri 15")
        self.l1.place(x=0, y=0, width=250)
        
        self.s1 = Scale(self.enem_win.master, from_=1, to=63, orient="horizontal")
        self.s1.place(x=0,y=25, width=250)
        self.l2 = Label(self.enem_win.master, text="Mode", justify="center", font="Calibri 15")
        self.l2.place(x=0, y=70, width=250)
        self.cbb = ttk.Combobox(self.enem_win.master, values=["Kill-Aura-On", "Kill-Aura-Off"], font="Calibri 15")
        self.cbb.place(x=0, y=95, width=250, height=30)
        if self.block.damage == 1:
            self.cbb.current(1)
        elif self.block.damage == 2:
            self.cbb.current(0)
        self.b1 = Button(self.enem_win.master, text="Save", font="Calibri 15", command=lambda:[self.set_value(self.pos_x,
                                                                                                              self.pos_y,
                                                                                                              self.cbb.get(),
                                                                                                              self.s1.get(),
                                                                                                              self.enem_win)])
        self.b1.place(x=0, y=125, width= 250, height=25)
        self.s1.set(self.block.health)
    def set_value(self, x,y, aura, health, win):
        if aura == "Kill-Aura-On":
            damag = 2
        elif aura == "Kill-Aura-Off":
            damag = 1
        bm.blocks[x][y].damage = damag
        bm.blocks[x][y].health = health
        enemy_win.exists = False
        win.master.destroy()
    
bm = Blocks()
bm.save()
d = Display()
d.master.bind("<Button-1>",lambda ev: bm.place(-1,-1))
d.master.bind("<space>",lambda ev: bm.place(-1,-1))
d.master.bind("<B1-Motion>", lambda ev: bm.place(-1,-1))
d.master.bind("<ButtonPress-1>", lambda ev: bm.save())
d.master.bind("<Control-z>", lambda ev: bm.load())
d.master.bind("<Button-3>", lambda ev: enemy_win())
d.master.bind("f", lambda ev: bm.load_from_json())
d.master.bind("r", lambda ev: bm.set_texture("white"))
bm.set_texture(1)

for i in range(25):
    bm.place(i, 0)
    bm.place(0,i)
    bm.place(24,i)
    bm.place(i, 24)
while True:
    for block in Blocks.update_list:
        block.move(1)
    d.update_frame()
    d.master.update()
    d.master.update_idletasks()
    time.sleep(0.02)
