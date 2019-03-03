import cv2
import numpy as np
import pyautogui
import random
import time

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Updated 11/2/2018
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''


r"""

 $$$$$$\                                 $$\                     $$\       $$\                 
$$  __$$\                                $$ |                    $$ |      $$ |                
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$ |      $$$$$$$\  $$\   $$\ 
$$ |      $$  __$$\ $$  __$$\  \____$$\\_$$  _|  $$  __$$\ $$  __$$ |      $$  __$$\ $$ |  $$ |
$$ |      $$ |  \__|$$$$$$$$ | $$$$$$$ | $$ |    $$$$$$$$ |$$ /  $$ |      $$ |  $$ |$$ |  $$ |
$$ |  $$\ $$ |      $$   ____|$$  __$$ | $$ |$$\ $$   ____|$$ |  $$ |      $$ |  $$ |$$ |  $$ |
\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ | \$$$$  |\$$$$$$$\ \$$$$$$$ |      $$$$$$$  |\$$$$$$$ |
 \______/ \__|       \_______| \_______|  \____/  \_______| \_______|      \_______/  \____$$ |
                                                                                     $$\   $$ |
                                                                                     \$$$$$$  |
                                                                                      \______/ 



          _____                    _____                    _____                   _______                 
         /\    \                  /\    \                  /\    \                 /::\    \                
        /::\____\                /::\    \                /::\    \               /::::\    \               
       /::::|   |                \:::\    \              /::::\    \             /::::::\    \              
      /:::::|   |                 \:::\    \            /::::::\    \           /::::::::\    \             
     /::::::|   |                  \:::\    \          /:::/\:::\    \         /:::/~~\:::\    \            
    /:::/|::|   |                   \:::\    \        /:::/  \:::\    \       /:::/    \:::\    \           
   /:::/ |::|   |                   /::::\    \      /:::/    \:::\    \     /:::/    / \:::\    \          
  /:::/  |::|   | _____    ____    /::::::\    \    /:::/    / \:::\    \   /:::/____/   \:::\____\         
 /:::/   |::|   |/\    \  /\   \  /:::/\:::\    \  /:::/    /   \:::\    \ |:::|    |     |:::|    |        
/:: /    |::|   /::\____\/::\   \/:::/  \:::\____\/:::/____/     \:::\____\|:::|____|     |:::|    |        
\::/    /|::|  /:::/    /\:::\  /:::/    \::/    /\:::\    \      \::/    / \:::\    \   /:::/    /         
 \/____/ |::| /:::/    /  \:::\/:::/    / \/____/  \:::\    \      \/____/   \:::\    \ /:::/    /          
         |::|/:::/    /    \::::::/    /            \:::\    \                \:::\    /:::/    /           
         |::::::/    /      \::::/____/              \:::\    \                \:::\__/:::/    /            
         |:::::/    /        \:::\    \               \:::\    \                \::::::::/    /             
         |::::/    /          \:::\    \               \:::\    \                \::::::/    /              
         /:::/    /            \:::\    \               \:::\    \                \::::/    /               
        /:::/    /              \:::\____\               \:::\____\                \::/____/                
        \::/    /                \::/    /                \::/    /                 ~~                      
         \/____/                  \/____/                  \/____/                                          
                                                                                                            
"""




'''

grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)

input : a tuple containing the 4 coordinates of the region to capture

output : a PIL image of the area selected.

'''
def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1
    # x1 = region[0]
    # y1 = region[1]
    # width = region[2]
    # height = region[3]
    return pyautogui.screenshot(region=(x1,y1,width,height))


'''

Searches for an image within an area

input :

image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not

'''


def imagesearcharea(image,x1,y1,width,height,precision=0.8,name=None,im=None) :
    if im is None :
        # im = region_grabber(region=(x1, y1, x2, y2))
        im = pyautogui.screenshot(region=(x1,y1,width, height))
        if name is not None:
            im.save(name)

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


'''
Searches for an image on the screen

input :

image : path to the image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, useful if you intend to search the same unchanging region for several elements

returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not

'''


def imagesearch(image, precision=0.8, screenshot=None):
    if screenshot is None:
        im = pyautogui.screenshot()
    else:
        im = screenshot
    #im.save(str(random.randint(1, 150)) + ".png")  #usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc



