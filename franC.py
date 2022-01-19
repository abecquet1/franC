traduction = {
    'inclure':'include',
    'esflux':'iostream',
    'utiliser':'using',
    'espacenom':'namespace',
    'ent':'int',
    'principale':'main',
    'chors':'cout',
    'cin':'cdans',
    'finl':'endl',
    'renvoyer':'return',
    }

programme_fc = open('exemple.fc')
programme_cpp = open('exemple.cpp', 'w') 
for ligne in programme_fc:
    for m in traduction:
        ligne = ligne.replace(m, traduction[m])
    programme_cpp.write(ligne)
programme_fc.close()
programme_cpp.close()

