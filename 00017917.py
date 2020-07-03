import tkinter as tk, threading
import AbsolutePath
import imageio
from PIL import Image, ImageTk, ImageSequence
import os
import sys

def animateBTN(cvs, prnt, sq, img, counter, speed):
    cvs.itemconfig(img, image=sq[counter])
    prnt.after(speed, lambda: animateBTN(cvs, prnt, sq, img, (counter+1) % len(sq), speed))
def olvidar():
    papa.place_forget()
    title.place_forget()
    c1.place_forget()
    c2.place_forget()
    c3.place_forget()
    c4.place_forget()
    c5.place_forget()
def recordarMain():
    papa.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    title.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.15)
    c1.place(relx = 0.1, rely = 0.35, relwidth = 0.25, relheight = 0.1)
    c2.place(relx = 0.1, rely = 0.55, relwidth = 0.25, relheight = 0.1)
    c3.place(relx = 0.1, rely = 0.75, relwidth = 0.25, relheight = 0.1)
    c4.place(relx = 0.65, rely = 0.35, relwidth = 0.25, relheight = 0.1)
    c5.place(relx = 0.65, rely = 0.55, relwidth = 0.25, relheight = 0.1)

def regresarMenu(e):
    if(e.x>35 and e.x<75 and e.y>30 and e.y<70 ):
        canvasHome.destroy()
        recordarMain()

def dominioWindow(e):
    global domImg,homeImg,canvasHome,dominioFlag,d1,d2,menu
    dominioFlag = 1
    olvidar()
    canvasHome = tk.Canvas(root, highlightthickness = 0)
    canvasHome.create_image(0,0,anchor="nw", image = domImg)
    menu = canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.place(x = 0 , y = 0, relwidth = 1, relheight = 1)
    canvasHome.bind("<Button-1>", regresarMenu)
    d1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = text, text = "1")
    d1.place(x = 750, y=130, width=75, height = 75)
    d2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "2")
    d2.place(x = 750, y=220, width=75, height = 75)
    d1.bind("<Button-1>", domView1)
    d2.bind("<Button-1>", domView2)
def domView1(e):
    global dominioFlag
    if(dominioFlag!=1):
        d1.config(bg = selectedBtnColor)
        d2.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = domImg)
        canvasHome.tag_raise(menu)
        dominioFlag = 1
def domView2(e):
    global dominioFlag
    if(dominioFlag!=2):
        d1.config(bg = btnColor)
        d2.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = domImg2)
        canvasHome.tag_raise(menu)
        dominioFlag = 2
def mallaWindow(e):
    global mallaImg,homeImg,canvasHome, mallaFlag,m1,m2,menu
    mallaFlag = 1
    olvidar()
    canvasHome = tk.Canvas(root, highlightthickness = 0)
    canvasHome.create_image(0,0,anchor="nw", image = mallaImg)
    menu = canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.place(x = 0 , y = 0, relwidth = 1, relheight = 1)
    canvasHome.bind("<Button-1>", regresarMenu)
    m1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = text, text = "1")
    m1.place(x = 750, y=130, width=75, height = 75)
    m2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "2")
    m2.place(x = 750, y=220, width=75, height = 75)
    m1.bind("<Button-1>", meshView1)
    m2.bind("<Button-1>", meshView2)
def meshView1(e):
    global mallaFlag
    if(mallaFlag!=1):
        m1.config(bg = selectedBtnColor)
        m2.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = mallaImg)
        canvasHome.tag_raise(menu)
        mallaFlag = 1
def meshView2(e):
    global mallaFlag
    if(mallaFlag!=2):
        m1.config(bg = btnColor)
        m2.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = mallaImg2)
        canvasHome.tag_raise(menu)
        mallaFlag = 2
def tablaWindow(e):
    global tablaImg,homeImg,canvasHome
    olvidar()
    canvasHome = tk.Canvas(root, highlightthickness = 0)
    canvasHome.create_image(0,0,anchor="nw", image = tablaImg)
    canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.place(x = 0 , y = 0, relwidth = 1, relheight = 1)
    canvasHome.bind("<Button-1>", regresarMenu)
def modeloWindow(e):
    global modeloImg,homeImg,canvasHome
    olvidar()
    canvasHome = tk.Canvas(root, highlightthickness = 0)
    canvasHome.create_image(0,0,anchor="nw", image = modeloImg)
    canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.place(x = 0 , y = 0, relwidth = 1, relheight = 1)
    canvasHome.bind("<Button-1>", regresarMenu)
