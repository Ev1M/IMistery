screen velgHvorEtterHeis() :
    imagemap:
        ground "gang.jpg"
        hotspot(980, 700, 65, 1041) action Jump("Lererkontor") alt "Lererkontor"
        hotspot(1580, 1895, 380, 325) action Jump("fellesareal") alt "fellesareal"
        hotspot(2950, 593, 353, 1645) action Jump("ImKlasserom") alt "ImKlasserom"


screen fellesareal():
    imagemap:
        ground "fellesareal.jpg"
        hotspot(2679, 315, 425, 977) action Jump("idleEtterHeis") alt "idleEtterHeis"
        hotspot(1275, 1434, 1000, 241) action Jump("BordEn") alt "BordEn"

screen AEJVbord() :
    imagemap:
        ground "AEJVbordTest.jpg"
        hotspot(500, 1050, 500, 500) action Jump("Aslak") alt "Aslak"
        hotspot(1200, 1050, 500, 500) action Jump("Even") alt "Even"
        hotspot(1900, 1050, 500, 500) action Jump("Vilmer") alt "Vilmer"
        hotspot(2800, 1050, 500, 500) action Jump("Jonas") alt "Jonas"


screen klasserom() :
    imagemap:
        ground "klasserom.jpg"

screen prat() :
    imagemap:
        ground "prat.jpg"



