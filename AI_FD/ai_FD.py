import cv2
import numpy as np
from tensorflow.keras.models import load_model
import deepface

# Memuat model-model yang telah dilatih
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gender_model = load_model('gender_model.h5')
emotion_model = load_model('emotion_model.h5')
age_model = load_model('age_model.h5')

# Fungsi untuk mendeteksi wajah dan memprediksi jenis kelamin, emosi, dan usia
def predict_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        # Memotong wajah dari gambar
        face = image[y:y+h, x:x+w]
        # Mengubah ukuran wajah untuk model-model deteksi jenis kelamin, emosi, dan usia
        face = cv2.resize(face, (48, 48))
        face = np.expand_dims(face, axis=0)
        face = face / 255.0  # Normalisasi nilai piksel
        
        # Memprediksi jenis kelamin
        gender_prediction = gender_model.predict(face)
        gender = "Pria" if gender_prediction[0][0] < 0.5 else "Wanita"
        
        # Memprediksi emosi
        emotion_prediction = emotion_model.predict(face)
        emotion = deepface.DeepFace.find_pretty_emotion(emotion_prediction[0])
        
        # Memprediksi usia
        age_prediction = age_model.predict(face)
        age = np.argmax(age_prediction)
        
        # Menggambar persegi di sekitar wajah dan label-label
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, f'Jenis Kelamin: {gender}', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.putText(image, f'Emosi: {emotion}', (x, y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.putText(image, f'Usia: {age}', (x, y-80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        
    return image

# Fungsi utama
def main():
    # Membuka webcam
    cap = cv2.VideoCapture(0)
    
    while(True):
        ret, frame = cap.read()
        
        # Menampilkan pengenalan wajah
        cv2.imshow('Pengenalan Wajah', predict_face(frame))
        
        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # Melepaskan webcam dan menutup jendela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
