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
        hotspot(1250, 1400, 1041, 300) action Jump("BordEn") alt "BordEn"

screen AEJVbord() :
    imagemap:
        ground "AEJVbordTest.jpg"
        hotspot(186,881,513,607) action Jump("Aslak") alt "Aslak"
        hotspot(861,918,503,550) action Jump("Even") alt "Even"
        hotspot(1549,918,510,567) action Jump("Vilmer") alt "Vilmer"
        hotspot(2511,921,540,557) action Jump("Jonas") alt "Jonas"

screen D1Dfellesareal():
    imagemap:
        ground "fellesareal_letetias.jpg"
        hotspot(2679, 315, 425, 977) action Jump("leterEtterTias") alt "leterEtterTias"
        hotspot(3085, 1150, 263, 337) action Jump("gangMotToalett") alt "gangMotToalett"

screen MotToalettD1():
    imagemap:
        ground "LeteMotToalett.jpg"
        hover "LeteMotToalett_hover.jpg"

        hotspot (115,1158,465,428) action Jump("D1Dfellesareal")
        hotspot (2872,1168,520,408) action Jump ("Toalett")

screen LeterEtterTiasGang() :
    imagemap:
        ground "gang.jpg"
        hover "gang_hover.jpg"

        hotspot(980, 700, 65, 1041) action Jump("LererkontorLeter")
        hotspot(1580, 1895, 380, 325) action Jump("D1Dfellesareal")
        hotspot(2950, 593, 353, 1645) action Jump("ImKlasseromLeter")


screen klasserom():
    imagemap:
        ground "klasserom.JPG"
        hover "klasserom_hover.jpg"

        hotspot (850,1336,355,200) action Jump ("Srimon")
        hotspot (1266,1208,327,193) action Jump ("Arin")
        hotspot (2157,1141,327,202) action Jump ("KarlGangster")
        hotspot (1441,1843,419,371) action Jump ("D1Dfellesareal")


screen ToalettInteract():
    imagemap:
        ground "ToalettTre.jpg"
        hotspot (2550,350,630,1970) action Jump ("Toalett1")
        hotspot (1965,600,310,1715) action Jump ("Toalett2")
        hotspot (1650,700,150,1529) action Jump ("Toalett3")
        hotspot (1450,765,110,1200) action Jump ("ToalettDead")






