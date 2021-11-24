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
        hotspot (1537,572,553,1490) action Jump("friUtforsk")
        hotspot (2872,1168,520,408) action Jump ("ToalettEn")

screen toalettEn():
    imagemap:
        ground "bg ToalettEn.png"
        hover "bg ToalettEn_hover.png"

        hotspot (1620,712,523,1300) action Jump ("ToalettTo")
        hotspot (98,1023,513,361) action Jump("gangMotToalett")


screen toalettTo():
    imagemap:
        ground "bg ToalettTo.png"
        hover "bg ToalettTo_hover.png"

        hotspot (1536,1721,374,449) action Jump("ToalettEn")
        hotspot (1677,850,216,844) action Jump("ToalettTre")

screen toalettTre():
    imagemap:
        ground "ToalettTre.png"
        hover "ToalettTre_hover.png"

        hotspot (1556,1958,348,303) action Jump("ToalettTo")
        hotspot (2511,125,695,2163) action Jump("Toalett1")
        hotspot (1944,412,371,1809) action Jump("Toalett2")
        hotspot (1644,580,212,1317) action Jump("Toalett3")
        hotspot (1472,709,134,1221) action Jump("ToalettDead")


screen LeterEtterTiasGang():
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
        hotspot (1441,1843,419,371) action Jump ("gangMotToalett")