def pasosWindow(e):
    global homeImg,canvasHome,pasosFlag,menu
    pasosFlag = 1
    olvidar()
    canvasHome = tk.Canvas(root, highlightthickness = 0)
    canvasHome.create_image(0,0,anchor="nw", image = paso1Img)
    menu = canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.place(x = 0 , y = 0, relwidth = 1, relheight = 1)
    canvasHome.tag_raise(menu)
    canvasHome.bind("<Button-1>", regresarMenu)
    botonesPasos()
def pasosWindow2(e):
    global componentesFlag, pasosFlag, componentesFlag2
    destroyTerminos()
    pasosFlag = 1
    componentesFlag = 0
    componentesFlag2 = 0
    canvasHome.create_image(0,0,anchor="nw", image = paso1Img)
    menu = canvasHome.create_image(35,30,anchor="nw", image = homeImg)
    canvasHome.tag_raise(menu)
    canvasHome.bind("<Button-1>", regresarMenu)
    botonesPasos()
def botonesPasos():
    global p1, p2, p3, p4, p5, p6, menu
    p1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = text, text = "1")
    p1.place(x = 0, y=408, width=143, height = 72)
    p2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "2")
    p2.place(x = 142.33, y=408, width=143, height = 72)
    p3 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "3")
    p3.place(x = 284.66, y=408, width=143, height = 72)
    p4 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "4")
    p4.place(x = 426.99, y=408, width=143, height = 72)
    p5 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "5")
    p5.place(x = 569.3233, y=408, width=143, height = 72)
    p6 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "6")
    p6.place(x = 711.6533, y=408, width=143, height = 72)
    componentes = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "Ver componentes")
    componentes.place(x = 684, y=10, width=160, height = 50)
    p1.bind("<Button-1>", pasoUno)
    p2.bind("<Button-1>", pasoDos)
    p3.bind("<Button-1>", pasoTres)
    p4.bind("<Button-1>", pasoCuatro)
    p5.bind("<Button-1>", pasoCinco)
    p6.bind("<Button-1>", pasoSeis)
    componentes.bind("<Button-1>", botonesComponentesMatrices)
def pasoUno(e):
    global pasosFlag
    if(pasosFlag != 1):
        p1.config(bg = selectedBtnColor)
        p2.config(bg = btnColor)
        p3.config(bg = btnColor)
        p4.config(bg = btnColor)
        p5.config(bg = btnColor)
        p6.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso1Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 1
def pasoDos(e):
    global pasosFlag
    if(pasosFlag !=2):
        p1.config(bg = btnColor)
        p2.config(bg = selectedBtnColor)
        p3.config(bg = btnColor)
        p4.config(bg = btnColor)
        p5.config(bg = btnColor)
        p6.config(bg = btnColor)
        p2.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso2Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 2
def pasoTres(e):
    global pasosFlag
    if(pasosFlag !=3):
        p1.config(bg = btnColor)
        p2.config(bg = btnColor)
        p3.config(bg = selectedBtnColor)
        p4.config(bg = btnColor)
        p5.config(bg = btnColor)
        p6.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso3Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 3
def pasoCuatro(e):
    global pasosFlag
    if(pasosFlag !=4):
        p1.config(bg = btnColor)
        p2.config(bg = btnColor)
        p3.config(bg = btnColor)
        p4.config(bg = selectedBtnColor)
        p5.config(bg = btnColor)
        p6.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso4Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 4
def pasoCinco(e):
    global pasosFlag
    if(pasosFlag !=5):
        p1.config(bg = btnColor)
        p2.config(bg = btnColor)
        p3.config(bg = btnColor)
        p4.config(bg = btnColor)
        p5.config(bg = selectedBtnColor)
        p6.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso5Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 5
def pasoSeis(e):
    global pasosFlag
    if(pasosFlag !=6):
        p1.config(bg = btnColor)
        p2.config(bg = btnColor)
        p3.config(bg = btnColor)
        p4.config(bg = btnColor)
        p5.config(bg = btnColor)
        p6.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = paso6Img)
        canvasHome.tag_raise(menu)
        pasosFlag = 6