'''
Searchs for an image on screen continuously until it's found.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

imagesearch_loop is only kept for backwards compatibility. looping_until_one_of_the_images_is_visible is the preferred way 

returns :
the top left corner coordinates of the element if found as an array [x,y] 

'''


def imagesearch_loop(image,timesample=1.5,precision=0.8,num_of_loops=5):
    pos = imagesearch(image, precision)
    counter = 0
    while pos[0] == -1:
        # print(image+" not found, waiting")  # Useful for debugging
        time.sleep(timesample)
        pos = imagesearch(image, precision)
        counter = counter + 1
        if counter == num_of_loops:
            print("Didn't find " + image + "\nBreaking while loop")
            break

    return pos

'''
Searches for an image on a region of the screen continuously until it's found.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns :
the top left corner coordinates of the element as an array [x,y] 

'''
def imagesearch_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1,y1,x2,y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    return pos


def r(num, rand):
    return num + rand*random.random()



'''
Clicking on image 

durationL must be lower than durationH

'''


def clicking_image(image, durationL=0.45, durationH=0.75, offset = 0, precision=0.8, to_print=True, amount_of_clicks=1, time_between_clicks=1, screenshot=None):
    pos = imagesearch(image, precision, screenshot=screenshot)
    if pos[0] != -1:
        offsetX = random.uniform(- offset, offset)
        offsetY = random.uniform(- offset, offset)

        pyautogui.moveTo(pos[0] + offsetX , pos[1] + offsetY, duration=random.uniform(durationL, durationH))
        time.sleep(random.uniform(0, 0.15))
        for _ in range(amount_of_clicks):
            print("Clicking on {}".format(image))
            pyautogui.click(pos[0] + offsetX, pos[1] + offsetY)
            time.sleep(time_between_clicks)

    elif to_print is True:
        print("{} not found!".format(image))


"""

"""


def pressing_key(key, time_to_sleep=0.25, amount=1, randomise=True):
    for _ in range(amount):
        print(f"Clicking '{key}'!")
        pyautogui.keyDown(key)
        if randomise is True:
            time.sleep(random.uniform(time_to_sleep - 0.05, time_to_sleep + 0.1))
        else:
            time.sleep(time)

        pyautogui.keyUp(key)
        time.sleep(0.05)

"""
Pos = x, y parameters on where to click.
"""


def moving_clicking_on_positions_x_y(pos, durationL=0.45, durationH=0.75, number_of_clicks=1):
    pyautogui.moveTo(pos[0], pos[1], duration=random.uniform(durationL, durationH))
    time.sleep(random.uniform(0.05, 0.15))
    for _ in range(number_of_clicks):
        pyautogui.click(pos[0], pos[1])
        print(f"Clicking on {pos[0]},{pos[1]}")
        time.sleep(random.uniform(0.05, 0.15))

"""
Is similar to imagesearch_loop, this is superior though, as it can search for more images at once.
imagesearch_loop is only kept for backwards compatibility

Can be optimized by adding an if codition in the for loop of dicts, am too lazy to implement
"""


def looping_until_one_of_the_images_is_visible(list_of_images, timesample=1.5,precision=0.8,num_of_loops=5):

    def loop_to_find_a_different_value(dictionary_of_positions):  # Is used in the while loop
        for pos in dictionary_of_positions:
            if pos[0] != -1:
                return pos
        return (-1, -1)  # Every image in dict is (-1, -1)

    dictionary_of_positions = {}
    screenshot = pyautogui.screenshot()
    for image in list_of_images:
        dictionary_of_positions[image] = imagesearch(image, precision, screenshot=screenshot)

    counter = 0
    condition = loop_to_find_a_different_value(dictionary_of_positions)
    while condition[0] == -1:
        time.sleep(timesample)

        screenshot = pyautogui.screenshot()
        for image in list_of_images:
            dictionary_of_positions[image] = imagesearch(image, precision, screenshot=screenshot)

        condition = loop_to_find_a_different_value(dictionary_of_positions)

        counter += 1
        if counter == num_of_loops:
            print("Didn't find " + list_of_images + "\nBreaking while loop")
            break

    return condition
