from webweb import Web
import json

web = Web(
    adjacency=[
        [61, 1],
        [1, 2],
        [61, 4],
        [1, 5],
        [5, 6],
        [6, 7],
        [8, 9],
        [11, 12],
        [11, 4],
        [12, 4],
        [14, 15],
        [15, 5],
        [16, 15],
        [16, 17],
        [18, 19],
        [19, 20],
        [20, 21],
        [22, 4],
        [22, 19],
        [21, 19],
        [21, 23],
        [24, 4],
        [24, 25],
        [26, 27],
        [26, 28],
        [29, 23],
        [21, 29],
        [30, 2],
        [30, 5],
        [31, 32],
        [31, 33],
        [27, 4],
        [34, 20],
        [34, 36],
        [34, 37],
        [35, 36],
        [17, 29],
        [17, 8],
        [24, 19],
        [38, 35],
        [38, 4],
        [39, 28],
        [39,38],
        [40,28],
        [13, 36],
        [27,12],
        [7,32],
        [3,32],
        [19,4],
        [41, 2],
        [42,35],
        [43,5],
        [43,44],
        [45, 3],
        [45,46],
        [46, 4],
        [53,54],
        [55,28],
        [55, 21],
        [2,54],
        [58, 4],
        [58,30],
        [60, 2],
        [46, 59],
        [62, 58],
        [62, 43],
        [63, 60],
        [65,64],
        [65, 46],
        [66, 35],
        [67, 64],
        [64, 4],
        [69, 63],
        [70,13],
        [71, 32],
        [74, 63],
        [74, 5],
        [83,38],
        [79, 4],
        [82, 25],
        [82,48],
        [48, 89],
        [78,38]
    ],
    display={
        "metadata": {
            "Zone": {"values": ["1. Twilight", "2. Dusk", "3. Gloom", "4. Shadow", "5. Void"]}
        },
        "nodes": {
            1: {
                "name": "The Great Sharay",
                "Zone": "3. Gloom",
            },
            2: {
                "name": "Skeletal Fisherman",
                "Zone": "2. Dusk",
            },
            3: {
                "name": "Enchanted Forest",
                "Zone": "1. Twilight",
            },
            4: {
                "name": "Depths of the Mind",
                "Zone": "5. Void",
            },
            5: {
                "name": "The Final Gauntlet",
                "Zone": "5. Void",
            },
            6: {
                "name": "Fzhbl",
                "Zone": "3. Gloom",
            },
            7: {
                "name": "Sword Wraith Warrior",
                "Zone": "1. Twilight",
            },
            8: {
                "name": "Roper Cavern",
                "Zone": "3. Gloom",
            },
            9: {
                "name": "The Mephitic Swamp",
                "Zone": "4. Shadow",
            },
            10: {
                "name": "Empty Castle Town",
                "Zone": "2. Dusk",
            },
            11: {
                "name": "The Mindflayer Outpost",
                "Zone": "3. Gloom",
            },
            12: {
                "name": "Dungeon of the Smiling One",
                "Zone": "4. Shadow",
            },
            13: {
                "name": "The Rot",
                "Zone": "2. Dusk",
            },
            14: {
                "name": "The Pit",
                "Zone": "1. Twilight",
            },
            15: {
                "name": "The Guild of Gloom",
                "Zone": "3. Gloom",
            },
            16: {
                "name": "Cave Spring",
                "Zone": "2. Dusk",
            },
            17: {
                "name": "Final Betrayal",
                "Zone": "5. Void",
            },
            18: {
                "name": "Oblex Party",
                "Zone": "2. Dusk",
            },
            19: {
                "name": "Juiblex's Plans",
                "Zone": "5. Void",
            },
            20: {
                "name": "Sulfurous Invasion",
                "Zone": "1. Twilight",
            },
            21: {
                "name": "Gnomish Village",
                "Zone": "2. Dusk",
            },
            22: {
                "name": "Baby Oblex",
                "Zone": "1. Twilight",
            },
            23: {
                "name": "Naga Hostages",
                "Zone": "2. Dusk",
            },
            24: {
                "name": "Behomoth Ooze",
                "Zone": "1. Twilight",
            },
            25: {
                "name": "Master of Golems",
                "Zone": "3. Gloom",
            },
            26: {
                "name": "Lost Goblins",
                "Zone": "1. Twilight",
            },
            27: {
                "name": "Tadpoles on the Mind",
                "Zone": "4. Shadow",
            },
            28: {
                "name": "The Broken Mountains",
                "Zone": "3. Gloom",
            },
            29: {
                "name": "Yuan-ti Ruins",
                "Zone": "3. Gloom",
            },
            30: {
                "name": "Th'lxi the Scourge",
                "Zone": "1. Twilight",
            },
            31: {
                "name": "Ghost of a Drow Samurai",
                "Zone": "1. Twilight",
            },
            32: {
                "name": "The Valley of Spirits",
                "Zone": "2. Dusk",
            },
            33: {
                "name": "Ruins of YYY",
                "Zone": "3. Gloom",
            },
            34: {
                "name": "Stalking Nothic",
                "Zone": "1. Twilight",
            },
            35: {
                "name": "Orcus Stuff",
                "Zone": "5. Void",
            },
            36: {
                "name": "Shrine of Orcus",
                "Zone": "4. Shadow",
            },
            37: {
                "name": "Mystery of the Tanaruks",
                "Zone": "2. Dusk",
            },
            38: {
                "name": "Silere the Absolute",
                "Zone": "4. Shadow",
            },
            39: {
                "name": "Waking Up",
                "Zone": "4. Shadow",
            },
            40: {
                "name": "Drow Hamlet",
                "Zone": "2. Dusk",
            },
            41: {
                "name": "Bottomless Valley",
                "Zone": "3. Gloom",
            },
            42: {
                "name": "The Words of Orcus",
                "Zone": "2. Dusk",
            },
            43: {
                "name": "Purple Worm Nest",
                "Zone": "3. Gloom",
            },
            44: {
                "name": "Purple Worm Crossing",
                "Zone": "2. Dusk",
            },
            45: {
                "name": "Colony of Myconids",
                "Zone": "1. Twilight",
            },
            46: {
                "name": "Death of a Colony",
                "Zone": "2. Dusk",
            },
            47: {
                "name": "Migrant Caravan",
                "Zone": "2. Dusk",
            },
            48: {
                "name": "Gaol of the Forsaken",
                "Zone": "4. Shadow",
            },
            49: {
                "name": "Void Oblex",
                "Zone": "5. Void",
            },
            50: {
                "name": "Temple of Demogorgon",
                "Zone": "4. Shadow",
            },
            51: {
                "name": "Inverted Pyramid",
                "Zone": "4. Shadow",
            },
            52: {
                "name": "Hierophant of Annihilation",
                "Zone": "4. Shadow",
            },
            53: {
                "name": "Charon's New Deal",
                "Zone": "5. Void",
            },
            54: {
                "name": "Ocean of Anguish",
                "Zone": "5. Void",
            },
            55: {
                "name": "Nightmare of Reality",
                "Zone": "2. Dusk",
            },
            56: {
                "name": "Wraith Hunters",
                "Zone": "2. Dusk",
            },
            57: {
                "name": "Gar'god's Libray",
                "Zone": "4. Shadow",
            },
            58: {
                "name": "Sapphire Veins",
                "Zone": "4. Shadow",
            },
            59: {
                "name": "Establishing Home",
                "Zone": "1. Twilight",
            },
            60: {
                "name": "Below the Lava",
                "Zone": "5. Void",
            },
            61: {
                "name": "Kua Toa Village",
                "Zone": "1. Twilight",
            },
            62: {
                "name": "Xorn Slaver",
                "Zone": "3. Gloom",
            },
            63: {
                "name": "Sands of Inferno",
                "Zone": "5. Void",
            },
            64: {
                "name": "Infected Solar",
                "Zone": "5. Void",
            },
            65: {
                "name": "Zuggtmoy's Plan",
                "Zone": "5. Void",
            },
            66: {
                "name": "A man and his horse",
                "Zone": "4. Shadow",
            },
            67: {
                "name": "Last of the Trio",
                "Zone": "4. Shadow",
            },
            68: {
                "name": "Boreal Mire of Necrosis",
                "Zone": "3. Gloom",
            },
            69: {
                "name": "Volcanic Breach",
                "Zone": "5. Void",
            },
            70: {
                "name": "Bizarre Bazaar",
                "Zone": "1. Twilight",
            },
            71: {
                "name": "Tomb of a Fallen Warrior",
                "Zone": "1. Twilight",
            },
            72: {
                "name": "Phantasmal Cliffs",
                "Zone": "3. Gloom",
            },
            73: {
                "name": "Permafrost Explosion",
                "Zone": "4. Shadow",
            },
            74: {
                "name": "Tornado Alley",
                "Zone": "3. Gloom",
            },
            75: {
                "name": "Shapeshifter City",
                "Zone": "2. Dusk",
            },
            76: {
                "name": "Fighting Pits of Pandemonium",
                "Zone": "3. Gloom",
            },
            77: {
                "name": "Darkroot Depths",
                "Zone": "3. Gloom",
            },
            78: {
                "name": "Sanctuary of Silence",
                "Zone": "4. Shadow",
            },
            79: {
                "name": "Crashed Ship",
                "Zone": "5. Void",
            },
            80: {
                "name": "Mine your Business",
                "Zone": "1. Twilight",
            },
            81: {
                "name": "Moloch's Scheme",
                "Zone": "5. Void",
            },
            82: {
                "name": "The Chase",
                "Zone": "4. Shadow",
            },
            83: {
                "name": "Workshop and Prison",
                "Zone": "1. Twilight",
            },
            84: {
                "name": "Lone Neogi",
                "Zone": "1. Twilight",
            },
            85: {
                "name": "Brain on the Menu",
                "Zone": "3. Gloom",
            },
            86: {
                "name": "Bobbing Light",
                "Zone": "4. Shadow",
            },
            87: {
                "name": "The God of Doors",
                "Zone": "5. Void",
            },
            88: {
                "name": "Crypt of Fate",
                "Zone": "2. Dusk",
            },
            89: {
                "name": "Deepbreach",
                "Zone": "2. Dusk",
            },
        },
    },
)
if __name__ == "__main__":
    web.display.colorBy = "Zone"
    web.display.charge = 100
    web.display.linkStrength = 0.2
    web.display.linkLength = 30
    web.display.colorPalette = "Greys"

    web.display.attachWebwebToElementWithId = 'encounterMap'
    # web.show()
    with open('src/stores/viz.json', 'w') as f:
        json.dump(web.json, f)

