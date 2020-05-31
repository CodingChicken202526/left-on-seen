from pygame import *
from random import *
from math import *
from time import *
from ctypes import *

windll.user32.SetProcessDPIAware()
mixer.pre_init(44100, -16, 4, 512)
font.init()
mixer.init()
init()
#input
click = False

#text
fonte = font.Font("font/Peepo.ttf",20)

introline = fonte.render("There he goes… well, Sophie, now you’ve done it. No friends, no boyfriend, and nothing to do. I hope Flykr’s got something for me.", False, (255,192,203))


#cursor
cursorxp = image.load("images/cursor.png")
cursorxp = transform.scale(cursorxp, (24,30))
mouse.set_visible(False)

def setcursor(mx,my):
    
    window.blit(cursorxp, (mx,my))

#window
DisplayInfo = display.Info()
width = DisplayInfo.current_w
height = DisplayInfo.current_h
window = display.set_mode((width,height), FULLSCREEN)


#music and sound

clickSFX = mixer.Sound("sound/click.wav")


mixer.music.set_volume(0.5)
mixer.music.load("music/Sixteen_Twenty_Five.mp3")
mixer.music.play(-1,0)

#transition
fade = Surface((width,height))
fade.fill((0,0,0))


#menu

#thumbnail
menugif = [transform.scale(image.load("menu\menu"+str(i)+".png"), (width,height)) for i in range (4)]
#start
startbutton = transform.scale(image.load("menu\startbutton.png"), (int(12*width/43),int(61*height/386)))
startbuttonbig = transform.scale(startbutton, (int(13*width/43),int(66*height/386)))
startbuttonhit = Rect(int(405*width/688),int(175*height/386),int(191*width/688),int(47*height/387))
startbuttonbighit = Rect((int(405*width/688-width/86),int(175*height/386-5*height/772)), (int(13*width/43),int(53*height/386)))
#quit
quitbutton = transform.scale(image.load("menu\quitbutton.png"), (int(12*width/43),int(61*height/386)))
quitbuttonbig = transform.scale(quitbutton, (int(13*width/43),int(66*height/386)))
quitbuttonhit = Rect(int(405*width/688),int(265*height/387),int(191*width/688),int(47*height/387))
quitbuttonbighit = Rect((int(405*width/688-width/86),int(265*height/386-5*height/772)), (int(13*width/43),int(53*height/386)))



startcheck = False
quitcheck = False

#main scene

#profiles
profilelist = [transform.scale(image.load("images\guy"+str(i)+".png"), (width, height)) for i in range(1,4)]
profilenum = 0


#arrows
rightarrow = image.load("images/rightarrow.png")
rightarrow = transform.scale(rightarrow, (int(width/20),int(height/10)))
rightarrowrect1 = Rect(int(3*width/4),int(9*height/20),int(width/40), int(height/10))
#rightarrowrect2 = Rect(int(3*
leftarrow = image.load("images/leftarrow.png")
leftarrow = transform.scale(leftarrow, (int(width/20),int(height/10)))
leftarrowmask = mask.from_surface(leftarrow)


#Triangle detection
triDect=Surface((width,height),SRCALPHA).convert_alpha()
triDect.fill((0,0,0,0))

triDect.blit(leftarrow, (int(width/5),int(9*height/20)))
triDect.blit(rightarrow, (int(3*width/4),int(9*height/20)))



#background
background = image.load("images\Cbackground.png")
background = transform.scale(background, (width, height))
#phone
phone = image.load("images\Cphone.jpg")
phone = transform.scale(phone, (int(2*width/5),height))
#phone screen
screen = Surface((int(width/3) * 0.717,int(3*height/4) * 0.72),SRCALPHA).convert_alpha()
screen.fill((0,0,0,255))

subwayPhone = image.load("images\subway.png")
subwayPhone = transform.scale(subwayPhone, (width,height))

textFont=font.Font("font/Peepo.ttf",int(height*(5/96)*0.71))


def fadetoblack():
    global fade
    
    for i in range(0,245,5):
        fade.set_alpha(i)
        window.blit(fade,(0,0))
        display.update()
        sleep(0.025)

def fadetomain():
    global fade, window
    for i in range(245, -1, -5):
        fade.set_alpha(i)
        window.fill((0, 0, 0))
        window.blit(background, (0, 0))
        window.blit(fade, (0, 0))
        display.update()
        sleep(0.025)


#menu scene
def start():
    global startbutton
    global startbuttonbig
    global startbuttonhit
    global startbuttonbighit
    global startcheck
    global quitbutton
    global quitbuttonbig
    global quitbuttonhit
    global quitbuttonbighit
    global quitcheck
    global click
    
    timer = time()
    gifnum = 0
    
    while True:
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                return False
        
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    click = True
        mx, my = mouse.get_pos()
        window.blit(menugif[gifnum],(0,0))      

        
        if startbuttonhit.collidepoint((mx,my)) or startbuttonbighit.collidepoint((mx,my)) and startcheck:
            if click:
                clickSFX.play()
                sleep(0.4)
                fadetoblack()
                fadetomain()
                return True

            window.blit(startbuttonbig, (int(405*width/688-width/86),int(175*height/386-5*height/772)))
            startcheck = True
        else:
            window.blit(startbutton, (int(405*width/688),int(175*height/386)))
            startcheck = False
            
        if quitbuttonhit.collidepoint((mx,my)) or quitbuttonbighit.collidepoint((mx,my)) and quitcheck:
            if click:
                clickSFX.play()
                sleep(0.7)
                return False
            window.blit(quitbuttonbig, (int(405*width/688-width/86),int(265*height/386-5*height/772)))
            quitcheck = True
        else:
            window.blit(quitbutton, (int(405*width/688),int(265*height/387)))
            quitcheck = False
    
            
        setcursor(mx,my)
        
        display.update()
        timercheck = time()
        if timercheck > timer + 0.65:
            gifnum += 1
            if gifnum > 3:
                gifnum = 0
            timer = timercheck
            
#main scene
def main():
    global background
    global phone
    global screen
    global subwayPhone
    global introline
    global profilenum
    global profilelist
    
    while True:
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                return False
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    click = True

        mx, my = mouse.get_pos()

        window.blit(profilelist[profilenum],(0,0))
        window.blit(rightarrow, (int(3*width/4),int(9*height/20)))
        window.blit(leftarrow, (int(width/5),int(9*height/20)))
        window.blit(triDect,(0,0))

        if triDect.get_at((mx,my)) != (0,0,0,0) and click:
            profilenum += 1
            if profilenum > 2:
                profilenum = 0
            clickSFX.play()

        setcursor(mx,my)
        display.flip()


running = True
while running:

    for evt in event.get():
        if evt.type == QUIT:
            running = False
            break
        if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    click = True
                    
    
    if start() == False:
        running = False
        break


    main()

    display.flip()

quit()
