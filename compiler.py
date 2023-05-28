class compiler():
    def __init__(self, source):
        self.command_length = [None, 3,3,2,5,3,3,4,3,2,4,4,4,1,2,5,5,2,1]
        self.source = source
        self.bytes = b""
        self.lines = self.source.split("\n")
    def get_length(self, line):
        line = line.split(" ")
        if line[0] == "tp":
            return 3
        if line[0] == "edit_inventory":
            return 3
        if line[0] == "edit_health":
            return 2
        if line[0] == "var":
            return 3
        if line[0] == "get":
            return 4
        if line[0] == "@":
            return 4
        if line[0] == "if":
            return 3
        if line[0] == "comp":
            return 5
        if line[0] == "jump":
            return 2
        if len(line) > 1:
                if line[1] == "+":
                    return 4
        if len(line) > 1:
                if line[1] == "-":
                    return 4
        if len(line) > 1:
                if line[1] == "*":
                    return 4
        if line[0] == "end":
            return 1
        if line[0] == "showText":
            return 2
        if line[0] == "draw":
            return 5
        if line[0] == "delete":
            return 2
        if line[0] == "win":
            return 1
    def compile(self):
        for i in range (0, len(self.lines)):
            line = self.lines[i].split(" ")
            bline = b"\x00"
            if line[0] == "tp":
                #print("Player Teleport registered") #01
                bline += b"\x01"
                bline += (int(line[1])).to_bytes(1,"big")
                bline += (int(line[2])).to_bytes(1,"big")
            if line[0] == "edit_inventory":
                #print("Player Inventory") #02
                t_colls = [None,"basic_bombs","range","dynamite","timebombs"]
                t = line[2]
                bline += b"\x02"
                for d in range (len(t_colls)):
                    if t_colls[d] == t:
                        bline += (d).to_bytes(1,"big")
                bline += (int(line[4])).to_bytes(1,"big")
            if line[0] == "edit_health":
                #print("Player Health") #03
                bline += b"\x03"
                bline += (int(line[1])).to_bytes(1,"big")
            if line[0] == "var":
                #print("Set Var") #05
                bline += b"\x05"
                bline += (int(line[1])).to_bytes(1,"big")
                bline += (int(line[3])).to_bytes(1,"big")
            if line[0] == "get":
                #print("get") #06
                t_colls = [None,"basic_bombs","range","dynamite","timebombs","health"]
                s_colls = [None,"player"]
                t = line[1]
                s = line[3]
                r = line[5]
                bline += b"\x06"
                bline += (int(r)).to_bytes(1,"big")
                for d in range (len(s_colls)):
                    if s_colls[d] == s:
                        bline += (d).to_bytes(1,"big")
                for d in range (len(t_colls)):
                    if t_colls[d] == t:
                        bline += (d).to_bytes(1,"big")
            if line[0] == "@":
                #print("Trigger") #07
                bline += b"\x07"
                event_list = [None, "on_step","on_collect","on_init"]
                e = line[1]
                X = int(line[3])
                Y = int(line[4])
                for d in range (0, len(event_list)):
                    if event_list[d] == e:
                        bline+= (d).to_bytes(1,"big")
                bline+= (X).to_bytes(1,"big")
                bline+= (Y).to_bytes(1,"big")
            if len(line) >= 4:
                if line[3] == "=>":
                    print("Compare")
                    bline += b"\x04" #compare
                    mods = [None,">","<","=="]
                    A = int(line[0])
                    m = line[1]
                    B = int(line[2])
                    C = int(line[4])
                    bline += (C).to_bytes(1,"big")
                    bline += (A).to_bytes(1,"big")
                    for d in range (0, len(mods)):
                        if mods[d] == m:
                            bline += (d).to_bytes(1,"big")
                    bline += (B).to_bytes(1,"big")
            if line[0] == "if":
                bline += b"\x08"
                bline += (int(line[1])).to_bytes(1,"big")
                jump_lines = int(line[3])
                byte_jump = 0
                if len(self.lines)-1 < jump_lines + i:
                    raise ValueError("Error in line " + str(i+1) + ": Jump Mark out of bounds")
                for l in range (i+1, i + 1 +jump_lines):
                    #print(self.get_length(self.lines[l]))
                    byte_jump += self.get_length(self.lines[l]) + 1
                if byte_jump > 255:
                    raise ValueError("Error in line " + str(i+1) + ": ByteBlock Size too large (" + str(byte_jump) + "/255)")
                bline += (byte_jump).to_bytes(1,"big")
            if line[0] == "jump":
                #print("jmp") #09
                bline += b"\x09"
                jump_lines = int(line[1])
                byte_jump = 0
                if len(self.lines)-1 < jump_lines + i:
                    raise ValueError("Error in line " + str(i+1) + ": Jump Mark out of bounds")
                for l in range (i+1, i + 1 +jump_lines):
                    #print(self.get_length(self.lines[l]))
                    byte_jump += self.get_length(self.lines[l]) + 1
                if byte_jump > 255:
                    raise ValueError("Error in line " + str(i+1) + ": ByteBlock Size too large (" + str(byte_jump) + "/255)")
                bline += (byte_jump).to_bytes(1,"big")
            if len(line) > 1:
                if line[1] == "+":
                    #print("add") #0A
                    bline += b"\x0a"
                    bline += (int(line[0])).to_bytes(1,"big")
                    bline += (int(line[2])).to_bytes(1,"big")
                    bline += (int(line[4])).to_bytes(1,"big")
            if len(line) > 1:
                if line[1] == "-":
                    #print("sub") #0B
                    bline += b"\x0b"
                    bline += (int(line[0])).to_bytes(1,"big")
                    bline += (int(line[2])).to_bytes(1,"big")
                    bline += (int(line[4])).to_bytes(1,"big")
            if len(line) > 1:
                if line[1] == "*":
                    #print("mul") #0C
                    bline += b"\x0c"
                    bline += (int(line[0])).to_bytes(1,"big")
                    bline += (int(line[2])).to_bytes(1,"big")
                    bline += (int(line[4])).to_bytes(1,"big")
            if line[0] == "end":
                #print("EXIT") #0D
                bline += b"\x0d"
            if line[0] == "showText":
                #print("Text") #0E
                bline += b"\x0e"
                bline += (int(line[1])).to_bytes(1,"big")
            #if line[0] == "drawImageFromRAM":
            #    #print("IMG 1") #0F
            if line[0] == "draw":
                #print("IMG 2") #10
                bline += b"\x10"
                bline += (int(line[6])).to_bytes(1,"big")
                bline += (int(line[1])).to_bytes(1,"big")
                bline += (int(line[3])).to_bytes(1,"big")
                bline += (int(line[4])).to_bytes(1,"big")
            if line[0] == "delete":
                #print("IMG 3") #11
                bline += b"\x11"
                bline += (int(line[1])).to_bytes(1,"big")
            if line[0] == "win":
                #print("WON")
                bline += b"\x12"
            if bline != B"\x00":
                self.bytes += bline
       # self.bytes += b"\x00\x0d"
        if self.bytes != b"":
            return self.bytes
        return None
