import time


class log:
    def __init__(self) -> None:
        self.logs = []

    def add_log(self, log):
        self.logs.append(f"[{time.time()}]" + log)

    def write_log(self, file):
        s = ""
        for log in self.logs:
            s += log + "\n"
        with open(file, "w") as file:
            file.write(s)


class util:
    def validateCommandLength(attrs, minlength, line):
        if len(attrs) < minlength:
            raise IndexError(
                f"Line {line} Compiler Error [002]: Short command. Expected >={minlength}, got {len(attrs)}"
            )

    def validateInteger(data, maxlength, line, logfile):
        try:
            i = int(data)
        except ValueError:
            try:
                i = int(data, 16)
                logfile.add_log(
                    f"WARNING [{line}]: Used hex as integer conversion for {data}. This is not recommended."
                )
            except ValueError:
                raise TypeError(
                    f"Line {line} Compiler Error [003]: Invalid integer Conversion of value {data}"
                )
        if i > maxlength:
            raise ValueError(
                f"Line {line} Compiler Error [004]: Maximum integer length exceeded. Exspected <= {maxlength}, got {i}"
            )
        if i < 0:
            raise ValueError(
                f"Line {line} Compiler Error [005]: Integer too small. Exspected >0, got {i}"
            )
        return i

    def validateEnum(data, enum, line, blacklisted=[]):
        if data not in enum:
            raise ValueError(
                f"Line {line} Compiler Error [001]: invalid Enum. Expected {enum}, got {data}."
            )
        if data in blacklisted:
            raise ValueError(
                f"Line {line} Compiler Error [006]: Blacklisted value. The value {data} is blacklisted for {enum}. The blacklist is {blacklisted}"
            )
        for i in range(len(enum)):
            if enum[i] == data:
                return i
        raise RuntimeError(f"Line {line} Compiler Error [999]: Impossible")

    def byte(i: int, l: int):
        return i.to_bytes(l, "big")


