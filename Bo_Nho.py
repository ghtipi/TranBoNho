import tkinter as tk
import random
import pygame

pygame.mixer.init()
def play_music():
    #Phát nhạc nền
    pygame.mixer.music.load("TRANBONHO.mp3")
    pygame.mixer.music.play()

def start_program_after_music():
    show_message("Nỗi nhớ em cầu kỳ!", 0, 1300, show_message_2)

def create_window(message, display_duration, callback):
    window = tk.Toplevel()
    window.title(" ")  
    window.iconbitmap('D:\\Documents\\SourceCode\\Documents_Python\\surrounding_code\\Tran bo nho/tim.ico')
    window.configure(bg='pink')
    window_width = 500
    window_height = 50
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    label = tk.Label(window, text=message, bg='pink', fg='black', font=('Arial', 16, 'bold'))
    label.pack(expand=True, padx=10, pady=10)
    window.after(display_duration, window.destroy)

    if callback:
        root.after(display_duration, callback)

def show_message(message, delay, display_duration, next_function):

    root.after(delay, create_window, message, display_duration, next_function)

def show_message_2():
    show_message("Nên chẳng biết lý do gì!", 0, 1700, show_message_3)

def show_message_3():
    show_message("Hao tốn Hơn nhiều G", 0, 1800, show_message_4)

def show_message_4():
    show_message("Nên cần dùng thêm USB!", 0, 1900, show_message_5)

def show_message_5():
    show_message("Nỗi nhớ em cầu kỳ!", 0, 1800, show_message_6)

def show_message_6():
    show_message("Nên chẳng biết lý do gì!", 0, 2000, show_message_7)

def show_message_7():
    show_message("Hao tốn Hơn nhiều G", 0, 1500, show_message_8)

def show_message_8():
    show_message("Nên Cần", 0, 700, show_message_9)

def show_message_9():
    show_message("D", 0, 500, show_message_10)

def show_message_10():
    show_message("O", 0, 500, show_message_11)

def show_message_11():
    show_message("M", 0, 300, show_message_12)

def show_message_12():
    show_message("I", 0, 300, show_message_13)

def show_message_13():
    show_message("C", 0, 1000, open_windows_2)

def create_window_2(message):
    window = tk.Toplevel()
    window.title(" ")  
    window.iconbitmap('D:\\Documents\\SourceCode\\Documents_Python\\surrounding_code\\Tran bo nho/tim.ico')
    window.configure(bg='pink')

    window_width = 200
    window_height = 50
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


    label = tk.Label(window, text=message, bg='pink', fg='black', font=('Arial', 10, 'bold'))
    label.pack(expand=True, padx=10, pady=10)

def open_windows_2():
    for i in range(500):
        root.after(i * 60, create_window_2, "Nhớ Em!")


root = tk.Tk()
root.withdraw() 

play_music()
root.after(14000, start_program_after_music)

root.mainloop()