def botonesComponentesMatrices(e):
    global terminoL, terminoP, terminoM, terminoQ, terminob, terminobprima, menu, homeImg, canvasHome, componentesFlag, componentesFlag2, terminoL1,terminoL2, terminoL3, switchToPasos
    componentesFlag = 1
    componentesFlag2 = 1
    canvasHome.create_image(0,0,anchor="nw", image = compL1Img)
    switchToPasos = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "Ver pasos")
    switchToPasos.place(x = 684, y=10, width=160, height = 50)
    
    terminoL = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = text, text = "L")
    terminoL.place(x = 0, y=408, width=143, height = 72)
    terminoL1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
    terminoL1.place(x = 0, y=384, width=47.67, height = 24)
    terminoL2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
    terminoL2.place(x = 47.67, y=384, width=47.67, height = 24)
    terminoL3 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "3")
    terminoL3.place(x = 95.34, y=384, width=47.67, height = 24)

    terminoP = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "P")
    terminoP.place(x = 142.33, y=408, width=143, height = 72)
    terminoM = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "M")
    terminoM.place(x = 284.66, y=408, width=143, height = 72)
    terminoQ = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "Q")
    terminoQ.place(x = 426.99, y=408, width=143, height = 72)
    terminob = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "b")
    terminob.place(x = 569.3233, y=408, width=143, height = 72)
    terminobprima = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = text, text = "b'")
    terminobprima.place(x = 711.6533, y=408, width=143, height = 72)
    canvasHome.tag_raise(menu)

    canvasHome.bind("<Button-1>", regresarMenu)
    terminoL.bind("<Button-1>", componenteL)
    terminoL1.bind("<Button-1>", componenteL1)
    terminoL2.bind("<Button-1>", componenteL2)
    terminoL3.bind("<Button-1>", componenteL3)
    terminoP.bind("<Button-1>", componenteP)
    terminoM.bind("<Button-1>", componenteM)
    terminoQ.bind("<Button-1>", componenteQ)
    terminob.bind("<Button-1>", componenteb)
    terminobprima.bind("<Button-1>", componentebprima)
    switchToPasos.bind("<Button-1>", pasosWindow2)
def componenteL(e):
    global componentesFlag, componentesFlag2, terminoL1,terminoL2, terminoL3
    if(componentesFlag != 1):
        destroyTerminos()
        terminoL.config(bg = selectedBtnColor)
        terminoP.config(bg = btnColor)
        terminoM.config(bg = btnColor)
        terminoQ.config(bg = btnColor)
        terminob.config(bg = btnColor)
        terminobprima.config(bg = btnColor)
        terminoL1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
        terminoL1.place(x = 0, y=384, width=47.67, height = 24)
        terminoL2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
        terminoL2.place(x = 47.67, y=384, width=47.67, height = 24)
        terminoL3 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "3")
        terminoL3.place(x = 95.34, y=384, width=47.67, height = 24)
        canvasHome.create_image(0,0,anchor="nw", image = compL1Img)
        canvasHome.tag_raise(menu)
        componentesFlag = 1
        componentesFlag2 = 1
        terminoL1.bind("<Button-1>", componenteL1)
        terminoL2.bind("<Button-1>", componenteL2)
        terminoL3.bind("<Button-1>", componenteL3)
def componenteL1(e):
    global componentesFlag2
    if(componentesFlag2 != 1):
        terminoL1.config(bg = selectedBtnColor)
        terminoL2.config(bg = btnColor)
        terminoL3.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compL1Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 1
def componenteL2(e):
    global componentesFlag2
    if(componentesFlag2 != 2):
        terminoL1.config(bg = btnColor)
        terminoL2.config(bg = selectedBtnColor)
        terminoL3.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compL2Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 2
def componenteL3(e):
    global componentesFlag2
    if(componentesFlag2 != 3):
        terminoL1.config(bg = btnColor)
        terminoL2.config(bg = btnColor)
        terminoL3.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compL3Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 3

def componenteP(e):
    global componentesFlag
    terminoL1.destroy()
    terminoL2.destroy()
    terminoL3.destroy()
    if(componentesFlag != 2):
        destroyTerminos()
        terminoL.config(bg = btnColor)
        terminoP.config(bg = selectedBtnColor)
        terminoM.config(bg = btnColor)
        terminoQ.config(bg = btnColor)
        terminob.config(bg = btnColor)
        terminobprima.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compPImg)
        canvasHome.tag_raise(menu)
        componentesFlag = 2

