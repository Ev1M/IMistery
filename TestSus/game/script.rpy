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
# Lærer animations
# Erik animation
image Erik:
    block:
        "erik/ErikTalk.png"
        pause 0.15
        "erik/ErikTalk2.png"
        pause 0.1
        repeat 12
    "erik/Erik_Resting.png"

# Christian 
image Christian:
    block:
        "christian/ChristianTalk.png"
        pause 0.15
        "christian/ChristianTalk2.png"
        pause 0.1
        repeat 12
    "christian/ChristianTalk.png"

# Elever Animation
# Jonas animation
image Jonas:
    block:
        "jonas/JonasTalk.png"
        pause 0.15
        "jonas/JonasTalk2.png"
        pause 0.1
        repeat 12
    "jonas/JonasTalk.png"

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
image Even1:
    block:
        "even/EvenTalk.png"
        pause 0.1
        "even/EvenTalk2.png"
        pause 0.1
        repeat 12
    "even/EvenResting.png"
# Even animation men bedre :)
image Even:
    block:
        "even/EvenTop.png"
        pause 0.1
        "even/EvenMiddle.png"
        pause 0.1
        "even/EvenBottom.png"
        pause 0.1
        repeat 9
    "even/EvenTalk.png"
# Janus animation
image Jonas:
    block:
        "jonas/jonasResting.png"
        pause 0.1
        "jonas/jonasTalk2.png"
        pause 0.1
        repeat 9
    "jonas/JonasResting.png"


#Dag 1
#Intro

label start:
    scene bg heisaapen
    show Christian
    voice "audio/gibberish_sound_effect.mp3"
    c "Heisann, velkommen til Kuben’s Informatikk linje. Så hyggelig at du ville starte hos oss. Gå til "
    hide Christian

#Kan gå hvor man vil
label idleEtterHeis:
    call screen velgHvorEtterHeis
    label Lererkontor:
        scene lærerkontor
        show Christian
        c "dette er lærer kontoret"
        hide Christian
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
        label BordEn: 
            show Even
            call screen AEJVbord
            show Even
            em "loloiol!"

            label Aslak:
                show Aslak
                ab "heisa"
                hide Aslak
                show Even
                em "loloiol!"
                hide Even
                scene prat
                jump BordEn
            
            label Even:
                show Even
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
                show Jonas
                joo "Heisann hopass"
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
        hide Christian
        show Christian
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








 
 

