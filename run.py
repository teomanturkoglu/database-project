from app import create_app

# Flask uygulamasını oluştur
app = create_app()

if __name__ == '__main__':
    # Uygulamayı çalıştır
    app.run(debug=True)
