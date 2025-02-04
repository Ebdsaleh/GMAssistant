# src/core/tables.py

"""
This file will hold all the core meaning tables from the Mythic Game Master Emulator
"""

class MeaningTables:
    def __init__(self):
        self.action_1 = self.create_action_table_1()
        self.action_2 = self.create_action_table_2()
        self.descriptor_1 = self.create_descriptor_table_1()
        self.descriptor_2 = self.create_descriptor_table_2()
        self.elements = self.create_elements_table()
        self.character_names = self.create_character_names_table()
        self.weapon_names = self.create_weapon_names_table()
        self.location_names = self.create_location_names_table()

    def create_action_table_1(self):
        action_table_1 = {
            1: "Abandon", 2: "Accompany", 3: "Activate", 4: "Agree", 5: "Ambush",
            6: "Arrive",  7: "Assist", 8: "Attack", 9: "Attain", 10: "Bargain",
            11: "Befriend", 12: "Bestow", 13: "Betray", 14: "Block", 15: "Break",
            16: "Carry", 17: "Celebrate", 18: "Change", 19: "Close", 20: "Combine",
            21: "Communicate", 22: "Conceal", 23: "Continue", 24: "Control", 25: "Create",
            26: "Deceive", 27: "Decrease", 28: "Defend", 29: "Delay", 30: "Deny",
            31: "Depart", 32: "Deposit", 33: "Destroy", 34: "Dispute", 35: "Disrupt",
            36: "Distrust", 37: "Divide", 38: "Drop", 39: "Easy", 40: "Energize",
            41: "Escape", 42: "Expose", 43: "Fail", 44: "Fight", 45: "Flee",
            46: "Free", 47: "Guide", 48: "Harm", 49: "Heal", 50: "Hinder",
            51: "Imitate", 52: "Impression", 53: "Increase", 54: "Indulge", 55: "Inform",
            56: "Inquire", 57: "Inspect", 58: "Invade", 59: "Leave", 60: "Lure",
            61: "Misuse", 62: "Move", 63: "Neglect", 64: "Observe", 65: "Open",
            66: "Oppose", 67: "Overthrow", 68: "Praise", 69: "Proceed", 70: "Protect",
            71: "Punish", 72: "Pursue", 73: "Recruit", 74: "Refuse", 75: "Release",
            76: "Relinquish", 77: "Repair", 78: "Repulse", 79: "Return", 80: "Reward",
            81: "Ruin", 82: "Separate", 83: "Start", 84: "Stop", 85: "Strange",
            86: "Struggle", 87: "Succeed", 88: "Support", 89: "Supress", 90: "Take",
            91: "Threaten", 92: "Transform", 93: "Trap", 94: "Travel", 95: "Triumph",
            96: "Truce", 97: "Trust", 98: "Use", 99: "Usurp", 100: "Waste",
        }
        return action_table_1

    def create_action_table_2(self):
        action_table_2 = {
            1: "Advantage", 2: "Adversity", 3: "Agreement", 4: "Animal", 5: "Attention",
            6: "Balance", 7: "Battle", 8: "Benefits", 9: "Building", 10: "Burden",
            11: "Bureaucracy", 12: "Business", 13: "Chaos", 14: "Comfort", 15: "Completion",
            16: "Conflict", 17: "Cooperation", 18: "Danger", 19: "Defense", 20: "Depletion",
            21: "Disadvantage", 22: "Distraction", 23: "Elements", 24: "Emotion", 25: "Enemy",
            26: "Energy", 27: "Environment", 28: "Expectation", 29: "Exterior", 30: "Extravagance",
            31: "Failure", 32: "Fame", 33: "Fear", 34: "Freedom", 35: "Friend",
            36: "Goal", 37: "Group", 38: "Health", 39: "Hinderance", 40: "Home",
            41: "Hope", 42: "Idea", 43: "Illness", 44: "Illusion", 45: "Individual",
            46: "Information", 47: "Innocent", 48: "Intellect", 49: "Interior", 50: "Investment",
            51: "Leadership", 52: "Legal", 53: "Location", 54: "Military", 55: "Misfortune",
            56: "Mundane", 57: "Nature", 58: "Needs", 59: "News", 60: "Normal",
            61: "Object", 62: "Obscurity", 63: "Official", 64: "Opposition", 65: " Outside",
            66: "Pain", 67: "Path", 68: "Peace", 69: "People", 70: "Personal",
            71: "Physical", 72: "Plot", 73: "Portal", 74: "Possessions", 75: "Poverty",
            76: "Power", 77: "Prison", 78: "Project", 79: "Protection", 80: "Reassurance",
            81: "Representative", 82: "Riches", 83: "Safety", 84: "Strength", 85: "Success",
            86: "Suffering", 87: "Surprise", 88: "Tactic", 89: "Technology", 90: "Tension",
            91: "Time", 92: "Trial", 93: "Value", 94: "Vehicle", 95: "Victory",
            96: "Vulnerability", 97: "Weapon", 98: "Weather", 99: "Work", 100: "Wound",
        }
        return action_table_2

    def create_descriptor_table_1(self):
        descriptor_table_1 = {
            1: "Adventurously", 2: "Aggressively", 3: "Anxiously", 4: "Awkwardly", 5: "Beautifully",
            6: "Bleakly", 7: "Boldly", 8: "Bravely", 9: "Busily", 10: "Calmly",
            11: "Carefully", 12: "Carelessly", 13: "Cautiously", 14: "Ceaselessly", 15: "Cheerfully",
            16: "Combative", 17: "Cooly", 18: "Crazily", 19: "Curiously", 20: "Dangerously",
            21: "Defiantly", 22: "Deliberately", 23: "Delicately", 24: "Delightfully", 25: "Dimly",
            26: "Efficiently", 27: "Emotionally", 28: "Energetically", 29: "Enormously", 30: "Enthusiastically",
            31: "Excitedly", 32: "Fearfully", 33: "Ferociously", 34: "Fiercely", 35: "Foolishly",
            36: "Fortunately", 37: "Frantically", 38: "Freely", 39: "Frighteningly", 40: "Fully",
            41: "Generously", 42: "Gently", 43: "Gladly", 44: "Gracefully", 45: "Gratefully",
            46: "Happily", 47: "Hastily", 48: "Healthily", 49: "Helpfully", 50: "Helplessly",
            51: "Hopelessly", 52: "Innocently", 53: "Intensely", 54: "Interestingly", 55: "Irritatingly",
            56: "Joyfully", 57: "Kindly", 58: "Lazily", 59: "Lightly", 60: "Loosely",
            61: "Loudly", 62: "Lovingly", 63: "Loyalty", 64: "Majestically", 65: "Meaningfully",
            66: "Mechanically", 67: "Mildly", 68: "Miserably", 69: "Mockingly", 70: "Mysteriously",
            71: "Naturally", 72: "Neatly", 73: "Nicely", 74: "Oddly", 75: "Offensively",
            76: "Officially", 77: "Partially", 78: "Passively", 79: "Peacefully", 80: "Perfectly",
            81: "Playfully", 82: "Politely", 83: "Positively", 84: "Powerfully", 85: "Quaintly",
            86: "Quarrelsome", 87: "Quietly", 88: "Roughly", 89: "Rudely", 90: "Ruthlessly",
            91: "Slowly", 92: "Softly", 93: "Strangely", 94: "Swiftly", 95: "Threateningly",
            96: "Timidly", 97: "Very", 98: "Violently", 99: "Wildly", 100: "Yieldingly"
        }
        return descriptor_table_1

    def create_descriptor_table_2(self):
        descriptor_table_2 = {
            1: "Abnormal", 2: "Amusing", 3: "Artificial", 4: "Average", 5: "Beautiful",
            6: "Bizarre", 7: "Boring", 8: "Bright", 9: "Broken", 10: "Clean",
            11: "Cold", 12: "Colorful", 13: "Colorless", 14: "Comforting", 15: "Creepy",
            16: "Cute", 17: "Damaged", 18: "Defeated", 19: "Dark", 20: "Dirty",
            21: "Disagreeable", 22: "Dry", 23: "Dull", 24: "Empty", 25: "Enormous",
            26: "Extraordinary", 27: "Extravagant", 28: "Faded", 29: "Familiar", 30: "Fancy",
            31: "Feeble", 32: "Festive", 33: "Flawless", 34: "Forlorn", 35: "Fragile",
            36: "Fragrant", 37: "Fresh", 38: "Full", 39: "Glorious", 40: "Graceful",
            41: "Hard", 42: "Harsh", 43: "Healthy", 44: "Heavy", 45: "Historical",
            46: "Horrible", 47: "Important", 48: "Interesting", 49: "Juvenile", 50 :"Lacking",
            51: "Large", 52: "Lavish", 53: "Lean", 54: "Less", 55: "Lethal",
            56: "Lively", 57: "Lonely", 58: "Lovely", 59: "Magnificent", 60: "Mature",
            61: "Messy", 62: "Mighty", 63: "Military", 64: "Modern", 65: "Mundane",
            66: "Mysterious", 67: "Natural", 68: "Normal", 69: "Odd", 70: "Old",
            71: "Pale", 72: "Peaceful", 73: "Petite", 74: "Plain", 75: "Poor",
            76: "Powerful", 77: "Protective", 78: "Quaint", 79: "Rare", 80: "Reassuring",
            81: "Remarkable", 82: "Rotten", 83: "Rough", 84:" Ruined", 85: "Rustic",
            86: "Scary", 87: "Shocking", 88: "Simple", 89: "Small", 90: "Smooth",
            91: "Soft", 92: "Strong", 93: "Stylish", 94: "Unpleasant", 95: "Valuable",
            96: "Vibrant", 97: "Warm", 98: "Watery", 99: "Weak", 100: "Young",
        }
        return descriptor_table_2

    def create_elements_table(self):
        elements_table= {
            "locations": {
                1: "Abandoned", 2: "Active", 3: "Artistic", 4: "Atmosphere", 5: "Beautiful",
                6: "bleak", 7: "Bright", 8: "Business", 9: "Calm", 10: "Charming",
                11: "Clean", 12: "Cluttered", 13: "Cold", 14: "Colorful", 15: "Colorless",
                16: "Confusing", 17: "Cramped", 18: "Creepy", 19: "Crude", 20: "Cute",
                21: "Damaged", 22: "Dangerous", 23: "Dark", 24: "Delightful", 25: "Dirty",
                26: "Domestic", 27: "Empty", 28: "Enclosed", 29: "Enormous", 30: "Entrance",
                31: "Exclusive", 32: "Exposed", 33: "Extravagant", 34: "Familiar", 35: "Fancy",
                36: "Festive", 37: "Foreboding", 38: "Fortunate", 39: "Fragrant", 40: "Frantic",
                41: "Frightening", 42: "Full", 43: "Harmful", 44: "Helpful", 45: "Horrible",
                46: "Important", 47: "Impressive", 48: "Inactive", 49: "Intense", 50: "Intriguing",
                51: "Lively", 52: "Lonely", 53: "Long", 54: "Loud", 55: "Meaningful",
                56: "Messy", 57: "Mobile", 58: "Modern", 59: "Mundane", 60: "Mysterious",
                61: "Natural", 62: "New", 63: "Occupied", 64: "Odd", 65: "Official",
                66: "Old", 67: "Open", 68: "Peaceful", 69: "Personal", 70: "Plain",
                71: "Portal", 72: "Protected", 73: "Protection", 74: "Purposeful", 75: "Quiet",
                76: "Reassuring", 77: "Remote", 78: "Resourceful", 79: "Ruined", 80: "Rustic",
                81: "Safe", 82: "Services", 83: "Simple", 84: "Small", 85: "Spacious",
                86: "Storage", 87: "Strange", 88: "Stylish", 89: "Suspicious", 90: "Tall",
                91: "Threatening", 92: "Tranquil", 93: "Unexpected", 94: "Unpleasant", 95: "Unusual",
                96: "Useful", 97: "Warm", 98: "Warning", 99: "Watery",  100: "Welcoming",
            },
            "characters": {
                1: "Accompanied", 2: "Active", 3: "Aggressive", 4: "Ambush", 5: "Animal",
                6: "Anxious", 7: "Armed", 8: "Beautiful", 9: "Bold", 10: "Busy",
                11: "Calm", 12: "Careless", 13: "Casual", 14: "Cautious", 15: "Classy",
                16: "Colorful", 17: "Combative", 18: "Crazy", 19: "Creepy", 20: "Curious",
                21: "Dangerous", 22: "Deceitful", 23: "Defeated", 24: "Defiant", 25: "Delightful",
                26: "Emotional", 27: "Energetic", 28: "Equipped", 29: "Excited", 30: "Expected",
                31: "Familiar", 32: "Fast", 33: "Feeble", 34: "Feminine", 35: "Ferocious",
                36: "Foe", 37: "Foolish", 38: "Fortunate", 39: "Fragrant", 40: "Frantic",
                41: "Friend", 42: "Frightened", 43: "Frightening", 44: "Generous", 45: "Glad",
                46: "Happy",  47: "Harmful", 48: "Helpful", 49: "Helpless", 50: "Hurt",
                51: "Important", 52: "Inactive", 53: "Influential", 54: "Innocent", 55: "Intense",
                56: "Knowledge", 57: "Large", 58: "Lonely", 59: "Loud", 60: "Loyal",
                61: "Masculine", 62: "Mighty", 63: "Miserable", 64: "Multiple", 65: "Mundane",
                66: "Mysterious", 67: "Natural", 68: "Odd", 69: "Official", 70: "Old",
                71: "Passive", 72: "Peaceful", 73: "Playful", 74: "Powerful", 75: "Professional",
                76: "Protected", 77: "Protecting", 78: "Questioning", 79: "Quiet", 80: "Reassuring",
                81: "Resourceful", 82: "Seeking", 83: "Skilled", 84: "Slow", 85: "Small",
                86: "Stealthy", 87: "Strange", 88: "Strong", 89: "Tall", 90: "Thieving",
                91: "Threatening", 92: "Triumphant", 93: "Unexpected", 94: "Unnatural", 95: "Unusual",
                96: "Violent", 97: "Vocal", 98: "Weak", 99: "Wild", 100: "Young",
            },
            "objects": {
                1: "Active", 2: "Artistic", 3: "Average", 4: "Beautiful", 5: "Bizarre",
                6: "Bright", 7: "Clothing", 8: "Clue", 9: "Cold", 10: "Colorful",
                11: "Communication", 12: "Complicated", 13: "Confusing", 14: "Consumable", 15: "Container",
                16: "Creepy", 17: "Crude", 18: "Cute", 19: "Damaged", 20: "Dangerous",
                21: "Deactivated", 22: "Deliberate", 23: "Delightful", 24: "Desired", 25: "Domestic",
                26: "Empty", 27: "Energy", 28: "Enormous", 29: "Equipment", 30: "Expected",
                31: "Expanded", 32: "Extravagant", 33: "Faded", 34: "Familiar", 35: "Fancy",
                36: "Flora", 37: "Fortunate", 38: "Fragile", 39: "Fragrant", 40: "Frightening",
                41: "Garbage", 42 :"Guidance", 43: "Hard", 44: "Harmful", 45: "Healing",
                46: "Heavy", 47: "Helpful", 48: "Horrible", 49: "Important", 50: "Inactive",
                51: "Information", 52: "Intriguing", 53: "Large", 54: "Lethal", 55: "Light",
                56: "Liquid", 57: "Loud", 58: "Majestic", 59: "Meaningful", 60: "Mechanical",
                61: "Modern", 62: "Moving", 63: "Multiple", 64: "Mundane", 65: "Mysterious",
                66: "Natural", 67: "New", 68: "Odd", 69: "Official", 70: "Old",
                71: "Ornamental", 72: "Ornate", 73: "Personal", 74: "Powerful", 75: "Prized",
                76: "Protection", 77: "Rare", 78: "Ready", 79: "Reassuring", 80: "Resource",
                81: "Ruined", 82: "Small", 83: "Soft", 84: "Solitary", 85: "Stolen",
                86: "Strange", 87: "Stylish", 88: "Threatening", 89: "Tool", 90: "Travel",
                91: "Unexpected", 92: "Unpleasant", 93: "Unusual", 94: "Useful", 95: "Useless",
                96: "Valuable", 97: "Warm", 98: "Weapon", 99: "Wet", 100: "Worn",
            },
        }
        return elements_table

    def create_character_names_table(self):
        character_names_table = {
            1: "Agostan", 2: "Abigel", 3: "Arapad", 4: "Aliz", 5: "Attila",
            6: "Amalia", 7: "Bognar", 8: "Andrea", 9: "Dense", 10: "Aranka",
            11: "Edmond", 12: "Csilla", 13: "Erno", 14: "Edit", 15: "Etele",
            16: "Erzebert", 17: "Ferdinand", 18: "Gertrud", 19: "Florian", 20: "Greta",
            21: "Geza", 22: "Iren", 23: "Gyula", 24: "Kamilla", 25: "Hugo",
            26: "Lara", 27: "Karsci", 28: "Lia", 29: "Konrad", 30: "Lujza",
            31: "Lazlo", 32: "Matild", 33: "Lukas", 34: "Olga", 35: "Marko",
            36: "Otilia", 37: "Miklos", 38: "Panna", 39: "Peti", 40: "Roza",
            41: "Robi", 42: "Terez", 43: "Tamas", 44: "Tunda", 45: "Rolond",
            46: "Valeria", 47: "Viktor", 48: "Vilma", 49: "Zoltan", 50:"Viola",
            51: "Adibemi", 52: "Abeni", 53: "Aboye", 54: "Ade", 55: "Adegoke",
            56: "Alaba", 57: "Ayokunle", 58: "Bolanle", 59: "Babajide", 60: "Bosade",
            61: "Babatunde", 62: "Daraja", 63: "Enitan", 64: "Fari", 65: "Femi",
            66: "Gbemisola", 67: "Kayin", 68: "Ife", 69: "Kayode", 70: "Ige",
            71: "Lanre", 72: "Lewa", 73: "Lekan", 74: "Mojisola", 75: "Mongo",
            76: "Monifa", 77: "Nwachukwu", 78: "Olufemi", 79: "Oban", 80: "Omolara",
            81: "Ogun", 82: "Oni", 83: "Olukayode", 84: "Orisa", 85: "Oluwalanni",
            86: "Osa", 87: "Oluwatoke", 88: "Ronke", 89: "Onipede", 90: "Shanum",
            91: "Sijuade", 92: "Simisola", 93: "Toben", 94: "Titlayo", 95: "Utiba",
            96: "Yejede", 97: "Zaki", 98: "Yewande", 99: "Zoputan", 100: "Zauna",
        }
        return character_names_table

    def create_weapon_names_table(self):
        weapon_names_table = {
            1: "Araman", 2: "Groudin", 3: "Dhossim", 4: "Dalom", 5: "Bhakel",
            6: "Brodrous", 7: " Grakim", 8: "Drolf", 9: "Hevrad", 10: "Sigril",
            11: "Nomoli", 12: "Kellyg", 13: "Kirdum", 14: "Dobrik", 15: "Bognur",
            16: "Thasdan", 17: "Bosteg", 18: "Bonad", 19: "Norrim", 20: "Thragg",
            21: "Thorgrd", 22: "Durmas", 23: "Kraznog", 24: "Dhold", 25: "Dorol",
            26: "Methild", 27: "Eldrin", 28: "Araie", 29: "Fana", 30: "Khiiral",
            31: "Ivasaar", 32: "Glynfir", 33: "Vesstan", 34: "Pywaln", 35: "Cyran",
            36: "Saelihn", 37: "Paeral", 38: "Shalanar", 39: "Perlen", 40: "Petsys",
            41: "Elion", 42: "Darieth", 43: "Vulen", 44: "Kharis", 45: "Aimer",
            46: "Genlee", 47: "Thalanil", 48: "Lianthorn", 49: "Ashryn", 50: "Sharian",
            51: "Linna", 52: "Kerston", 53: "Ari", 54: "Halden", 55: "Lenia",
            56: "Bando", 57: "Landon", 58: "Eltor", 59: "Torville", 60: "Corin",
            61: "Elrick", 62: "Lowmore", 63: "Tavor", 64: "Talmorn", 65: "Bodie",
            66: "Nesbin", 67: "Caltor", 68: "Orina", 69: "Tera", 70: "Philia",
            71: "Lilrin", 72: "Lervin", 73: "Marlos", 74: "Davrus", 75: "Alros",
            76: "Fillcath", 77: "Caldon", 78: "Rosvor", 79: "Keltor", 80: "Mox",
            81: "Poe", 82: "Torbrim", 83: "Jorian", 84: "Menlow", 85: "Oran",
            86: "Ragill", 87: "Halle", 88: "Rimcall", 89: "Anesa", 90: "Krina",
            91: "Farnor", 92: "Orlow", 93: "Kelbin", 94: "Orlos", 95: "Fargim",
            96: "Alvor", 97: "Ormox", 98: "Fenris", 99: "Thora", 100: "Torgrin",
        }
        return  weapon_names_table

    def create_location_names_table(self):
        location_names_table = {
            1: "Avion", 2: "Dolmen", 3: "Ramsen", 4: "Ammina", 5: "Innaya",
            6: "Ashur-Dan", 7: "Nabo Pal", 8: "Imshu", 9: "Kushi", 10: "Mardokh",
            11: "Kishara", 12: "Kishari", 13: "Kishar", 14: "Ettu", 15: "Aralu",
            16: "Makru", 17: "Nabu-Salim", 18: "Urukh", 19: "Uruk", 20: "Anu",
            21: "Amarsin", 22: "Lapis", 23: "Tauret", 24: "Samira", 25: "Ma-Ani",
            26: "Fukyana", 27: "Suvan", 28: "Siti-Pala", 29: "Safiya", 30: "Anka",
            31: "Oni", 32: "Neferu", 33: "Nefetiti", 34: "Urshu", 35: "Mera",
            36: "Amon", 37: "Amenthes", 38: "Snefru", 39: "Osiris", 40: "Husani",
            41: "Hagar-Aries", 42: "Hijra", 43: "Medina", 45: "Sadiki",
            46: "Xene", 47: "Isidora", 48: "Sibylla", 49: "Olympia", 50: "Kyra",
            51: "Zenia", 52: "Damalis", 53: "Titania", 54: "Hekate", 55: "Hecate",
            56: "Sapphira", 57: "Sapphire Isles", 58: "Iris", 59: "Melina Hills", 60: "Ouriana",
            61: "Ladon", 62: "Galen Vale", 63: "Ianos", 64: "Leon", 65: "Basileus",
            66: "Kreon", 76: "Isokrates", 77: "Cydonia", 78: "Nikolaos Ranges", 79: "Lapis River", 80: "Diodoros",
            81: "Ariston", 82: "Drakon", 83: "Apollos", 84: "Phoenixya", 85: "Aeton",
            86: "Adonis", 87: "Pretos", 88: "Petra", 89: "Diablos", 90: "Takis Mountains",
            91: "Midas Plateau", 92: "Midgar", 93: "Vasilios", 94: "Alexandros", 95: "Eros",
            96: "Spiros", 97: "Myron", 98: "Quarta", 99: "Baal", 100: "Ishtar",
        }
        return location_names_table

