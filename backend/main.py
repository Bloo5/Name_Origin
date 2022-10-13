from flask import Flask
import torch
import torch.nn as nn
import torch.nn.functional as F
import string
import os


args = {}
args['device'] = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class RNN(nn.Module):
    def __init__(self, tam_entrada, tam_feature, tam_saida):
        super(RNN, self).__init__()
        
        self.tam_entrada = tam_entrada
        self.tam_feature = tam_feature
        self.tam_saida   = tam_saida
        
        self.rnn    = nn.RNNCell(self.tam_entrada, self.tam_feature)
        self.linear = nn.Linear(self.tam_feature, self.tam_saida)
        self.softmax = nn.LogSoftmax()
    
    def forward(self, nome):
      
        # Inicialize o estado interno da RNN
        hidden = torch.zeros(1, self.tam_feature).to(args['device'])
        
        for letra in nome:
          letra = letra.unsqueeze(0)
          hidden = self.rnn(letra, hidden)
        
        saida = self.linear(hidden)
        saida = self.softmax(saida) 
        return saida

model = torch.load('model')
model.eval()
caracteres_validos = string.ascii_letters
root_path = 'data/names/'
arquivos = sorted(os.listdir(root_path))
categorias = [a[:-4] for a in arquivos]
tam_dicionario = len(caracteres_validos)

def predict(nome):
  model.eval()

  tns = torch.zeros( len(nome), tam_dicionario )
  for k, letra in enumerate(nome):
    idx = caracteres_validos.find(letra)
    tns[k, idx] = 1
  tns = tns.to(args['device'])

  saida = model(tns)
  topv, topi = saida.data.topk(3, 1, True)

  origins = []

  for value, index in zip(topv[0], topi[0]):
    origins.append(categorias[index])

  return origins

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ola Mundo'

@app.route('/teste/<val>')
def previsao(val):
  return predict(val)

if __name__ == '__main__':
    app.run(
        debug=True,
        #port=int(os.getenv('PORT', 4444))
    )