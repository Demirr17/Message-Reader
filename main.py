
from flask import Flask, request, jsonify, send_from_directory
import pyttsx3
import threading#gerekli kütüphanelerin importu

app = Flask(__name__)

def seslendir(yazi):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)
    engine.say(yazi)
    engine.runAndWait()
    engine.stop()  #:ayarlar ve seslendirme

@app.route("/")
def home():
    return send_from_directory(".", "index.html") #web adresine kullanıcı gittiyse index.htmli açıyor

@app.route("/oku", methods=["POST"])
def oku():
    yazi = request.json.get("yazi", "")

    if not yazi.strip():
        return jsonify({"mesaj": "Metin boş!"}) #metinde bişey olmayınca yazan yazı

    threading.Thread(
        target=seslendir,
        args=(yazi,),
        daemon=True
    ).start()

    return jsonify({"mesaj": "Seslendiriliyor!"})#mesaj okunurken gelen yazı

if __name__ == "__main__":
    app.run(debug=False, port=5000)#siteyi başlatıyor
