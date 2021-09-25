# персонажи, в большей степени, влияющие на сюжет
define e = Character("Егор", color = "#3EB489")
define m = Character("Мику", color = "#00FFBF")
define a = Character("Алиса", color = "#FC760F")
define s = Character("Шурик", color = "#F2E088")
define y = Character("Юля", color = "#00FF00")
define p = Character("Пионер", color = "#FF0000")

#персонажи, которые иногда влияют на сюжет
define el = Character("Электроник", color = "#F2E088")
define u = Character("Ульяна", color = "#FC760F")
define vi = Character("Виола", color = "#1100FF")
define l = Character("Лена", color = "#4900FF")

# персонажи, которые не влияют на сюжет
define od = Character("Ольга Дмитриевна", color = "#00FF55")
define sl = Character("Славя", color = "#F2FF99")
define zh = Character("Женя", color = "#0045FF")


#треки для игры
define audio.blow = "music/Between August and December - Blow With the Fires.mp3"
define audio.orchid = "music/Between August and December - Orchid.mp3"
define audio.sayonara = "music/Between August and December - Sayonara Cruel World.mp3"
define audio.dtn = "music/Sergey Eybog - Door To Nightmare.mp3"
define audio.nuclear = "music/Mike Oldfield - Nuclear.mp3"
define audio.sparkle = "music/RADWIMPS - Sparkle.mp3"
define audio.ghs = "music/Sergey Eybog - Goodbye Home Shores.mp3"
define audio.tid = "music/Sergey Eybog - Trapped In Dreams.mp3"
label start:

    play music blow
    e "Тест Blow with the Fires"
    play music orchid
    e "Тест Orchid"
    play music sayonara
    e "Тест Sayonara Cruel World"
    play music dtn
    e "Тест Door To Nightmare"
    play music nuclear
    e "Тест Nuclear"
    play music sparkle
    e "Тест Sparkle"
    play music ghs
    e "Тест Goodbye Home Shores"
    play music tid
    e "Тест Trapped In Dreams"
    return