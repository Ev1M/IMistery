# define characters
define pov = Character("[povname]")
define hmm = Character("?????")
define c = Character("Christian")
define e = Character("Erik")
define em = Character("Even")
define vh = Character("Vilmer")
define ab = Character("Aslak")
define joo = Character("Jonas")
define kg = Character("Karl-Gustav")
define tb = Character("Titas")
define kn = Character("Kantam")
define jk = Character("JonasK")
define sp = Character("Srimon")
define al = Character("Arin")
# ANIMATIONS
# Erik animation
image Erik:
    block:
        "erik/ErikTalk.png"
        pause 0.15
        "erik/ErikTalk2.png"
        pause 0.1
        repeat 12
    "erik/Erik_Resting.png"

# Vilomer animation
image Vilmer:
    block:
        "vilmer/VilmerTalk.png"
        pause 0.1
        "vilmer/VilmerTalk2.png"
        pause 0.1
        repeat 12
    "vilmer/VilmerResting.png"

# Aslak animation
image Aslak:
    block:
        "aslak/AslakTalk.png"
        pause 0.1
        "aslak/AslakTalk2.png"
        pause 0.1
        repeat 12
    "aslak/AslakResting.png"

# Even animation
image Even:
    block:
        "even/EvenTalk.png"
        pause 0.1
        "even/EvenTalk2.png"
        pause 0.1
        repeat 12
    "even/EvenResting.png"
# Even animation 2 :3
image EvenTwerk:
    block:
        "even/EvenTop.png"
        pause 0.1
        "even/EvenMiddle.png"
        pause 0.1
        "even/EvenBottom.png"
        pause 0.1
        repeat 9
    "even/EvenTalk.png"

#Dag 1
#Intro
label start:
    scene bg heisaapen
    show Erik
    voice "audio/gibberish_sound_effect.mp3"
    c "Heisann, velkommen til Kuben’s Informatikk linje. Så hyggelig at du ville starte hos oss. Gå til "
    hide Erik

