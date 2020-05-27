import keyboard
import pyautogui

#左上角座標
def Upper_left_corner():
    pyautogui.alert('請移至欲截圖之左上角按下z鍵!')
    while True:
        if keyboard.is_pressed('z'):
            global pos1
            pos1=pyautogui.position()
            print(pos1)
            break

#右下角座標
def Lower_right_corner():
    pyautogui.alert('請移至欲截圖之右下角按下x鍵!')
    while True:
        if keyboard.is_pressed('x'):
            global pos2
            pos2=pyautogui.position()
            print(pos2)
            break


if __name__ == "__main__":
    Upper_left_corner()
    Lower_right_corner()
    x=pos1.x
    y=pos1.y
    w=pos2.x-pos1.x
    h=pos2.y-pos1.y
    img=pyautogui.screenshot(region=(x,y,w,h))
    img.save(r'.\img.png')
    pyautogui.alert('截圖已成功!')
