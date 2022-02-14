# Autoencoder ile örnek çalışma

Merhaba, bu projede Türkçe ismiyle "otokodlayıcı" kullandık ve kanserli hücre fotoğraflarının boyutunu düşürdük.

Otokodlayıcı, denetimsiz bir şekilde öğrenmek için kullanılan bir tür yapay sinir ağıdır. Temelde iki bölmeden oluşur: kodlayıcı ve deşifreci. Kodlayıcı bölme giderek boyutu azalan çok katmanlı perseptronlardan oluşur. Deşifreci bölme ise giderek artan çok katmanlı perseptronlardan oluşur. Kodlayıcıya verinin girdi boyutu ile deşifrecinin sonucundan oluşan çıktının nöron sayısı (boyutu) aynıdır.

Verisetine ulaşmak için buraya [tıklayın](https://mucahitdemirhan.com/veriseti.zip).

# Sonuç

![öncesi ve sonrası](https://imgyukle.com/f/2022/02/14/EotUUv.png)




# Kaynaklar
- https://en.wikipedia.org/wiki/Autoencoder
- https://cihanongun.medium.com/autoencoder-otokodlay%C4%B1c%C4%B1-nedir-ne-i%C3%A7in-kullan%C4%B1l%C4%B1r-e520a591746a
- https://towardsdatascience.com/auto-encoder-what-is-it-and-what-is-it-used-for-part-1-3e5c6f017726
- https://www.tensorflow.org/tutorials/generative/autoencoder
- https://blog.keras.io/building-autoencoders-in-keras.html
- https://blog.paperspace.com/autoencoder-image-compression-keras/
