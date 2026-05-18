

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

    # ===== FASE DE GRUPOS =====
    grupos = {
        "Grupo A": [
            {"dupla": "Dupla A1  1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla A2  2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla A3", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo B": [
            {"dupla": "Dupla B1  1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla B2  2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla B3", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo C": [
            {"dupla": "Dupla C1  1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla C2  2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla C3", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo D": [
            {"dupla": "Dupla D1  1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla D2  2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Dupla D3", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ]
    }

    # ===== ELIMINATÓRIAS =====
    grupo_jogos_A = [
        "Dupla A1 0 x 0 Dupla A2",
        "Dupla A1 0 x 0 Dupla A3",
        "Dupla A2 0 x 0 Dupla A3"
    ]
    
    grupo_jogos_B = [
        "Dupla B1 0 x 0 Dupla B2",
        "Dupla B1 0 x 0 Dupla B3",
        "Dupla B2 0 x 0 Dupla B3"
    ]
    
    grupo_jogos_C = [
        "Dupla C1 0 x 0 Dupla C2",
        "Dupla C1 0 x 0 Dupla C3",
        "Dupla C2 0 x 0 Dupla C3"
    ]
    
    grupo_jogos_D = [
        "Dupla D1 0 x 0 Dupla D2",
        "Dupla D1 0 x 0 Dupla D3",
        "Dupla D2 0 x 0 Dupla D3"
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
