image bg kanehall = "bg_kane_hall.png"
image bg space = "bg_space.png"
image bg aldshota_zero = "bg_aldshota_zero.png"
image bg classroom = "bg_classroom.png"
image bg roof = "bg_roof.png"
image bg sex = "bg_sex.png"
image bg explosion = "bg_explosion.png"
image bg shark = "bg_shark.png"
image bg treasure = "bg_treasure.png"
image bg robot = "bg_robot.png"

define professor = Character("Professor",color="#B3B3B3")

define lainee = Character("Lainee",color="#B3499A")
image lainee normal = "char_lainee.png"
image lainee cell = "char_lainee_cell.png"

define slaine = Character("Slaine",color="#3074E3")
image slaine normal = "char_slaine.png"
image slaine space = "char_slaine_space.png"

define inaho = Character("Inaho",color="#875D4A")
image inaho normal = "char_inaho.png"
image inaho space = "char_inaho_space.png"
image inaho note = "char_inaho_note.png"

label start:
 scene bg kanehall with fade
 play music "music_university.mp3"
 "On another dreary 10:00 AM lecture in Kane hall..."
 play sound "sfx_class_dismissed.mp3"
 professor "...When we integrate, the area under the v(x) curve is f(x) minux f(0). Our problem asks for the area out of x = 4..."
 show lainee normal at right with dissolve
 lainee "UGH no idea what profs talking about "
 lainee "would rather be home reading slainexinaho fics instead u_u"
 show lainee cell with dissolve
 "As I was considering whether to retweet this slaine fanart I found on pixiv, my eyes began to grow a little heavy."
 show lainee normal at right with dissolve
 "Before I knew it, I was dozing off..."
 lainee "Zzz...Zzz...No Slaine...Heeheehee...Zzz...Stop it~"

 scene bg space with fade
 play music "music_space_loop.mp3"
 "I awoke to find myself floating in space, with the Earth and remnants of the destroyed moon on the horizon."
 show lainee normal at right with dissolve
 lainee "WTFFFF is this"
 "Far in the distance I see a large battle going on. At the center, a trail of blue and another of orange lock together in an intricate and deadly dance."
 show inaho space at right with moveinright
 inaho "I've come for you, Slaine Troyard."
 show slaine space at left with moveinleft
 slaine "Let's settle this once and for all, Inaho Kaizuka!"
 "The two trails were two giant robots, piloted by Inaho and Slaine, locked in fierce combat against each other."
 hide lainee
 show lainee normal with dissolve
 lainee "Waaaaaaah Slainexinaho my OTP ><!!"
 "As they fought for the future of the Earth, there was a great sexual tension in the air."
 "And as if it was responding to my deepest desires, this dream suddenly got a lot weirder. A whole lot weirder."

 scene bg aldshota_zero with fade
 play music "music_logo.mp3"
 $ renpy.pause(9.2)
 
 scene bg classroom with fade
 play music "music_class.mp3"
 "Suddenly, I'm in a typical Japanese highschool classroom."
 show lainee normal with dissolve
 lainee "and i just got out of class... -_-;;"
 hide lainee with dissolve
 "It's peaceful, in a slice-of-life sort of way."
 show slaine normal at right with moveinright
 "Nervously peeking around the corner, Slaine pokes his head around the door and then quietly makes his way in."
 "I can't help but notice a packed bento lunch in his hands."
 show lainee normal with dissolve
 lainee "shy slaine is best slaine ((*/Д\\)"
 hide lainee with dissolve
 show inaho normal at left with dissolve
 "On the other side of the room is Inaho, sitting alone at his desk and looking disinterestedly out the window."
 "Slaine timidly walks over, and as he gets close Inaho notices turns around."
 inaho "Slaine-san? Don't you usually eat with Asseylum and the others?"
 slaine "I-I-I..."
 "Shaking nervously, he seems to be almost at a loss for words."
 slaine "I..."
 slaine "...I JUST WANTED TO GIVE YOU THIS, INAHO-SAMA!!"
 "He lifts up his hands and drops the bento lunchbox on Inaho's desk."
 slaine "I made you your favorite, Hanbāgā! Please enjoy it, Inaho-sama!"
 inaho "I just ate."
 slaine "WAAAH!! I'm so dumb! Now senpai will never notice me!"
 hide slaine with moveoutright
 "And with that, Slaine clumsily runs out of the room crying."
 inaho "I..."
 hide inaho with dissolve
 show lainee normal with dissolve
 lainee "that was sooooooo kawaii XDDDDD"
 
 hide lainee with dissolve
 show inaho normal with dissolve
 "Inaho sits there, looking at the bento box with his usual blank expression."
 inaho "Guess I might as well eat it."
 "As he unwraps the box, a handwritten card falls out."
 show inaho note with dissolve
 inaho "What's this?"
 "Please meet me on the roof after class. I have something I want to tell you. -Slaine"
 inaho "I..."
 "Should he go?"
 menu:
  "Yes":
   jump choice_yes
  "No":
   jump choice_no
