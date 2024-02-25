from tkinter import *
import customtkinter
from customtkinter import *
customtkinter.set_appearance_mode('dark')
import threading
from PIL import Image, ImageTk

# create the root element

root = CTk()
root.geometry('900x700')
root.title('ASD Detector')
root.after(100, lambda: root.wm_iconbitmap("./my_brain.ico"))
root.resizable(0,0)

# custom variables and labels and such

# gif_frames = []
# frame_delay = 0
# frame_count = 0

# custom functions

# def ready_gif():
#     global frame_delay

#     gif_file = Image.open('./brain_file.gif')

#     for r in range(0, gif_file.n_frames):
#         gif_file.seek(r)
#         gif_frames.append(gif_file.copy())

#     frame_delay = gif_file.info['duration']

# def play_gif():
    
#     global frame_count, current_frame
    
#     if frame_count >= len(gif_frames) - 1:
#         frame_count = -1
#         # play_gif()
#     else:
#         frame_count+=1
#         print(frame_count)

#     current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
#     gif_lb.configure(image=current_frame)

#     root.after(frame_delay, play_gif)

def home_page():
    home_frame = CTkFrame(main_frame, fg_color=('black', 'black'))
    lb = CTkLabel(home_frame, text='Home\n\n\n\n\n This is the home page', font=('Bold', 22))
    lb.pack()
    home_frame.pack(pady=20)
    home_frame.pack_propagate(False)
    home_frame.configure(width=800, height=500)
    # play_gif()


def about_page():
    about_frame = CTkFrame(main_frame, fg_color=('black', 'black'))
    lb = CTkLabel(about_frame, text='About\n\n\n\n\n This is the about page', font=('Bold', 22))
    lb.pack()
    about_frame.pack(pady=20)
    about_frame.pack_propagate(False)
    about_frame.configure(width=800, height=500)

def help_page():
    help_frame = CTkFrame(main_frame, fg_color=('black', 'black'))
    lb = CTkLabel(help_frame, text='Help\n\n\n\n\n This is the help page', font=('Bold', 22))
    lb.pack()
    help_frame.pack(pady=20)
    help_frame.pack_propagate(False)
    help_frame.configure(width=800, height=500)


def no_indicate():
    home_button.configure(fg_color=('darkgrey', 'darkgrey'))
    home_indicator.configure(bg_color=('darkgrey', 'darkgrey'))
    about_button.configure(fg_color=('darkgrey', 'darkgrey'))
    about_indicator.configure(bg_color=('darkgrey', 'darkgrey'))
    help_button.configure(fg_color=('darkgrey', 'darkgrey'))
    help_indicator.configure(bg_color=('darkgrey', 'darkgrey'))

    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(curr, ind, page):
    no_indicate()
    curr.configure(fg_color=('#ADD8E6', '#ADD8E6'))
    ind.configure(bg_color=('black', 'black'))
    page()

#options frame - navbar

options_frame = Frame(root, bg='darkgrey')
options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=320, height=900)


# main frame - content page

main_frame = Frame(root, 
                bg='black',
                highlightbackground='black',
                highlightthickness=4)
main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(width=800, height=900)

# gif_lb = CTkLabel(main_frame)
# gif_lb.pack(fill=BOTH)

# pages
# -----

# home page
home_button = CTkButton(options_frame, text='Home',
                    font=('Bold', 24), fg_color=('darkgrey', 'darkgrey'),
                    hover_color='#ADD8E6', text_color='black',
                    command= lambda: indicate(home_button,home_indicator,home_page), width=232, height=40)
home_button.place(x=10, y=20)

home_indicator = CTkLabel(options_frame, text='', width=3, height=40, bg_color=('darkgrey', 'darkgrey'))
home_indicator.place(x=2,y=20)

# about page
about_button = CTkButton(options_frame, text='About',
                        font=('Bold', 24), fg_color=('darkgrey', 'darkgrey'),
                        hover_color='#ADD8E6', text_color='black',
                        command= lambda: indicate(about_button, about_indicator,about_page), width=232, height=40)
about_button.place(x=10, y=80)

about_indicator = CTkLabel(options_frame, text='', width=3, height=40, bg_color=('darkgrey', 'darkgrey'))
about_indicator.place(x=2,y=80)

# help page
help_button = CTkButton(options_frame, text='Help', 
                    font=('Bold', 24), fg_color=('darkgrey', 'darkgrey'),
                    hover_color='#ADD8E6', text_color='black',
                    command= lambda: indicate(help_button, help_indicator,help_page), width=232, height=40)
help_button.place(x=10, y=140)

help_indicator = CTkLabel(options_frame, text='', width=3, height=40, bg_color=('darkgrey', 'darkgrey'))
help_indicator.place(x=2,y=140)







# ready_gif()
# threading.Thread(target=ready_gif).start()
indicate(home_button, home_indicator,home_page)



root.mainloop()