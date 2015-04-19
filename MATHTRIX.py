import pygame,sys
import random
import time

Aqua=(  0, 255, 255)
Black=(  0,   0,   0)
Blue=(  0,  0, 255)
Gray=(128, 128, 128)
Red=(255,   0,   0)
White=(255, 255, 255)
Yellow=(255, 255,   0)
Pink=(255,200,200)

class click:
    def __init__(self):
        self.points=0
        self.flag=1
    def help_(self):
        pygame.init()
        screen=pygame.display.set_mode([600,400])
        pygame.display.set_caption('MATHTRIX')
        font = pygame.font.SysFont('Times New Roman', 25)
        screen.fill((Aqua))
        screen.blit(font.render('*You will be shown two numbers and an operator.', True, (Black)),(30,100))
        screen.blit(font.render('*Calculate the answer before it disappears.', True, (Black)),(30,150))
        pygame.draw.rect(screen,(Pink), pygame.Rect(500,350,510,360),2)
        screen.blit(font.render('BACK', True, (Black)),(505,355))
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type is pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if mouseX>500 and mouseX<600 and mouseY>350 and mouseY<400:
                        main()

    def highscore(self):
        pygame.init()
        screen=pygame.display.set_mode([600,400])
        pygame.display.set_caption('MATHTRIX')
        font = pygame.font.SysFont('Times New Roman', 25)
        screen.fill((Aqua))
        for i in range (0,len(stack.itemsN)):
            screen.blit(font.render(stack.itemsN[i], True, (Blue)),(50,i*30))
            screen.blit(font.render(str(stack.itemsS[i]), True, (Blue)),(200,i*30))
        pygame.draw.rect(screen,(Pink), pygame.Rect(500,350,510,360),2)
        screen.blit(font.render('BACK', True, (Black)),(505,355))
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type is pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if mouseX>500 and mouseX<600 and mouseY>350 and mouseY<400:
                        main()
                
    def play(self,x,y):
        self.flag=1
        sl=2.8
        while self.flag is not 0:                
            screen=pygame.display.set_mode([800,600])
            pygame.display.set_caption('MATHTRIX')
            font = pygame.font.SysFont('Times New Roman', 40)
            screen.fill((Gray))
            fl=random.randint(1,3)
            if fl is 2:
                Range=15
                if self.points>25:
                    Range=50
                if self.points>50:
                    Range=100
                v1=random.randint(0,Range)
                v2=random.randint(0,Range)
                z=v1*v2
                op='*'
            elif fl is 1:
                Range=10+(10*self.points)
                v1=random.randint(0,Range)
                v2=random.randint(0,Range)
                z=v1+v2
                op='+'
            elif fl is 3:
                Range=10+(10*self.points)
                v1=random.randint(0,Range)
                v2=random.randint(0,Range)
                z=abs(v1-v2)
                op='-'
                
            self.flag=0
            sl=sl-0.3
            if sl<0.4:
                sl=0.4
            screen.fill((Gray))
            rand1=random.randint(50,750)
            rand2=random.randint(50,550)
            while 1:
                rand3=random.randint(50,750)
                if not rand1-15<=rand3<=rand1+15:
                    break
            while 1:
                rand4=random.randint(50,550)
                if not rand2-15<=rand4<=rand2+15:
                    break
            while 1:
                rand5=random.randint(50,750)
                if not rand1-15<=rand5<=rand1+15 and not rand3-15<=rand5<=rand3+15:
                    break
            while 1:
                rand6=random.randint(50,550)
                if not rand2-15<=rand6<=rand2+15 and not rand4-15<=rand6<=rand4+15:
                    break
            screen.blit(font.render(str(v1), True, (Aqua)),(rand1,rand2))
            pygame.display.update()
            screen.blit(font.render(str(v2), True, (Aqua)),(rand3,rand4))
            pygame.display.update()
            if fl is 1:
                screen.blit(font.render('+', True, (Aqua)),(rand5,rand6))
            elif fl is 2:
                screen.blit(font.render('*', True, (Aqua)),(rand5,rand6))
            elif fl is 3:
                screen.blit(font.render('-', True, (Aqua)),(rand5,rand6))
            pygame.display.update()
            events=pygame.event.get()
            time.sleep(sl)
            screen.fill(Gray)
            pygame.display.update()
            ans=input("Ans: ")
            stack1.push(v1,op,v2,ans)
            if ans is z:
                screen.fill((Gray))
                screen.blit(font.render('CORRECT', True, (Aqua)),(300,250))
                pygame.display.update()
                time.sleep(1)
                self.points=self.points+1
                self.flag=1
            else:
                screen.fill((Gray))
                screen.blit(font.render('WRONG', True, (Aqua)),(20,30))
                pygame.display.update()
                screen.blit(font.render('SCORE : ', True, (Aqua)),(20,90))
                screen.blit(font.render(str(self.points), True, (Aqua)),(200,90))
                pygame.draw.rect(screen,(Pink), pygame.Rect(600,500,700,600),2)
                font = pygame.font.SysFont('Times New Roman', 30)
                screen.blit(font.render('MAIN MENU', True, (Black)),(630,530))
                pygame.display.update()
                name=raw_input("\nEnter Your name : ")
                stack.push1(name,self.points)
                print "\n\n_________\n"
                for i in range (0,len(stack1.a)):
                    print stack1.a[i],stack1.b[i],stack1.c[i],'=',stack1.d[i]
                print "\n\n_________\n"
                self.points=0
        while 1:
            for event in pygame.event.get():
                if event.type is pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if mouseX>600 and mouseX<800 and mouseY>500 and mouseY<600:
                        return self.points
