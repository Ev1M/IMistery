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


label start:
    scene bg heisaapen
    show Erik animated at right:
        xalign 0.75
        yalign 0.25
        yalign 0.15
    voice "audio/gibberish_sound_effect.mp3"
    c "Heisann, velkommen til Kuben’s Informatikk linje. Så hyggelig at du ville starte hos oss. Gå til "
    hide Erik


label idleEtterHeis:
    call screen velgHvorEtterHeis
    label Lererkontor:
        scene lærerkontor
        show Christian
        c "dette er lærer kontoret"
        jump idleEtterHeis
    
    label ImKlasserom:
        scene ImKlasserom
        show Christian
        c "Her har vi IM klasserommene for A, B og C klassen. De er i praksis nå, så du vil dessverre ikke få møtt dem "
        jump idleEtterHeis
    
    label D1Mfellesareal:
        call screen D1Mfellesareal

        label BordEn : 
            call screen AEJVbord

            label Aslak:
                show Aslak
                ab "heisa"
                show Even
                em "loloiol!"
                scene prat
                jump BordEn
            
            label Even:
                em "Heisann hopass"
                scene prat
                jump BordEn
                
            label Vilmer:
                show Vilmer
                vh "Yo, velkommen til IM, det er ingen jenter her, men vi klarer oss. Hva heter du?"
                
                python:
                    povname = renpy.input("Skriv navnet ditt:")
                    povname = povname.strip()

                vh "ok nice [povname]"
                
                scene prat
                jump mordEn
            
            label Jonas:
                joo "Heisann hopass"
                scene prat
                jump BordEn
            

    label mordEn:

        scene utenforklasserommet
        
        show Christian at right 
        c "Inn her er toalettene, det kan være greit å vite i tilfelle …"
        show Karl-Gustav at left
        kg "Hallo"
        c "Hallo KG! Dette er din nye klassekamerat [povname]!"
        kg "..."
        kg "Jeg heter Karl-Gustav"
        c "Kan du ta med [povname] inn til klasserommet for å hilse på de andre?"
        kg "Selvfølgelig!"


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
        e "hemm … [povname], kunne du tatt å se om du finner Tias"
        pov "Den er grei"

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







 
 

