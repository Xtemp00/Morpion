
from pygame import *
from random import *
init()


surf = display.set_mode((600,600),FULLSCREEN)
run = True

#grile du jeu
def case():
    draw.line(surf,(255,255,255),(600,400),(0,400),2)
    draw.line(surf,(255,255,255),(600,200),(0,200),2)
    draw.line(surf,(255,255,255),(200,0),(200,600),2)
    draw.line(surf,(255,255,255),(400,00),(400,600),2)


Morpion=[["" for k in range(3)] for i in range(3)]


def croix(ligne,colonne):
    draw.line(surf,(255,255,255),(10+colonne,10+ligne),(190+colonne,190+ligne),10)
    draw.line(surf,(255,255,255),(10+colonne,190+ligne),(190+colonne,10+ligne),10)




def get_cases_vides(Morpion):
    result=[]
    for k in range(3):
        for l in range(3):
            if est_vide(Morpion,k,l)==True:
                result.append([k,l])
    return result

def est_vide(grille, i, j):
    if grille[i][j]=="":
        return True
    else:
        return False

def almost_win_ligne(Morpion,pion):
    result=[]
    for ligne in range(3):
        compteur=0
        vides=0
        for k in range(3):
            if Morpion[ligne][k]==pion:
                compteur=compteur+1
            if Morpion[ligne][k]=="":
                vides=vides+1
        if compteur==2 and vides==1:
            for x in range(3):
                if Morpion[ligne][x]=="":
                    result.append([ligne,x])
    return result

def almost_win_colonne(Morpion,pion):
    result=[]
    for colonne in range(3):
        compteur=0
        vides=0
        for k in range(3):
            if Morpion[k][colonne]==pion:
                compteur=compteur+1
            if Morpion[k][colonne]=="":
                vides=vides+1
        if compteur==2 and vides==1:
            for x in range(3):
                if Morpion[x][colonne]=="":
                    result.append([x,colonne])
    return result

def almost_win_diagonale(Morpion,pion):
    result=[]
    compteur=0
    vides=0
    for k in range(3):
        if Morpion[k][k]==pion:
            compteur=compteur+1
        if Morpion[k][k]=="":
            vides=vides+1
    if compteur==2 and vides==1:
        for k in range(3):
            if Morpion[k][k]=="":
                result.append([k,k])
    compteur=0
    vides=0
    for k in range(3):
        if Morpion[k][2-k]==pion:
            compteur=compteur+1
        if Morpion[k][2-k]=="":
            vides=vides+1
    if compteur==2 and vides==1:
        for k in range(3):
            if Morpion[k][2-k]=="":
                result.append([k,2-k])
    return result

def almost_win(Morpion,pion):
    result=[]
    for k in range(len(almost_win_ligne(Morpion,pion))):
        result.append(almost_win_ligne(Morpion,pion)[k])
    for k in range(len(almost_win_colonne(Morpion,pion))):
        result.append(almost_win_colonne(Morpion,pion)[k])
    for k in range(len(almost_win_diagonale(Morpion,pion))):
        result.append(almost_win_diagonale(Morpion,pion)[k])
    return result


# recherche de la case ou va jouer l'ordinateur
def ajoute_case_ordi(Morpion):
    if len(get_cases_vides(Morpion))==0:
        return False
    elif len(almost_win(Morpion,"O"))>0:
        case_ordi=randint(0,len(almost_win(Morpion,"O"))-1)
        Morpion[almost_win(Morpion,"O")[case_ordi][0]][almost_win(Morpion,"O")[case_ordi][1]]="O"
    elif len(almost_win(Morpion,"X"))>0:
        case_ordi=randint(0,len(almost_win(Morpion,"X"))-1)
        Morpion[almost_win(Morpion,"X")[case_ordi][0]][almost_win(Morpion,"X")[case_ordi][1]]="O"
        return True
    else:
        case_ordi=get_cases_vides(Morpion)
        case_ordi=case_ordi[randint(0,len(case_ordi)-1)]
        Morpion[case_ordi[0]][case_ordi[1]]="O"
        return True