obj=click()

class Stack:
     def __init__(self):
         self.itemsN = []
         self.itemsS = []
         self.a=[]
         self.b=[]
         self.c=[]
         self.d=[]
     def push1(self, item1,item2):
         self.itemsN.append(item1)
         self.itemsS.append(item2)
     def push(self,v1,op,v2,ans):
         self.a.append(v1)
         self.b.append(op)
         self.c.append(v2)
         self.d.append(ans)
     def pop(self):
         a=self.itemsN.pop()
         b=self.itemsS.pop()
         print a
         print b
     def size(self):
         return len(self.items)
stack=Stack()
stack1=Stack()

def main():
        
    # Initialise screen
    pygame.init()
    screen=pygame.display.set_mode([600,400])
    pygame.display.set_caption('MATHTRIX')
    font = pygame.font.SysFont('Times New Roman', 25)
    mouseX=0
    mouseY=0
    
    screen.fill((Aqua))
    
    def draw():
        draw_rect(Pink,250,70,100,30,2)
        print_text('PLAY',Black,268,70)
        draw_rect(Pink,220,130,160,30,2)
        print_text('HIGHSCORE',Black,228,130)
        draw_rect(Pink,250,190,100,30,2)
        print_text('HELP',Black,270,190)
        draw_rect(Pink,250,250,100,30,2)
        print_text('QUIT',Black,270,250)
        pygame.display.update()

    def draw_rect(color,a,b,c,d,t):
        pygame.draw.rect(screen,(Pink), pygame.Rect(a,b,c,d),t)

    def print_text(text,color,x,y):      
        screen.blit(font.render(text, True, (color)),(x,y))
        
        
    draw()
    
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type is pygame.QUIT: 
                pygame.quit()
                sys.exit()
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX>250 and mouseX<350 and mouseY>70 and mouseY<100:
                    obj.play(mouseX,mouseY)                    
                    main()
                if mouseX>220 and mouseX<380 and mouseY>130 and mouseY<160:
                    obj.highscore()
                if mouseX>250 and mouseX<350 and mouseY>190 and mouseY<220:
                    obj.help_()
                if mouseX>250 and mouseX<350 and mouseY>250 and mouseY<280:
                    pygame.quit()
                    sys.exit()
                    pygame.display.flip()
            (mouseX,mouseY)=pygame.mouse.get_pos()
            if mouseX>250 and mouseX<350 and mouseY>70 and mouseY<100:
                draw_rect(Pink,250,70,100,30,0)
                print_text('PLAY',Black,268,70)
                pygame.display.update()
            elif mouseX>220 and mouseX<380 and mouseY>130 and mouseY<160:
                draw_rect(Pink,220,130,160,30,0)
                print_text('HIGHSCORE',Black,228,130)
                pygame.display.update()
            elif mouseX>250 and mouseX<350 and mouseY>190 and mouseY<220:
                draw_rect(Pink,250,190,100,30,0)
                print_text('HELP',Black,270,190)
                pygame.display.update()
            elif mouseX>250 and mouseX<350 and mouseY>250 and mouseY<280:
                draw_rect(Pink,250,250,100,30,0)
                print_text('QUIT',Black,270,250)
                pygame.display.update()
            else:
                main()

if __name__ == '__main__': main()
