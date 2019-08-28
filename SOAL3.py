from flask import Flask, request, render_template, redirect
import json

app = Flask (__name__)

@app.route('/')
def lovemodul1 ():
    return render_template('hello.html')

@app.route('/pokemonmu', methods = ['POST'])
def lovemodul2 ():
    body = request.form
    p = str(body['pokemon'])
    kecil = p.lower()
    url= f'https://pokeapi.co/api/v2/pokemon/{kecil}'

    data=request.get(url)

    if data.status_code==200:
        hasil = data.json()
        return render_template ('pokehome.html', nama = str(hasil['name']).capitalize(), id=hasil['id'], gambar=hasil['sprites']['front_default'], tinggi=hasil['height'], berat=hasil['weight'])
    elif data.status_code=='''<Response[404]>''':
        return render_template('notfound.html')



if __name__ == '__main__':
    app.run(debug = True,host = 'localhost',port = 5000)