class compiler:
    def __init__(self):
        self.comp_scripts = [
            None,
            self.compile_trigger,
            self.compile_end,
            self.compile_math,
            self.compile_math,
            self.compile_math,
            self.compile_math,
            self.compile_set,
            self.compile_reset,
            self.compile_get,
            self.compile_get,
            self.compile_end,
            self.compile_end,
            self.compile_drawimg,
            self.compile_rect,
            self.compile_clear,
            self.compile_comp,
            self.compile_jump,
            self.compile_flag,
            self.compile_tp,
        ]
        self.logfile = log()

    def getLineSize(self):
        ls = []

    def getEnumHelp(self, enum):
        enum = enum.lower()
        help = {"event": "No help here yet :("}
        try:
            return help[enum]
        except KeyError:
            return f"Hilfe für {enum} kann nicht abgerufen werden."

    def getCmdHelp(self, cmId):
        if type(cmId) == str:
            cmId = self.getCommandId(cmId)
        if type(cmId) != int:
            return f"Ungültige ID {cmId}"
        help = [
            "General: Konstante Zahlen sind maximal 8 Bit groß, Adressen bis zu 16 Bit. Die Speicherzellen haben kein größenlimit.\n Keine Zahlen dürfen 0 groß sein!!!"
            "@: Dieser Befehl stellt einen einstiegspunkt da. Nutzung:\n@ event on x y\nevent ist ein Enum. Für mehr info zu enums benutze getEnumHelp(enum).\n x und y sind die koordinaten des triggers und sind konstanten\nWenn das event ausgelöst wird, startet das script bei diesem Befehl.",
            "end: Dieser Befehl stoppt die Ausführung des aktuellen scripts.\n Wird end nicht aufgerufen, läuft das script auch über andere @ Anweisungen",
            "add: Dieser Befehl addiert 2 zahlen aus dem Speicher und speichert das Ergebnis.Syntax: \n add a , b => c\n a und b werden addiert und in c gespeichert",
            "subtract: Dieser Befehlt subtrahiert 2 Zahlen. Für mehr info, siehe getCmdHelp(3)\nAlle mathematikbefehle sind syntaktisch gleich",
            "multiply: Dieser Befehl multipliziert 2 Zahlen. Für mehr infor siehe getCmdHelp(3)\nAlle mathematikbefehle sind syntaktisch gleich",
            "divide: Dieser Befehl dividiert 2 Zahlen. Für mehr infor siehe getCmdHelp(3)\nAlle mathematikbefehle sind syntaktisch gleich.\nWICHTIG: Das teilen von Zahlen liefert IMMER eine ganzzahl.",
            "set: Dieser Befehlt speichert eine Konstante im speicher.\nset location = value\n",
            "reset: Dieser Befehl bewirkt set location = 0, da set location = 0 nicht verwendet werden DARF",
            "store: Dieser Befehl lädt einen wert (enum) vom spiel und speichert ihn.\nstore value to cell",
            "set_item: Dieser Befehl ändert einen Wert im SPiel.\nset_item value = cell",
            "win: wins the game, even if no enemys are present.\nwin",
            "loose: loose the game instantly.\nloose",
            "drawImage: draws an image to the screen.\ndrawImage image on x y => stor\nImage is the ID of an image in the game files. Custom images are supportet. x and y are the coords of the image.\nThe image ist stored to stor.\nDO NOT EDIT STOR. If stor is changed or deleted you won't be able to destroy the image",
            "drawRect on x y with color ( r g b ) => stor",
            "clear graphics\n graphics; adress of image",
        ]
        try:
            return help[cmId]
        except IndexError:
            return f"Hilfe für ID {cmId} konnte nicht abgerufen werden. Gültige IDs sind {0}-{len(help)-1}."

    def getCommandId(self, cmd):
        cm = {
            "@": 1,
            "end": 2,
            "add": 3,
            "subtract": 4,
            "multiply": 5,
            "divide": 6,
            "set": 7,
            "reset": 8,
            "store": 9,
            "set_item": 10,
            "win": 11,
            "loose": 12,
            "drawImage": 13,
            "drawRect": 14,
            "clear": 15,
            "compare": 16,
            "jump": 17,
            "setFlag": 18,
            "tp": 19,
        }
        try:
            return cm[cmd]
        except KeyError:
            return False

    def getCommandString(self, cmd):
        cm = [
            None,
            "@",
            "end",
            "add",
            "subtract",
            "multiply",
            "divide",
            "set",
            "reset",
            "store",
            "set_item",
            "win",
            "loose",
            "drawImage",
            "drawRect",
            "clear",
            "compare",
            "jump",
            "setFlag",
            "tp",
        ]
        try:
            return cm[cmd]
        except IndexError:
            return False

    def getCommandMask(self, cmd):
        ms = [
            "",
            "@ {} on {} {}",
            "end",
            "add {} , {} => {}",
            "subtract {} , {} => {}",
            "multiply {} , {} => {}",
            "divide {} , {} => {}",
            "set {} = {}",
            "reset {}",
            "store {1} to {0}",
            "set_item {1} = {0}",
            "win",
            "loose",
            "drawImage {3} on {1} {2} => {0}",
            "drawRect on {1} {2} with color ( {3} {4} {5} ) => {0}",
            "clear {}",
            "compare {} {} {} => {}",
            "jump {} lines if {}",
            "setFlag {} = {}",
            "tp to {} {}",
        ]
        try:
            return ms[cmd]
        except IndexError:
            return "ERROR:INVALID_COMMAND"

    def getEnum(self, cmd):
        ens = [
            None,
            [None, "on_init", "on_step", "on_collect", "on_explode", "on_destroy"],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [
                None,
                "player.health",
                "player.bombs",
                "player.range",
                "player.dynamite",
                "player.timed_bombs",
                "player.damage",
                "player.nukes",
            ],
            [
                None,
                "player.health",
                "player.bombs",
                "player.range",
                "player.dynamite",
                "player.timed_bombs",
                "player.damage",
                "player.nukes",
            ],
            None,
            None,
            None,
            None,
            None,
            [None, ">", "<", "==", "<=", ">="],
            [None, "dop_items"],
            None,
        ]
        return ens[cmd]

    def get_config(self, cmd):
        cc = [
            "",
            "§$$",
            "",
            "***",
            "***",
            "***",
            "***",
            "*$",
            "*",
            "*§",
            "*§",
            "",
            "",
            "****",
            "******",
            "*",
            "*§**",
            "**",
            "§*",
            "**",
        ]
        return cc[cmd]

    def compile_trigger(self, attrs, line):
        util.validateCommandLength(attrs, 5, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        events = [None, "on_init", "on_step", "on_collect", "on_explode", "on_destroy"]
        i = util.validateEnum(attrs[1], events, line, [None])
        result += util.byte(i, 1)
        x = util.validateInteger(attrs[3], 255, line, self.logfile)
        y = util.validateInteger(attrs[4], 255, line, self.logfile)
        result += util.byte(x, 1)
        result += util.byte(y, 1)
        return result

    def compile_end(self, attrs, line):
        util.validateCommandLength(attrs, 1, line)
        cmd = self.getCommandId(attrs[0])
        return util.byte(cmd, 1)

    def compile_math(self, attrs, line):
        util.validateCommandLength(attrs, 6, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        a = util.validateInteger(attrs[1], 65535, line, self.logfile)
        b = util.validateInteger(attrs[3], 65535, line, self.logfile)
        c = util.validateInteger(attrs[5], 65535, line, self.logfile)
        result += util.byte(a, 2)
        result += util.byte(b, 2)
        result += util.byte(c, 2)
        return result

    def compile_set(self, attrs, line):
        util.validateCommandLength(attrs, 4, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        m = util.validateInteger(attrs[1], 65535, line, self.logfile)
        v = util.validateInteger(attrs[3], 255, line, self.logfile)
        result += util.byte(m, 2)
        result += util.byte(v, 1)
        return result

    def compile_reset(self, attrs, line):
        util.validateCommandLength(attrs, 2, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        m = util.validateInteger(attrs[1], 65535, line, self.logfile)
        result += util.byte(m, 2)
        return result

    def compile_get(self, attrs, line):
        util.validateCommandLength(attrs, 5, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        values = [
            None,
            "player.health",
            "player.bombs",
            "player.range",
            "player.dynamite",
            "player.timed_bombs",
            "player.damage",
            "player.nukes",
        ]
        i = util.validateEnum(attrs[1], values, line, [None])
        m = util.validateInteger(attrs[3], 65535, line, self.logfile)
        result += util.byte(m, 2)
        result += util.byte(i, 1)
        return result

    def compile_drawimg(self, attrs, line):
        # draw image on x y => stor
        util.validateCommandLength(attrs, 7, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        x = util.validateInteger(attrs[3], 65535, line, self.logfile)
        y = util.validateInteger(attrs[4], 65535, line, self.logfile)
        i = util.validateInteger(attrs[1], 65535, line, self.logfile)
        s = util.validateInteger(attrs[6], 65535, line, self.logfile)
        result += util.byte(s, 2)
        result += util.byte(x, 2)
        result += util.byte(y, 2)
        result += util.byte(i, 2)
        return result

    def compile_rect(self, attrs, line):
        # drawRect on x y with color ( r g b ) => stor
        util.validateCommandLength(attrs, 13, line)
        mx = 65535
        x = util.validateInteger(attrs[2], mx, line, self.logfile)
        y = util.validateInteger(attrs[3], mx, line, self.logfile)
        r = util.validateInteger(attrs[7], mx, line, self.logfile)
        g = util.validateInteger(attrs[8], mx, line, self.logfile)
        b = util.validateInteger(attrs[9], mx, line, self.logfile)
        s = util.validateInteger(attrs[12], mx, line, self.logfile)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        result += util.byte(s, 2)
        result += util.byte(x, 2)
        result += util.byte(y, 2)
        result += util.byte(r, 2)
        result += util.byte(g, 2)
        result += util.byte(b, 2)
        return result

    def compile_clear(self, attrs, line):
        util.validateCommandLength(attrs, 2, line)
        slot = util.validateInteger(attrs[1], 65535, line, self.logfile)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        result += util.byte(slot, 2)
        return result

    def compile_comp(self, attrs, line):
        # compare a o b => c
        util.validateCommandLength(attrs, 6, line)
        a = util.validateInteger(attrs[1], 65535, line, self.logfile)
        b = util.validateInteger(attrs[3], 65535, line, self.logfile)
        c = util.validateInteger(attrs[5], 65535, line, self.logfile)
        operands = [None, ">", "<", "==", "<=", ">="]
        o = util.validateEnum(attrs[2], operands, line, [None])
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        result += util.byte(a, 2)
        result += util.byte(o, 1)
        result += util.byte(b, 2)
        result += util.byte(c, 2)
        return result

    def compile_jump(self, attrs, line):
        # jump m lines if a
        util.validateCommandLength(attrs, 5, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        j = util.validateInteger(attrs[1], 65535, line, self.logfile)
        c = util.validateInteger(attrs[4], 65535, line, self.logfile)
        result += util.byte(j, 2)
        result += util.byte(c, 2)
        return result

    def compile_flag(self, attrs, line):
        util.validateCommandLength(attrs, 4, line)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        values = [None, "dop_items"]
        i = util.validateEnum(attrs[1], values, line, [None])
        result += util.byte(i, 1)
        v = util.validateInteger(attrs[3], 255, line, self.logfile)
        result += util.byte(v, 1)
        return result

    def accessCompilationScript(self, cmd):
        return self.comp_scripts[cmd]

    def compileCommand(self, cmd, attrs, line):
        return self.accessCompilationScript(cmd)(attrs, line)

    def compile_tp(self, attrs, line):
        util.validateCommandLength(attrs, 4, line)
        x = util.validateInteger(attrs[2], 65535, line, self.logfile)
        y = util.validateInteger(attrs[3], 65535, line, self.logfile)
        cmd = self.getCommandId(attrs[0])
        result = util.byte(cmd, 1)
        result += util.byte(x, 2)
        result += util.byte(y, 2)
        return result

    def compile(self, script: str, options="") -> bytes:
        self.logfile.add_log(f"Compiling started with options {options}")
        result = b"\x00"
        lines = script.split("\n")
        for i in range(len(lines)):
            line = lines[i]
            attrs = line.split(" ")
            cmd = self.getCommandId(attrs[0])
            if cmd == False:
                if "--disable_comment_warnings" not in options:
                    self.logfile.write_log(
                        f"WARNING Line {i} is not a valid command. Use --disable_comment_warnigns to remove this from the log."
                    )
                continue
            result += self.compileCommand(cmd, attrs, i)
        self.logfile.add_log(f"Compiling finished.")
        if "--write_log" in options:
            self.logfile.write_log("LOG " + str(time.time()) + ".log")
        self.logfile = log()
        return result

    def process_line(self, line: bytes, config):
        exl = 1
        for c in config:
            if c == "$" or c == "§":
                exl += 1
            elif c == "*":
                exl += 2
            else:
                raise ValueError("Invalid Config")
        if len(line) != exl:
            raise ValueError(
                f"Decompiler Error [006]: Length missmatch. Exspected {exl}, got {len(line)}"
            )
        chrs = [line[0]]
        line = line[1:]
        i = 0
        j = 0
        while i < len(config):
            if config[i] == "§" or config[i] == "$":
                chrs.append(line[j])
            elif config[i] == "*":
                chrs.append(256 * line[j] + line[j + 1])
                j += 1
            j += 1
            i += 1
        cmd = chrs.pop(0)
        for i in range(len(chrs)):
            if config[i] == "§":
                chrs[i] = self.getEnum(cmd)[chrs[i]]
        mask = self.getCommandMask(cmd)
        cmd = self.getCommandString(cmd)
        return mask.format(*tuple(chrs))

    def decompile(self, data: bytes) -> str:
        data = data[1:]
        lines = []
        result = ""
        i = 0
        while i < len(data):
            cmi = self.get_config(data[i])
            ll = 1
            for c in cmi:
                if c == "$" or c == "§":
                    ll += 1
                elif c == "*":
                    ll += 2
            lines.append(data[i : i + ll])
            i += ll
        for line in lines:
            result += self.process_line(line, self.get_config(line[0])) + "\n"
        result = result[:-1]
        return result


# Usage: a = compiler()
# a.comile(script: str, options: str="") -> bytes
# a.decomile(script: bytes) -> str
"""
script = "@ on_collect on 1 1\nset 0 = 20\ntp to 0 0\nend"
a = compiler()
print(a.compile(script))
print(a.decompile(a.compile(script, "--write_log")))
"""
