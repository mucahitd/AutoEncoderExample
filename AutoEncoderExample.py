from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os



#Model oluştur
#------------- 
input_img = keras.Input(shape=(100*100*3,)) # giriş katmanı belirttik 100x100x3'lük resimler tek tensor halinde veriyoruz
encoded = layers.Dense(128, activation='relu')(input_img) # 128'lik yogunluk katmanı
encoded = layers.Dense(32, activation='relu')(encoded) # 32'lik kod katmanımız, 100x100x3'lük resimi 32x1'lik boyuta sıkıştırdık

decoded = layers.Dense(128, activation='relu')(encoded) # çözücü yogunluk 128
decoded = layers.Dense(100*100*3, activation='sigmoid')(decoded) # cozucu cıktısı



autoencoder = keras.Model(input_img, decoded) # kodlayıcı ve cozucusu egğitim modelini birleştirdik

print(autoencoder.summary()) # özetine baktık

encoder = keras.Model(input_img, encoded) # kodlayıcı modeli birleştirdik

encoded_input = keras.Input(shape=(32)) #kod çözücünün giriş katmanını olusturduk

decoder_layers = autoencoder.layers[-2:] # gerekli katmanları egitim modelinden aldık
decoder_layers[0] = decoder_layers[0](encoded_input)
decoder_layers[1] = decoder_layers[1](decoder_layers[0]) #tekrar cağırma (call) işlemi yaptık
decoder = keras.Model(encoded_input,decoder_layers[1]) #  çözücü modeli oluşturduk

print(decoder.summary())

autoencoder.compile(optimizer="adam",loss="binary_crossentropy") #modeli adam ile optimze edici ve loss olarakta binary cross'u verdik

#veri setini indirmek için https://mucahitdemirhan.com/veriseti.zip , aynı dizinde olmasına dikkat ediniz.

#veri setilerini okuduk
x = []
for resim in os.listdir("veriseti"):
    img = cv2.imread("veriseti/"+resim)
    img = cv2.resize(img,(100,100))
    x.append(img)

x = np.array(x)
X = x.copy()


x = (x/255).astype(np.float32) # veri setini normalledik
x = x.reshape(-1,100*100*3)
y = x.copy()

autoencoder.fit(x,y,epochs=300,batch_size=5,shuffle=True) # eğitimi gerçekleştirdik

encoded_imgs = encoder.predict(x) #32'lik sıkıştırmaları yaptık
decoded_imgs = decoder.predict(encoded_imgs) #çözücü ile 32lik şifreden çözme işlemini yaptık


# verileri ekranda görsellşetirdik
f, axarr = plt.subplots(2,10)
print(axarr.shape)


for i in range(10):
    img = decoded_imgs[i]*255
    img = img.reshape(100,100,3)
    img = img.astype(np.uint8)

    axarr[0,i].imshow(X[i])
    axarr[0,i].axis("off")
    axarr[0,i].set_title("Önce")
    axarr[1,i].imshow(img)
    axarr[1,i].axis("off")
    axarr[1,i].set_title("Sonra")

plt.show()





