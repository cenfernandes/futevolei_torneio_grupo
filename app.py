

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
            {"dupla": "Dani Moraes & Vinicius Japa Night (INGLATERRA)  1️⃣", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 7, "saldo": 11},
            {"dupla": "Rapha Barros & Tchuco (ALEMANHA) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Isabela Neris & Yully (CROACIA)", "vitorias": 0, "derrotas": 1, "pro": 7, "contra": 18, "saldo": -11},
        ],
        
        "Grupo B": [
            {"dupla": "Breno Travasso & Bruno Freire (HOLANDA) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "DN & Foca (MEXICO) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Leo Carvalho & Luan Mendes (AFRICA DO SUL)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo C": [
            {"dupla": "Jota & 2K (FRANÇA) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Leo Robalo & Leo Salama (PORTUGAL) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Breno Menezes & Paquetá (ARGENTINA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo D": [
            {"dupla": "Davizinho & Regis (BELGICA) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Bigode & Charlys (URUGUAI) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Gui Araujo & Lucas (COLOMBIA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ]
    }

    # ===== ELIMINATÓRIAS =====
    grupo_jogos_A = [
        "Isabela Neris & Yully (CROACIA) 0 x 0 Rapha Barros & Tchuco (ALEMANHA)",
        "Isabela Neris & Yully (CROACIA) 7 x 18 Dani Moraes & Vinicius Japa Night (INGLATERRA)",
        "Rapha Barros & Tchuco (ALEMANHA) 0 x 0 Dani Moraes & Vinicius Japa Night (INGLATERRA)"
    ]
    
    grupo_jogos_B = [
        "Breno Travasso & Bruno Freire (HOLANDA) 0 x 0 DN & Foca (MEXICO)",
        "Breno Travasso & Bruno Freire (HOLANDA) 0 x 0 Leo Carvalho & Luan Mendes (AFRICA DO SUL)",
        "DN & Foca (MEXICO) 0 x 0 Leo Carvalho & Luan Mendes (AFRICA DO SUL)"
    ]
    
    grupo_jogos_C = [
        "Jota & 2K (FRANÇA) 0 x 0 Leo Robalo & Leo Salama (PORTUGAL)",
        "Jota & 2K (FRANÇA) 0 x 0 Breno Menezes & Paquetá (ARGENTINA)",
        "Leo Robalo & Leo Salama (PORTUGAL) 0 x 0 Breno Menezes & Paquetá (ARGENTINA)"
    ]
    
    grupo_jogos_D = [
        "Davizinho & Regis (BELGICA) 0 x 0 Bigode & Charlys (URUGUAI)",
        "Davizinho & Regis (BELGICA) 0 x 0 Gui Araujo & Lucas (COLOMBIA)",
        "Bigode & Charlys (URUGUAI) 0 x 0 Gui Araujo & Lucas (COLOMBIA)"
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
