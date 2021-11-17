screen velgHvorEtterHeis() :
    imagemap:
        ground "gang.jpg"
        hover "gang_hover.jpg"

        hotspot(980, 700, 65, 1041) action Jump("Lererkontor") alt "Lererkontor"
        hotspot(1580, 1895, 380, 325) action Jump("D1Mfellesareal") alt "D1Mfellesareal"
        hotspot(2950, 593, 353, 1645) action Jump("ImKlasserom") alt "ImKlasserom"


screen D1Mfellesareal():
    imagemap:
        ground "fellesareal.jpg"
        hotspot(2679, 315, 425, 977) action Jump("idleEtterHeis") alt "idleEtterHeis"
        hotspot(1275, 1434, 1000, 241) action Jump("BordEn") alt "BordEn"

screen AEJVbord() :
    imagemap:
        ground "AEJVbordTest.jpg"
        hotspot(186,881,513,607) action Jump("Aslak") alt "Aslak"
        hotspot(861,918,503,550) action Jump("Even") alt "Even"
        hotspot(1549,918,510,567) action Jump("Vilmer") alt "Vilmer"
        hotspot(2511,921,540,557) action Jump("Jonas") alt "Jonas"


screen D1Mfellesareal():
    imagemap:
        ground "fellesareal.jpg"
        hotspot(2679, 315, 425, 977) action Jump("idleEtterHeis") alt "idleEtterHeis"
        

screen klasserom():
    imagemap:
        ground "klasserom.JPG"
        hover "klasserom_hover.jpg"

        hotspot (850,1336,355,200) action Jump ("Srimon")
        hotspot (1266,1208,327,193) action Jump ("Arin")
        hotspot (2157,1141,327,202) action Jump ("KarlGangster")
        hotspot (1441,1843,419,371) action Jump ("D1Mfellesareal")





