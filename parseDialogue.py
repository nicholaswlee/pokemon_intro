import json
from slowedText import sprint, sinput
def dialogue(fileName, variables=None, seconds=0.02):
    file = open(fileName)
    content = json.load(file)
    dialogueLines = content["dialogue"]
    readDialogue(dialogueLines, seconds, variables=variables)

def readDialogue(dialogueLines, seconds, variables=None):
    for line in dialogueLines:
        if(line["type"] == "text"):
            sinput(line["value"], seconds=seconds)
        elif(line["type"] == "text_var"):
            txt = line["value"].replace(line["variable"], findVariableValue(line["variable"], variables))
            sinput(txt)
        elif(line["type"] == "text_vars"):
            txt = line["value"]
            for var in line["variables"]:
                txt = txt.replace(var, findVariableValue(var, variables))
            sinput(txt)
        elif(line["type"] == "text_tree"):
            response = sinput(line["value"])
            for choice in line["tree"]:
                if choice["choice"] == response:
                    readDialogue(choice["path"], seconds, variables=variables)        
        elif(line["type"] == "text_key_var_set"):
            response = ""
            while(response == ""):
                response = sinput(line["value"])
                confirmation = sinput(response + "? Is that correct (Y/N):")
                if(confirmation.capitalize() != "Y"):
                    response = ""
            variables[line["variable"]] = response
        elif(line["type"] == "text_tree_key_var"):
            response = ""
            while(response == ""):
                response = sinput(line["value"])
                value = ""
                confirmation = ""
                for choice in line["tree"]:
                    if choice["choice"] == response:
                        value = choice["value"]
                        confirmation = sinput(value.capitalize() + "? Is that correct (Y/N): ")
                        break
                if(confirmation.capitalize() != "Y"):
                    response = ""
                    value = ""
            variables[line["variable"]] = value
            if(line["variable"] == "STARTER_NAME"):
                opponent = int(response) + 1
                if(opponent > 3):
                    opponent = 1
                opponentValue = ""
                for choice in line["tree"]:
                    if choice["choice"] == str(opponent):
                        opponentValue = choice["value"]
                variables["RIVAL_STARTER_NAME"] = opponentValue
        elif(line["type"] == "text_tree_conditional_key_var"):
            for choice in line["tree"]:
                if choice["value"] == variables[line["variable"]]:
                    readDialogue(choice["path"], seconds, variables=variables)
        elif(line["type"] == "option_tree"):
            tree = line["tree"]
            required_remaining = line["required"]
            while(True):
                sprint(line["value"])
                choices = 0
                for i in range(len(tree)):
                    if(line["tree"][i]["locked"] and required_remaining > 0):
                        continue
                    sprint("\t" + str(i + 1) + ". " + line["tree"][i]["value"])
                    choices += 1
                index = int(sinput("Please select a number: ").strip()) - 1
                if(choices - 1 < index):
                    sprint("That's not an option")
                    continue
                choice = tree[index]
                readDialogue(choice["path"], seconds, variables=variables)
                if(choice["required"]):
                    required_remaining -= 1
                    tree.pop(index)
                if(choice["proceed"]):
                    break
def findVariableValue(key, variables):
    if key in variables:
        return str(variables[key])
    else:
        return ""
