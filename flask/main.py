from flask import Flask
import random

app = Flask(__name__)
facts_list = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",
"De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
"As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.",
"O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."]

cara_coroa_list = ["Cara, E você perdeu!", "Coroa, Boa você ganhou!"]
@app.route("/random-facts")
def facts():
    return f'{random.choice(facts_list)}'

@app.route("/cara ou coroa")
def cara_ou_coroa():
    return f'{random.choice(cara_coroa_list)}'
@app.route("/")
def home():
    return """""
    <h1>Bem-vindo ao site de fatos aleatórios sobre redes sociais!</h1>
    <a href="/random-facts">Veja um fato aleatório!</a>
    <h1> </h1>
    <a href="/cara ou coroa">Teste a sua sorte no cara ou coroa!(se cair na cara, você ganha!)</a>
"""""
app.run(debug=True)