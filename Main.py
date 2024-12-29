import tkinter as tk
from tkinter import ttk
from Skins import SkinData
from Cases import CaseData

def main():
    root = tk.Tk()

    #Configures the title of the window
    root.title("Find CSGO Skins")

    #Configures the button in the window
    button = tk.Button(root, text="Search", width=15)
    button.pack()

    #Maintains the window after running the script
    root.mainloop()

def select(event):
    """Controls the dropdown for the skin search function in the tkinter window"""
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Search for a weapon skin")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["AK-47", "AUG", "AWP", "Bayonet", "Bowie Knife", "Butterfly Knife", "Classic Knife", "CZ75-Auto", "Desert Eagle", "Dual Berettas", "Falchion Knife", "FAMAS",
                                       "Flip Knife", "Five-Seven", "G3SG1", "Gut Knife", "Galil AR", "Glock-18", "Huntsman Knife", "Karambit", "Kukri Knife", "M249", "M4A4", "M4A1-S", "M9 Bayonet",
                                       "MAC-10", "MAG-7", "MP5-SD", "MP7", "MP9", "Navaja Knife", "Negev", "Nomad Knife", "Nova", "P2000", "P250", "P90", "Paracord Knife", "PP-Bizon",
                                       "R8 Revolver", "Sawed-Off", "Scar-20", "SG 553", "Shadow Daggers", "Skeleton Knife", "SSG 08", "Stiletto Knife", "Survival Knife", "Talon Knife", "Tec-9",
                                       "UMP-45","Ursus Knife", "USP-S", "XM1014", "Zeus x27"])
combo_box.pack(pady=5)

# Set default value
combo_box.set("Select a Weapon")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()


if __name__ == "__main__":
    main()