from tkinter import *
from tkinter import messagebox
import pathlib
import os
from functools import partial
from tkinter import ttk
import copy
from jsonload import *
from compiler import compiler, decompiler
from compressor import *
import easygui

class Display():
    def __init__(self, master):
        self.master = master
        self.top = None
        self.w = Canvas(self.master, bg="white")
        self.w.pack()
        self.w.place(x=80, y=0, width=500, height=500)
        self.path = str(pathlib.Path(__file__).parent.absolute()) + "/textures/"
        self.files = os.listdir(self.path)
        self.addpath = "textures/"
        for i in range(0, len(self.files)):
            bm.textures.append(PhotoImage(file=self.addpath + self.files[i]))
        for i in range(25):
            self.w.create_line(20*i, 0,20*i, 500)
            self.w.create_line(0, 20*i, 500, 20*i)
        for i in range(len(bm.textures)):
            l = Button(self.master, image=bm.textures[i], border=1,command=partial(bm.set_texture, i, True))
            def make_lambda(i, dire):
                return lambda ev: bm.set_texture(i, dire)
            l.bind("<Button-3>", make_lambda(i, False))
            if i %2==0:
                x=15
                l.place(x=x, y=(i*20)+20, width=20, height=20)
            else:
                x=45
                l.place(x=x, y=(i*20), width=20, height=20)
            if i == 10:
                l.bind("<Control-Button-1>", lambda ev: enemy_win(True))
                
        f = Button(self.master, bg = "blue", command=partial(bm.load_from_json))
        f.place(x=15, y=430, width=20, height=20) 
        l = Button(self.master, bg = "orange", command=partial(bm.set_texture, -1, True))
        l.place(x=15, y=460, width=20, height=20)
        l.bind("<Button-3>", lambda ev: bm.set_texture(-1, False))
        c = Button(self.master, bg = "red", command=partial(bm.set_texture, -2, True))
        c.place(x=45, y=460, width=20, height=20)
        editor = Button(self.master, text="Scripts", bg="black", fg="white", command=partial(Script_Editor, bm))
        editor.place(x=15, y=370, width=50, height=20)
        editor = Button(self.master, text="Texts", bg="black", fg="white", command=partial(Text_Editor, bm))
        editor.place(x=15, y=340, width=50, height=20)
        save = Button(self.master, bg = "green", command=partial(bm.to_json))
        save.place(x=45, y=430, width=20, height=20)
        self.bl = Button(self.master, bg="white", border = 0)
        self.bl.place(x=15, y=400, width=20, height=20)
        self.br = Button(self.master, bg="white", border = 0)
        self.br.place(x=45, y=400, width=20, height=20)
    def update_frame(self):
        if bm.get_texture(True) < 0:
            self.bl.config(bg="white", image ="")
        else:
            self.bl.config(image=bm.textures[bm.get_texture(True)])
        if bm.get_texture(False) < 0:
            self.br.config(bg="white", image="")
        else:
            self.br.config(image=bm.textures[bm.get_texture(False)])
