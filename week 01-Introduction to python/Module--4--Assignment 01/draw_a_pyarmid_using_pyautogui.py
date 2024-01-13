import pyautogui
def pyramid(height):
    for i in range(1,height+1):
        stars='*'*i
        line=stars
        print(line)
        pyautogui.typewrite(line)
        pyautogui.press('enter')
height=int(input())
pyramid(height)