#Kan gå hvor man vil
label idleEtterHeis:
    call screen velgHvorEtterHeis
    label Lererkontor:
        scene lærerkontor
        show Christian
        c "dette er lærer kontoret"
        jump idleEtterHeis
    #Du og Christian ser i IM klasserommene
    label ImKlasserom:
        scene ImKlasserom
        show Christian
        c "Her har vi IM klasserommene for A, B og C klassen. De er i praksis nå, så du vil dessverre ikke få møtt dem "
        jump idleEtterHeis
    #Dag 1 Morning fellesareal
    label D1Mfellesareal:
        call screen D1Mfellesareal
        #Bordet hvor Aslak, Even, Jonas og Vilmer sitter.
        label BordEn : 
            call screen AEJVbord

            label Aslak:
                hide Vilmer
                hide Jonas
                hide Even
                show Aslak
                ab "ENDELIG! En ny kar her! *rister av glede* ser fram til en ny person, begynner å bli lei av 	folk som Tias, sånne folk bli bare kjedelige etterhvert"
                "{i}OK?!{/i}"
                jump BordEn
            
            #Prate med Even på morgen.
            label Even:
                hide Vilmer
                hide Aslak
                hide Jonas
                hide Even
                show EvenTwerk
                menu:
                    "Hei":
                        jump pratmdEv1
                    
                    "...":
                        jump LoLnei

                label pratmdEv1:
                    hide EvenTwerk
                    hide Even
                    show Even
                    em "hei, spiller du league of legends?"
                    menu:
                        "Ja":
                            jump LoLja
                        
                        "Nei":
                            jump LoLnei
                        
                        "...":
                            jump LoLnei
                    
                    label LoLja:
                        hide EvenTwerk
                        hide Even
                        show Even
                        $menu_flag = True
                        em "Jippi, hva slags champs spiller du?"
                        menu:
                            "Assasins":
                                jump aksepter
                            "Bruisers":
                                jump aksepter
                            "Tanks":
                                jump aksepter
                            "Mages":
                                jump LoLnei

                        hide Even
                    
                    label LoLnei:
                        hide EvenTwerk
                        hide Even
                        show Even
                        $menu_flag = False
                        em "Din stygge dritt, hvorfor kom du hit da!? *sparker deg i ansiktet, du får vondt*"
                        jump BordEn
                        hide Even
                    
                    label aksepter:
                        hide EvenTwerk
                        $menu_flag = False
                        em "Acceptable"
                        jump BordEn
                        hide Even
                    
                    hide Even
                    scene prat
                    
                
                label Vilmer:
                    hide Even
                    hide Aslak
                    hide Jonas
                    show Vilmer
                    vh "Yo, velkommen til IM, det er ingen jenter her, men vi klarer oss. Hva heter du?"
                    
                    python:
                        povname = renpy.input("Skriv navnet ditt:")
                        povname = povname.strip()

                    vh "må si det var meget hyggelig å hilse på deg [povname]"
                    vh "check out the shuffle *stokker kort*"
                    menu: 
                        "imponerende":
                            jump VillyTakk
                        "sett bedre":
                            jump VillySint
                        
                    label VillyTakk:
                        vh "takker takker"
                        jump timeSnart

                    label VillySint:
                        vh "eeh jaaa"  
                        jump timeSnart

                    label timeSnart:
                        vh "det er time nå, så vi bør jette"
                        jump mordEn
                    
                    scene prat
                    
                label Jonas:
                    hide Vilmer
                    hide Aslak
                    hide Even
                    show Jonas
                    joo "Yo! Sorry jeg måtte løpe, rakk så 	vitt bussen, men er her nå. Jeg heter Jonas, håper du er litt effektiv for det er ikke jeg, men vi skal nok hygge oss uansett"
                    scene prat
                    jump BordEn
            
    #Her starter sekvesen for å finne Tias død
    label mordEn:

        scene utenforklasserommet
        #Prat mellom KG og Christian
        show Christian at right 
        c "Inn her er toalettene, det kan være greit å vite i tilfelle …"
        show Karl-Gustav at left
        kg "Hallo"
        c "Hallo KG! Dette er din nye klassekamerat [povname]!"
        kg "..."
        kg "Jeg heter Karl-Gustav"
        c "Kan du ta med [povname] inn til klasserommet for å hilse på de andre?"
        kg "Selvfølgelig!"

        #Opprop uten Tias
        scene klasserom
        show Erik
        hmm "Hallo hallo! Erik heter jeg. Velkommen skal du være til IMI. Vi skal akkurat til å ta opprop"
        e "Titas?"
        tb "AmongUs!"
        e "Kantam"
        kn "Ja!"
        e "Jonas K"
        jk "Ja!"
        e "Tias!"
        pause 2.0
        e "Ingen Tias?"
        e "hemm … [povname], kunne du sett om du finner Tias"
        pov "Den er grei"

        #Her kan du begynne å lete etter Tias
        label friUtforsk:
            call screen klasserom
            
            label Srimon:
                scene PratKlasserom
                show Srimon
                pov "har du sett Tias?"
                sp "Jeg tror han gikk på do"
                jump friUtforsk
            
            label Arin:
                scene PratKlasserom
                show Arin
                al "Jeg tror han dro på kiwi med Peder"
                jump friUtforsk

            label KarlGangster:
                scene PratKlasserom
                show Karl-Gustav
                kg "Jeg så han ikke på do ista"
                jump friUtforsk
        
            label D1Dfellesareal:
                call screen D1Dfellesareal

            label gangMotToalett:
                call screen MotToalettD1
            
            label leterEtterTias:
                call screen LeterEtterTiasGang
                label LererkontorLeter:
                    scene lærerkontor
                    "*du leter litt*"
                    pov "Ingenting her"
                    jump leterEtterTias
    
            label ImKlasseromLeter:
                scene ImKlasserom
                "*du leter litt*"
                pov "Ingenting her"
                jump leterEtterTias