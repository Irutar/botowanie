import pyautogui, time, os, logging, sys, random, copy
import multiprocessing as mp
import mss
import mss.tools
import takeSS
import iconPosition



A_LIGHT = os.path.join('images', 'aLight.png')
A_DARK = os.path.join('images', 'aDark.png')
B_LIGHT = os.path.join('images', 'bLight.png')
B_DARK = os.path.join('images', 'bDark.png')
AF_ICON = os.path.join('images', 'AF3.png')
JS_ICON = os.path.join('images', 'JS.png')
BLANK_DARK = os.path.join('images', 'blankDark.png')
BLANK_LIGHT = os.path.join('images', 'blankLight.png')
FULL_LIGHT = os.path.join('images', 'fullLight.png')
FULL_DARK = os.path.join('images', 'fullDark.png')

DELAY_IN_MOVEMENT = 1 #time in seconds to move mouse from A to B
IMAGE_SAFE_BUFFOR = 10
NECESSARY_DELAY = (1/1000)
DELAY_FOR_LOAD = (250/1000)



GRAY_VALUE = True


GET_EXECUTION_TIME_INFO = 1
GET_TIME_FOR_1_ATTACK = 1


#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages



#TO DO: 
# -contol click in the same location
# -check white A and B
# -reduce ammount of code


#HIGH PRIORITY:



def main():
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    time.sleep(5)
    print('program start')
    sendAttack100Times()

    
