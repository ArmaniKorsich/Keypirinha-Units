import keypirinha as kp
import keypirinha_util as kpu

class Units(kp.Plugin):
    global unitNames
    global inUnit
    global outUnit
    global inValue
    global outValue
    outValue = [None, None]
    global outUnitString
    outUnitString = None
    global inUnitString
##    global outUnitString
    #converts metric and Imperial units
    
    ITEMCAT_RESULT = kp.ItemCategory.USER_BASE + 1

    units = [[1, 4, 2, 2, 8, 2, 3, .00000492892, 1000, 1000, 0.000264172],#gal to quart, to pint, to cup, to oz, to tbsp, to tsp, to kiloliter, to liter, to milliliter, to gal
            [1, 5280, 12, .0000254, 1000, 100, 10, 0.000000621371], #mile to foot to inch, to km, to meter, to cm, to mm, to foot
            [1, 0.01745327777, 57.2958279088] #degree to radians to degree
            ]
    unitNames = ["gal", "gallon", "gallons", "quart", "quarts", "qrt", "pint", "pints", "cup", "cups", "floz", "tablespoon", "tablespoons", "tbsp", "teaspoon", "teaspoons", "tsp", "kiloliter", "kiloliters", "kl", "liter", "liters", "l", "li",
                 "milliliter", "milliliters", "ml", "mile", "miles", "mi", "foot", "feet", "ft", "inch", "inches", "in", "kilometer", "kilometers", "km",
                 "meter", "meters", "m", "centimeter", "centimeters", "cm", "millimeter", "millimeters", "mm", "degree", "degrees", "deg", "radian", "radians", "rad"]
    def __init__(self):
        super().__init__()

    
    def handleConversion(self, userInput):
        suggestions = []
        inUnit = [None,None]
        outUnit = [None,None]
##        print ("handling conversions")
        splitInput = userInput.split(" ")
