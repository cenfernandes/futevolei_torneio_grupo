

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

##  1️⃣
##  2️⃣

    # ===== FASE DE GRUPOS =====
    grupos = {
        "Grupo A": [
            {"dupla": "Dani Moraes & Vinicius Japa Night (INGLATERRA)", "vitorias": 2, "derrotas": 0, "pro": 36, "contra": 22, "saldo": 14},
            {"dupla": "Rapha Barros & Tchuco (ALEMANHA)", "vitorias": 1, "derrotas": 1, "pro": 33, "contra": 25, "saldo": 8},
            {"dupla": "Isabela Neris & Yully (CROACIA)", "vitorias": 0, "derrotas": 2, "pro": 14, "contra": 36, "saldo": -22},
        ],
        
        "Grupo B": [
            {"dupla": "Breno Travasso & Bruno Freire (HOLANDA)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 15, "saldo": 3},
            {"dupla": "DN & Foca (MEXICO)", "vitorias": 1, "derrotas": 1, "pro": 33, "contra": 34, "saldo": -1},
            {"dupla": "Leo Carvalho & Luan Mendes (AFRICA DO SUL)", "vitorias": 0, "derrotas": 1, "pro": 16, "contra": 18, "saldo": -2},
        ],
        
        "Grupo C": [
            {"dupla": "Leo Robalo & Leo Salama (PORTUGAL)", "vitorias": 2, "derrotas": 0, "pro": 37, "contra": 23, "saldo": 14},
            {"dupla": "Jota & 2K (FRANÇA)", "vitorias": 0, "derrotas": 1, "pro": 17, "contra": 19, "saldo": -2},
            {"dupla": "Breno Menezes & Paquetá (ARGENTINA)", "vitorias": 0, "derrotas": 1, "pro": 6, "contra": 18, "saldo": -12},
        ],
        
        "Grupo D": [
            {"dupla": "Davizinho & Regis (BELGICA)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 13, "saldo": 5},
            {"dupla": "Gui Araujo & Lucas (COLOMBIA)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 13, "saldo": 5},
            {"dupla": "Bigode & Charlys (URUGUAI)", "vitorias": 0, "derrotas": 2, "pro": 26, "contra": 36, "saldo": -10},
        ]
    }

    # ===== ELIMINATÓRIAS =====
    grupo_jogos_A = [
        "Isabela Neris & Yully (CROACIA) 7 x 18 Rapha Barros & Tchuco (ALEMANHA)",
        "Isabela Neris & Yully (CROACIA) 7 x 18 Dani Moraes & Vinicius Japa Night (INGLATERRA)",
        "Rapha Barros & Tchuco (ALEMANHA) 15 x 18 Dani Moraes & Vinicius Japa Night (INGLATERRA)"
    ]
    
    grupo_jogos_B = [
        "Breno Travasso & Bruno Freire (HOLANDA) 18 x 15 DN & Foca (MEXICO)",
        "Breno Travasso & Bruno Freire (HOLANDA) 0 x 0 Leo Carvalho & Luan Mendes (AFRICA DO SUL)",
        "DN & Foca (MEXICO) 18 x 16 Leo Carvalho & Luan Mendes (AFRICA DO SUL)"
    ]
  
    grupo_jogos_C = [
        "Jota & 2K (FRANÇA) 17 x 19 Leo Robalo & Leo Salama (PORTUGAL)",
        "Jota & 2K (FRANÇA) 0 x 0 Breno Menezes & Paquetá (ARGENTINA)",
        "Leo Robalo & Leo Salama (PORTUGAL) 18 x 6 Breno Menezes & Paquetá (ARGENTINA)"
    ]
    
    grupo_jogos_D = [
        "Davizinho & Regis (BELGICA) 18 x 13 Bigode & Charlys (URUGUAI)",
        "Davizinho & Regis (BELGICA) 0 x 0 Gui Araujo & Lucas (COLOMBIA)",
        "Bigode & Charlys (URUGUAI) 13 x 18 Gui Araujo & Lucas (COLOMBIA)"
    ]
    
    quartas = [
        "Dupla A1 0 x 0 Dupla B2",
        "Dupla B1 0 x 0 Dupla A2",
        "Dupla C1 0 x 0 Dupla D2",
        "Dupla D1 0 x 0 Dupla C2"
    ]

    semifinais = [
        "Vencedor Quarta 1 0 x 0 Vencedor Quarta 3",
        "Vencedor Quarta 2 0 x 0 Vencedor Quarta 4"
    ]

    terceiro = [
        "Perdedor Semifinal 1 0 x 0 Perdedor Semifinal 2"
    ]

    final = [
        "Vencedor Semifinal 1 0 x 0 Vencedor Semifinal 2"
    ]

    return render_template(
        "index.html",
        grupos=grupos,
        grupo_jogos_A = grupo_jogos_A,
        grupo_jogos_B = grupo_jogos_B,
        grupo_jogos_C = grupo_jogos_C,
        grupo_jogos_D = grupo_jogos_D,
        quartas=quartas,
        semifinais=semifinais,
        terceiro=terceiro,
        final=final
    )


# para usar em ambiente de teste
"""
if __name__ == "__main__":
    app.run(debug=True)
"""

# para usar em producao
if __name__ == "__main__":
    app.run()
