# -*- coding: utf-8 -*-

def findSuspect(filePath):

    eva = [0, 0, 0, 0, 0]
    larisa = [0, 0, 0, 0, 0]
    matej = [0, 0, 0, 0, 0]
    miha = [0, 0, 0, 0, 0]
    black = 0
    asian = 0
    round = 0
    with open(filePath, "r") as file:
        content = file.read()
        length = len(content)
        for i in range(length - 7):
            if i < length - 12:
                # Gender female
                if content[i:(i + 12)] == "TGAAGGACCTTC":
                    eva[0] = 1
                    larisa[0] = 1
                # Gender male
                if content[i:(i + 12)] == "TGCAGGAACTTC":
                    matej[0] = 1
                    miha[0] = 1
            if i < length - 11:
                # Hair color black
                if content[i:(i + 11)] == "CCAGCAATCGC":
                    matej[2] = 1
                # Hair color blonde
                if content[i:(i + 11)] == "TTAGCTATCGC":
                    eva[2] = 1
            if i < length - 10:
                # Hair color brown
                if content[i:(i + 10)] == "GCCAGTGCCG":
                    larisa[2] = 1
                    miha[2] = 1
                # Eye color blue
                if content[i:(i + 10)] == "TTGTGGTGGC":
                    eva[3] = 1
                    matej[3] = 1
                # Eye color green
                if content[i:(i + 10)] == "GGGAGGTGGC":
                    miha[3] = 1
                # Eye color brown
                if content[i:(i + 10)] == "AAGTAGTGAC":
                    larisa[3] = 1
            if i < length - 9:
                # Race white
                if content[i:(i + 9)] == "AAAACCTCA":
                    eva[1] = 1
                    larisa[1] = 1
                    matej[1] = 1
                    miha[1] = 1
                # Race black
                if content[i:(i + 9)] == "CGACTACAG":
                    black = 1
                # Race asian
                if content[i:(i + 9)] == "CGCGGGCCG":
                    asian = 1
            if i < length - 8:
                # Face shape oval
                if content[i:(i + 8)] == "AGGCCTCA":
                    eva[4] = 1
                    larisa[4] = 1
                    matej[4] = 1
            if i < length - 7:
                # Face shape square
                if content[i:(i + 7)] == "GCCACGG":
                    miha[4] = 1
                # Face shape round
                if content[i:(i + 7)] == "ACCACAA":
                    round = 1

        result = "The ice cream was eaten by"
        if sum(eva) == 5:
            if result[-1] == "y": result += " Eva"
            else: result += ", Eva"
        if sum(larisa) == 5:
            if result[-1] == "y": result += " Larisa"
            else: result += ", Larisa"
        if sum(matej) == 5:
            if result[-1] == "y": result += " Matej"
            else: result += ", Matej"
        if sum(miha) == 5:
            if result[-1] == "y": result += " Miha"
            else: result += ", Miha"
        if black == 1:
            if result[-1] == "y": result += " some black individual"
            else: result += ", some black individual"
        if asian == 1:
            if result[-1] == "y": result += " some asian individual"
            else: result += ", some asian individual"
        if round == 1:
            if result[-1] == "y": result += " some individual with round face"
            else: result += ", some individual with round face"
        if result[-1] == "y": # we still don't know the suspect
            result += " ... we do not know"
        result += "."
        print result

def findSuspectsShort(filePath):

    with open(filePath, "r") as file:
        content = file.read()
        result = "The ice cream was eaten by"

        # if the suspect is white
        if content.find("AAAACCTCA") != -1:
            # if the suspect is female and has oval face
            if content.find("TGAAGGACCTTC") != -1 and content.find("AGGCCTCA") != -1:
                # if the suspect has blonde hair and blue eyes
                if content.find("TTAGCTATCGC") != -1 and content.find("TTGTGGTGGC") != -1:
                    if result[-1] == "y": result += " Eva"
                    else: result += ", Eva"
                # if the suspect has brown hair and brown eyes
                if content.find("GCCAGTGCCG") != -1 and content.find("AAGTAGTGAC") != -1:
                    if result[-1] == "y": result += " Larisa"
                    else: result += ", Larisa"
            # if the suspect is male
            if content.find("TGCAGGAACTTC") != -1:
                # if the suspect has black hair, blue eyes and oval face
                if content.find("CCAGCAATCGC") != -1 and content.find("TTGTGGTGGC") != -1 and content.find("AGGCCTCA") != -1:
                    if result[-1] == "y": result += " Matej"
                    else: result += ", Matej"
                # if the suspect has brown hair, green eyes and square face
                if content.find("GCCAGTGCCG") != -1 and content.find("GGGAGGTGGC") != -1 and content.find("GCCACGG") != -1:
                    if result[-1] == "y": result += " Miha"
                    else: result += ", Miha"
        else:
            result += " ... we do not know"
        result += "."

    print result

if __name__ == "__main__":
    findSuspect("dna.txt")
    findSuspectsShort("dna.txt")