##        print (splitInput)
        if Units.isNumber(splitInput[0]):
            if len(splitInput) == 2:
                inValue = float(splitInput[0])
                inUnitString = splitInput[1].lower()
                outUnitString = splitInput[1].lower()
                Units.outUnitString = outUnitString
                Units.determineUnits(inUnitString, inUnit)
                Units.determineUnits(outUnitString, outUnit)
                #Gives quick converts of common units, to their most common counterparts. Requires only a value and a unit. (Ex: "5 Inches")
                if inUnit == [0, 0]: #gal
                    Units.outUnitString = "liters"
                    outUnit = [0, 8]
                if inUnit == [0, 8]: #Liter
                    Units.outUnitString = "Gal"
                    outUnit = [0, 0]
                if inUnit == [1, 0]: #mile
                    Units.outUnitString = "kilometers"
                    outUnit = [1, 3]
                if inUnit == [1, 3]: #kilometer
                    Units.outUnitString = "mile"
                    outUnit = [1, 0]
                if inUnit == [1, 1]: #feet
                    Units.outUnitString = "inches"
                    outUnit = [1, 2]
                if inUnit == [1, 2]: #inches
                    Units.outUnitString = "mm"
                    outUnit = [1, 6]
                if inUnit == [1, 6]: #mm
                    Units.outUnitString = "inches"
                    outUnit = [1, 2]
                if inUnit == [2, 0]: #degree
                    Units.outUnitString = "radians"
                    outUnit = [2, 1]
                if inUnit == [2, 1]: ##Radians
                    Units.outUnitString = "degrees"
                    outUnit = [2, 0]
                Units.convert(inValue, inUnit, outUnit)
            if len(splitInput) == 4:
                inValue = float(splitInput[0])
                inUnitString = splitInput[1].lower()
                outUnitString = splitInput[3].lower()
                Units.outUnitString = outUnitString
                Units.determineUnits(inUnitString, inUnit)
                Units.determineUnits(outUnitString, outUnit)
                Units.convert(inValue, inUnit, outUnit)
            #else: print "query not formatted properly"
        else:
            if len(splitInput) == 3:
                inValue = 1
                inUnitString = splitInput[0].lower()
                outUnitString = splitInput[2].lower()
                Units.outUnitString = outUnitString
                Units.determineUnits(inUnitString, inUnit)
                Units.determineUnits(outUnitString, outUnit)
                Units.convert(inValue, inUnit, outUnit)

        
        
  
    def isNumber(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    def determineUnits(string, unit):
##        print ("determining units")
        string = string.lower()
        if string == "gal" or string == "gallon" or string == "gallons":
            unit[0] = 0 #liquid
            unit[1] = 0
        elif string == "quart" or string == "qrt" or string == "quarts":
            unit[0] = 0
            unit[1] = 1
        elif string == "pint" or string == "pints":
            unit[0] = 0
            unit[1] = 2
        elif string == "cup" or string == "cups":
            unit[0] = 0
            unit[1] = 3
        elif string == "floz":
            unit[0] = 0
            unit[1] = 4
        elif string == "tablespoon" or string == "tablespoons" or string == "tbsp":
            unit[0] = 0
            unit[1] = 5
        elif string == "teaspoon" or string == "teaspoons" or string == "tsp":
            unit[0] = 0
            unit[1] = 6
        elif string == "kiloliter" or string == "kiloliters" or string == "kl":
            unit[0] = 0
            unit[1] = 7
        elif string == "liter" or string == "liters" or string == "l" or string == "li":
            unit[0] = 0
            unit[1] = 8
        elif string == "milliliter" or string == "milliliters" or string == "ml":
            unit[0] = 0
            unit[1] = 9
        elif string == "mile" or string == "miles" or string == "mi":
            unit[0] = 1#length
            unit[1] = 0
        elif string == "foot" or string == "feet" or string == "ft":
            unit[0] = 1
            unit[1] = 1
        elif string == "inch" or string == "inches" or string == "in":
            unit[0] = 1
            unit[1] = 2
        elif string == "kilometer" or string == "kilometers" or string == "km":
            unit[0] = 1
            unit[1] = 3
        elif string == "meter" or string == "meters" or string == "m":
            unit[0] = 1
            unit[1] = 4
        elif string == "centimeter" or string == "centimeters" or string == "cm":
            unit[0] = 1
            unit[1] = 5
        elif string == "millimiter" or string == "millimeters" or string == "mm":
            unit[0] = 1
            unit[1] = 6
        elif string == "degree" or string == "degrees" or string == "deg":
            unit[0] = 2#angle
            unit[1] = 0
        elif string == "radian" or string == "radians" or string == "rad":
            unit[0] = 2
            unit[1] = 1
        else:
            return
    #@classmethod
    def convert(inValue, inUnit, outUnit):
        global outValue
##        print ("converting")            
        if inUnit[0] != outUnit[0]:
##            print ("Units are not of the same type")
            return
        if inUnit[1] > outUnit[1]: #will require a cycle to convert
##            print ("Greater")
            pos = inUnit[1] + 1
            for x in range(len(Units.units[inUnit[0]]) - inUnit[1] - 1):
                inValue *= Units.units[inUnit[0]][pos]
                pos += 1
            pos = 0
            for x in range(outUnit[1] + 1):
                inValue *= Units.units[inUnit[0]][pos]
                pos += 1
        elif inUnit[1] < outUnit[1]:
##            print ("Lesser")
            pos = inUnit[1] + 1
            for x in range(outUnit[1] - inUnit[1]):
                inValue *= Units.units[inUnit[0]][pos]
                pos = pos + 1
        outValue[0] = inValue

        
    def on_start(self):
        self.set_actions(self.ITEMCAT_RESULT, [
            self.create_action(
                name="copy",
                label="Copy",
                short_desc="Copy the converted units")])
        
    def on_catalog(self):
        self.set_catalog([self.create_item(
            category=kp.ItemCategory.KEYWORD,
            label="=",
            short_desc="Convert from one currency to another",
            target="=",
            args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.NOARGS)])
                         
    def on_suggest(self, user_input, items_chain):
        global outValue
        global unitNames
        global inValue
        global outUnitString
        suggestions = []
        shortDesc = "Press Enter to copy the results"
        x = False
        inputChain = user_input.split()
        for item in inputChain:
            if item.lower() in unitNames:
                x = True
        if x == False:
            return
        try:
            self.handleConversion(user_input)
            if Units.outUnitString.lower() in unitNames:
##                print ("%f %s" %(outValue[0], Units.outUnitString))
                val = outValue[0]
                val1 = val
                if val == int(val):
                    val = int(val)
                else:
                    val1 = round(val,3)
                    val1 = str(val1)
                    suggestions.append(self.create_item(
                        category=kp.ItemCategory.EXPRESSION,
                        label=val1 + " " + Units.outUnitString,
                        short_desc="Press Enter to copy the result",
                        target=val1,
                        args_hint=kp.ItemArgsHint.FORBIDDEN,
                        hit_hint=kp.ItemHitHint.IGNORE))
                    if val < .01:
                        val2 = round(val,5)
                        val2 = str(val2)
                        suggestions.append(self.create_item(
                            category=kp.ItemCategory.EXPRESSION,
                            label=val2 + " " + Units.outUnitString,
                            short_desc="Press Enter to copy the result",
                            target=val2,
                            args_hint=kp.ItemArgsHint.FORBIDDEN,
                            hit_hint=kp.ItemHitHint.IGNORE))
                val = str(val)
##                print ("#")
            suggestions.append(self.create_item(
                category=kp.ItemCategory.EXPRESSION,
                label=val + " " + Units.outUnitString,
                short_desc="Press Enter to copy the result",
                target=val,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE))
        except:
            None
        self.set_suggestions(suggestions, kp.Match.ANY, kp.Sort.NONE)
        
    def on_execute(self, item, action):
        kpu.set_clipboard(item.target())
