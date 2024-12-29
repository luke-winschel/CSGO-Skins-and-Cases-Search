import json
from types import NoneType
from colorist import BrightColor, hex, ColorHex

class InvalidInput:
    pass

class SkinData:
    def __init__(self):
        """Opens the json file for other functions to read from"""
        with open ('skins.json', 'r') as infile:
            self._list = json.load(infile)
            self._matching_weapon_list = []

    def search_by_weapon (self, weapon):
        """Finds matching skins by weapon"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range (0, skins_length):
            if self._list[i]['weapon']['name'] == weapon:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_stattrack(self, stattrak):
        """Finds matching skins by stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_rarity(self, rarity):
        """Finds skins by rarity"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_rarity_and_weapon(self, rarity, weapon):
        """Finds Skins by weapon type and rarity"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity and self._list[i]['weapon']['name'] == weapon:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_rarity_and_stattrak(self, rarity, stattrak):
        """Finds Skins by weapon type and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity and self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_weapon_and_stattrak(self, weapon, stattrak):
        """Finds Skins by weapon type and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['weapon']['name'] == weapon and self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def search_by_weapon_rarity_stattrakk(self, weapon, rarity, stattrak):
        """Finds skins by weapon, rarity, and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['weapon']['name'] == weapon and self._list[i]['stattrak'] == stattrak and self._list[i]['rarity']['name'] == rarity:
                matching_weapon_list.append(self._list[i]['id'])
        return matching_weapon_list

    def get_name(self, id):
        """Finds the name of a skin from the Skin ID"""
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if id == self._list[i]['id']:
                name = self._list[i]['name']
        return name

    def find_case(self, id):
        """Finds the cases that an item can be inside"""
        case_list = []
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if id == self._list[i]['id']:
                cases = self._list[i]['crates']
                if cases == []:
                    case_list.append("There are no available cases for this weapon!")
                else:
                    for j in range (0, len(cases)):
                        case_list.append(cases[j]['name'])
        return case_list

    def is_knife (self, id):
        """Takes an item name and determines if the item is a knife"""
        skins_length = len(self._list)
        knife = False
        for i in range (0, skins_length):
            if id == self._list[i]['id']:
                if self._list[i]['category']['name'] == 'Knives':
                    knife = True
        return knife

    def is_doppler(self, id):
        """Returns the phase of the doppler for skin clarification"""
        doppler = False
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if id == self._list[i]['id']:
                name = self._list[i]['name']
                if "Doppler" in name:
                    doppler = True
        return doppler

    def get_phase(self, id):
        """Returns the name of an items skin pattern"""
        skins_length = len(self._list)
        for i in range(0, skins_length):
            if id == self._list[i]['id']:
                skin_phase = self._list[i]['phase']
        return skin_phase

    def get_item_rarity(self, id):
        """Returns the rarity of an item"""
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if id == self._list[i]['id']:
                item_rarity = self._list[i]['rarity']['name']
        return item_rarity

    def get_item_color (self, id):
        """Returns the hex value of the item requested"""
        gold = ColorHex ("#e4ae39")
        red = ColorHex ("#eb4b4b")
        pink = ColorHex ("#d32ce6")
        purple = ColorHex ("#8847ff")
        blue = ColorHex ("#4b69ff")
        light_blue = ColorHex ("#5e98d9")
        white = ColorHex ("#b0c3d9")
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if self._list[i]['id'] == id:
                color = self._list[i]['rarity']['color']
                if color == "#e4ae39" or self.is_knife(id) == True:
                    item_color = gold
                    break
                if color == "#eb4b4b":
                    item_color = red
                    break
                if color == "#d32ce6":
                    item_color = pink
                    break
                if color == "#8847ff":
                    item_color = purple
                    break
                if color == "#4b69ff":
                    item_color = blue
                    break
                if color == "#5e98d9":
                    item_color = light_blue
                    break
                if color == "#b0c3d9":
                    item_color = white
                    break
        return item_color

    def sort_list(self, matching_weapon_list):
        """Sorts lists alphabetically and by item rarities"""
        new_matching_weapons_list = []
        contraband = []
        covert = []
        classified = []
        restricted = []
        mil_spec = []
        industrial = []
        consumer = []
        skins_length = len(self._list)
        for id in matching_weapon_list:
            current_item = self.is_knife(id)
            for i in range (0, skins_length):
                if self._list[i]['id'] == id:
                    item_rarity = self.get_item_rarity(id)
                    if item_rarity == 'Contraband' or current_item == True:
                        contraband.append(id)
                    elif item_rarity == 'Covert':
                        covert.append(id)
                    elif item_rarity == 'Classified':
                        classified.append(id)
                    elif item_rarity == 'Restricted':
                        restricted.append(id)
                    elif item_rarity == 'Mil-Spec Grade':
                        mil_spec.append(id)
                    elif item_rarity == 'Industrial Grade':
                        industrial.append(id)
                    else:
                        consumer.append(id)

        new_contraband = sorted(contraband)
        new_covert = sorted(covert)
        new_classified = sorted(classified)
        new_restricted = sorted(restricted)
        new_mil_spec = sorted(mil_spec)
        new_industrial = sorted(industrial)
        new_consumer = sorted(consumer)

        if new_contraband is not NoneType:
            new_matching_weapons_list.extend(new_contraband)
        if new_covert is not NoneType:
            new_matching_weapons_list.extend(new_covert)
        if new_classified is not NoneType:
            new_matching_weapons_list.extend(new_classified)
        if new_restricted is not NoneType:
            new_matching_weapons_list.extend(new_restricted)
        if new_mil_spec is not NoneType:
            new_matching_weapons_list.extend(new_mil_spec)
        if new_industrial is not NoneType:
            new_matching_weapons_list.extend(new_industrial)
        if new_consumer is not NoneType:
            new_matching_weapons_list.extend(new_consumer)

        return new_matching_weapons_list

    def remove_duplicates(self, case_list):
            list_2 = []
            for i in range(0, len(case_list)):
                index = case_list[i]
                if index not in list_2:
                    list_2.append(index)
            list_2.sort()
            return list_2

    def display(self, matching_weapon_list):
        """Prints matching weapons list in a more readable format"""
        new_matching_weapon_list = self.sort_list(matching_weapon_list)
        for id in new_matching_weapon_list:
            cases = self.find_case(id)
            refined_cases = self.remove_duplicates(cases)
            color = self.get_item_color(id)
            item = self.get_name(id)
            if self.is_knife(id) and self.is_doppler(id) == True:
                phase = self.get_phase(id)
                print(f"{color}{item} {phase}{color.OFF}, can be found in:")
            else:
                print(f"{color}{item}{color.OFF}, can be found in:")
            for i in range (len(refined_cases)):
                print("\t", refined_cases[i])
            print()


sd = SkinData()
try:
    test = sd.search_by_weapon("Talon Knife")
    sd.display(test)
except InvalidInput:
    print("No matching value!")