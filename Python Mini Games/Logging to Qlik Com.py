import time
import keyboard as kb
import pyautogui as pt

print("Logging started!")
time.sleep(1)

i=0
t=0
while True:
    """Log In Qlik comunity 10 days in a row to earn the 'Regular Badge' 
    """
    t=t+1
    print("T= ",t, time.ctime())
    if t<288: # 5 min groups in 24h
        x, y = pt.position()
        pt.moveTo(x + 50, y + 50)
        pt.moveTo(x, y)
        pt.click()
        time.sleep(5*60)
    else:    
        i=i+1
        print("i= " ,i, time.ctime())
        
        if i<11:
    
            pt.hotkey('win', 'm') # minimize current screen
            # time.sleep(1)

            pt.moveTo(pt.locateCenterOnScreen("new_Explorer.png", confidence=0.8))
            pt.doubleClick()
            # time.sleep(1)

            # pt.hotkey('ctrl', 't') # open new tap
            # time.sleep(2)

            pt.moveTo(pt.locateCenterOnScreen("searchWeb.png", confidence=0.8))
            # pt.click()
            time.sleep(1)
            pt.write("https://login.qlik.com/login?state=hKFo2SBfbzU2R245WFNMQjN2ckNUeFdrb2lQWkRMUDQ4V0JpY6FupWxvZ2luo3RpZNkgVEZ4VmQ3ZTF5NHdGSG40dC1oU05iRzVpcGNvX0p0Rk-jY2lk2SB6YlNaVG8yVzRRVnpsTGhlVW9rNTVxWXZtOTJ3cGVEcw&client=zbSZTo2W4QVzlLheUok55qYvm92wpeDs&protocol=samlp&SAMLRequest=pVLbTuMwEP0Va94b51IgtZqiQkFUCqKQlNXyZlJTGxI7tZ3S8vU4vUB4QSvt43jOzLmMh%2BebqkRrpo1QMoHA8wExWaiFkMsE5vl1L4bz0dDQqgxrMm4slw9s1TBjkRuUhuw7CTRaEkWNMETSihliC5KNb1MSej6ptbKqUCWgsTFMW0d1qaRpKqYzpteiYPOHNAFubW0IxoWqqkYKu%2FVWpXjzXImpI8YtFS7VUkhAE6dASGp3qo%2BDu973UIuv8cdz9pSr8E%2F%2F%2FvGjTDmbq7eTk9XfdTUI32s2MYCmkwRoxLngYhD7Sxqz%2Fmuf%2B2cs5Kc8Wr68xgsHMqZhU2kslTaB0A%2Bjnh%2F1oiAPAhL0SRB6p4P4CdDs4PVCyH2GvwXzvAcZcpPns97sLssBPR5v4QBwSJ7s2HU38t8X02POMPqXVIe4S%2FN17qxQtZPXetpsL1Wzcw5f7elklgpju%2FWVtHqLUlX891Ec51osmG6P0zr9uQbw6KC5IwP%2FlP390P22o08%3D&RelayState=ac006c785a64fig9d329i534e7a39")
            time.sleep(2)
            pt.hotkey("enter")
            time.sleep(1)

            pt.hotkey('win', 'up') # maximize current screen
            time.sleep(4)

            pt.moveTo(pt.locateCenterOnScreen("logInButton.png", confidence=0.9))
            pt.click()
            time.sleep(5)

            pt.hotkey("enter")
            time.sleep(2)
            t=0

    kb.is_pressed('q') # it will stop working by clicking q you can change to to any key
    try:
        if kb.is_pressed('q'): # it will stop working by clicking q you can change to to any key
            break
        else:
            pass
    finally:
        pass