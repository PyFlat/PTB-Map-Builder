import json
from src.compressor import *
class PtbLoad():
    li = [[None for i in range(25)] for j in range(25)]
    scripts = None
    texts = None
    def load_ptb(file):
        com = compressor()
        com.load(file)
        com.decompress()
        data = PtbLoad.convert_json(com.get_data())
        return PtbLoad.get_json()
    def convert_json(json_data):
        data = json.dumps(json_data[0])
        data = json.loads(data)["world"]
        PtbLoad.scripts = json_data[1]
        PtbLoad.texts = json.dumps(json_data[0])
        PtbLoad.texts = json.loads(PtbLoad.texts)["texts"]
        id_mapping = {
            0: 1, -1: None, 2: 0, 3: 3, 4: 2, 5: {450: 4,700: 5,900: 6,20: 7,150: 8,55: 9,80: 11,0: 12,260: 13},
            6: lambda temp: [10, temp["objectData"]["health"], temp["objectData"]["id2"], temp["objectData"]["id1"]]
        }

        for x in range(25):
            for y in range(25):
                temp = data[x][y]
                id_map = id_mapping.get(temp["id"])
                if id_map is not None:
                    if isinstance(id_map, int):
                        PtbLoad.li[x][y] = id_map
                    elif isinstance(id_map, dict):
                        PtbLoad.li[x][y] = id_map.get(temp["objectData"]["start"])
                    else:
                        PtbLoad.li[x][y] = id_map(temp)

    def get_json():
        return (PtbLoad.li, PtbLoad.scripts, PtbLoad.texts)
