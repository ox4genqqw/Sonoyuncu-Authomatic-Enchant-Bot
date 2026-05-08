import cv2
import keyboard
from tkinter import Tk, Button, Checkbutton, IntVar,BooleanVar
import pyautogui
import time
import numpy as np
import threading
import pyscreeze
import json
import os
import requests

import os
import requests
import json

# Global değişkenler
button_pressed = False
karakter_level_30 = False
karakter_level_5 = False
lapis = False
basılacak_item = (550, 315)
lapis_koordinat = (588, 317)
#level_30_sol_alt = (628, 343)
level_30_sol_alt = (638 ,333)
level_5_sol_alt = (628, 268)


basilacak_kitaplar = []
kirilmazlik_append_value = False
keskinlik_append_value = False
derin_kosucu_append_value = False
verimlilik_append_value = False




SIZIN_X_KOORDINATI1 = 531
SIZIN_Y_KOORDINATI1 = 296
SIZIN_X_KOORDINATI2 = 570
SIZIN_Y_KOORDINATI2 = 336

SIZIN1_X_KOORDINATI1 = 572
SIZIN1_Y_KOORDINATI1 = 298
SIZIN1_X_KOORDINATI2 = 610
SIZIN1_Y_KOORDINATI2 = 335

# Checkbox1 durum değişikliğinde yapılacaklar


def shift_sol_click():
    pyautogui.keyDown('shift')
    pyautogui.leftClick()
    pyautogui.keyUp('shift')


def level_30_check():
    global karakter_level_30
    try:
        image_path = "resimler/level_30_sag_ust.png"
        location = pyautogui.locateOnScreen(image_path)

        if location is not None:
          #  print(f"Karakter durumu 30 Level: {karakter_level_30}")
            karakter_level_30 = True

    except pyautogui.ImageNotFoundException:
        #print(f"Karakter durumu 30 Level : {karakter_level_30}")
        karakter_level_30 = False


def level_30_check_loop():
    while True:
        level_30_check()


def level_5_check():
    global karakter_level_5
    try:
        image_path = "resimler/level_5_sag_ust.png"
        location = pyautogui.locateOnScreen(image_path)
       # print(location)
        if location is not None:
           # print(f"Karakter durumu 5 Level :{karakter_level_5}")
            karakter_level_5 = True

    except pyautogui.ImageNotFoundException:
      #  print(f"Karakter durumu 5 Level : {karakter_level_5}")
        karakter_level_5 = False


def level_5_check_loop():
    while True:
        level_5_check()


