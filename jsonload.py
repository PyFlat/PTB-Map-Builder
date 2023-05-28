import json
from compressor import *
class ptbload():
    li = [[None for i in range(25)] for j in range(25)]
    scripts = None
    texts = None
    def load_ptb(file):
        com = compressor()
        com.load(file)
        com.decompress()
        data = ptbload.convert_json(com.get_data())
        return ptbload.get_json()
    def convert_json(json_data):
        data = json.dumps(json_data[0])
        data = json.loads(data)["world"]
        ptbload.scripts = json_data[1]
        ptbload.texts = json.dumps(json_data[0])
        ptbload.texts = json.loads(ptbload.texts)["texts"]
        #print(json_data)
        for x in range(25):
            for y in range(25):
                temp = data[x][y]
                if temp["id"] == 0:
                    ptbload.li[x][y] = 1
                elif temp["id"] == -1:
                    ptbload.li[x][y] = None
                elif temp["id"] == 2:
                    ptbload.li[x][y] = 0
                elif temp["id"] == 3:
                    ptbload.li[x][y] = 3
                elif temp["id"] == 4:
                    ptbload.li[x][y] = 2
                elif temp["id"] == 5:
                    if temp["objectData"]["start"] == 450:
                        ptbload.li[x][y] = 4
                    elif temp["objectData"]["start"] == 700:
                        ptbload.li[x][y] = 5
                    elif temp["objectData"]["start"] == 900:
                        ptbload.li[x][y] = 6
                    elif temp["objectData"]["start"] == 20:
                        ptbload.li[x][y] = 7
                    elif temp["objectData"]["start"] == 150:
                        ptbload.li[x][y] = 8
                    elif temp["objectData"]["start"] == 55:
                        ptbload.li[x][y] = 9
                    elif temp["objectData"]["start"] == 80:
                        ptbload.li[x][y] = 11
                    elif temp["objectData"]["start"] == 0:
                        ptbload.li[x][y] = 12
                    elif temp["objectData"]["start"] == 260:
                        ptbload.li[x][y] = 13
                elif temp["id"] == 6:
                    ptbload.li[x][y] = [10, temp["objectData"]["health"],temp["objectData"]["id2"],temp["objectData"]["id1"]]
    def get_json():
        return (ptbload.li, ptbload.scripts, ptbload.texts)
class jsonload():
    li = [[None for i in range(25)] for j in range(25)]
    scripts = None
    texts = None
    def load_json(file):
        data = json.loads(open(file, "r").read())["world"]
        scripts = json.loads(open(file, "r").read())["scripts"]
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
                    jsonload.li[x][y] = 3
                elif temp["id"] == 4:
                    jsonload.li[x][y] = 2
                elif temp["id"] == 5:
                    if temp["objectData"]["start"] == 450:
                        jsonload.li[x][y] = 4
                    elif temp["objectData"]["start"] == 700:
                        jsonload.li[x][y] = 5
                    elif temp["objectData"]["start"] == 900:
                        jsonload.li[x][y] = 6
                    elif temp["objectData"]["start"] == 20:
                        jsonload.li[x][y] = 7
                    elif temp["objectData"]["start"] == 150:
                        jsonload.li[x][y] = 8
                    elif temp["objectData"]["start"] == 55:
                        jsonload.li[x][y] = 9
                    elif temp["objectData"]["start"] == 80:
                        ptbload.li[x][y] = 11
                    elif temp["objectData"]["start"] == 0:
                        ptbload.li[x][y] = 12
                    elif temp["objectData"]["start"] == 260:
                        ptbload.li[x][y] = 13
                elif temp["id"] == 6:
                    jsonload.li[x][y] = [10, temp["objectData"]["health"],temp["objectData"]["id2"], temp["objectData"]["extra1"], temp["objectData"]["extra2"]]
        return jsonload.get_json()
    def get_json():
        return (jsonload.li, jsonload.scripts, jsonload.texts)
