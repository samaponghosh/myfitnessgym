import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall
from count import count
from PushUpCounter import push_up
from curl_counter import curl
from squat import squat_count
from crunch import crunch
from pull import pull
from walk import walk
from PushIt import push
from jump import jump
from squattt import squat_count
from contra import contra


window = tk.Tk()
window.title("Smart Gym")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Indranil Smart Gym-Trainer")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('ico/fitness.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('ico/push.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('ico/bicep.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('ico/contra.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('ico/pullup.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('ico/crunch.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)



btn4_image = Image.open('ico/squat1.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('ico/walk.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn8_image = Image.open('ico/jump.png')
btn8_image = btn8_image.resize((50,50), Image.ANTIALIAS)
btn8_image = ImageTk.PhotoImage(btn8_image)


# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='PushUp', height=90, width=180, fg='green',command = push, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='BicepCurl', height=90, width=180, fg='orange', command=curl, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='PullUp', height=90, width=180, fg='green', command=pull, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Squat', height=90, width=180, fg='orange', command=squat_count, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)



btn6 = tk.Button(frame1, text='Crunch', height=90, width=180, fg='green', command=crunch, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=2)

btn5 = tk.Button(frame1, text='G-Cardio', height=90, width=180, fg='red', command=contra, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

btn7 = tk.Button(frame1, text="Walk", fg="orange",command=walk, compound='left', image=btn7_image, height=90, width=180)
btn7['font'] = btn_font
btn7.grid(row=3, column=2, pady=(20,10))

btn8 = tk.Button(frame1, text="Jump", fg="violet",command=jump, compound='left', image=btn8_image, height=90, width=180)
btn8['font'] = btn_font
btn8.grid(row=6, column=3, pady=(40,10))

frame1.pack()
window.mainloop()


