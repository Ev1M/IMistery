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
define ek = Character("Eirik")
define aa = Character("August")
define ta = Character("Tias")
define am = Character("Ali")
define ms = Character("Mathias")
define ph = Character("Peder")

# Character positions
transform midleft:
    xcenter 0.20 
    yalign 0.0
transform midright:
    xcenter 0.80
    yalign 0.0
#___________________________________________________________________________________________________________________________
# ANIMATIONS
# Lærer animations
# Erik animation
image Erik animated:
    block:
        "erik/erikTalk.png"
        pause 0.15
        "erik/erikTalk2.png"
        pause 0.1
        repeat 12
    "erik/erikTalk.png"
# May-lil animation
image MayLil animated:
    block:
        "maylil/mayLilTalk.png"
        pause 0.15
        "maylil/mayLilTalk2.png"
        pause 0.1
        repeat 12
    "maylil/mayLilTalk.png"

# Christian 
image Christian animated:
    block:
        "christian/christianTalk.png"
        pause 0.15
        "christian/christianTalk2.png"
        pause 0.1
        repeat 12
    "christian/christianTalk.png"
image Christian resting:
    "christian/christianTalk.png"

# Elever 
# Srimon animation
image Srimon animated:
    block:
        "srimon/srimonTalk.png"
        pause 0.15
        "srimon/srimonTalk2.png"
        pause 0.1
        repeat 12
    "srimon/srimonTalk.png"

# Karl-Gustav Animation
image KarlGustav animated:
    block:
        "kg/kgTalk.png"
        pause 0.15
        "kg/kgTalk2.png"
        pause 0.1
        repeat 12
    "kg/kgTalk.png"

image KarlGustav resting:
        "kg/kgTalk.png"

# Jonas animation
image Jonas animated:
    block:
        "jonas/jonasTalk.png"
        pause 0.15
        "jonas/jonasTalk2.png"
        pause 0.1
        repeat 12
    "jonas/jonasTalk.png"

# Vilomer animation
image Vilmer animated:
    block:
        "vilmer/vilmerTalk.png"
        pause 0.1
        "vilmer/vilmerTalk2.png"
        pause 0.1
        repeat 12
    "vilmer/vilmerResting.png"
    
# vilmer Shuffle
image Arms:
    "shuffle/ARMS.png"
image Shuffle:
    block:
        "shuffle/shuffle_adobespark.png"
        pause 0.001
        "shuffle/shuffle1_adobespark.png"
        pause 0.001
        "shuffle/shuffle2_adobespark.png"
        pause 0.001
        "shuffle/shuffle3_adobespark.png"
        pause 0.001
        "shuffle/shuffle4_adobespark.png"
        pause 0.001
        "shuffle/shuffle5_adobespark.png"
        pause 0.001
        repeat 200

# Aslak animation
image Aslak animated:
    block:
        "aslak/aslakTalk.png"
        pause 0.1
        "aslak/aslakTalk2.png"
        pause 0.1
        repeat 12
    "aslak/aslakResting.png"

# Even animation
image Even animated:
    block:
        "even/evenTalk.png"
        pause 0.1
        "even/evenTalk2.png"
        pause 0.1
        repeat 12
    "even/evenTalk.png"

# Even animation men bedre :)
image Even twerk animated:
    block:
        "even/evenTop.png"
        pause 0.1
        "even/evenMiddle.png"
        pause 0.1
        "even/evenBottom.png"
        pause 0.1
        repeat 9
    "even/evenTalk.png"

# Jonas Krog animation
image JonasK animated:
    block:
        "jonasK/jonasTalk.png"
        pause 0.15
        "jonasK/jonasTalk2.png"
        pause 0.1
        repeat 12
    "jonasK/jonasTalk.png"

# Arin animation
image Arin animated:
    block:
        "arin/arinTalk.png"
        pause 0.15
        "arin/arinTalk2.png"
        pause 0.1
        repeat 12
    "arin/arinTalk.png"

# Kantam animation
image Kantam animated:
    block:
        "kantam/kantamTalk.png"
        pause 0.15
        "kantam/kantamTalk2.png"
        pause 0.1
        repeat 12
    "kantam/kantamTalk.png"

