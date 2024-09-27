from flask import Flask, request, jsonify, send_from_directory
from huggingface_hub import InferenceClient

app = Flask(__name__)

client = InferenceClient(
    "microsoft/Phi-3.5-mini-instruct",
    token="insira_seu_token_aqui", #Crie seu token em https://huggingface.co/settings/tokens
)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html') 

@app.route('/summarize', methods=['POST'])
def resumir():
    data = request.json
    inputUsuario = data['text']
    # comando = "Resuma todas as informações em pontos principais(• ) e em Português brasileiro (se estiver em outra língua traduza antes), sem falar qualquer outra coisa além do resumo ou duplicação:"
    # comando = "Em Português brasileiro (se estiver em outra língua como ingles traduza tudo antes, exceto os termos de programação em inglês), resuma todas as informações de forma bem curta, sem falar qualquer outra coisa além do resumo e sem duplicação:"
    comando = "Interprete o texto e resuma deixando o texto curto e objetivo, sem duplicação; se a entrada estiver em outra língua (como inglês), traduza obrigatoriamente tudo para Português"

    mensagens = [
        {"role": "user", "content": f"{comando} {inputUsuario}"}
    ]

    respostaIA = ""
    for mensagem in client.chat_completion(
        messages=mensagens,
        max_tokens=300,
        stream=True,
    ):
        respostaIA += mensagem.choices[0].delta.content

    return jsonify({'summary': respostaIA})

if __name__ == '__main__':
    app.run(debug=True)
