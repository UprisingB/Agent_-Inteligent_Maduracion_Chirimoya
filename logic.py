import tensorflow as tf
import numpy as np
import cv2
from tkinter import messagebox

# Ruta al modelo guardado
saved_model_path = 'C:/Users/Asus/Documents/Inteligencia Artificial/Trabajo Final/estado-madurez-cnn-ad.keras'

# Cargar el modelo
model = tf.keras.models.load_model(saved_model_path)

def predict_image(img_path):
    if img_path:
        img = cv2.imread(img_path)
        if img is None:
            messagebox.showerror("Error", "No se pudo leer la imagen. Verifica la ruta del archivo.")
            return None

        resize = tf.image.resize(img, (180, 180))
        resize = resize.numpy().astype('float32') / 255.0
        resize = np.expand_dims(resize, axis=0)  # Expandir dimensiones para que el modelo lo acepte
        prediction = model.predict(resize)
        return 'La chirimoya esta madura' if prediction > 0.5 else 'La chirimoya esta inmadura'
    else:
        messagebox.showerror("Error", "No se ha cargado ninguna imagen.")
        return None