def componenteM(e):
    global componentesFlag, componentesFlag2, terminoM1,terminoM2, terminoM3, terminoM4
    if(componentesFlag != 3):
        destroyTerminos()
        terminoL.config(bg = btnColor)
        terminoP.config(bg = btnColor)
        terminoM.config(bg = selectedBtnColor)
        terminoQ.config(bg = btnColor)
        terminob.config(bg = btnColor)
        terminobprima.config(bg = btnColor)
        terminoM1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
        terminoM1.place(x = 284, y=384, width=35.75, height = 24)
        terminoM2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
        terminoM2.place(x = 320, y=384, width=35.75, height = 24)
        terminoM3 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "3")
        terminoM3.place(x = 356, y=384, width=35.75, height = 24)
        terminoM4 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "4")
        terminoM4.place(x = 391, y=384, width=35.75, height = 24)
        canvasHome.create_image(0,0,anchor="nw", image = compM1Img)
        canvasHome.tag_raise(menu)
        componentesFlag = 3
        componentesFlag2 = 1
        terminoM1.bind("<Button-1>", componenteM1)
        terminoM2.bind("<Button-1>", componenteM2)
        terminoM3.bind("<Button-1>", componenteM3)
        terminoM4.bind("<Button-1>", componenteM4)
def componenteM1(e):
    global componentesFlag2
    if(componentesFlag2 != 1):
        terminoM1.config(bg = selectedBtnColor)
        terminoM2.config(bg = btnColor)
        terminoM3.config(bg = btnColor)
        terminoM4.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compM1Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 1
def componenteM2(e):
    global componentesFlag2
    if(componentesFlag2 != 2):
        terminoM1.config(bg = btnColor)
        terminoM2.config(bg = selectedBtnColor)
        terminoM3.config(bg = btnColor)
        terminoM4.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compM2Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 2
def componenteM3(e):
    global componentesFlag2
    if(componentesFlag2 != 3):
        terminoM1.config(bg = btnColor)
        terminoM2.config(bg = btnColor)
        terminoM3.config(bg = selectedBtnColor)
        terminoM4.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compM3Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 3
def componenteM4(e):
    global componentesFlag2
    if(componentesFlag2 != 4):
        terminoM1.config(bg = btnColor)
        terminoM2.config(bg = btnColor)
        terminoM3.config(bg = btnColor)
        terminoM4.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compM4Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 4

def componenteQ(e):
    global componentesFlag, componentesFlag2, terminoQ1,terminoQ2, terminoQ3
    if(componentesFlag != 4):
        destroyTerminos()
        terminoL.config(bg = btnColor)
        terminoP.config(bg = btnColor)
        terminoM.config(bg = btnColor)
        terminoQ.config(bg = selectedBtnColor)
        terminob.config(bg = btnColor)
        terminobprima.config(bg = btnColor)
        terminoQ1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
        terminoQ1.place(x = 426.99, y=384, width=47.67, height = 24)
        terminoQ2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
        terminoQ2.place(x = 474.66, y=384, width=47.67, height = 24)
        terminoQ3 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "3")
        terminoQ3.place(x = 522.33, y=384, width=47.67, height = 24)
        canvasHome.create_image(0,0,anchor="nw", image = compQ1Img)
        canvasHome.tag_raise(menu)
        componentesFlag = 4
        componentesFlag2 = 1
        terminoQ1.bind("<Button-1>", componenteQ1)
        terminoQ2.bind("<Button-1>", componenteQ2)
        terminoQ3.bind("<Button-1>", componenteQ3)
def componenteQ1(e):
    global componentesFlag2
    if(componentesFlag2 != 1):
        terminoQ1.config(bg = selectedBtnColor)
        terminoQ2.config(bg = btnColor)
        terminoQ3.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compQ1Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 1
def componenteQ2(e):
    global componentesFlag2
    if(componentesFlag2 != 2):
        terminoQ1.config(bg = btnColor)
        terminoQ2.config(bg = selectedBtnColor)
        terminoQ3.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compQ2Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 2
def componenteQ3(e):
    global componentesFlag2
    if(componentesFlag2 != 3):
        terminoQ1.config(bg = btnColor)
        terminoQ2.config(bg = btnColor)
        terminoQ3.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compQ3Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 3

def componenteb(e):
    global componentesFlag, componentesFlag2, terminob1, terminob2
    if(componentesFlag != 5):
        destroyTerminos()
        terminoL.config(bg = btnColor)
        terminoP.config(bg = btnColor)
        terminoM.config(bg = btnColor)
        terminoQ.config(bg = btnColor)
        terminob.config(bg = selectedBtnColor)
        terminobprima.config(bg = btnColor)
        terminob1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
        terminob1.place(x = 569.3233, y=384, width=71.5, height = 24)
        terminob2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
        terminob2.place(x = 640.8233, y=384, width=71.5, height = 24)
        canvasHome.create_image(0,0,anchor="nw", image = compb1Img)
        canvasHome.tag_raise(menu)
        componentesFlag = 5
        componentesFlag2 = 1
        terminob1.bind("<Button-1>", componenteb1)
        terminob2.bind("<Button-1>", componenteb2)
