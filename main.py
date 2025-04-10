from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

users = {}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sonuc', methods=['POST'])
def sonuc():
    araba = float(request.form['araba'])
    elektrik = float(request.form['elektrik'])
    ucak = float(request.form['ucak'])
    et = float(request.form['et'])

    toplam = araba * 0.21 * 52 + elektrik * 0.475 * 12 + ucak * 0.115 + et * 2.5 * 52

    return render_template('result.html', emisyon=round(toplam, 2))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı var mı kontrol et
        if username in users:
            return redirect(url_for('register'))  # Aynı kullanıcı adı varsa tekrar kayıt sayfasına yönlendir
        
        # Yeni kullanıcı kaydet
        users[username] = password
        return redirect(url_for('login'))  # Kayıt başarılıysa giriş sayfasına yönlendir
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı adı ve şifreyi kontrol et
        if username in users and users[username] == password:
            return redirect(url_for('index'))  # Giriş başarılıysa ana sayfaya yönlendir
        else:
            return redirect(url_for('login'))  # Geçersiz giriş varsa tekrar giriş sayfasına yönlendir
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Oturumu sonlandır
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
