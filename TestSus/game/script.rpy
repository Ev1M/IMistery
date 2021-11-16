# define characters
define pov = Character("[povname]")
define c = Character("Christian")
define e = Character("Erik")
define em = Character("Even")
define vh = Character("Vilmer")
define ab = Character("Aslak")
define joo = Character("Jonas")

# Erik animation
image Erik animated:
    block:
        "erik/ErikTalk.png"
        pause 0.15
        "erik/ErikTalk2.png"
        pause 0.1
        repeat 12
    "erik/Erik_Resting.png"


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
            c "Til venstre her har vi IM klasserommene for A, B og C klassen. De er i praksis nå, så du vil dessverre ikke få møtt dem "
            jump idleEtterHeis


        label fellesareal:

            call screen fellesareal
    
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
                    python:                    
                        povname = renpy.input("Yo, velkommen til IM, det er ingen jenter her, men vi klarer oss. Hva heter du?")
                        povname = povname.strip()

                    vh "ok nice [povname]"
                    scene prat
                    jump klasserom_intro

                label Jonas:
                    joo "Heisann hopass"


                    scene prat
                label Pov:

                    jump BordEn

                label klasserom_intro:
                    call screen klasserom






 
 

