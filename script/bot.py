import time
import pyautogui as py


def testeChat():
    chat = py.locateOnScreen('mensagem_chat.png', confidence= 0.50)            
    if chat != None:
        time.sleep(2)
        controle = 0
        return True
    return False

centro_x = 945
centro_y = 535
while True: 
    for i in range(1,4):
        mato = py.locateOnScreen('mato' + str(i) +'.png', confidence= 0.80)
        num = i
        if mato != None: 
            controle = 0 
            x_mato, y_mato = py.center(mato)
            if controle != 1:
                if (py.locateOnScreen('mato'+str(num) +'_baixo.png', confidence= 0.94)) != None  :
                    controle = 1
                    py.moveTo(x_mato, y_mato, duration= 0.15)
                    py.moveRel(0,75, duration= 0.15)
                    py.leftClick()
                    py.moveTo(centro_x, centro_y)
                    py.moveRel(0,-75)

                    while testeChat() == False :
                        py.middleClick(interval= 1.5)
                        testeChat()

            if controle != 1:
                if (py.locateOnScreen('mato'+str(num) +'_cima.png', confidence= 0.94)) != None   :
                    controle = 1
                    py.moveTo(x_mato, y_mato, duration= 0.15)
                    py.moveRel(0,-75, duration= 0.15)
                    py.leftClick()
                    py.moveTo(centro_x, centro_y)
                    py.moveRel(0,75)

                    while testeChat() == False :
                        time.sleep(0.5)
                        py.middleClick()
                        testeChat() 

            if controle != 1:
                if (py.locateOnScreen('mato'+str(num) +'_dir.png', confidence= 0.94)) != None  :
                    controle = 1                
                    py.moveTo(x_mato, y_mato, duration= 0.15)
                    py.moveRel(75,0, duration= 0.15)
                    py.leftClick()
                    py.moveTo(centro_x, centro_y)
                    py.moveRel(-75,0)


                    while testeChat() == False :
                        py.middleClick()
                        testeChat()

            if controle != 1:
                if (py.locateOnScreen('mato'+str(num) +'_esq.png', confidence= 0.94)) != None  :
                    controle = 1                
                    py.moveTo(x_mato, y_mato, duration= 0.15)
                    py.moveRel(-75,0, duration= 0.15)
                    py.leftClick()
                    py.moveTo(centro_x, centro_y)
                    py.moveRel(75,0)

                    while testeChat() == False :
                        py.middleClick()
                        testeChat() 




        

        