init()


surf = display.set_mode((600,600),FULLSCREEN)
run = True
run2= True
run3=True
mode_compteur=0
mode_compteur_height=0

#titre du jeu
Title_game=font.SysFont("Comic Sans MS",80).render("Morpion",1,(255,0,0))
surf.blit(Title_game,Rect(150,70,100,50))
#selecteur de mode
chose_mode=font.SysFont("Comic Sans MS",30).render("Singleplayer",1,(100,100,100))
surf.blit(chose_mode,Rect(210,200,100,50))
chose_mode2=font.SysFont("Comic Sans MS",30).render("Multiplayer",1,(100,100,100))
surf.blit(chose_mode2,Rect(210,280,100,50))






while run:
    if run2==False or run3==False:
        surf.fill((0,0,0))
        #titre du jeu
        Title_game=font.SysFont("Comic Sans MS",80).render("Morpion",1,(255,0,0))
        surf.blit(Title_game,Rect(150,70,100,50))
        #selecteur de mode
        chose_mode=font.SysFont("Comic Sans MS",30).render("Singleplayer",1,(100,100,100))
        surf.blit(chose_mode,Rect(210,200,100,50))
        chose_mode2=font.SysFont("Comic Sans MS",30).render("Multiplayer",1,(100,100,100))
        surf.blit(chose_mode,Rect(210,200,100,50))

    run2=True
    run3=True
    #selection du mode de jeu
    if mode_compteur_height==0:
        chose_mode=font.SysFont("Comic Sans MS",30).render("Singleplayer",1,(150,150,150))
        surf.blit(chose_mode,Rect(210,200,100,50))
    if mode_compteur_height==1:
        chose_mode=font.SysFont("Comic Sans MS",30).render("Singleplayer",1,(100,100,100))
        surf.blit(chose_mode,Rect(210,200,100,50))
    if mode_compteur_height==0:
        chose_mode2=font.SysFont("Comic Sans MS",30).render("Multiplayer",1,(100,100,100))
        surf.blit(chose_mode2,Rect(210,280,100,50))
    if  mode_compteur_height==1:
        chose_mode2=font.SysFont("Comic Sans MS",30).render("Multiplayer",1,(150,150,150))
        surf.blit(chose_mode2,Rect(210,280,100,50))
    display.flip()
    for events in event.get():
        if events.type == QUIT:
                run = False
        if events.type==KEYDOWN and events.key==K_ESCAPE:

            if events.type == QUIT:
                run = False
        if events.type==KEYDOWN and events.key==K_DOWN:
            if mode_compteur_height<2:
                mode_compteur_height +=1
        if events.type==KEYDOWN and events.key==K_UP:
            if mode_compteur_height>=0 and mode_compteur_height<2:
                mode_compteur_height -=1
        if events.type==KEYDOWN and events.key==K_RETURN:
            if mode_compteur_height==0:
                surf.fill((0,0,0))
                mode_compteur=0
                """ce while est le mode singleplayer"""
                while run2 :
                      obj=font.SysFont("Comic Sans MS",50).render("Joueur 1 a gagné",1,(255,255,0))
                      obj2=font.SysFont("Comic Sans MS",50).render("Le robot a gagné",1,(255,255,0))
                      obj3=font.SysFont("Comic Sans MS",50).render("Egalité",1,(255,255,0))
                      vainqueur=0
                      if Morpion[0][0]=="O":
                                        draw.circle(surf, (255,0,0), (100, 100), 90, 6)
                                        Morpion[0][0]="O"
                      if Morpion[1][0]=="O":
                                        draw.circle(surf, (255,0,0), (100, 300), 90, 6)
                                        Morpion[1][0]= "O"
                      if Morpion[0][1]=="O":
                                        draw.circle(surf, (255,0,0), (300, 100), 90, 6)
                                        Morpion[0][1]= "O"
                      if Morpion[0][2]=="O":
                                        draw.circle(surf, (255,0,0), (500, 100), 90, 6)
                                        Morpion[0][2]="O"
                      if Morpion[2][0]=="O":
                                        draw.circle(surf, (255,0,0), (100, 500), 90, 6)
                                        Morpion[2][0]="O"
                      if Morpion[2][1]=="O":
                                        draw.circle(surf, (255,0,0), (300, 500), 90, 6)
                                        Morpion[2][1]="O"
                      if Morpion[2][2]=="O":
                                        draw.circle(surf, (255,0,0), (500, 500), 90, 6)
                                        Morpion[2][2]="O"
                      if Morpion[1][2]=="O":
                                        draw.circle(surf, (255,0,0), (500, 300), 90, 6)
                                        Morpion[1][2]="O"
                      if Morpion[1][1]=="O":
                                        draw.circle(surf, (255,0,0), (300, 300), 90, 6)
                                        Morpion[1][1]="O"
                      #si les rond gagne
                              #en longueur
                      if Morpion[0][0]=="O" and Morpion[0][1]=="O" and Morpion[0][2]=="O":
                                    draw.line(surf,(255,0,0),(10,100),(590,100),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                      if Morpion[1][0]=="O" and Morpion[1][1]=="O" and Morpion[1][2]=="O":
                                    draw.line(surf,(255,0,0),(10,300),(590,300),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                      if Morpion[2][0]=="O" and Morpion[2][1]=="O" and Morpion[2][2]=="O":
                                    draw.line(surf,(255,0,0),(10,500),(590,500),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                              #en hauteur
                      if Morpion[0][0]=="O" and Morpion[1][0]=="O" and Morpion[2][0]=="O":
                                    draw.line(surf,(255,0,0),(100,50),(100,550),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                      if Morpion[0][1]=="O" and Morpion[1][1]=="O" and Morpion[2][1]=="O":
                                    draw.line(surf,(255,0,0),(300,50),(300,550),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                      if Morpion[0][2]=="O" and Morpion[1][2]=="O" and Morpion[2][2]=="O":
                                    draw.line(surf,(255,0,0),(500,50),(500,550),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                              #sur les diagonales
                      if Morpion[0][0]=="O" and Morpion[1][1]=="O" and Morpion[2][2]=="O":
                                    draw.line(surf,(255,0,0),(50,50),(560,550),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1
                      if Morpion[0][2]=="O" and Morpion[1][1]=="O" and Morpion[2][0]=="O":
                                    draw.line(surf,(255,0,0),(550,50),(40,550),10)
                                    surf.blit(obj2,Rect(100,100,100,50))
                                    vainqueur+=1

                      for events in event.get():
                        #pour quitter le jeux
                        if events.type == QUIT:
                          run = False
                          run2=False
                          run3=False
                        #retour au menu principal
                        if events.type==KEYDOWN and events.key==K_BACKSPACE:
                            run2= False
                            Morpion=[["" for k in range(3)] for i in range(3)]
                        if mouse.get_pressed() == (1,0,0) :

                            #toute les croix
                            pos2 = mouse.get_pos()

                            if pos2[0] <200 and pos2[1]<200:
                                if Morpion[0][0]=="":
                                    Morpion[0][0]="X"
                                    croix(0,0)
                            if pos2[0] >200 and pos2[0]<400 and pos2[1]<200:
                                if Morpion[0][1]=="":
                                    Morpion[0][1]="X"
                                    croix(0,200)
                            if pos2[0] >400 and pos2[0] <600 and pos2[1]<200:
                                if Morpion[0][2]=="":
                                    Morpion[0][2]="X"
                                    croix(0,400)
                            if pos2[0] >400 and pos2[0] <600 and pos2[1]>200 and pos2[1]<400:
                                if Morpion[1][2]=="":
                                    Morpion[1][2]="X"
                                    croix(200,400)
                            if pos2[0] >400 and pos2[0] <600 and pos2[1]>400 and pos2[1]<600:
                                if Morpion[2][2]=="":
                                    Morpion[2][2]="X"
                                    croix(400,400)
                            if pos2[0] >200 and pos2[1]>200 and pos2[1]<400 and pos2[0]<400:
                                if Morpion[1][1]=="":
                                    Morpion[1][1]="X"
                                    croix(200,200)
                            if pos2[0] >200 and pos2[1]>400 and pos2[1]<600 and pos2[0]<400:
                                if Morpion[2][1]=="":
                                    Morpion[2][1]="X"
                                    croix(400,200)
                            if pos2[0] <200 and pos2[1]>200 and pos2[1]<400:
                                if Morpion[1][0]=="":
                                    Morpion[1][0]="X"
                                    croix(200,0)
                            if pos2[0] <200 and pos2[1]>400 and pos2[1]<600:
                                if Morpion[2][0]=="":
                                    Morpion[2][0]="X"
                                    croix(400,0)

                            #si les croix gagne
                              #en longueur
                            if Morpion[0][0]=="X" and Morpion[0][1]=="X" and Morpion[0][2]=="X":
                                    draw.line(surf,(255,0,0),(10,100),(590,100),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                            if Morpion[1][0]=="X" and Morpion[1][1]=="X" and Morpion[1][2]=="X":
                                    draw.line(surf,(255,0,0),(10,300),(590,300),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                            if Morpion[2][0]=="X" and Morpion[2][1]=="X" and Morpion[2][2]=="X":
                                    draw.line(surf,(255,0,0),(10,500),(590,500),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                              #en hauteur
                            if Morpion[0][0]=="X" and Morpion[1][0]=="X" and Morpion[2][0]=="X":
                                    draw.line(surf,(255,0,0),(100,50),(100,550),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                            if Morpion[0][1]=="X" and Morpion[1][1]=="X" and Morpion[2][1]=="X":
                                    draw.line(surf,(255,0,0),(300,50),(300,550),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                            if Morpion[0][2]=="X" and Morpion[1][2]=="X" and Morpion[2][2]=="X":
                                    draw.line(surf,(255,0,0),(500,50),(500,550),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                              #sur les diagonales
                            if Morpion[0][0]=="X" and Morpion[1][1]=="X" and Morpion[2][2]=="X":
                                    draw.line(surf,(255,0,0),(50,50),(550,550),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1
                            if Morpion[0][2]=="X" and Morpion[1][1]=="X" and Morpion[2][0]=="X":
                                    draw.line(surf,(255,0,0),(550,50),(40,550),10)
                                    surf.blit(obj,Rect(100,100,100,50))
                                    vainqueur+=1



                            if vainqueur!=1:
                                ajoute_case_ordi(Morpion)


                      if mouse.get_pressed() == (0,1,0) :
                            Morpion=[["" for k in range(3)] for i in range(3)]
                            surf.fill((0,0,0))
                            display.flip()
                      if events.type==KEYDOWN and events.key==K_ESCAPE:
                        run3=False
                        run = False
                        run2=False
                      compteur=0
                      for k in range(3):
                        for i in range(3):
                            if Morpion[k][i]=="":
                                compteur+=1
                      if compteur==0 and vainqueur==0:
                        surf.blit(obj3,Rect(215,100,100,50))

                      case()
                      display.flip()
            if mode_compteur_height==1:
                mode_compteur=0
                surf.fill((0,0,0))
                """ce while est le mode multiplayer"""
                while run3 :
                      obj=font.SysFont("Comic Sans MS",50).render("Joueur 1 a gagné",1,(255,255,0))
                      obj2=font.SysFont("Comic Sans MS",50).render("Joueur 2 a gagné",1,(255,255,0))
                      obj3=font.SysFont("Comic Sans MS",50).render("Egalité",1,(255,255,0))
                      vainqueur=0

                      for events in event.get():
                        #pour quitter le jeux
                        if events.type == QUIT:
                          run = False
                          run2=False
                          run3=False
                        #retour au menu principal
                        if events.type==KEYDOWN and events.key==K_BACKSPACE:
                            run3= False
                            Morpion=[["" for k in range(3)] for i in range(3)]
                        if mouse.get_pressed() == (0,0,1) :
                              #tous les ronds
                              pos = mouse.get_pos()
                              if pos[0] <200 and pos[1]<200:
                                        if Morpion[0][0]=="":
                                            draw.circle(surf, (255,0,0), (100, 100), 90, 6)
                                            Morpion[0][0]="O"
                              if pos[0] <200 and pos[1]>200 and pos[1]<400:
                                        if Morpion[1][0]=="":
                                            draw.circle(surf, (255,0,0), (100, 300), 90, 6)
                                            Morpion[1][0]= "O"
                              if pos[0] >200 and pos[0]<400 and pos[1]<200:
                                        if Morpion[0][1]=="":
                                            draw.circle(surf, (255,0,0), (300, 100), 90, 6)
                                            Morpion[0][1]= "O"
                              if pos[0] >400 and pos[0] <600 and pos[1]<200:
                                        if Morpion[0][2]=="":
                                            draw.circle(surf, (255,0,0), (500, 100), 90, 6)
                                            Morpion[0][2]="O"
                              if pos[0] <200 and pos[1]>400 and pos[1]<600:
                                        if Morpion[2][0]=="":
                                            draw.circle(surf, (255,0,0), (100, 500), 90, 6)
                                            Morpion[2][0]="O"
                              if pos[0] >200 and pos[1]>400 and pos[1]<600 and pos[0]<400:
                                        if Morpion[2][1]=="":
                                            draw.circle(surf, (255,0,0), (300, 500), 90, 6)
                                            Morpion[2][1]="O"
                              if pos[0] >400 and pos[0] <600 and pos[1]>400 and pos[1]<600:
                                        if Morpion[2][2]=="":
                                            draw.circle(surf, (255,0,0), (500, 500), 90, 6)
                                            Morpion[2][2]="O"
                              if pos[0] >400 and pos[0] <600 and pos[1]>200 and pos[1]<400:
                                        if Morpion[1][2]=="":
                                            draw.circle(surf, (255,0,0), (500, 300), 90, 6)
                                            Morpion[1][2]="O"
                              if pos[0] >200 and pos[1]>200 and pos[1]<400 and pos[0]<400:
                                        if Morpion[1][1]=="":
                                            draw.circle(surf, (255,0,0), (300, 300), 90, 6)
                                            Morpion[1][1]="O"
                      if mouse.get_pressed() == (1,0,0) :
                                #toute les croix
                                pos2 = mouse.get_pos()

                                if pos2[0] <200 and pos2[1]<200:
                                    if Morpion[0][0]=="":
                                        Morpion[0][0]="X"
                                        croix(0,0)
                                if pos2[0] >200 and pos2[0]<400 and pos2[1]<200:
                                    if Morpion[0][1]=="":
                                        Morpion[0][1]="X"
                                        croix(0,200)
                                if pos2[0] >400 and pos2[0] <600 and pos2[1]<200:
                                    if Morpion[0][2]=="":
                                        Morpion[0][2]="X"
                                        croix(0,400)
                                if pos2[0] >400 and pos2[0] <600 and pos2[1]>200 and pos2[1]<400:
                                    if Morpion[1][2]=="":
                                        Morpion[1][2]="X"
                                        croix(200,400)
                                if pos2[0] >400 and pos2[0] <600 and pos2[1]>400 and pos2[1]<600:
                                    if Morpion[2][2]=="":
                                        Morpion[2][2]="X"
                                        croix(400,400)
                                if pos2[0] >200 and pos2[1]>200 and pos2[1]<400 and pos2[0]<400:
                                    if Morpion[1][1]=="":
                                        Morpion[1][1]="X"
                                        croix(200,200)
                                if pos2[0] >200 and pos2[1]>400 and pos2[1]<600 and pos2[0]<400:
                                    if Morpion[2][1]=="":
                                        Morpion[2][1]="X"
                                        croix(400,200)
                                if pos2[0] <200 and pos2[1]>200 and pos2[1]<400:
                                    if Morpion[1][0]=="":
                                        Morpion[1][0]="X"
                                        croix(200,0)
                                if pos2[0] <200 and pos2[1]>400 and pos2[1]<600:
                                    if Morpion[2][0]=="":
                                        Morpion[2][0]="X"
                                        croix(400,0)


                      if mouse.get_pressed() == (0,1,0) :
                            Morpion=[["" for k in range(3)] for i in range(3)]
                            surf.fill((0,0,0))
                      display.flip()
                      if events.type==KEYDOWN and events.key==K_ESCAPE:
                        run3=False
                        run = False
                        run2=False
                      #si les croix gagne
                      #en longueur
                      if Morpion[0][0]=="X" and Morpion[0][1]=="X" and Morpion[0][2]=="X":
                            draw.line(surf,(255,0,0),(10,100),(590,100),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[1][0]=="X" and Morpion[1][1]=="X" and Morpion[1][2]=="X":
                            draw.line(surf,(255,0,0),(10,300),(590,300),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[2][0]=="X" and Morpion[2][1]=="X" and Morpion[2][2]=="X":
                            draw.line(surf,(255,0,0),(10,500),(590,500),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      #en hauteur
                      if Morpion[0][0]=="X" and Morpion[1][0]=="X" and Morpion[2][0]=="X":
                            draw.line(surf,(255,0,0),(100,50),(100,550),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][1]=="X" and Morpion[1][1]=="X" and Morpion[2][1]=="X":
                            draw.line(surf,(255,0,0),(300,50),(300,550),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][2]=="X" and Morpion[1][2]=="X" and Morpion[2][2]=="X":
                            draw.line(surf,(255,0,0),(500,50),(500,550),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      #sur les diagonales
                      if Morpion[0][0]=="X" and Morpion[1][1]=="X" and Morpion[2][2]=="X":
                            draw.line(surf,(255,0,0),(50,50),(550,550),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][2]=="X" and Morpion[1][1]=="X" and Morpion[2][0]=="X":
                            draw.line(surf,(255,0,0),(550,50),(40,550),10)
                            surf.blit(obj,Rect(100,100,100,50))
                            vainqueur+=1


                      #si les rond gagne
                      #en longueur
                      if Morpion[0][0]=="O" and Morpion[0][1]=="O" and Morpion[0][2]=="O":
                            draw.line(surf,(255,0,0),(10,100),(590,100),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[1][0]=="O" and Morpion[1][1]=="O" and Morpion[1][2]=="O":
                            draw.line(surf,(255,0,0),(10,300),(590,300),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[2][0]=="O" and Morpion[2][1]=="O" and Morpion[2][2]=="O":
                            draw.line(surf,(255,0,0),(10,500),(590,500),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      #en hauteur
                      if Morpion[0][0]=="O" and Morpion[1][0]=="O" and Morpion[2][0]=="O":
                            draw.line(surf,(255,0,0),(100,50),(100,550),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][1]=="O" and Morpion[1][1]=="O" and Morpion[2][1]=="O":
                            draw.line(surf,(255,0,0),(300,50),(300,550),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][2]=="O" and Morpion[1][2]=="O" and Morpion[2][2]=="O":
                            draw.line(surf,(255,0,0),(500,50),(500,550),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      #sur les diagonales
                      if Morpion[0][0]=="O" and Morpion[1][1]=="O" and Morpion[2][2]=="O":
                            draw.line(surf,(255,0,0),(50,50),(560,550),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      if Morpion[0][2]=="O" and Morpion[1][1]=="O" and Morpion[2][0]=="O":
                            draw.line(surf,(255,0,0),(550,50),(40,550),10)
                            surf.blit(obj2,Rect(100,100,100,50))
                            vainqueur+=1
                      compteur=0


                      for k in range(3):
                        for i in range(3):
                            if Morpion[k][i]=="":
                                compteur+=1
                      if compteur==0 and vainqueur==0:
                        surf.blit(obj3,Rect(215,100,100,50))




                      case()
                      display.flip()
    if events.type==KEYDOWN and events.key==K_ESCAPE:
        run3=False
        run = False
        run2=False
quit()
