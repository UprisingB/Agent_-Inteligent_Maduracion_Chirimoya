from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import cv2
import logic

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

def center_window(window, width, height):
    # Obtener el tamano de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular la posicion x e y para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

def show_custom_message(title, message):
    # Crear una nueva ventana
    custom_msg = tk.Toplevel()
    custom_msg.title(title)
    custom_msg.configure(bg='white')

    # Configurar el tamano de la ventana
    width, height = 300, 150
    center_window(custom_msg, width, height)

    # Crear un marco para organizar los widgets
    frame = tk.Frame(custom_msg, padx=10, pady=10, bg='white')
    frame.pack(expand=True, fill='both')

    # Etiqueta del mensaje
    message_label = tk.Label(frame, text=message, font=('Helvetica', 12), bg='white')
    message_label.pack(pady=10)

    # Boton de cerrar con estilo
    close_button = tk.Button(frame, text="Cerrar", width=20, pady=7, bg='#57a1f8', fg='white', border=0, command=custom_msg.destroy)
    close_button.pack(pady=10)

    custom_msg.grab_set()

def signin():
    global img_label
    username = user.get()
    password = code.get()
    
    if username == 'admin' and password == '1234':
        root.destroy()  # Cerrar la ventana de inicio de sesion
        screen = Tk()
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        img_label = Label(screen, bg="white")
        img_label.pack(pady=20)

        # Boton para subir o cargar una imagen
        upload_button = Button(screen, width=20, pady=7, text="Upload Image", bg='#57a1f8', fg='white', border=0, command=upload_image)
        upload_button.pack(pady=20)

        # Boton para tomar una foto con la camara
        capture_button = Button(screen, width=20, pady=7, text="Capture Image", bg='#57a1f8', fg='white', border=0, command=capture_image)
        capture_button.pack(pady=20)

        # Boton para verificar si una chirimoya es madura
        check_button = Button(screen, width=20, pady=7, text="Check Maturity", bg='#57a1f8', fg='white', border=0, command=check_maturity)
        check_button.pack(pady=20)

        screen.mainloop()

def upload_image():
    global img_label, img_path
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

def capture_image():
    global img_label, img_path
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        show_custom_message("Error", "No se pudo abrir la camara.")
        return

    ret, frame = cap.read()
    cap.release()
    
    if ret:
        img_path = "captured_image.png"
        cv2.imwrite(img_path, frame)
        
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img
    else:
        show_custom_message("Error", "No se pudo capturar la imagen.")

def check_maturity():
    result = logic.predict_image(img_path)
    if result:
        show_custom_message("Resultado de Prediccion", result)

img = PhotoImage(file='C:/Users/Asus/Documents/Inteligencia Artificial/menu.png')
Label(root, image=img, bg='white').place(x=50, y=80)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')
        
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')
        
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
