import pygame,random,math
pygame.init();s=pygame.display.set_mode((800,600))
p=[ [400,300,random.random()*6.28,random.random()*4] for _ in range(400)]
while 1:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:exit()
    s.fill((0,0,0))
    for i in p:
        i[0]+=math.cos(i[2])*i[3];i[1]+=math.sin(i[2])*i[3]
        pygame.draw.circle(s,(random.randint(0,255),0,255),(int(i[0]),int(i[1])),2)
        if not (0<i[0]<800 and 0<i[1]<600): i[0],i[1]=400,300
    pygame.display.flip()