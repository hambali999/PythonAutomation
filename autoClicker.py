import pyautogui, time

time.sleep(5)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

# pyautogui.moveTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(1000, 500, duration=1, tween=pyautogui.easeInOutQuad)
# pyautogui.moveTo(1000, 1000, duration=1, tween=pyautogui.easeInOutQuad)
# pyautogui.moveTo(500, 1000, duration=1, tween=pyautogui.easeInOutQuad)

#FUNCTION TO OPEN GOOGLE CHROME, YOUTUBE, SEARCH CAT MEMES
# pyautogui.moveTo(660, 875, duration=0.5, tween=pyautogui.easeInOutQuad)
# pyautogui.rightClick()
# pyautogui.moveTo(723, 677, duration=0.5, tween=pyautogui.easeInOutQuad)
# pyautogui.leftClick()
# pyautogui.moveTo(734, 84, duration=0.5, tween=pyautogui.easeInOutQuad)
# pyautogui.leftClick()
# pyautogui.write('youtube.com')
# pyautogui.keyDown('enter')
# pyautogui.moveTo(817, 138, duration=0.5, tween=pyautogui.easeInOutQuad)
# pyautogui.doubleClick()
# pyautogui.write('cat memes')
# pyautogui.keyDown('enter')
# pyautogui.moveTo(484, 341, duration=0.5, tween=pyautogui.easeInOutQuad)
# pyautogui.doubleClick()


#FUNCTION FOR AUTOMATED VIEWING OF INSTAGRAM STORIES... (WHEN UR TOO LAZY TO CLICK AND SCROLL THROUGH THEM)
pyautogui.moveTo(660, 875, duration=0.5, tween=pyautogui.easeInOutQuad)
pyautogui.rightClick()
pyautogui.moveTo(723, 677, duration=0.5, tween=pyautogui.easeInOutQuad)
pyautogui.leftClick()
pyautogui.moveTo(734, 84, duration=0.5, tween=pyautogui.easeInOutQuad)
pyautogui.leftClick()
pyautogui.write('instagram.com')
pyautogui.keyDown('enter')
time.sleep(6)
pyautogui.moveTo(287, 235, duration=0.5, tween=pyautogui.easeInOutQuad)
pyautogui.leftClick()
pyautogui.moveTo(942, 478, duration=0.5, tween=pyautogui.easeInOutQuad)
for i in range(300):
    pyautogui.leftClick()



#FUNCTION SPAMMER
# for i in range(500):
#     pyautogui.write('eh want wr?')
#     pyautogui.keyDown('enter')
# for i in range(500):
#     pyautogui.leftClick()

# pyautogui.click(clicks=10000000)come 1v1 me


#FUNCTION TESTING POINTER MOVEMENTS
# pyautogui.moveTo(100, 100, 0.7, pyautogui.easeInQuad)     # start slow, end fast
# pyautogui.moveTo(100, 100, 0.5, pyautogui.easeOutQuad)    # start fast, end slow
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end