def componenteb1(e):
    global componentesFlag2
    if(componentesFlag2 != 1):
        terminob1.config(bg = selectedBtnColor)
        terminob2.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compb1Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 1
def componenteb2(e):
    global componentesFlag2
    if(componentesFlag2 != 2):
        terminob1.config(bg = btnColor)
        terminob2.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compb2Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 2

def componentebprima(e):
    global componentesFlag, componentesFlag2, terminobprima1, terminobprima2
    if(componentesFlag != 6):
        destroyTerminos()
        terminoL.config(bg = btnColor)
        terminoP.config(bg = btnColor)
        terminoM.config(bg = btnColor)
        terminoQ.config(bg = btnColor)
        terminob.config(bg = btnColor)
        terminobprima.config(bg = selectedBtnColor)
        terminobprima1 = tk.Label(canvasHome, fg = fgColor, bg = selectedBtnColor,font = textBTNsmall, text = "1")
        terminobprima1.place(x = 711.6533, y=384, width=71.5, height = 24)
        terminobprima2 = tk.Label(canvasHome, fg = fgColor, bg = btnColor,font = textBTNsmall, text = "2")
        terminobprima2.place(x = 783.1533, y=384, width=71.5, height = 24)
        canvasHome.create_image(0,0,anchor="nw", image = compbprima1Img)
        canvasHome.tag_raise(menu)
        componentesFlag = 6
        componentesFlag2 = 1
        terminobprima1.bind("<Button-1>", componentebprima1)
        terminobprima2.bind("<Button-1>", componentebprima2)
def componentebprima1(e):
    global componentesFlag2
    if(componentesFlag2 != 1):
        terminobprima1.config(bg = selectedBtnColor)
        terminobprima2.config(bg = btnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compbprima1Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 1
def componentebprima2(e):
    global componentesFlag2
    if(componentesFlag2 != 2):
        terminobprima1.config(bg = btnColor)
        terminobprima2.config(bg = selectedBtnColor)
        canvasHome.create_image(0,0,anchor="nw", image = compbprima2Img)
        canvasHome.tag_raise(menu)
        componentesFlag2 = 2
def destroyTerminos():
    if(componentesFlag == 1):
        terminoL1.destroy()
        terminoL2.destroy()
        terminoL3.destroy()
    if(componentesFlag == 3):
        terminoM1.destroy()
        terminoM2.destroy()
        terminoM3.destroy()
        terminoM4.destroy()
    if(componentesFlag == 4):
        terminoQ1.destroy()
        terminoQ2.destroy()
        terminoQ3.destroy()
    if(componentesFlag == 5):
        terminob1.destroy()
        terminob2.destroy()
    if(componentesFlag == 6):
        terminobprima1.destroy()
        terminobprima2.destroy()
root = tk.Tk()
root.geometry('854x480')
root.title("MEF 3D")
text = ("courier new", 17)
textBTN = ("courier new", 17)
textBTNsmall = ("courier new", 12)
fgColor = "#FFFFFF"
bgColor = "#000000"
btnColor = "#252525"
selectedBtnColor = "#121212"
backgroundImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/bg.png'))
homeImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/home.png'))
domImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/Dominio.png'))
domImg2 = tk.PhotoImage(file = AbsolutePath.resource_path('images/Dominio2.png'))
mallaImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/Malla.png'))
mallaImg2 = tk.PhotoImage(file = AbsolutePath.resource_path('images/Malla2.png'))
tablaImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/tablaConectividades.png'))
modeloImg = tk.PhotoImage(file = AbsolutePath.resource_path('images/Modelo.png'))
paso1Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso1.png'))
paso2Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso2.png')) 
paso3Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso3.png')) 
paso4Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso4.png')) 
paso5Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso5.png')) 
paso6Img = tk.PhotoImage(file = AbsolutePath.resource_path('pasos/paso6.png')) 

compL1Img  = tk.PhotoImage(file = AbsolutePath.resource_path('compM/L1.png'))
compL2Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/L2.png'))
compL3Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/L3.png'))
compPImg = tk.PhotoImage(file = AbsolutePath.resource_path('compM/P.png'))
compM1Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/M1.png'))
compM2Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/M2.png'))
compM3Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/M3.png'))
compM4Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/M4.png'))
compQ1Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/Q1.png'))
compQ2Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/Q2.png'))
compQ3Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/Q3.png'))
compb1Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/b1.png'))
compb2Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/b2.png'))
compbprima1Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/bprima1.png'))
compbprima2Img = tk.PhotoImage(file = AbsolutePath.resource_path('compM/bprima2.png'))

papa = tk.Label(root, image = backgroundImg)
papa.place(x = 0, y = 0, relwidth = 1, relheight = 1)

title = tk.Label(root, fg = fgColor, bg = btnColor,font = text, text = "Metodo de los elementos finitos en 3 dimensiones")
title.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.15)