class Script_Editor():
    running = False
    def __init__(self, blocks):
        self.bm = blocks
        if Script_Editor.running:
            return
        Script_Editor.running = True
        self.window = window(600, 600)
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
        self.window = window(600, 600)
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
class Blocks():
    update_list = []
    def __init__(self):
        self.texts = None
        self.scripts = None
        self.texture_left = -1
        self.texture_right = -1
        self.textures = []
        self.blocks = []
        self.block = False
        self.last_blocks = []
        temp = []
        self.enemy_damage = 1
        self.enemy_health = 1
        self.line_x = None
        self.line_y = None
        self.move_x_s = None
        self.move_y_s = None
        self.mouse_x = None
        self.mouse_y = None
        self.load_dire = None
        self.mobj = None
        for j in range(25):
            for i in range(25):
                temp.append(None)
            self.blocks.append(temp)
            temp = []
    def get_texture(self, dire):
        if dire:
            return self.texture_left
        else:
            return self.texture_right
    def set_damage_health(self, damage, health):
        if health == 0:
            health = 1
        try:
            health = int(health)
        except ValueError:
            health = 1
        if damage == "Kill-Aura-On":
            damag = 2
        elif damage == "Kill-Aura-Off":
            damag = 1
        self.enemy_damage = damag
        self.enemy_health = health
    def set_texture(self, tex, dire):
        old_texture_left = self.get_texture(True)
        old_texture_right = self.get_texture(False)
        if tex == -2:
            self.texts = None
            self.scripts = None
            for i in range(23):
                for j in range(23):
                    if self.blocks[i+1][j+1] != None:
                        self.delete(self.blocks[i+1][j+1].obj)
                        self.blocks[i+1][j+1] = None
            self.texture_left = old_texture_left
            self.texture_right = old_texture_right
            return
        if dire:
            self.texture_left = tex
        else:
            self.texture_right = tex
    def delete(self, item):
        d.w.delete(item)
    def set_mouse_pos(self,event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        abs_x_r = round(self.mouse_x, -1)
        abs_y_r = round(self.mouse_y, -1)
        if abs_x_r % 20 == 0:
            abs_x_r += 10
        if abs_y_r % 20 ==0:
            abs_y_r += 10
        self.num_x = round((abs_x_r-10)/20)
        self.num_y = round((abs_y_r-10)/20)
    def get_pos(self):
        abs_x = d.master.winfo_pointerx() - d.master.winfo_rootx()
        abs_y = d.master.winfo_pointery() - d.master.winfo_rooty()
        abs_x_r = round(abs_x, -1)-80
        abs_y_r = round(abs_y, -1)
        if abs_x_r % 20 == 0:
            abs_x_r += 10
        if abs_y_r % 20 ==0:
            abs_y_r += 10
        self.num_x = round((abs_x_r-10)/20)
        self.num_y = round((abs_y_r-10)/20)
        return [self.num_x, self.num_y]
    def place(self, x, y, dire):
        if x < 0 and y < 0:
            num_x = self.get_pos()[0]
            num_y = self.get_pos()[1]
            if num_x > 23 or num_x < 1 or num_y < 1 or num_y > 23:
                return
        elif x < 0:
            num_x = self.get_pos()[0]
            num_y = y
            if num_x > 23 or num_x < 1:
                return
        elif y < 0:
            num_y = self.get_pos()[1]
            num_x = x
            if num_y < 1 or num_y > 23:
                return
        else:
            num_x = x
            num_y = y
        if self.block == True:
            if self.blocks[num_x][num_y] != None:
                self.delete(self.blocks[num_x][num_y].obj)
                self.blocks[num_x][num_y] = None
            self.set_texture(Blocks.update_list[0].texture, dire)
            b = Block(num_x*20+10, num_y*20+10, dire)
            self.blocks[num_x][num_y] = b
            self.block = False
            Blocks.update_list = []
            return
        if self.get_texture(dire) < 0:
            if self.blocks[num_x][num_y] == None:
                return
            self.delete(self.blocks[num_x][num_y].obj)
            self.blocks[num_x][num_y] = None
            return
        for i in range(25):
            for j in range(25):
                if (self.blocks[i][j] != None) and (self.blocks[i][j].texture == 0) and self.get_texture(dire) == 0:
                    self.delete(self.blocks[i][j].obj)
                    self.blocks[i][j] = None
        if self.blocks[num_x][num_y] != None:
            self.delete(self.blocks[num_x][num_y].obj)
            self.blocks[num_x][num_y] = None
        b = Block(num_x*20+10, num_y*20+10, dire)
        self.blocks[num_x][num_y] = b
        del b
    def place_line(self, dire):
        if self.line_x == None or self.line_y == None:
            self.line_x = self.get_pos()[0]
            self.line_y = self.get_pos()[1]
            return
        x1 = self.get_pos()[0]
        y1 = self.get_pos()[1]
        if x1 == self.line_x and y1 == self.line_y:
            return
        elif x1 != self.line_x and self.line_y != -1:
            self.line_x = -1
            self.place(self.line_x, self.line_y, dire)
        elif y1 != self.line_y:
            self.line_y = -1
            self.place(self.line_x, self.line_y, dire)
    def start_move(self):
        x,y = self.get_pos()
        if self.move_x_s == None or self.move_y_s == None:
            self.move_x_s = x
            self.move_y_s = y
        else:
            if self.mobj == None:
                tex = self.blocks[self.move_x_s][self.move_y_s].get_block()
                self.mobj = d.w.create_image(x*20+10,y*20+10,image=self.textures[tex])
            else:
                d.w.moveto(self.mobj,x*20,y*20)
    def stop_move(self):
        x = self.get_pos()[0]
        y = self.get_pos()[1]
        b = self.blocks[self.move_x_s][self.move_y_s]
        if b == None:
            self.move_x_s = None
            self.move_x_s = None
            d.w.delete(self.mobj)
            self.mobj = None
            return
        if x > 23 or x < 1 or y < 1 or y > 23:
            return
        oblock = self.blocks[self.move_x_s][self.move_y_s]
        otex = self.get_texture(True)
        ntex = oblock.get_block()
        self.delete(oblock.obj)
        self.blocks[self.move_x_s][self.move_y_s] = None
        enemy = oblock.get_enemy()
        self.set_texture(ntex, True)
        self.place(-1,-1,True)
        if enemy != None:
            self.blocks[x][y].health = enemy[0]
            self.blocks[x][y].damage = enemy[1]
        self.set_texture(otex, True)
        self.move_x_s = None
        self.move_x_s = None
        d.w.delete(self.mobj)
        self.mobj = None
    def reset_line(self):
        self.line_x = None
        self.line_y = None
    def save(self):
        if self.get_texture(True) > -2:
            self.last_blocks = copy.deepcopy(self.blocks)
            self.last_texture = self.get_texture(True)
    def load(self):
        dire = True
        self.set_texture(-2, dire)
        for i in range(25):
            for j in range(25):
                if self.last_blocks[i][j] == None:
                    self.blocks[i][j] = None
                else:
                    self.set_texture(self.last_blocks[i][j].texture, dire)
                    b = Block(i*20+10, j*20+10, dire)
                    if self.get_texture(dire) == 10:
                        b.damage = self.last_blocks[i][j].damage
                        b.health = self.last_blocks[i][j].health
                    self.blocks[i][j] = b
        self.set_texture(self.last_texture, dire)
    def load_from_json(self):
        file = easygui.fileopenbox(msg="Choose a PTB or JSON file to load", default="~/Downloads/", filetypes = ["*.ptb", "*.json"])
        if file == None:
            return
        elif (file[-4:] != ".ptb") and (file[-5:] != ".json"):
            messagebox.showerror("Error while Loading", "False File Format")
            return
        else:
            self.set_texture("clear", True)
            if file[-4:] == ".ptb":
                out = ptbload.load_ptb(file)
            elif file[-5:] == ".json":
                out = jsonload.load_json(file)
            self.texts = out[2]
            print(out[2])
            d = decompiler(out[1])
            self.scripts = d.decompile()
            new_blocks = out[0]
            for i in range(25):
                for j in range(25):
                    if new_blocks[i][j] == None:
                        self.blocks[i][j] = None
                    elif isinstance(new_blocks[i][j], list):
                        self.set_texture(new_blocks[i][j][0], True)
                        b = Block(i*20+10, j*20+10, True)
                        b.damage = new_blocks[i][j][2]
                        b.health = new_blocks[i][j][1]
                        self.blocks[i][j] = b
                    else:
                        self.set_texture(new_blocks[i][j], True)
                        b = Block(i*20+10, j*20+10, True)
                        self.blocks[i][j] = b
            self.set_texture("white", True)
    def to_json(self):
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
            temp = []
        path = easygui.filesavebox(msg="Choose a Place to Save your Map", default="~/Downloads/*.ptb")
        if path == None:
            return
        if path[-4:] != ".ptb":
            messagebox.showerror("Error while Saving", "False File Format")
            return
        World = {"world":block_list}
        if self.scripts != None:
            c = compiler(self.scripts)
            script = c.compile()
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
class window():
    def __init__(self, width, height):
        self.master = Tk()
        self.master.geometry(str(width)+"x"+str(height))
        self.master.resizable(width=0, height=0)
class Block():
    def __init__(self, x, y, dire):
        self.x = x
        self.y = y
        self.pix_x = round((self.x-10)/20)
        self.pix_y = round((self.y-10)/20)
        self.health = bm.enemy_health
        self.damage = bm.enemy_damage
        self.texture = bm.get_texture(dire)
        self.obj = d.w.create_image(self.x, self.y, image = bm.textures[self.texture])
        d.w.lower(self.obj)
        if self.texture == 10:
            self.edit = True
        else:
            self.edit = False
    def move(self, x, y):
        d.w.moveto(self.obj, x=x,y=y) 
    def get_block(self):
        return self.texture
    def get_enemy(self):
        if self.texture == 10:
            return (self.health, self.damage)
class enemy_win():
    exists = False
    def __init__(self, gen):
        self.general = gen
        self.pos_x = bm.get_pos()[0]
        self.pos_y = bm.get_pos()[1]
        self.block = bm.blocks[self.pos_x][self.pos_y]
        if self.block == None or self.block.edit == False or enemy_win.exists == True:
            if not self.general:
                return
        self.enem_win = window(250, 150)
        self.enem_win.master.protocol("WM_DELETE_WINDOW", partial(self.destroy, self.enem_win))
        enemy_win.exists = True
        self.l1 = Label(self.enem_win.master, text="Health", justify="center", font="Calibri 15")
        self.l1.place(x=0, y=0, width=250)
        self.e1 = Entry(self.enem_win.master)
        self.e1.place(x=0,y=35,width=250)
        self.l2 = Label(self.enem_win.master, text="Mode", justify="center", font="Calibri 15")
        self.l2.place(x=0, y=70, width=250)
        self.cbb = ttk.Combobox(self.enem_win.master, values=["Kill-Aura-On", "Kill-Aura-Off"], font="Calibri 15")
        self.cbb.place(x=0, y=95, width=250, height=30)
        if not self.general:
            if self.block.damage == 1:
                self.cbb.current(1)
            elif self.block.damage == 2:
                self.cbb.current(0)
            self.b1 = Button(self.enem_win.master, text="Save", font="Calibri 15", command=lambda:[self.set_value(self.pos_x,self.pos_y,self.cbb.get(),self.e1.get(),self.enem_win)])
            self.b1.place(x=0, y=125, width= 250, height=25)
            self.set_health(self.block.health)
        else:
            if bm.enemy_damage == 1:
                self.cbb.current(1)
            elif bm.enemy_damage == 2:
                self.cbb.current(0)
            self.b1 = Button(self.enem_win.master, text="Save", font="Calibri 15", command=lambda:[bm.set_damage_health(self.cbb.get(), self.e1.get()), self.destroy(self.enem_win)])
            self.b1.place(x=0, y=125, width= 250, height=25)
            self.set_health(bm.enemy_health)
    def set_health(self, health):
        self.e1.delete(1)
        self.e1.insert(1, health)
    def set_value(self, x,y, aura, health, win):
        if health == 0:
            health = 1
        try:
            health = int(health)
        except ValueError:
            health = 1
        if aura == "Kill-Aura-On":
            damag = 2
        elif aura == "Kill-Aura-Off":
            damag = 1
        bm.blocks[x][y].damage = damag
        bm.blocks[x][y].health = health
        self.destroy(win)
    def destroy(self, win):
        enemy_win.exists = False
        win.master.destroy()
        
active = True    
def on_close():
    global active
    active = False
    master.quit()
    master.destroy()
master = Tk()
master.geometry('580x500')
master.title("Map Builder")
master.resizable(width = 0, height=0)
master.protocol("WM_DELETE_WINDOW", on_close)    
bm = Blocks()
bm.save()
d = Display(master)
d.master.bind("<space>", lambda ev: bm.start_move())
d.master.bind("<KeyRelease-space>", lambda ev: bm.stop_move())
d.master.bind("<Control-B1-Motion>", lambda ev: bm.place_line(True))
d.master.bind("<Control-B3-Motion>", lambda ev: bm.place_line(False))
d.master.bind("<Control-KeyRelease>", lambda ev: bm.reset_line())
d.master.bind("<B1-Motion>", lambda ev: bm.place(-1,-1, True))
d.master.bind("<B3-Motion>", lambda ev: bm.place(-1,-1, False))
d.master.bind("<ButtonPress-1>", lambda ev: [bm.save(),bm.place(-1,-1, True)])
d.master.bind("<ButtonPress-3>", lambda ev: [bm.save(),bm.place(-1,-1, False)])
d.master.bind("<Control-z>", lambda ev: bm.load())
d.master.bind("<Control-Button-1>", lambda ev: enemy_win(False))
bm.set_texture(1, True)
for i in range(25):
    bm.place(i, 0, True)
    bm.place(0,i, True)
    bm.place(24,i, True)
    bm.place(i, 24, True)
bm.set_texture(-1, True)
while active:
    for block in Blocks.update_list:
        block.move(1)
    d.update_frame()
    d.master.update()
    d.master.update_idletasks()
    #time.sleep(0.02)