# Mathias animation
image Mathias animated:
    block:
        "mathias/mathiasTalk.png"
        pause 0.15
        "mathias/mathiasTalk2.png"
        pause 0.1
        repeat 12
    "mathias/mathiasTalk.png"

# Eirik animation
image Eirik animated:
    block:
        "eirik/eirikTalk.png"
        pause 0.15
        "eirik/eirikTalk2.png"
        pause 0.1
        repeat 12
    "eirik/eirikTalk.png"

# Peder animation
image Peder animated:
    block:
        "peder/pederTalk.png"
        pause 0.15
        "peder/pederTalk2.png"
        pause 0.1
        repeat 12
    "peder/pederTalk.png"

# Ali animation
image Ali animated:
    block:
        "ali/aliTalk.png"
        pause 0.15
        "ali/aliTalk2.png"
        pause 0.1
        repeat 12
    "ali/aliTalk.png"

# Titas animation
image Titas animated:
    block:
        "titas/titasTalk.png"
        pause 0.15
        "titas/titasTalk.png"
        pause 0.1
        repeat 12
    "titas/titasTalk.png"

# August animation
image August animated:
    block:
        "august/augustTalk.png"
        pause 0.15
        "august/augustTalk2.png"
        pause 0.1
        repeat 12
    "august/augustTalk.png"
# Tias animation
image Tias animated:
    block:
        "kantam/kantamTalk.png"
        pause 0.15
        "kantam/kantamTalk2.png"
        pause 0.1
        repeat 12
    "kantam/kantamTalk.png"


#___________________________________________________________________________________________________________________________

#Dag 1
#Intro

label start:
    scene bg heisaapen
    show Christian animated
    voice "audio/gibberish_sound_effect.mp3"
    c "Heisann, velkommen til Kuben’s Informatikk linje. Så hyggelig at du ville starte hos oss. Gå til "
    hide Christian animated

#Kan gå hvor man vil
label idleEtterHeis:
    call screen velgHvorEtterHeis
    label Lererkontor:
        scene lærerkontor
        show Christian animated
        c "dette er lærer kontoret"
        hide Christian animated
        jump idleEtterHeis
    #Du og Christian ser i IM klasserommene
    label ImKlasserom:
        scene ImKlasserom
        show Christian animated
        c "Her har vi IM klasserommene for A, B og C klassen. De er i praksis nå, så du vil dessverre ikke få møtt dem "
        jump idleEtterHeis
    #Dag 1 Morning fellesareal
    label D1Mfellesareal:
        call screen D1Mfellesareal

        #Bordet hvor Aslak, Even, Jonas og Vilmer sitter.
        label BordEn: 
            call screen AEJVbord
            label Aslak:
                scene fellesareal
                hide Christian animated
                hide Vilmer animated
                hide Jonas animated
                hide Even animated
                show Aslak animated
                ab "ENDELIG! En ny kar her! *rister av glede* ser fram til en ny person, begynner å bli lei av 	folk som Tias, sånne folk bli bare kjedelige etterhvert"
                "{i}OK?!{/i}"
                jump BordEn
            
            #Prate med Even på morgen.
            label Even:
                scene fellesareal
                hide Vilmer animated
                hide Aslak animated
                hide Jonas animated
                show Even animated
                menu:
                    "Hei":
                        jump pratmdEv1
                    
                    "...":
                        jump LoLnei

                label pratmdEv1:
                    show Even animated
                    em "hei, spiller du league of legends?"
                    menu:
                        "Ja":
                            jump LoLja
                        
                        "Nei":
                            jump LoLnei
                        
                        "...":
                            jump LoLnei
                    
                    label LoLja:
                        show Even animated
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

                        hide Even animated
                    
                    label LoLnei:
                        hide Even twerk animated
                        hide Even animated
                        show Even animated
                        $menu_flag = False
                        em "Din stygge dritt, hvorfor kom du hit da!? *sparker deg i ansiktet, du får vondt*"
                        jump BordEn
                        hide Even animated
                    
                    label aksepter:
                        hide Even twerk animated
                        $menu_flag = False
                        em "Acceptable"
                        jump BordEn 
                        hide Even animated
                    
                    hide Even animated
                    scene prat
                    
                
                
            label Vilmer:
                scene fellesareal
                hide Even animated
                hide Aslak animated
                hide Jonas animated
                show Vilmer animated
                vh "Yo, velkommen til IM, det er ingen jenter her, men vi klarer oss. Hva heter du?"
                
                python:
                    povname = renpy.input("Skriv navnet ditt:")
                    povname = povname.strip()

                vh "må si det var meget hyggelig å hilse på deg [povname]"
                show Arms:
                    xalign 0.33
                    ycenter 0.99
                show Shuffle:
                    xalign 0.3
                    ycenter 0.639
                vh "check out the shuffle *stokker kort*"
                hide Arms
                hide Shuffle
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
                scene fellesareal
                hide Vilmer animated
                hide Aslak animated
                hide Even animated
                show Jonas animated
                joo "Yo! Sorry jeg måtte løpe, rakk så 	vitt bussen, men er her nå. Jeg heter Jonas, håper du er litt effektiv for det er ikke jeg, men vi skal nok hygge oss uansett"
                scene prat
                jump BordEn
            
