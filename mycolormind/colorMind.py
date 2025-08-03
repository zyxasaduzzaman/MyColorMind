class ColorMind:
    __DEFAULT_PRIMARY = ["yellow", "red", "blue"]
    __DEFAULT_SECONDARY = ["orange", "violet", "green"]
    __TERTIARY = ["yelloworange", "redorange", "redviolet", "blueviolet", "bluegreen", "yellowgreen"]
    __COLOR_HEX = {
        "red": "#FF0000",
        "blue": "#0000FF",
        "green": "#008000",
        "yellow": "#FFFF00",
        "orange": "#FFA500",
        "violet": "#8F00FF",
        "purple": "#800080",
        "pink": "#FFC0CB",
        "brown": "#A52A2A",
        "black": "#000000",
        "white": "#FFFFFF",
        "gray": "#808080",
        "cyan": "#00FFFF",
        "magenta": "#FF00FF",
        "maroon": "#800000",
        "navy": "#000080",
        "teal": "#008080",
        "lime": "#00FF00",
        "olive": "#808000",
        "gold": "#FFD700",
        "silver": "#C0C0C0",
        "beige": "#F5F5DC",
        "turquoise": "#40E0D0",
        "coral": "#FF7F50",
        "lavender": "#E6E6FA",
        "salmon": "#FA8072",
        "tan": "#D2B48C",
        "aqua": "#00FFFF",
        "azure": "#F0FFFF",
        "chocolate": "#D2691E",
        "crimson": "#DC143C",
        "darkblue": "#00008B",
        "darkgreen": "#006400",
        "darkred": "#8B0000",
        "lightblue": "#ADD8E6",
        "lightgreen": "#90EE90",
        "lightgray": "#D3D3D3",
        "khaki": "#F0E68C",
        "plum": "#DDA0DD",
        "skyblue": "#87CEEB",
        "snow": "#FFFAFA",
        "tomato": "#FF6347",
        "wheat": "#F5DEB3",
        "seagreen": "#2E8B57",
        "orchid": "#DA70D6",
        "steelblue": "#4682B4",
        "sienna": "#A0522D",
        "yelloworange": "#FFAE42",
        "redorange": "#FF5349",
        "redviolet": "#C71585",
        "blueviolet": "#8A2BE2",
        "bluegreen": "#0D98BA",
        "yellowgreen": "#9ACD32",
        "mint": "#98FF98"
    }

    def __init__(self):
        """
        Initialize ColorMind with default colors, generate color wheel,
        and setup relations (complementary, analogous, triadic).
        """
        self.__PRIMARY = ColorMind.__DEFAULT_PRIMARY
        self.__SECONDARY = ColorMind.__DEFAULT_SECONDARY
        self.__TERTIARY = ColorMind.__TERTIARY
        self.__ALLCOLOR = self.__generate_all_colors()
        self.__relation = {
            "complementary": self.__complementary(),
            "analogous": self.__analogous(),
            "triadic": self.__triadic()
        }
        self.__mood_palettes = {
            "happy": ["yellow", "pink", "orange", "lightgreen"],
            "calm": ["blue", "white", "skyblue", "lightgray"],
            "serious": ["black", "darkblue", "gray", "navy"],
            "romantic": ["red", "pink", "crimson", "purple"],
            "earthy": ["brown", "khaki", "olive", "sienna"],
            "fresh": ["mint", "aqua", "lightgreen", "turquoise"],
            "luxury": ["gold", "purple", "violet", "silver"],
            "peaceful": ["white", "lavender", "plum", "seagreen"],
            "energetic": ["red", "orange", "tomato", "yellow"],
            "cold": ["blue", "navy", "cyan", "darkgreen"]
        }

    def __generate_all_colors(self):
        """
        Generate combined color wheel including primary, secondary, and tertiary colors.
        """
        all_color = []
        for i in range(len(self.__PRIMARY)):
            all_color.append(self.__PRIMARY[i])
            all_color.append(self.__SECONDARY[i])

        insert_index = 1
        for color in ColorMind.__TERTIARY:
            if insert_index < len(all_color):
                all_color.insert(insert_index, color)
            else:
                all_color.append(color)
            insert_index += 2

        return all_color

    def __complementary(self):
        """
        Generate list of complementary color pairs from the color wheel.
        """
        comList = []
        end = 6
        for i in range(6):
            comList.append([self.__ALLCOLOR[i], self.__ALLCOLOR[end]])
            end += 1
        return comList

    def __analogous(self):
        """
        Generate list of analogous color triplets from the color wheel.
        """
        angList = []
        total = len(self.__ALLCOLOR)
        for i in range(total):
            first = self.__ALLCOLOR[i]
            second = self.__ALLCOLOR[(i + 1) % total]
            third = self.__ALLCOLOR[(i + 2) % total]
            angList.append([first, second, third])
        return angList

    def __triadic(self):
        """
        Generate list of triadic color triplets from the color wheel.
        """
        triadicList = []
        total = 12
        for i in range(total):
            a = self.__ALLCOLOR[i % total]
            b = self.__ALLCOLOR[(i + 4) % total]
            c = self.__ALLCOLOR[(i + 8) % total]
            triadicList.append([a, b, c])
        return triadicList

    def primaryColor(self, index=None):
        """
        Return primary colors or a specific primary color by index.
        """
        if index is not None:
            return self.__PRIMARY[index]
        else:
            return self.__PRIMARY

    def secondaryColor(self, index=None):
        """
        Return secondary colors or a specific secondary color by index.
        """
        if index is not None:
            return self.__SECONDARY[index]
        else:
            return self.__SECONDARY

    def tertiaryColor(self, index=None):
        """
        Return tertiary colors or a specific tertiary color by index.
        """
        if index is not None:
            return self.__TERTIARY[index]
        else:
            return ColorMind.__TERTIARY

    def allColor(self):
        """
        Return the complete color wheel list.
        """
        return self.__ALLCOLOR

    def colorDict(self):
        """
        Return dictionary of primary, secondary, and tertiary colors.
        """
        return {
            "primary": self.primaryColor(),
            "secondary": self.secondaryColor(),
            "tertiary": self.tertiaryColor()
        }

    def relation(self, rel=None):
        """
        Return color relations based on the input type:
        - 'complementary'
        - 'analogous'
        - 'triadic'

        If no argument given, return all relations as a dictionary.
        Raises ValueError if relation type is invalid.
        """
        if rel is None or rel == "":
            return self.__relation

        rel = rel.lower()
        if rel in self.__relation:
            return self.__relation[rel]
        else:
            raise ValueError(f"Invalid relation type: '{rel}'. Valid options are 'complementary', 'analogous', 'triadic'.")

    def colorMeaning(self, color):
        """
        Return psychological meaning of a given color.
        """
        color = color.lower()
        meanings = {
            "red": "Energy, passion, danger, love",
            "blue": "Trust, calm, intelligence, professionalism",
            "green": "Health, nature, freshness, safety",
            "yellow": "Happiness, creativity, optimism",
            "orange": "Enthusiasm, fascination, warmth",
            "violet": "Luxury, royalty, mystery, spirituality",
            "purple": "Creativity, wisdom, dignity",
            "pink": "Love, kindness, femininity",
            "brown": "Stability, reliability, comfort",
            "black": "Power, elegance, mystery, sophistication",
            "white": "Purity, innocence, cleanliness, simplicity",
            "gray": "Neutrality, balance, formality",
            "cyan": "Freshness, clarity, energy",
            "magenta": "Harmony, emotional balance, compassion",
            "maroon": "Control, responsibility, groundedness",
            "navy": "Authority, confidence, trust",
            "teal": "Sophistication, calm, emotional balance",
            "lime": "Energy, renewal, youth",
            "olive": "Peace, earthiness, tradition",
            "gold": "Success, luxury, wealth",
            "silver": "Modernity, elegance, grace",
            "beige": "Softness, calm, neutrality",
            "turquoise": "Healing, protection, sophistication",
            "coral": "Warmth, acceptance, social interaction",
            "lavender": "Grace, elegance, serenity",
            "salmon": "Health, vitality, youth",
            "tan": "Stability, simplicity, warmth",
            "aqua": "Clarity, refreshing, energy",
            "azure": "Peace, openness, creativity",
            "chocolate": "Comfort, richness, reliability",
            "crimson": "Power, excitement, intensity",
            "darkblue": "Depth, knowledge, seriousness",
            "darkgreen": "Ambition, wealth, conservatism",
            "darkred": "Urgency, power, danger",
            "lightblue": "Peace, tranquility, friendliness",
            "lightgreen": "Growth, freshness, recovery",
            "lightgray": "Balance, calm, neutrality",
            "khaki": "Stability, calmness, subtle strength",
            "plum": "Richness, depth, creativity",
            "skyblue": "Freedom, imagination, peace",
            "snow": "Purity, calm, softness",
            "tomato": "Excitement, vibrancy, energy",
            "wheat": "Warmth, comfort, nature",
            "seagreen": "Balance, renewal, freshness",
            "orchid": "Charm, mystery, femininity",
            "steelblue": "Dependability, trust, strength",
            "sienna": "Earthiness, grounding, warmth",
            "mint": "Freshness, calm, renewal",
            "indigo": "Intuition, perception, deep contemplation"
        }
        return meanings.get(color, "Meaning not available for this color.")

    def isWarmColor(self, color):
        """
        Check if the color is considered warm.
        """
        warm = {"red", "orange", "yellow", "pink", "tomato", "gold", "coral", "salmon"}
        return color.lower() in warm

    def isCoolColor(self, color):
        """
        Check if the color is considered cool.
        """
        cool = {"blue", "green", "cyan", "teal", "navy", "skyblue", "aqua", "indigo", "violet"}
        return color.lower() in cool

    def colorGroup(self, color):
        """
        Return the group of a color: Primary, Secondary, Tertiary, Extra, or Not in palette.
        """
        color = color.lower()
        if color in self.__PRIMARY:
            return "Primary"
        elif color in self.__SECONDARY:
            return "Secondary"
        elif color in self.__TERTIARY:
            return "Tertiary"
        elif color in self.__ALLCOLOR:
            return "Extra (in palette)"
        else:
            return "Not in palette"

    def suggestComplement(self, color):
        """
        Suggest the complementary color of the input color.
        """
        color = color.lower()
        if color in self.__ALLCOLOR:
            index = self.__ALLCOLOR.index(color)
            complement = self.__ALLCOLOR[(index + 6) % 12]
            return complement
        return "Color not in main wheel (cannot determine complement)"

    def suggestAnalogous(self, color):
        """
        Suggest analogous colors (3 colors) including the input color.
        """
        color = color.lower()
        if color in self.__ALLCOLOR:
            index = self.__ALLCOLOR.index(color)
            return [
                self.__ALLCOLOR[index % 12],
                self.__ALLCOLOR[(index + 1) % 12],
                self.__ALLCOLOR[(index + 2) % 12]
            ]
        return "Color not in main wheel (cannot determine analogous)"

    def suggestTriadic(self, color):
        """
        Suggest triadic colors (3 colors) including the input color.
        """
        color = color.lower()
        if color in self.__ALLCOLOR:
            index = self.__ALLCOLOR.index(color)
            return [
                self.__ALLCOLOR[index % 12],
                self.__ALLCOLOR[(index + 4) % 12],
                self.__ALLCOLOR[(index + 8) % 12]
            ]
        return "Color not in main wheel (cannot determine triadic)"

    def generatePaletteByMood(self, mood):
        """
        Return a color palette list based on the mood input.
        """
        mood = mood.lower()
        return self.__mood_palettes.get(mood, ["No palette available for this mood."])

    def addMoodPalette(self, mood, colors):
        """
        Add or update a mood palette with a list of colors.
        """
        if not isinstance(colors, list):
            raise ValueError("Colors must be provided as a list.")
        self.__mood_palettes[mood.lower()] = colors
        return f"Mood palette for '{mood}' updated."

    def availableMethods(self):
        """
        Return a list of available public method names of this class.
        """
        return [func for func in dir(self)
                if callable(getattr(self, func))
                and not func.startswith("_")]

    def hexValue(self, color):
        """
        Return the HEX value string of a given color.
        """
        return self.__COLOR_HEX.get(color.lower(), "Hex code not available")

    def help(self):
        """
        Return a dictionary explaining the public methods and their usage.
        """
        return {
            "primaryColor(index=None)": "Get primary color(s). If index provided, returns color at that index.",
            "secondaryColor(index=None)": "Get secondary color(s). If index provided, returns color at that index.",
            "tertiaryColor(index=None)": "Get tertiary color(s). If index provided, returns color at that index.",
            "allColor()": "Get the full color wheel list.",
            "relation(rel=None)": "Get color relations like complementary, analogous, triadic.",
            "colorMeaning(color)": "Get psychological meaning of a color.",
            "isWarmColor(color)": "Check if a color is warm.",
            "isCoolColor(color)": "Check if a color is cool.",
            "colorGroup(color)": "Get group of a color (primary/secondary/tertiary/extra).",
            "suggestComplement(color)": "Get complementary color.",
            "suggestAnalogous(color)": "Get analogous colors.",
            "suggestTriadic(color)": "Get triadic colors.",
            "generatePaletteByMood(mood)": "Get color palette based on mood.",
            "addMoodPalette(mood, colors)": "Add or update a custom mood palette.",
            "hexValue(color)": "Get HEX value of a color.",
            "availableMethods()": "List all public methods."
        }