def Kazma():
    try:
        KazmaYol = 'resimler/kazma.png'

        # Load the template image in color
        template = cv2.imread(KazmaYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KazmaYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.99
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Kazma bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
        else:
            print("Kazma bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def Kilic():
    try:
        KazmaYol = 'resimler/kilic.png'

        # Load the template image in color
        template = cv2.imread(KazmaYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KazmaYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.99
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Kılıç bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
        else:
            print("Kılıç bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def Savas_Balta():
    try:
        KazmaYol = 'resimler/savasbalta.png'

        # Load the template image in color
        template = cv2.imread(KazmaYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KazmaYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.99
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Savaş baltası bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
        else:
            print("Savaş baltası bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def Yay():
    try:
        KazmaYol = 'resimler/yay.png'

        # Load the template image in color
        template = cv2.imread(KazmaYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KazmaYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.99
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Yay bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
        else:
            print("Kılıç bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Template resimleri tarayan fonksiyon

def Lapis():
    try:
        image_path = "resimler/lapis1.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.99)

        if location is not None:
            print(f"Kitap ekranda bulundu!")

            # Belirli iki koordinat arasında mı kontrol et
            if is_within_coordinate_range(location, (SIZIN1_X_KOORDINATI1, SIZIN1_Y_KOORDINATI1), (SIZIN1_X_KOORDINATI2, SIZIN1_Y_KOORDINATI2)):
                print("Kitap belirli koordinat aralığında bulundu. Başka bir seçeneği seçiyoruz.")
                # Bir fonksiyonu çağır veya alternatif seçenek için işlemleri gerçekleştir
                # alternatif_secenek_fonksiyonu()
            else:
                # Kitap belirtilen aralıkta bulunuyorsa, ancak belirtilen aralıkta değilse varsayılan işlemi gerçekleştir
                pyautogui.moveTo(location)
                shift_sol_click()

        else:
            print("Kitap bulunamadı.")
    except pyautogui.ImageNotFoundException:
        print(f"Kitap ekranda bulunamadı")


def koruma_ara1():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/p4.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.92)
        if location is not None and karakter_level_30 == True:
            print(f"Koruma Bulundu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Koruma Bulundu! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break
            

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()

def koruma_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/p4.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.92)
        if location is not None and karakter_level_30 == True:
            print(f"Koruma Bulundu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Koruma Bulundu! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()
      #  Kitap()
        pyautogui.moveTo(level_5_sol_alt)
        level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break


    

def kask_ara():
    try:
        KaskYol = 'resimler/kask.png'

        # Load the template image in color
        template = cv2.imread(KaskYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KaskYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Kask bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()
          #  koruma_ara()
            
        else:
            print("Kask bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")  

def cp_ara():
    try:
        CpYol = 'resimler/cp.png'

        template = cv2.imread(CpYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{CpYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Cp bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Cp bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")  

def pant_ara():
    try:
        PantYol = 'resimler/pant.png'

        # Load the template image in color
        template = cv2.imread(PantYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{PantYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Pant bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Pant bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}") 

def bot_ara():
    try:
        BotYol = 'resimler/bot.png'

        # Load the template image in color
        template = cv2.imread(BotYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{BotYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Bot bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Bot bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}") 

def tkask_ara():
    try:
        KaskYol = 'resimler/tkask.png'

        # Load the template image in color
        template = cv2.imread(KaskYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{KaskYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Kask bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()
          #  koruma_ara()
            
        else:
            print("Kask bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")  

def tcp_ara():
    try:
        CpYol = 'resimler/tcp.png'

        # Load the template image in color
        template = cv2.imread(CpYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{CpYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Cp bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Cp bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")  

def tpant_ara():
    try:
        PantYol = 'resimler/tpant.png'

        # Load the template image in color
        template = cv2.imread(PantYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{PantYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Pant bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Pant bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}") 

def tbot_ara():
    try:
        BotYol = 'resimler/tbot.png'

        # Load the template image in color
        template = cv2.imread(BotYol)

        if template is None:
            raise FileNotFoundError(f"Template image '{BotYol}' not found.")

        # Get the dimensions of the template
        h, w, _ = template.shape

        # Read the screen image
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        # Match the template
        result = cv2.matchTemplate(
            screen_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider it a match
        threshold = 0.999
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Bot bulundu!")

            # Get the coordinates of the top-left corner of the template
            top_left = (loc[1][0], loc[0][0])

            # Move the mouse to the coordinates
            pyautogui.moveTo(top_left[0] + w // 2, top_left[1] + h // 2)
            shift_sol_click()
            koruma_ara1()

          #  koruma_ara()
            
        else:
            print("Bot bulunamadı!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except cv2.error as e:
        print(f"OpenCV Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}") 


def servet_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/servet.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Servetbulundu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Servetbulundu! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()
        Kitap()
        pyautogui.moveTo(level_5_sol_alt)
       # level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def basılacak_itemler():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = basilacak_kitaplar
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Servetbulundu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Servetbulundu! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()
        Kitap()
        pyautogui.moveTo(level_5_sol_alt)
       # level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def keskinlik_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/keskinlik4.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Keskinlik! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Keskinlik! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()

def keskinlik_ara1():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/keskinlik4.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Keskinlik! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Keskinlik! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Servet bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()
        Kitap()
        pyautogui.moveTo(level_5_sol_alt)
       # level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def yumruk_iki_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/yumruk2.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Yumruk II! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Keskinlik! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Yumruk II bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()


def yumruk_iki_ara1():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/yumruk2.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.95)
        if location is not None and karakter_level_30 == True:
            print(f"Yumruk II! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)

            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Keskinlik! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Yumruk II bulunamadı')
        pyautogui.moveTo(basılacak_item)
        shift_sol_click()
        Kitap()
        pyautogui.moveTo(level_5_sol_alt)
       # level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def derin_kousucu_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/derinkos.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.9)
        if location is not None and karakter_level_30 == True:
            print(f"Derin Koşucu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Derin Koşucu! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Derin koşucu bulunamadı')
       # Kitap()
        pyautogui.moveTo(level_5_sol_alt)
        level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def verimlilik_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/verimlilik.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.9)
        if location is not None and karakter_level_30 == True:
            print(f"Verimlilik Koşucu! Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Verimlilik ! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Verimlilik bulunamadı')
       # Kitap()
        pyautogui.moveTo(level_5_sol_alt)
        level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break
                

def kirilmazlik_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path = 'resimler/kirilmazlik.png'
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.9)
        if location is not None and karakter_level_30 == True:
            print(f"Kırılmazlık Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Kırılmazlık ! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Kırılmazlık bulunamadı')
       # Kitap()
        pyautogui.moveTo(level_5_sol_alt)
        level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def kirilmazlik_derin_ara():
    try:
        pyautogui.moveTo(level_30_sol_alt)
        image_path1 = 'resimler/kirilmazlik.png' 
        image_path2 = 'resimler/derinkos.png'
        location = pyautogui.locateOnScreen(image_path1, confidence=0.9)
        location2 = pyautogui.locateOnScreen(image_path2, confidence=0.9)
        if (location is not None or location2 is not None) and karakter_level_30:
            print(f"Kırılmazlık,Derin Konum: {location}")
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            shift_sol_click()
        elif karakter_level_30 == False:
            print("Karakter 30 level değil bekleniyor...")
            while True:
                if karakter_level_30 == True:
                    print(f"Kırılmazlık ! Konum: {location}")
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    shift_sol_click()
                    break

    except pyautogui.ImageNotFoundException:
        print(f'Hata: Kırılmazlık,Derin bulunamadı')
       # Kitap()
        pyautogui.moveTo(level_5_sol_alt)
        level_5_check()
        if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
        elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def f8_pc_kapat():
    keyboard.wait('f8')
   # root.destroy()


def Kitap():
    try:
        image_path = "resimler/kitap.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.99)

        if location is not None:
            print(f"Kitap ekranda bulundu!")

            # Belirli iki koordinat arasında mı kontrol et
            if is_within_coordinate_range(location, (SIZIN_X_KOORDINATI1, SIZIN_Y_KOORDINATI1), (SIZIN_X_KOORDINATI2, SIZIN_Y_KOORDINATI2)):
                print("Kitap belirli koordinat aralığında bulundu. Başka bir seçeneği seçiyoruz.")
                # Bir fonksiyonu çağır veya alternatif seçenek için işlemleri gerçekleştir
                # alternatif_secenek_fonksiyonu()
            else:
                # Kitap belirtilen aralıkta bulunuyorsa, ancak belirtilen aralıkta değilse varsayılan işlemi gerçekleştir
                pyautogui.moveTo(location)
                shift_sol_click()

        else:
            print("Kitap bulunamadı.")
    except pyautogui.ImageNotFoundException:
        print(f"Kitap ekranda bulunamadı")

# Belirli iki koordinat aralığında olup olmadığını kontrol etmek için yardımcı bir fonksiyon
def is_within_coordinate_range(location, koordinat1, koordinat2):
    x_within_range = koordinat1[0] <= location[0] <= koordinat2[0] or koordinat2[0] <= location[0] <= koordinat1[0]
    y_within_range = koordinat1[1] <= location[1] <= koordinat2[1] or koordinat2[1] <= location[1] <= koordinat1[1]
    return x_within_range and y_within_range

def Mouse_Koordinatlar():
    while True:
        x, y = pyautogui.position()

        # Koordinatları ekrana yazdır
        print(f"Fare Koordinatları: X = {x}, Y = {y}")
        time.sleep(1)


def Elmas_Kazma():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kazma()
        servet_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def Elmas_Kılıç():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kilic()
        keskinlik_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def Elmas_Set():
    keyboard.wait('enter')
    Lapis()
    while True:
      kask_ara()
      cp_ara()
      pant_ara()
      bot_ara()
      pyautogui.moveTo(lapis_koordinat)
      pyautogui.doubleClick()
      time.sleep(0.5)
      pyautogui.leftClick()
      Kitap()
      pyautogui.moveTo(level_5_sol_alt)
      if karakter_level_5 == True:
          pyautogui.leftClick()
          pyautogui.moveTo(basılacak_item)
          pyautogui.keyDown('q')
          pyautogui.keyUp('q')

def Tit_Set():
    keyboard.wait('enter')
    Lapis()
    while True:
      tkask_ara()
      tcp_ara()
      tpant_ara()
      tbot_ara()
      pyautogui.moveTo(lapis_koordinat)
      pyautogui.doubleClick()
      time.sleep(0.5)
      pyautogui.leftClick()
      Kitap()
      pyautogui.moveTo(level_5_sol_alt)
      if karakter_level_5 == True:
          pyautogui.leftClick()
          pyautogui.moveTo(basılacak_item)
          pyautogui.keyDown('q')
          pyautogui.keyUp('q')
      


def Verimlilik_Dort_Kitap():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kitap()
        verimlilik_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def Kirilmazlik_Kitap():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kitap()
        kirilmazlik_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def derin_kosucu():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kitap()
        derin_kousucu_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def kirilmazlik_derin():
    keyboard.wait('enter')
    Lapis()
    while True:
        Kitap()
        kirilmazlik_derin_ara()
        pyautogui.moveTo(lapis_koordinat)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.leftClick()

def elmas_duel_kit():
    keyboard.wait('enter')
    Lapis()
    while True:
      Kilic()
      keskinlik_ara()
      Yay()
      yumruk_iki_ara()
      kask_ara()
      cp_ara()
      pant_ara()
      bot_ara()
      pyautogui.moveTo(lapis_koordinat)
      pyautogui.doubleClick()
      time.sleep(0.5)
      pyautogui.leftClick()
      Kitap()
      pyautogui.moveTo(level_5_sol_alt)
      if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
      elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def titanyum_duel_kit():
    keyboard.wait('enter')
    Lapis()
    while True:
      Savas_Balta()
      keskinlik_ara()
      Yay()
      yumruk_iki_ara()
      tkask_ara()
      tcp_ara()
      tpant_ara()
      tbot_ara()
      pyautogui.moveTo(lapis_koordinat)
      pyautogui.doubleClick()
      time.sleep(0.5)
      pyautogui.leftClick()
      Kitap()
      pyautogui.moveTo(level_5_sol_alt)
      if karakter_level_5 == True:
            pyautogui.moveTo(level_5_sol_alt)
            pyautogui.leftClick()
            pyautogui.moveTo(basılacak_item)
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
      elif karakter_level_5 == False:
            print(f"Karakter level 5 = {karakter_level_5}")
            print("Karakter 5 level değil bekleniyor...")
            level_5_check()
            while True:
                if karakter_level_5 == True:
                    pyautogui.leftClick()
                    pyautogui.moveTo(basılacak_item)
                    pyautogui.keyDown("q")
                    pyautogui.keyUp("q")
                    break

def baslat_main():
    print(f"Başlatıldı")

def kirilmazlik_append():
    global kirilmazlik_append_value
    if kirilmazlik_append_value == True:
        kirilmazlik_append_value = False
        basilacak_kitaplar.remove("resimler/kirilmazlik.png")
        print(f"{basilacak_kitaplar}")
    else:
        kirilmazlik_append_value = True
        basilacak_kitaplar.append("resimler/kirilmazlik.png")
        print(f"{basilacak_kitaplar}")

def keskinlik_append():
    global keskinlik_append_value
    if keskinlik_append_value == True:
        keskinlik_append_value = False
        basilacak_kitaplar.remove("resimler/keskinlik4.png")
        print(f"{basilacak_kitaplar}")
    else:
        keskinlik_append_value = True
        basilacak_kitaplar.append("resimler/keskinlik4.png")
        print(f"{basilacak_kitaplar}")
     

        
def Main():
    global kirilmazlik, keskinlik, verimlilik
    root = Tk()
    root.title("Minecraft 1.8.9 - Sonoyuncu Client")

    button1 = Button(root, text="Elmas kazma", command=Elmas_Kazma, width=15, height=2)
    button1.pack()

    button7 = Button(root, text="Elmas kılıç", command=Elmas_Kılıç, width=15, height=2)
    button7.pack()

    button9 = Button(root, text="Savaş baltası", command=Savas_Balta, width=15, height=2)
    button9.pack()

    button3 = Button(root, text="Verimlilik 4", command=Verimlilik_Dort_Kitap, width=15, height=2)
    button3.pack()

    derinKosKitap = Button(root, text="Derin koşucu", command=derin_kosucu, width=15, height=2)
    derinKosKitap.pack()

    button4 = Button(root, text="Kırılmazlık", command=Kirilmazlik_Kitap, width=15, height=2)
    button4.pack()

    button5 = Button(root, text="Elmas set", command=Elmas_Set, width=15, height=2)
    button5.pack()

    button6 = Button(root, text="Tit set", command=Tit_Set, width=15, height=2)
    button6.pack()

    button8 = Button(root, text="Duel kiti", command=elmas_duel_kit, width=15, height=2)
    button8.pack()

    button8 = Button(root, text="Titanyum Duel Kiti", command=titanyum_duel_kit, width=15, height=2)
    button8.pack()

    button2 = Button(root, text="Mouse Koordinat", command=Mouse_Koordinatlar, width=15, height=2)
    button2.pack()

    checkbox1 = Checkbutton(root,text="Kırılmazlık",command=kirilmazlik_append)
    checkbox1.pack()

    checkbox2 = Checkbutton(root,text="Keskinlik 4",command=keskinlik_append)
    checkbox2.pack()

    checkbox3 = Checkbutton(root,text="Verimlilik",command=verimlilik_ara)
    checkbox3.pack()

    checkbox4 = Checkbutton(root,text="Derin koşucu",command=derin_kousucu_ara)
    checkbox4.pack()

    baslat = Button(root, text="Başlat", command=basılacak_itemler, width=15, height=2)
    baslat.pack()
    

  #  checkbox1 = Checkbutton(root,text="Kırılmazlık",command=checkbox_tiklandi)
  #  checkbox1.pack()

    # Threading işlemlerini başlat
    level_30_thread = threading.Thread(target=level_30_check_loop)
    level_30_thread.daemon = True
    level_30_thread.start()

    level_5_thread = threading.Thread(target=level_5_check_loop)
    level_5_thread.daemon = True
    level_5_thread.start()

    f8_pc_kapat_thread = threading.Thread(target=f8_pc_kapat)
    f8_pc_kapat_thread.daemon = True
    f8_pc_kapat_thread.start()

    # Pencereyi çalıştır
    root.mainloop()

Main()