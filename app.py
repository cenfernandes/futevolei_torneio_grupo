

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
            {"dupla": "Guilherme Yath & Heitor Simões (MEXICO) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Rafael & Vinicius Japa Night (CROACIA) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "João Caovila & Lucca (PORTUGAL)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo B": [
            {"dupla": "Arthur Medeiros & Victor (HOLANDA)  1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "LC & Luiz Fernando (COLOMBIA) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Caio & Hernane (ALEMANHA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo C": [
            {"dupla": "Breno Menezes & Junior (ARGENTINA) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Jhonathan & Rafael Gouveia (BÉLGICA) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "MK & Matheus (INGLATERRA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ],
        
        "Grupo D": [
            {"dupla": "Carlinhos & Silvio (ESPANHA) 1️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Cadu & João (JAPAO) 2️⃣", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Diogo & José (URUGUAI)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ]
    }

    # ===== ELIMINATÓRIAS =====
    grupo_jogos_A = [
        "Guilherme Yath & Heitor Simões (MEXICO) 0 x 0 Rafael & Vinicius Japa Night (CROACIA)",
        "Guilherme Yath & Heitor Simões (MEXICO) 0 x 0 João Caovila & Lucca (PORTUGAL)",
        "Rafael & Vinicius Japa Night (CROACIA) 0 x 0 João Caovila & Lucca (PORTUGAL)"
    ]
    
    grupo_jogos_B = [
        "Arthur Medeiros & Victor (HOLANDA) 0 x 0 LC & Luiz Fernando (COLOMBIA)",
        "Arthur Medeiros & Victor (HOLANDA) 0 x 0 Caio & Hernane (ALEMANHA)",
        "LC & Luiz Fernando (COLOMBIA) 0 x 0 Caio & Hernane (ALEMANHA)"
    ]
    
    grupo_jogos_C = [
        "Breno Menezes & Junior (ARGENTINA) 0 x 0 Jhonathan & Rafael Gouveia (BÉLGICA)",
        "Breno Menezes & Junior (ARGENTINA) 0 x 0 MK & Matheus (INGLATERRA)",
        "Jhonathan & Rafael Gouveia (BÉLGICA) 0 x 0 MK & Matheus (INGLATERRA)"
    ]
    
    grupo_jogos_D = [
        "Carlinhos & Silvio (ESPANHA) 0 x 0 Cadu & João (JAPAO)",
        "Carlinhos & Silvio (ESPANHA) 0 x 0 Diogo & José (URUGUAI)",
        "Cadu & João (JAPAO) 0 x 0 Diogo & José (URUGUAI)"
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
