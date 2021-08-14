import json
import re
import os

def parselanguinv(t):
    lines = t.split("\n")
    res = {}
    current = ""
    for j in range(len(lines)):
        line = lines[j]
        regres = re.search(r"^\?\?\?\?\?(.*)\[(.*)\]$",line)
        if regres:
            lang = regres.groups()[0]
            fileout = regres.groups()[1]
            res[lang] = {}
            res[lang]["fileout"] = fileout
            res[lang]["content"] = ""
            current = lang
        else:
            res[current]["content"] += line+"\n"

    for key,value in res.items():
        tmp = open("tmp.py",'w+')
        tmp.write("import json\ndata = json.loads(open(\"reco.json\").read())\n")
        splitted = value["content"].split("%")
        final = ""
        lasortie = open(value["fileout"],'w+')
        for i in range(len(splitted)):
            if (i%2==0):
                todisplay = splitted[i].split("\n")
                for e in todisplay:
                    final+=("print(\""+e+"\")\n")
            else:
                final+=(splitted[i])
        tmp.write(final)
        tmp.close()
        os.system("sed -i 's/\\\\/\\\\\\\\/g' tmp.py")
        # os.system("sed -i 's/\"/\\\"/g' tmp.py")
        os.system("python3 tmp.py >> "+value["fileout"])
    
codeaffich = open("affich.languinv").read()
parselanguinv(codeaffich)