import json
from colorist import BrightColor, hex
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

    def display(self, case_contents):
        """Prints matching weapons list in a more readable format"""
        print("Skins:")
        for item in case_contents:
            color = self.get_item_color(item)
            hex(item, color)

cd = CaseData()
try:
    case = cd.see_case_contents('Operation Bravo Case')
    cd.display(case)

except InvalidInput:
    print("User entered an invalid input.  Please Try Again!")