class decompiler():
    def __init__(self, source):
        self.source = source
        #self.source = self.source[:-1]
        self.results = ""
    def cts(self, c, i):
        cs = [None, "tp","edit_inventory","edit_health","=>","var","get","@","if","jump","+","-","*","end","showText",None,"draw","delete","win"]
        rv = None
        try:
            rv = cs[c]
        except IndexError:
            raise ValueError("Decompiler Error: command index missmatch for value {} at location {}".format(c,i))
        if cs[c] == None:
            raise ValueError("Decompiler Error: command index missmatch for value {} at location {}".format(c,i))
        return rv
    def gln(self, c, i):
        ls = [None, 3, 3, 2, 5, 3, 4, 4, 3,2,4,4,4,1,2,None,5,2,1]
        return ls[c]
    def decompile(self):
        pt = 0
        results = ""
        while pt < len(self.source):
            #If Command is found:
            if self.source[pt] == 0:
                #Get command type
                b_c_type = self.source[pt+1]
                #Convert command type to str
                s_c_type = self.cts(b_c_type,pt+1)
                #Process Command
                if s_c_type == "tp":
                    results += ("tp {} {}".format(self.source[pt+2],self.source[pt+3]))
                elif s_c_type == "edit_inventory":
                    t_colls = [None,"basic_bombs","range","dynamite","timebombs"]
                    results += ("edit_inventory set {} to {}".format(t_colls[self.source[pt+2]],self.source[pt+3]))
                elif s_c_type == "edit_health":
                    results += ("edit_health {}".format(self.source[pt+2]))
                elif s_c_type == "=>":
                    forms = [None, ">", "<", "=="]
                    results += ("comp {} {} {} => {}".format(self.source[pt+3],forms[self.source[pt+4]],self.source[pt+5],self.source[pt+2]))
                elif s_c_type == "var":
                    results += ("var {} = {}".format(self.source[pt+2],self.source[pt+3]))
                elif s_c_type in ["+","-","*"]:
                    results += ("{} {} {} = {}".format(self.source[pt+2],s_c_type,self.source[pt+3],self.source[pt+4],self.source[pt+5]))
                elif s_c_type == "get":
                    il = [None,"basic_bombs","range","dynamite","timebombs","health"]
                    sl = [None,"player"]
                    results += ("get {} from {} to {}".format(il[self.source[pt+4]],sl[self.source[pt+3]],self.source[pt+2]))
                elif s_c_type == "@":
                    evl = [None, "on_step","on_collect","on_init"]
                    results += ("@ {} on {} {}".format(evl[self.source[pt+2]],self.source[pt+3],self.source[pt+4]))
                elif s_c_type == "if":
                    byte_jump = self.source[pt+3]
                    temp_parser = pt + self.gln(b_c_type, pt+1) + 1
                    jump_lines = 0
                    while byte_jump > 0:
                        jump_lines += 1
                        byte_jump -= (self.gln(self.source[temp_parser+1],temp_parser+1)+1)
                        temp_parser += self.gln(self.source[temp_parser+1],temp_parser+1)+1
                    results += ("if {} jump {}".format(self.source[pt+2],jump_lines))
                elif s_c_type == "jump":
                    byte_jump = self.source[pt+3]
                    temp_parser = pt + self.gln(b_c_type, pt+1) + 1
                    jump_lines = 0
                    while byte_jump > 0:
                        jump_lines += 1
                        byte_jump -= (self.gln(self.source[temp_parser+1],temp_parser+1)+1)
                        temp_parser += self.gln(self.source[temp_parser+1],temp_parser+1)+1
                    results += ("jump {}".format(jump_lines))
                elif s_c_type == "showText":
                    results += ("showText {}".format(self.source[pt+2]))
                elif s_c_type == "draw":
                    #print(self.source[pt+3],self.source[pt+4],self.source[pt+5],self.source[pt+2])
                    results += ("draw {} on {} {} to {}".format(self.source[pt+3],self.source[pt+4],self.source[pt+5],self.source[pt+2]))
                elif s_c_type == "delete":
                    results += ("delete {}".format(self.source[pt+2]))
                elif s_c_type == "end":
                    results += ("end")
                elif s_c_type == "win":
                    results += ("win")
                results += "\n"
                pt += self.gln(b_c_type,pt+1)
            pt += 1
        results = results[:-1]
        return results
