

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
            {"dupla": "Heitor Foquinha (AFRICA DO SUL)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 15, "saldo": 3},
            {"dupla": "Gabrielle Sena (PORTUGAL)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Lucila (CROACIA)", "vitorias": 0, "derrotas": 1, "pro": 15, "contra": 18, "saldo": -3},
        ],
        
        "Grupo B": [
            {"dupla": "James Fogão (HOLANDA)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 15, "saldo": 3},
            {"dupla": "Maria Luiza (ARGENTINA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Beatriz Moreira (MEXICO)", "vitorias": 0, "derrotas": 1, "pro": 15, "contra": 18, "saldo": -3},
        ],
        
        "Grupo C": [
            {"dupla": "Michelle Santos (EUA)", "vitorias": 1, "derrotas": 0, "pro": 18, "contra": 15, "saldo": 3},
            {"dupla": "Manuela Mesquita (JAPAO)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Giovanna Trotte (COLOMBIA)", "vitorias": 0, "derrotas": 1, "pro": 15, "contra": 18, "saldo": -3},
        ],
        
        "Grupo D": [
            {"dupla": "Nathalia Santana (ALEMANHA)", "vitorias": 1, "derrotas": 0, "pro": 19, "contra": 17, "saldo": 2},
            {"dupla": "Beatriz Castro (INGLATERRA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Fabiana (FRANÇA)", "vitorias": 0, "derrotas": 1, "pro": 17, "contra": 19, "saldo": -2},
        ],
        
        "Grupo E": [
            {"dupla": "Giulia Medeiros (ESPANHA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Danielle Rodrigues (BELGICA)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
            {"dupla": "Mariana Noga (URUGUAI)", "vitorias": 0, "derrotas": 0, "pro": 0, "contra": 0, "saldo": 0},
        ]
    }

    # ===== ELIMINATÓRIAS =====
    grupo_jogos_A = [
        "Heitor Foquinha (AFRICA DO SUL) 18 x 15 Lucila (CROACIA)",
        "Heitor Foquinha (AFRICA DO SUL) 0 x 0 Gabrielle Sena (PORTUGAL)",
        "Lucila (CROACIA) 0 x 0 Gabrielle Sena (PORTUGAL)"
    ]
    
    grupo_jogos_B = [
        "Beatriz Moreira (MEXICO) 15 x 18 James Fogão (HOLANDA)",
        "Beatriz Moreira (MEXICO) 0 x 0 Maria Luiza (ARGENTINA)",
        "James Fogão (HOLANDA) 0 x 0 Maria Luiza (ARGENTINA)"
    ]
    
    grupo_jogos_C = [
        "Michelle Santos (EUA) 18 x 15 Giovanna Trotte (COLOMBIA)",
        "Michelle Santos (EUA) 0 x 0 Manuela Mesquita (JAPAO)",
        "Giovanna Trotte (COLOMBIA) 0 x 0 Manuela Mesquita (JAPAO)"
    ]
    
    grupo_jogos_D = [
        "Nathalia Santana (ALEMANHA) 19 x 17 Fabiana (FRANÇA)",
        "Nathalia Santana (ALEMANHA) 0 x 0 Beatriz Castro (INGLATERRA)",
        "Fabiana (FRANÇA) 0 x 0 Beatriz Castro (INGLATERRA)"
    ]
    
    grupo_jogos_E = [
        "Giulia Medeiros (ESPANHA) 0 x 0 Danielle Rodrigues (BELGICA)",
        "Giulia Medeiros (ESPANHA) 0 x 0 Mariana Noga (URUGUAI)",
        "Danielle Rodrigues (BELGICA) 0 x 0 Mariana Noga (URUGUAI)"
    ]

    oitavas = [
        "Atleta 1 0 x 0 Atleta 5",
        "Atleta 2 0 x 0 Atleta 6",
        "Atleta 3 0 x 0 Atleta 7",
        "Atleta 4 0 x 0 Atleta 8"
    ]
    
    quartas = [
        "Atleta Grupo 1 0 x 0 Atleta Oitavas 1 ",
        "Atleta Grupo 2 0 x 0 Atleta Oitavas 2",
        "Atleta Grupo 3 0 x 0 Atleta Oitavas 3",
        "Atleta Grupo 4 0 x 0 Atleta Oitavas 4"
    ]

    semifinais = [
        "Atleta Quarta 1 0 x 0 Atleta Quarta 3",
        "Atleta Quarta 2 0 x 0 Atleta Quarta 4"
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
        grupo_jogos_E = grupo_jogos_E,
        oitavas=oitavas,
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