#Her starter sekvesen for å finne Tias død
label mordEn:
    scene utenforklasserommet
    #Prat mellom KG og Christian
    show Christian animated at midleft
    c "Inn her er toalettene, det kan være greit å vite i tilfelle …"
    show Christian resting at midleft
    show KarlGustav animated at midright
    kg "Hallo"
    show KarlGustav resting at midright
    hide Christian animated 
    show Christian animated at midleft
    c "Hallo Karl! Dette er din nye klassekamerat [povname]!"
    show Christian resting at midleft
    hide KarlGustav animated
    show KarlGustav animated at midright
    kg "..."
    kg "Jeg heter Karl-Gustav"
    show KarlGustav resting at midright
    hide Christian animated
    show Christian animated at midleft
    c "Kan du ta med [povname] inn til klasserommet for å hilse på de andre?"
    show Christian resting at midleft 
    hide KarlGustav animated
    show KarlGustav animated at midright
    kg "Selvfølgelig!"
    hide Christian
    hide KarlGustav
    #Opprop uten Tias
    scene klasserom
    show Erik animated
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
            show Srimon animated
            pov "har du sett Tias?"
            sp "Jeg tror han gikk på do"
            jump friUtforsk
        
        label Arin:
            scene PratKlasserom
            show Arin animated
            al "Jeg tror han dro på kiwi med Peder"
            jump friUtforsk

        label KarlGangster:
            scene PratKlasserom
            show KarlGustav animated
            kg "Jeg så han ikke på do ista"
            jump friUtforsk
        
        label leterEtterTias:
            call screen LeterEtterTiasGang
            label LererkontorLeter:
                scene lærerkontor
                "*du leter litt*"
                pov "Ingenting her"
                jump leterEtterTias
        if tias == "død":
            pov "mamma mia"
            jump hjelp

        label ImKlasseromLeter:
            scene ImKlasserom
            "*du leter litt*"
            pov "Ingenting her"
            jump leterEtterTias
        
            label D1Dfellesareal:
                call screen D1Dfellesareal

            label gangMotToalett:
                call screen MotToalettD1
            
            label ToalettEn:
                call screen toalettEn
            label ToalettTo:
                call screen toalettTo
            label ToalettTre:
                call screen toalettTre

            label Toalett1:
                scene toalett-tomt
                "*du leter litt*"
                pov "Ingenting her"
                jump ToalettTre
            
            label Toalett2:
                scene toalett-tomt
                "*du leter litt*"
                show Even twerk animated
                pov "WTF"
                em "Gå ut kompis!"
                jump ToalettTre

            label Toalett3:
                scene toalett-tomt
                "*du leter litt*"
                pov "Ingenting her"
                jump ToalettTre
            
            label ToalettDead:
                scene tias-død
                pov "Å dvæen!"
                pov "Er det Tias? og er han død?!"
                pov "SHIT! Jeg må si ifra til Erik."
                $ tias = "død"
                jump ToalettTre

        label hjelp:
            pov "TIAS ER DRUKNET PÅ DO"
            e "HÆ!"