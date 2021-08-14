import json
data = json.loads(open('reco.json').read())

print("")

def printbook(e):
    print("\\subsubsection{"+e["title"]+"}")
    print("\\textit{By "+e["author"]+"}\\\\\\\\")
    print("First published in "+e["year"]+"\\\\\\\\")
    if ("trad" in e):
        for key,value in e["trad"].items():
            sortie = "(Also in "+key+" : "+value["title"]
            if "year" in value:
                sortie += " ("+value["year"]+") "
            sortie += ")\\\\\\\\"
            print(sortie)
print("")
print("\\documentclass{article}")
print("")
print("\\begin{document}")
print("    \\section{Books}")
print("")

for key,value in data["books"].items():
    print("\\subsection{"+key+"}")
    for e in value:
        printbook(e)
print("")
print("\\end{document}")
print("")
