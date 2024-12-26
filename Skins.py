import json

from colorist import BrightColor, hex
class InvalidInput:
    pass

class SkinData:
    def __init__(self):
        with open ('skins.json', 'r') as infile:
            self._list = json.load(infile)
            self._matching_weapon_list = []

    def is_knife (self, item_name):
        """Takes an item name and determines if the item is a knife"""
        knife = False
        if "★" in item_name:
            knife = True
        return knife

    def get_item_color (self, item_name):
        """Returns the hex value of the item requested"""
        skins_length = len(self._list)
        for i in range (0, skins_length):
            if self._list[i]['name'] == item_name:
                color = self._list[i]['rarity']['color']
        return color

    def get_matching_weapon_list(self):
        """Returns matching weapons list"""
        return self._matching_weapon_list()

    def search_by_weapon (self, weapon):
        """Finds matching skins by weapon"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range (0, skins_length):
            if self._list[i]['weapon']['name'] == weapon:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_stattrack(self, stattrak):
        """Finds matching skins by stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_rarity(self, rarity):
        """Finds skins by rarity"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_rarity_and_weapon(self, rarity, weapon):
        """Finds Skins by weapon type and rarity"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity and self._list[i]['weapon']['name'] == weapon:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_rarity_and_stattrak(self, rarity, stattrak):
        """Finds Skins by weapon type and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['rarity']['name'] == rarity and self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_weapon_and_stattrak(self, weapon, stattrak):
        """Finds Skins by weapon type and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['weapon']['name'] == weapon and self._list[i]['stattrak'] == stattrak:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def search_by_weapon_rarity_stattrakk(self, weapon, rarity, stattrak):
        """Finds skins by weapon, rarity, and stattrak"""
        skins_length = len(self._list)
        matching_weapon_list = []
        for i in range(0, skins_length):
            if self._list[i]['weapon']['name'] == weapon and self._list[i]['stattrak'] == stattrak and self._list[i]['rarity']['name'] == rarity:
                matching_weapon_list.append(self._list[i]['name'])
        return matching_weapon_list

    def sort_list(self, matching_weapon_list):
        """Sorts lists alphabetically and by item rarities"""
        #break down lists by rarity, sort alphabetically and merge back into one list?



    def display(self, matching_weapon_list):
        """Prints matching weapons list in a more readable format"""
        print("Skins:")
        for item in matching_weapon_list:
            current_item = self.is_knife(item)
            if current_item == True:
                hex(item, '#e4ae39')
            else:
                color = self.get_item_color(item)
                hex(item, color)

sd = SkinData()
try:
    #Tests the weapon search function.
    #Returns all the M4A4 Skins from the linked Json file
    #skins = sd.search_by_weapon('M4A4')
    #sd.display(skins)

    #Tests the search by stattrak function
    #Returns all weapons that are stattrak from the linked Json file
    skins2 = sd.search_by_stattrack(True)
    sd.display(skins2)

    #Tests the Search by rarity function
    #Returns all weapons that have an Industrial Grade Rarity from the linked Json file
    #skins3 = sd.search_by_rarity('Industrial Grade')
    #sd.display(skins3)

    #Testst the search by rarity and weapon function
    #Returns all weapons that are M4A4 and have an industrial grade rarity
    #skins4 = sd.search_by_rarity_and_weapon('Industrial Grade', 'M4A4')
    #sd.display(skins4)

    #Tests the Search by rarity and stattrak function
    #Returns all weapons that have a Mil-Spec Grade rarity and are stattrak
    #skins5 = sd.search_by_rarity_and_stattrak('Mil-Spec Grade', True)
    #sd.display(skins5)

    #Tests the Search by weapon and stattrak
    #Returns all weapons that are M4A4 and are stattrak
    #skins6 = sd.search_by_weapon_and_stattrak('M4A4', True)
    #sd.display(skins6)

    #Tests the Search by weapon, rarity, and stattrack function
    #Returns all weapons that are M4A4, have an industrial grade rarity and are not stattrak
    #skins7 = sd.search_by_weapon_rarity_stattrakk('M4A4', 'Industrial Grade', False)
    #sd.display(skins7)

except InvalidInput:
    print("User entered an invalid input.  Please Try Again!")
