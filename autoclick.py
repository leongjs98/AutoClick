from tkinter import messagebox, Tk, Label, Button, Frame, Entry, OptionMenu, StringVar
from PIL import Image, ImageTk
import pyautogui
import time
import keyboard


BTN_HEIGHT = 1
BTN_WIDTH = 18
BG_GREY = '#2f3136'
FONT_STYLE = ('Helvetica', 13)


pos1 = [0,0]
pos2 = [0,0]
pos3 = [0,0]


def main():
    root = Tk()
    root.title('AutoClick')
    root.configure(bg=BG_GREY)
    root.resizable(width=False, height=False)

    # Logo
    img = Image.open('./icon/logo.png')
    img = ImageTk.PhotoImage(img)
    logo = Label(root, image=img)
    logo.config(bg=BG_GREY)
    logo.grid(row=0, column=0, columnspan=2)

    # Instruction 
    inst_btn = Button(root, text='Show instruction', command=show_inst, width=15, height=1)
    inst_btn.config(font=FONT_STYLE, bg='grey', fg='white')
    inst_btn.grid(row=1, column=0, columnspan=2, pady=20)

    # Mouse Position 1
    def detect_pos1():
        pos1_txt.set('"Ctrl" to Detect')
        keyboard.wait('ctrl')
        pos1[0] = pyautogui.position()[0]
        pos1[1] = pyautogui.position()[1]

        if pos1[0] and pos1[1]:
            pos1_txt.set(f'Detected: {pos1[0]}, {pos1[1]}')

    pos1_label = Label(root, text="Mouseclick Position 1:")
    pos1_label.config(font=FONT_STYLE, bg=BG_GREY, fg='white')
    pos1_label.grid(row=2, column=0)
    pos1_txt = StringVar()
    pos1_txt.set('Click to Detect')
    detect_btn1 = Button(root, command=detect_pos1, textvariable=pos1_txt, height=BTN_HEIGHT, width=BTN_WIDTH)
    detect_btn1.config(font=FONT_STYLE, bg='grey', fg='white')
    detect_btn1.grid(row=2, column=1, pady=15, padx=20)

    # Mouse Position 2
    def detect_pos2():
        pos2_txt.set('"Ctrl" to Detect')
        keyboard.wait('ctrl')
        pos2[0] = pyautogui.position()[0]
        pos2[1] = pyautogui.position()[1]

        if pos2[0] and pos2[1]:
            pos2_txt.set(f'Detected: {pos2[0]}, {pos2[1]}')

    pos2_label = Label(root, text="Mouseclick Position 2:")
    pos2_label.config(font=FONT_STYLE, bg=BG_GREY, fg='white')
    pos2_label.grid(row=3, column=0)
    pos2_txt = StringVar()
    pos2_txt.set('Click to Detect')
    detect_btn2 = Button(root, command=detect_pos2, textvariable=pos2_txt, height=BTN_HEIGHT, width=BTN_WIDTH)
    detect_btn2.config(font=FONT_STYLE, bg='grey', fg='white')
    detect_btn2.grid(row=3, column=1, pady=15, padx=20)

    # # Mouse Position 3
    # def detect_pos3():
    #     pos3_txt.set('"Ctrl" to Detect')
    #     keyboard.wait('ctrl')
    #     pos3[0] = pyautogui.position()[0]
    #     pos3[1] = pyautogui.position()[1]

    #     if pos3[0] and pos3[1]:
    #         pos3_txt.set(f'Detected: {pos3[0]}, {pos3[1]}')

    # pos3_label = Label(root, text="Mouseclick Position 3:")
    # pos3_label.config(font=FONT_STYLE, bg=BG_GREY, fg='white')
    # pos3_label.grid(row=4, column=0)
    # pos3_txt = StringVar()
    # pos3_txt.set('Click to Detect')
    # detect_btn3 = Button(root, command=detect_pos3, textvariable=pos3_txt, height=BTN_HEIGHT, width=BTN_WIDTH)
    # detect_btn3.config(font=FONT_STYLE, bg='grey', fg='white')
    # detect_btn3.grid(row=4, column=1, pady=15, padx=20)

    # Intervals between clicks
    interval_label = Label(root, text="Select interval between clicks:")
    interval_label.config(font=FONT_STYLE, bg=BG_GREY, fg='white')
    interval_label.grid(row=5, column=0, padx=20, pady=20)
    interval_txt = StringVar()
    interval_txt.set('1')
    interval_dropdown = OptionMenu(root, interval_txt, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    interval_dropdown.config(font=FONT_STYLE, bg='grey', fg='white')
    interval_dropdown.grid(row=5, column=1, padx=20, pady=20)

    # Start button
    def start():
        # print("Starting")
        time.sleep(1)
        # print("Started")

        while True:
            if keyboard.is_pressed('esc'):
                break
            pyautogui.click(pos1[0], pos1[1])
            time.sleep(int(interval_txt.get()))
            pyautogui.click(pos2[0], pos2[1])
            time.sleep(int(interval_txt.get()))

        messagebox.showinfo('Autoclick ended.')

    start_btn = Button(root, command=start, text='Start', width=15)
    start_btn.config(font=FONT_STYLE, bg='grey', fg='white')
    start_btn.grid(row=6, column=0, columnspan=2, pady=20)
    start_label = Label(root, text='Hold "Esc" to stop the program.')
    start_label.config(font=FONT_STYLE, bg=BG_GREY, fg='white')
    start_label.grid(row=7, column=0, columnspan=2, pady=10)
    
    root.mainloop()


def show_inst():
    messagebox.showinfo('AutoClick', 'Click on each of the button, point your mouse at the position, press "Ctrl" to save the position.')
    

main()