label choice_yes:
 show lainee normal with dissolve
 lainee "YES go inaho, i want slaine to love me back so much too~"
 jump choice_end
label choice_no:
 show lainee normal with dissolve
 lainee "NUU u don't deserve slaine o(-`д´- o)"
 jump choice_end
label choice_end:
 hide lainee with dissolve
 inaho "Well, I guess I don't have anything better to do..."
 scene bg roof with fade
 play music "music_roof.mp3"
 show inaho normal at left with moveinleft
 "As class ends, Inaho heads up to the roof."
 "The beautiful, picturesque sunset in the background almost screams confession scene."
 "Inaho, however, is blissfully unaware."
 inaho "I wonder what Slaine called me up here for."
 show slaine normal at right with dissolve
 "At the other end, stood Slaine waiting paitently."
 slaine "Y-You came..."
 inaho "Slaine..."
 show lainee normal with dissolve
 lainee "Yes..?"
 hide lainee with dissolve
 slaine "I always...I always wanted to tell..."
 inaho "Slaine...I..."
 show lainee normal with dissolve
 lainee "YES. YES."
 hide lainee with dissolve
 slaine "I wanted to tell you that..."
 inaho "Slaine I don't..."
 show lainee normal with dissolve
 lainee "YES YES YES!!!"
 hide lainee with dissolve
 slaine "I..."

 scene bg sex with fade
 play music "music_sex.mp3"
 play sound "sfx_scared.mp3"
 "As they were starting to get busy..."
 inaho "Slaine..."
 scene bg explosion with fade
 "**CRASH**"
 show slaine normal at right with dissolve
 show inaho normal at left with dissolve
 "The door blew open, and seeing this both Slaine and Inaho jumped off the roof (with parachutes)."
 slaine "Inaho, don't let go!!!"
 "They hold hands tightly as they fall into the school swimming pool which unfortunately..."
 scene bg shark with fade
 "is full of sharks."
 show lainee normal with dissolve
 lainee "OMG what now??? @_@;;"
 menu:
  "Come at him":
   jump shark
  ";;;;;_;;;;;;":
   jump shark
  "fly away":
   jump shark
  "''entertain'' the shark":
   jump shark
label shark:
 "...so they decide to jump the shark..."
 show slaine normal at right with dissolve
 show inaho normal at left with dissolve
 inaho "Slaine, do you see that sparkly thing at the bottom of the pool?"
 slaine "That must be Asseylum's pendant from Ep1 S1!!!!"
 "Slaine, summoning strength unexpected of his little shota body, punches the shark and knocks it straight to New England."
 show bg treasure with dissolve
 show inaho normal at left with dissolve
 inaho "so stronk"
 "They dive down to get the pendant, but Slaine can't swim."
 inaho "its okay ill share my breath with you"
 show lainee with dissolve
 lainee "imaho i love ur seme charms waaaaahhhhhh~~~"
 "They discovered the treasure was just a bandaid(tm) at the bottom of the pool (as luminous as the sun)."
 "Inaho sees that slaine has a wound and takes this pool bandaid and puts it on slaines wound."
 lainee "YEESSS 4get about aseylum hime u only need each other~~~~~~~<3"
 "Inaho tenderly lifts slaine out of the pool"
 show slaine normal at right with dissolve
 slaine "I'm sorry I wasn't stronk enuf"
 "Inaho strokes slaines face soft..."
 inaho "the fuc u talking about m8 u punched that shark in the face lel"
 slaine "We need to escape cuz most otakus NOTP us"
 lainee "BOOOOOO fuc the h8rs inahoxslaine4lyf"
label test:
 show bg robot with dissolve
 "In order to skip the legion of NOTP-ers, they get into that one orange training kataphract just like in Rebuild of eva 3"
 "Some slaine has a timed explosion collar around his neck, you can guess what happens (kawrou also had white hair)"
 show bg kanehall with fade
 show lainee normal with dissolve
 play music "music_lel.mp3"
 professor "Your dissertaion on this OTP was incredible, we're incredibly pleased to give you our very first..."
 professor "PHD in Shotaology. Congratulations, Dr. Lainee"
 lainee "I'd like to thank Slaine."
 "THE END"
 return