'''    

def takeFullScreenShoot():
    mss.mss().shot(output='images/fullscreen.png')
     
    
def takeSSOfARegion():
    global aIconRegion
    r = aIconRegion[0]
    r1 = aIconRegion[1]
    r2 = aIconRegion[2]
    r3 = aIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/aRegion.png'
    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    
    
def takeSSOfARegion1():
    global aIconRegion
    r = aIconRegion[0]
    r1 = aIconRegion[1]
    r2 = aIconRegion[2]
    r3 = aIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/aRegion1.png'
    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)    
    
    
def takeSSOfBRegion():
    global bIconRegion
    r = bIconRegion[0]
    r1 = bIconRegion[1]
    r2 = bIconRegion[2]
    r3 = bIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/bRegion.png'
    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    
    
def takeSSOfBRegion1():
    global bIconRegion
    r = bIconRegion[0]
    r1 = bIconRegion[1]
    r2 = bIconRegion[2]
    r3 = bIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/bRegion1.png'
    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)    
    
    
def takeSSOfResourceRegion():
    global resourceIconRegion
    r = resourceIconRegion[0]
    r1 = resourceIconRegion[1]
    r2 = resourceIconRegion[2]
    r3 = resourceIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/resourceRegion.png'

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def takeSSOfResourceRegion1():
    global resourceIconRegion
    r = resourceIconRegion[0]
    r1 = resourceIconRegion[1]
    r2 = resourceIconRegion[2]
    r3 = resourceIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/resourceRegion1.png'

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)  
    
    
def takeSSOfResourceRegion2():
    global resourceIconRegion
    r = resourceIconRegion[0]
    r1 = resourceIconRegion[1]
    r2 = resourceIconRegion[2]
    r3 = resourceIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/resourceRegion2.png'

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def takeSSOfResourceRegion3():
    global resourceIconRegion
    r = resourceIconRegion[0]
    r1 = resourceIconRegion[1]
    r2 = resourceIconRegion[2]
    r3 = resourceIconRegion[3]
    monitor = {'top': r1, 'left': r, 'width': r2, 'height': r3}
    output = 'images/resourceRegion3.png'

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
'''    
'''    
def aFirstLightIconPosition():
    a1Icon = pyautogui.locate(A_LIGHT, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return a1Icon
        
        
def aFirstDarkIconPosition():
    aIcon = pyautogui.locate(A_DARK, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return aIcon


def bFirstLightIconPosition():
    b1IconPosition = pyautogui.locate(B_LIGHT, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return b1IconPosition


def bFirstDarkIconPosition():
    bIcon = pyautogui.locate(B_DARK, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return bIcon


def aLightIconPosition():
    takeSS.ARegion(aIconRegion)
    aIcon = pyautogui.locate(A_LIGHT, 'images/aRegion.png',
     grayscale = GRAY_VALUE)
    if aIcon != None:
        aIcon = list(aIcon)
        aIcon[0] = aIcon[0] + aIconRegion[0]
        aIcon[1] = aIcon[1] + aIconRegion[1]
        aIcon[2] = aIcon[2] + aIconRegion[2]
        aIcon[3] = aIcon[3] + aIconRegion[3]
        aIcon = tuple(aIcon)
    return aIcon
        
        
def aDarkIconPosition():
    takeSS.ARegion1(aIconRegion)
    aIcon = pyautogui.locate(A_DARK, 'images/aRegion1.png',
     grayscale = GRAY_VALUE)
    if aIcon != None:
        aIcon = list(aIcon)
        aIcon[0] = aIcon[0] + aIconRegion[0]
        aIcon[1] = aIcon[1] + aIconRegion[1]
        aIcon[2] = aIcon[2] + aIconRegion[2]
        aIcon[3] = aIcon[3] + aIconRegion[3]
        aIcon = tuple(aIcon)
    return aIcon


def bLightIconPosition():
    takeSS.BRegion(bIconRegion)
    bIcon = pyautogui.locate(B_LIGHT, 'images/bRegion.png',
     grayscale = GRAY_VALUE)
    if bIcon != None:
        bIcon = list(bIcon)
        bIcon[0] = bIcon[0] + bIconRegion[0]
        bIcon[1] = bIcon[1] + bIconRegion[1]
        bIcon[2] = bIcon[2] + bIconRegion[2]
        bIcon[3] = bIcon[3] + bIconRegion[3]
        bIcon = tuple(bIcon)
    return bIcon


def bDarkIconPosition():
    takeSS.BRegion1(bIconRegion)
    bIcon = pyautogui.locate(B_DARK, 'images/bRegion1.png',
     grayscale = GRAY_VALUE)
    if bIcon != None:
        bIcon = list(bIcon)
        bIcon[0] = bIcon[0] + bIconRegion[0]
        bIcon[1] = bIcon[1] + bIconRegion[1]
        bIcon[2] = bIcon[2] + bIconRegion[2]
        bIcon[3] = bIcon[3] + bIconRegion[3]
    bIcon = tuple(bIcon)
    return bIcon

    
def afIconPosition():
    takeSS.FullScreen()
    afIcon = pyautogui.locate(AF_ICON, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return afIcon
    
    
def JSIconPosition():
    JSIcon = pyautogui.locate(JS_ICON, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return JSIcon
    

def blankDarkResourcesIconPosition():
    takeSS.ResourceRegion(resourceIconRegion)
    resourceIcon = pyautogui.locate(BLANK_DARK, 'images/resourceRegion.png',
     grayscale = GRAY_VALUE)
    if resourceIcon != None:
        resourceIcon = list(resourceIcon)
        resourceIcon[0] = resourceIcon[0] + resourceIconRegion[0]
        resourceIcon[1] = resourceIcon[1] + resourceIconRegion[1]
        resourceIcon[2] = resourceIcon[2] + resourceIconRegion[2]
        resourceIcon[3] = resourceIcon[3] + resourceIconRegion[3]
        resourceIcon = tuple(resourceIcon)
    return resourceIcon


def blankLightResourcesIconPosition():
    takeSS.ResourceRegion1(resourceIconRegion)
    resourceIcon = pyautogui.locate(BLANK_LIGHT, 'images/resourceRegion1.png',
     grayscale = GRAY_VALUE)
    if resourceIcon != None:
        resourceIcon = list(resourceIcon)
        resourceIcon[0] = resourceIcon[0] + resourceIconRegion[0]
        resourceIcon[1] = resourceIcon[1] + resourceIconRegion[1]
        resourceIcon[2] = resourceIcon[2] + resourceIconRegion[2]
        resourceIcon[3] = resourceIcon[3] + resourceIconRegion[3]
        resourceIcon = tuple(resourceIcon)
    return resourceIcon
    
    
def fullDarkResourcesIconPosition():
    takeSS.ResourceRegion2(resourceIconRegion)
    resourceIcon = pyautogui.locate(FULL_DARK, 'images/resourceRegion2.png',
     grayscale = GRAY_VALUE)
    if resourceIcon != None:
        resourceIcon = list(resourceIcon)
        resourceIcon[0] = resourceIcon[0] + resourceIconRegion[0]
        resourceIcon[1] = resourceIcon[1] + resourceIconRegion[1]
        resourceIcon[2] = resourceIcon[2] + resourceIconRegion[2]
        resourceIcon[3] = resourceIcon[3] + resourceIconRegion[3]
        resourceIcon = tuple(resourceIcon)
    return resourceIcon    
    
    
def fullLightResourcesIconPosition():
    takeSS.ResourceRegion3(resourceIconRegion)
    resourceIcon = pyautogui.locate(FULL_LIGHT, 'images/resourceRegion3.png',
     grayscale = GRAY_VALUE)
    if resourceIcon != None:
        resourceIcon = list(resourceIcon)
        resourceIcon[0] = resourceIcon[0] + resourceIconRegion[0]
        resourceIcon[1] = resourceIcon[1] + resourceIconRegion[1]
        resourceIcon[2] = resourceIcon[2] + resourceIconRegion[2]
        resourceIcon[3] = resourceIcon[3] + resourceIconRegion[3]
        resourceIcon = tuple(resourceIcon)
    return resourceIcon


def blankFirstDarkResourcesIconPosition():
    blankDarkIcon = pyautogui.locate(BLANK_DARK, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return blankDarkIcon


def blankFirstLightResourcesIconPosition():
    blankLightIcon = pyautogui.locate(BLANK_LIGHT, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return blankLightIcon
    
    
def fullFirstDarkResourcesIconPosition():
    fullDarkIcon = pyautogui.locate(FULL_DARK, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return fullDarkIcon    
    
    
def fullFirstLightResourcesIconPosition():
    fullLightIcon = pyautogui.locate(FULL_LIGHT, 'images/fullscreen.png',
     grayscale = GRAY_VALUE)
    return fullLightIcon
'''    
    
