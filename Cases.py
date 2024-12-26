import json
from colorist import BrightColor, hex
from types import NoneType
class InvalidInput:
    pass

class CaseData:
    def __init__(self):
        with open ('skins.json', 'r') as infile:
            self._list = json.load(infile)

    def get_item_color(self, item_name):
        """Returns the hex value of the item requested"""
        skins_length = len(self._list)
        for i in range(0, skins_length):
            if self._list[i]['name'] == item_name:
                color = self._list[i]['rarity']['color']
        return color

    def see_case_contents(self, case_name):
        cases_length = len(self._list)
        case_contents = []
        for i in range(0, cases_length):
            current_line = self._list[i]['crates']
            for j in range (0, len(current_line)):
                if current_line[j]['name'] == case_name:
                    case_contents.append(self._list[i]['name'])
        return case_contents

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
        for item in matching_weapon_list:
            current_item = self.is_knife(item)
            for i in range (0, skins_length):
                if self._list[i]['name'] == item:
                    item_rarity = self.get_item_rarity(item)
                    if item_rarity == 'Contraband' or current_item == True:
                        contraband.append(item)
                    elif item_rarity == 'Covert':
                        covert.append(item)
                    elif item_rarity == 'Classified':
                        classified.append(item)
                    elif item_rarity == 'Restricted':
                        restricted.append(item)
                    elif item_rarity == 'Mil-Spec Grade':
                        mil_spec.append(item)
                    elif item_rarity == 'Industrial Grade':
                        industrial.append(item)
                    else:
                        consumer.append(item)

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

    def is_knife (self, item_name):
        """Takes an item name and determines if the item is a knife"""
        knife = False
        if "★" in item_name:
            knife = True
        return knife

    def get_item_rarity(self, item_name):
        """Returns the rarity of an item"""
        skins_length = len(self._list)
        for i in range(0, skins_length):
            if item_name == self._list[i]['name']:
                item_rarity = self._list[i]['rarity']['name']
        return item_rarity

    def display(self, matching_weapon_list):
        """Prints matching weapons list in a more readable format"""
        new_matching_weapon_list = self.sort_list(matching_weapon_list)
        print("Skins:")
        for item in new_matching_weapon_list:
            current_item = self.is_knife(item)
            if current_item:
                hex(item, '#e4ae39')
            else:
                color = self.get_item_color(item)
                hex(item, color)

cd = CaseData()
try:
    case = cd.see_case_contents('Operation Bravo Case')
    cd.display(case)

except InvalidInput:
    print("User entered an invalid input.  Please Try Again!")