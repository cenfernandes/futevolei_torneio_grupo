

## Estrutura do projeto
"""
futevolei/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
"""


## Backend em Python (Flask) - arquivo app.py (controla a lógica do site (backend))

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

duplas = [

    "Dupla 1",
    "Dupla 2",

    "Dupla 3",
    "Dupla 4",

    "Dupla 5",
    "Dupla 6",

    "Dupla 7",
    "Dupla 8",

    "Dupla 9",
    "Dupla 10",

    "Dupla 11",
    "Dupla 12",

    "Dupla 13",
    "Dupla 14",

    "Dupla 15",
    "Dupla 16"
]

jogos_iniciais = [

    (duplas[0], duplas[1]),

    (duplas[2], duplas[3]),

    (duplas[4], duplas[5]),

    (duplas[6], duplas[7]),

    (duplas[8], duplas[9]),

    (duplas[10], duplas[11]),

    (duplas[12], duplas[13]),

    (duplas[14], duplas[15])

]
    return render_template(
        "index.html",
        jogos=jogos_iniciais
    )


# para usar em ambiente de teste
"""
if __name__ == "__main__":
    app.run(debug=True)
"""

# para usar em producao
if __name__ == "__main__":
    app.run()