def mouseMovementToBDark():
    bPosition = iconPosition.bDark(bIconRegion)
    changeInMovementX = random.randint(0,11)
    changeInMovementY = random.randint(0,11)
    pyautogui.moveTo(bPosition[0] + 15,
     bPosition[1] + 4 + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
     

def mouseMovementToBLight():
    bPosition = iconPosition.bLight(bIconRegion)
    changeInMovementX = random.randint(0,11)
    changeInMovementY = random.randint(0,11)
    pyautogui.moveTo(bPosition[0] + 15,
     bPosition[1] + 4 + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
     
     
def mouseMovementToADark():
    aPosition = iconPosition.aDark(aIconRegion)
    changeInMovementX = random.randint(0,11)
    changeInMovementY = random.randint(0,11)
    pyautogui.moveTo(aPosition[0] + 15,
     aPosition[1] + 4 + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
     
     
def mouseMovementToALight():
    aPosition = iconPosition.aLight(aIconRegion)
    changeInMovementX = random.randint(0,11)
    changeInMovementY = random.randint(0,11)
    pyautogui.moveTo(aPosition[0] + 15,
     aPosition[1] + 4 + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
    
    
def mouseMovementToAF():
    afPosition = iconPosition.af()
    changeInMovementX = random.randint(0,3)
    changeInMovementY = random.randint(0,3)
    pyautogui.moveTo(afPosition[0] + changeInMovementX,
     afPosition[1] + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
     
     
def mouseMovementToJS():
    JSPosition = iconPosition.JS()
    changeInMovementX = random.randint(0,3)
    changeInMovementY = random.randint(0,3)
    pyautogui.moveTo(JSPosition[0] + 5 + changeInMovementX,
     JSPosition[1] + 3 + changeInMovementY, DELAY_IN_MOVEMENT,
     pyautogui.easeInOutQuad)
     
    
def resetMousePosition():
    x, y = pyautogui.position()
    pyautogui.moveTo(1, 1, 3)
    
    
def mouseLeftClick():
    pyautogui.click(button='left')
    
    
def sendAttack100Times():
    
    previousPosition = 100
    mouseMovementToAF()
    mouseLeftClick()
    time.sleep(5)
    mouseMovementToJS()
    mouseLeftClick()
    getRegionOfAFImages()
    for i in range(0, 100):
        
        if GET_TIME_FOR_1_ATTACK == 1:
            start = time.time()
        
        x = randomDelayBetweenAttacks()
        time.sleep(x)
        '''Resources 0-fullLight, 1-fullDark, 2-blankLight,
         3-blankDark''' 
        resources = checkResources()
        #print('Resources: {}' .format(resources))
        #print('Previous position: {}' .format(previousPosition))
        if(resources == 0):
            if(previousPosition == 0):
                mouseLeftClick()
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
            else:
                mouseMovementToALight()
                mouseLeftClick()
                previousPosition = 0
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
        if(resources == 1):
            if(previousPosition == 0):
                mouseLeftClick()
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
            else:
                mouseMovementToADark()
                mouseLeftClick()
                previousPosition = 0
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
        if(resources == 2):
            if(previousPosition == 1):
                mouseLeftClick()
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
            else:
                mouseMovementToBLight()
                mouseLeftClick()
                previousPosition = 1
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
        if(resources == 3):
            if(previousPosition == 1):
                mouseLeftClick()
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
            else:
                mouseMovementToBDark()
                mouseLeftClick()
                previousPosition = 1
                if GET_TIME_FOR_1_ATTACK == 1:
                    end = time.time()
                    print('Time for 1 attack {}' .format(end-start))
 
 
def dispatcherForCheckResources(n):
    if n == 0:
        return iconPosition.blankLightResources(resourceIconRegion)
    if n == 1:
        return iconPosition.blankDarkResources(resourceIconRegion)
    if n == 2:
        return iconPosition.fullLightResources(resourceIconRegion)
    if n == 3:
        return iconPosition.fullDarkResources(resourceIconRegion)
                            
    
'''Resources 0-fullLight, 1-fullDark, 2-blankLight, 3-blankDark''' 
def checkResources():
    if GET_EXECUTION_TIME_INFO == 1:
        start = time.time()
    
    
    pool = mp.Pool(processes=4)
    v = pool.map(dispatcherForCheckResources, range(4))
    
    pool.close()
    pool.join()
    
    blankLight = v[0]
    blankDark = v[1]
    fullLight = v[2]
    fullDark = v[3]
    '''
    
    blankLight = blankLightResourcesIconPosition()
    blankDark = blankDarkResourcesIconPosition()
    fullLight = fullLightResourcesIconPosition()
    fullDark = fullDarkResourcesIconPosition()
    '''
    if((blankLight == None) and (blankDark == None)
     and (fullLight == None) and (fullDark == None)):
         end = time.time()
         if GET_EXECUTION_TIME_INFO == 1:
             end = time.time()
             print('None checking resources in: {} ' .format(end - start))
         return None

    #print(blankLight)
    #print(blankDark)
    #print(fullLight)
    #print(fullDark)
            
    if(blankLight == None):
        BL = 2000
    else:
        BL = blankLight[1]
    
    if(blankDark == None):
        BD = 2000
    else:
        BD = blankDark[1]
        
    if(fullLight == None):
        FL = 2000
    else:
        FL = fullLight[1]
        
    if(fullDark == None):
        FD = 2000
    else:
        FD = fullDark[1]
        
    minimum = min(BL, BD, FL, FD)
    #print(minimum)
            
            
    if(minimum == FL):
        if GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} ' .format(end - start))
        return 0
    elif(minimum == FD):
        if GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} ' .format(end - start))
        return 1
    elif(minimum == BL):
        if GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} ' .format(end - start))
        return 2
    elif(minimum == BD):
        if GET_EXECUTION_TIME_INFO == 1:
            end = time.time()
            print('checking resources in: {} ' .format(end - start))
        return 3
        
    
    

def getRegionOfAFImages():
    if GET_EXECUTION_TIME_INFO == 1:
        start = time.time()
    takeSS.FullScreen()
    getRegionOfAImage()
    getRegionOfBImage()
    getRegionOfResourceImage()
    if GET_EXECUTION_TIME_INFO == 1:
        end = time.time()
        print('getting all icon in: {} ' .format(end - start)) 
    

def dispatcherForAFirstRegion(n):
    if n == 0:
        return iconPosition.aFirstLight()
    if n == 1:
        return iconPosition.aFirstDark()
    
    
 
def getRegionOfAImage():
    global aIconRegion
    
    if GET_EXECUTION_TIME_INFO == 1:
        start = time.time()
    takeSS.FullScreen()
    pool = mp.Pool(processes=2)
    v = pool.map(dispatcherForAFirstRegion, range(2))
    #bLightTemp = bFirstLightIconPosition()
    #bDarkTemp = bFirstDarkIconPosition()
    pool.close()
    pool.join()
    aLightTemp = v[0]
    aDarkTemp = v[1]
    #aLightTemp = aFirstLightIconPosition()
    #aDarkTemp = aFirstDarkIconPosition()

    aMinimum = min(aLightTemp[1], aDarkTemp[1])
    
    if(aMinimum == aLightTemp[1]):
        aLightTemp = list(aLightTemp)
        aLightTemp[0] -= IMAGE_SAFE_BUFFOR
        aLightTemp[1] -= IMAGE_SAFE_BUFFOR
        aLightTemp[2] += IMAGE_SAFE_BUFFOR*2
        aLightTemp[3] += IMAGE_SAFE_BUFFOR*2
        aLightTemp = tuple(aLightTemp)
        aIconRegion = aLightTemp
    elif(aMinimum == aDarkTemp[1]):
        aDarkTemp = list(aDarkTemp)
        aDarkTemp[0] -= IMAGE_SAFE_BUFFOR
        aDarkTemp[1] -= IMAGE_SAFE_BUFFOR
        aDarkTemp[2] += IMAGE_SAFE_BUFFOR*2
        aDarkTemp[3] += IMAGE_SAFE_BUFFOR*2
        aDarkTemp = tuple(aDarkTemp)
        aIconRegion = aDarkTemp
    if GET_EXECUTION_TIME_INFO == 1:    
        end = time.time()
        print('getting B icon in: {} ' .format(end - start))     
    print('Region of A')
    print(aIconRegion)


def dispatcherForBFirstRegion(n):
    if n == 0:
        return iconPosition.bFirstLight()
    if n == 1:
        return iconPosition.bFirstDark()
    
       
   
def getRegionOfBImage():
    global bIconRegion
    
    if GET_EXECUTION_TIME_INFO == 1:
        start = time.time()
    takeSS.FullScreen()
    pool = mp.Pool(processes=2)
    v = pool.map(dispatcherForBFirstRegion, range(2))
    pool.close()
    pool.join()
    #bLightTemp = bFirstLightIconPosition()
    #bDarkTemp = bFirstDarkIconPosition()
    
    bLightTemp = v[0]
    bDarkTemp = v[1]

    bMinimum = min(bLightTemp[1], bDarkTemp[1])
        
    if(bMinimum == bLightTemp[1]):
        bLightTemp = list(bLightTemp)
        bLightTemp[0] -= IMAGE_SAFE_BUFFOR
        bLightTemp[1] -= IMAGE_SAFE_BUFFOR
        bLightTemp[2] += IMAGE_SAFE_BUFFOR*2
        bLightTemp[3] += IMAGE_SAFE_BUFFOR*2
        bLightTemp = tuple(bLightTemp)
        bIconRegion = bLightTemp
    elif(bMinimum == bDarkTemp[1]):
        bDarkTemp = list(bDarkTemp)
        bDarkTemp[0] -= IMAGE_SAFE_BUFFOR
        bDarkTemp[1] -= IMAGE_SAFE_BUFFOR
        bDarkTemp[2] += IMAGE_SAFE_BUFFOR*2
        bDarkTemp[3] += IMAGE_SAFE_BUFFOR*2
        bDarkTemp = tuple(bDarkTemp)
        bIconRegion = bDarkTemp    

    if GET_EXECUTION_TIME_INFO == 1:
        end = time.time()
        print('getting B icon in: {} ' .format(end - start))    
    print('Region of B')
    print(bIconRegion)        


def dispatcherForResourceFirstRegion(n):
    if n == 0:
        return iconPosition.blankFirstLightResources()
    if n == 1:
        return iconPosition.blankFirstDarkResources()
    if n == 2:
        return iconPosition.fullFirstLightResources()
    if n == 3:
        return iconPosition.fullFirstDarkResources()

        
def getRegionOfResourceImage():
    
    global resourceIconRegion
    
    if GET_EXECUTION_TIME_INFO == 1:
        start = time.time()
    takeSS.FullScreen()
    pool = mp.Pool(processes=4)
    v = pool.map(dispatcherForResourceFirstRegion, range(4))
    pool.close()
    pool.join()
    
    resourceBlankLightTemp = v[0]
    resourceBlankDarkTemp = v[1]
    resourceFullLightTemp = v[2]
    resourceFullDarkTemp = v[3]
    
    if(resourceBlankLightTemp == None):
        checkNumber1 = 2000
    else:
        checkNumber1 = resourceBlankLightTemp[1]

    if(resourceBlankDarkTemp == None):
        checkNumber2 = 2000
    else:
        checkNumber2 = resourceBlankDarkTemp[1]
        
    if(resourceFullLightTemp == None):
        checkNumber3 = 2000
    else:
        checkNumber3 = resourceFullLightTemp[1]
        
    if(resourceFullDarkTemp == None):
        checkNumber4 = 2000
    else:
        checkNumber4 = resourceFullDarkTemp[1]
    
    print(resourceFullLightTemp)
    print(resourceFullDarkTemp)
    

    resourceMinimum = min(checkNumber1, checkNumber2, checkNumber3,
     checkNumber4)
    
    if(resourceMinimum == checkNumber1):
        resourceBlankLightTemp = list(resourceBlankLightTemp)
        resourceBlankLightTemp[0] -= IMAGE_SAFE_BUFFOR
        resourceBlankLightTemp[1] -= IMAGE_SAFE_BUFFOR
        resourceBlankLightTemp[2] += IMAGE_SAFE_BUFFOR*2
        resourceBlankLightTemp[3] += IMAGE_SAFE_BUFFOR*2
        resourceBlankLightTemp = tuple(resourceBlankLightTemp)
        resourceIconRegion = resourceBlankLightTemp
    elif(resourceMinimum == checkNumber2):
        resourceBlankDarkTemp = list(resourceBlankDarkTemp)
        resourceBlankDarkTemp[0] -= IMAGE_SAFE_BUFFOR
        resourceBlankDarkTemp[1] -= IMAGE_SAFE_BUFFOR
        resourceBlankDarkTemp[2] += IMAGE_SAFE_BUFFOR*2
        resourceBlankDarkTemp[3] += IMAGE_SAFE_BUFFOR*2
        resourceBlankDarkTemp = tuple(resourceBlankDarkTemp)
        resourceIconRegion = resourceBlankDarkTemp
    elif(resourceMinimum == checkNumber3):
        resourceFullLightTemp = list(resourceFullLightTemp)
        resourceFullLightTemp[0] -= IMAGE_SAFE_BUFFOR
        resourceFullLightTemp[1] -= IMAGE_SAFE_BUFFOR
        resourceFullLightTemp[2] += IMAGE_SAFE_BUFFOR*2
        resourceFullLightTemp[3] += IMAGE_SAFE_BUFFOR*2
        resourceFullLightTemp = tuple(resourceFullLightTemp)
        resourceIconRegion = resourceFullLightTemp
    elif(resourceMinimum == checkNumber4):
        resourceFullDarkTemp = list(resourceFullDarkTemp)
        resourceFullDarkTemp[0] -= IMAGE_SAFE_BUFFOR
        resourceFullDarkTemp[1] -= IMAGE_SAFE_BUFFOR
        resourceFullDarkTemp[2] += IMAGE_SAFE_BUFFOR*2
        resourceFullDarkTemp[3] += IMAGE_SAFE_BUFFOR*2
        resourceFullDarkTemp = tuple(resourceFullDarkTemp)
        resourceIconRegion = resourceFullDarkTemp
        
    #print('Here')    
    #print(resourceIconRegion)
    if GET_EXECUTION_TIME_INFO == 1:    
        end5 = time.time()
        print('getting resource icon in: {} ' .format(end5 - start))
           
        
def randomDelayBetweenAttacks():
    x = random.randint(50, 70)
    return (x/1000)
    

if __name__ == '__main__':
    main()
