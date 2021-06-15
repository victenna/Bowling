import pygame,sys,math,time
pygame.init()
t_ime=pygame.time.Clock()
screen = pygame.display.set_mode((1500,900))
pygame.display.set_caption('Show Text')
font = pygame.font.Font(None, 64)
text4=font.render('Enter an angle:',True,(0,128,0))
A=0
t,g,delta=0,9.81,0.5
Vo=130
pi=math.pi
teta=40
i=0
X,Y=100,600
Point00=(X,Y)
Point1=(X,Y)
Point2=(X,Y)
ball_image=pygame.image.load('ball.png')
ball_image1=pygame.transform.scale(ball_image,(40,40))

Stair=pygame.image.load('stair.png')
Player=pygame.image.load('player.png')
img1=pygame.image.load('image1_1.png')
img2=pygame.image.load('image2_1.png')
img3=pygame.image.load('image3_1.png')
img4=pygame.image.load('image4_1.png')
img5=pygame.image.load('image5_1.png')
Angle=pygame.image.load('image6.png')
Enter_angle=pygame.image.load('image7.png')
game=pygame.image.load('game_over.png')
custom_cursor=pygame.image.load('cursor2.png')
push0=0
push=0
text = ''
PlotPoints=[]
Point1=(940,460)
Point2=(1167,254)
Point3=(1269,163)
Point4=(765,615)
Point5=(1042,365)
distance1=300
q1=0
distance2=300
q2=0
distance3=300
q3=0
distance4=300
q4=0
distance5=300
q5=0
transparent=(0,0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
counter= 0
q=0
s=0
cur=0
def Distance(Point,img):
    global q
    distance=D0.distance_to(pygame.Vector2(Point))
    if distance <30:
        img.fill(transparent)
        q=q+1
rect=screen.get_rect()

while Y<1001:
    s=s+1
    s1=s%10
    screen.fill((255,153,255))
    if push0==1:
        counter += 1
        counter1=round(counter/10)
        text1 = font.render(str(counter1), True, (0, 128, 0))
        text2=font.render('Time in sec:',True,(0,128,0))
        screen.blit(text2,(1005,600))
        screen.blit(text1, (1280, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                push0=1
                push=1
                #s=0
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
                A=text
                
    teta=int(A)
    txt_surface = font.render(text, True, 'red')
    if s1==0:
        screen.blit(custom_cursor,(100,160))
    screen.blit(txt_surface, (134,165))
    pygame.draw.rect(screen, 'black',[90,150,150,70],4)
    screen.blit(Player,(10,610))
    screen.blit(Stair,(400,0))
    screen.blit(img1,Point1)
    screen.blit(img2,Point2)
    screen.blit(img3,Point3)
    screen.blit(img4,Point4)
    screen.blit(img5,Point5)
    screen.blit(Angle,(400,100))
    screen.blit(text4, (30, 90))
    #screen.blit(Enter_angle,(85,120))
    rect=ball_image1.get_rect(center=rect.center)
    pygame.time.delay(10)
    if push==0:
        screen.blit(ball_image1,(100,600))
    if push ==1:
        push0=1
        txt=font.render(text,True,(255,255,255))
        Vox,Voy=Vo*math.cos(pi*teta/180), Vo*math.sin(pi*teta/180)
        i=i+1
        #i2=i%50
        t=i*delta
        X=Vox*t+100
        Y=600-(Voy*t-g*t*t/2)
        PlotPoints.append([X+15,Y+15])
        Point=(X,Y)
        screen.blit(ball_image1,(X,Y))
        if i>1:
            pygame.draw.lines(screen,'blue',False,PlotPoints,3)
        D0=pygame.Vector2(Point)
        Distance(Point1,img1)
        Distance(Point2,img2)
        Distance(Point3,img3)
        Distance(Point4,img4)
        Distance(Point5,img5)
                 
        if Y>1000:
            push=0
            text = ''
            X,Y=100,600
            PlotPoints.clear()
            PlotPoints.append([100,600+30])
            A,i=0,0
            if q==5:
                break
    pygame.display.flip()
    t_ime.tick(10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text3 = font.render('Game Over', True, green, blue)
    textRect = text3.get_rect()
    textRect.center = (300,800)
    screen.blit(text3, textRect)
    t_ime.tick(1)
    pygame.display.update()