################################# botones ##############################################
c1 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence1 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c1IMG = c1.create_image(0,0,anchor="nw", image=sequence1[0])
animateBTN(c1, root, sequence1, c1IMG, 1, 66)
c1.create_text(60, 12, anchor = "nw", fill="#ffffff", font=textBTN, text="Dominio")
c1.place(relx = 0.1, rely = 0.35, relwidth = 0.25, relheight = 0.1)

c2 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence2 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c2IMG = c2.create_image(0,0,anchor="nw", image=sequence2[0])
animateBTN(c2, root, sequence2, c2IMG, 1, 66)
c2.create_text(75, 12, anchor = "nw", fill="#ffffff", font=textBTN, text="Malla")
c2.place(relx = 0.1, rely = 0.55, relwidth = 0.25, relheight = 0.1)

c3 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence3 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c3IMG = c3.create_image(0,0,anchor="nw", image=sequence3[0])
animateBTN(c3, root, sequence3, c3IMG, 1, 66)
c3.create_text(68, 5, anchor = "nw", fill="#ffffff", font=textBTNsmall, text="Tabla de")
c3.create_text(42, 23, anchor = "nw", fill="#ffffff", font=textBTNsmall, text="conectividades")
c3.place(relx = 0.1, rely = 0.75, relwidth = 0.25, relheight = 0.1)


c4 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence4 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c4IMG = c4.create_image(0,0,anchor="nw", image=sequence4[0])
animateBTN(c4, root, sequence4, c4IMG, 1, 66)
c4.create_text(70, 12, anchor = "nw", fill="#ffffff", font=textBTN, text="Modelo")
c4.place(relx = 0.65, rely = 0.35, relwidth = 0.25, relheight = 0.1)

c5 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence5 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c5IMG = c5.create_image(0,0,anchor="nw", image=sequence5[0])
animateBTN(c5, root, sequence5, c5IMG, 1, 66)
c5.create_text(70, 5, anchor = "nw", fill="#ffffff", font=textBTNsmall, text="Pasos y")
c5.create_text(50, 23, anchor = "nw", fill="#ffffff", font=textBTNsmall, text="componentes")
c5.place(relx = 0.65, rely = 0.55, relwidth = 0.25, relheight = 0.1)

c6 = tk.Canvas(root, bd=0, highlightthickness=0)
sequence5 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/neon.gif')))]
c6IMG = c6.create_image(0,0,anchor="nw", image=sequence5[0])
animateBTN(c6, root, sequence5, c6IMG, 1, 66)
c6.create_text(45, 12, anchor = "nw", fill="#ffffff", font=textBTN, text="Ensamblaje")
c6.place(relx = 0.65, rely = 0.75, relwidth = 0.25, relheight = 0.1)

def ensamblajeWindow(e):
    newWindow = tk.Toplevel(root)
    newWindow.geometry("854x480")
    newWindow.title("Ensamblaje")

    def animateBTN2(cvs, prnt, sq, img, counter, speed):
        cvs.itemconfig(img, image=sq[counter])
        prnt.after(speed, lambda: animateBTN2(cvs, prnt, sq, img, (counter+1) % len(sq), speed))

    c6 = tk.Canvas(newWindow, bd=0, highlightthickness=0)
    c6.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    sequence5 = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(AbsolutePath.resource_path('gifs/sample2.gif')))]
    c6IMG = c6.create_image(0,0,anchor="nw", image=sequence5[0])
    animateBTN2(c6, c6, sequence5, c6IMG, 0, 3000)

c1.bind("<Button-1>", dominioWindow)
c2.bind("<Button-1>", mallaWindow)
c3.bind("<Button-1>", tablaWindow)
c4.bind("<Button-1>", modeloWindow)
c5.bind("<Button-1>", pasosWindow)
c6.bind("<Button-1>", ensamblajeWindow)

root.resizable(0,0)
root.mainloop()