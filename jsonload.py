import json
import easygui


class jsonload():
    li = [[None for i in range(25)] for j in range(25)]
    def load_json():
        file = easygui.fileopenbox()
        data = json.loads(open(file, "r").read())["world"]
        scriptdata = json.loads(open(file, "r").read())["scripts"]
        texts = json.loads(open(file, "r").read())["texts"]
        for x in range(25):
            for y in range(25):
                temp = data[x][y]
                if temp["id"] == 0:
                    jsonload.li[x][y] = 1
                elif temp["id"] == -1:
                    jsonload.li[x][y] = None
                elif temp["id"] == 2:
                    jsonload.li[x][y] = 0
                elif temp["id"] == 3:
                    jsonload.li[x][y] = 4
                elif temp["id"] == 4:
                    jsonload.li[x][y] = 3
                elif temp["id"] == 5:
                    if temp["objectData"]["start"] == 300:
                        jsonload.li[x][y] = 5
                    elif temp["objectData"]["start"] == 550:
                        jsonload.li[x][y] = 6
                    elif temp["objectData"]["start"] == 800:
                        jsonload.li[x][y] = 7
                    elif temp["objectData"]["start"] == 0:
                        jsonload.li[x][y] = 8
                    elif temp["objectData"]["start"] == 60:
                        jsonload.li[x][y] = 9
                    elif temp["objectData"]["start"] == 950:
                        jsonload.li[x][y] = 10
                    elif temp["objectData"]["start"] == 30:
                        jsonload.li[x][y] = 11
                elif temp["id"] == 6:
                    jsonload.li[x][y] = [12, temp["objectData"]["health"],temp["objectData"]["id2"], temp["objectData"]["extra1"], temp["objectData"]["extra2"]]
    def get_json():
        return jsonload.li
