# VPC-Power-On-off
#Steps

1 - git clone github.com/lucas2179/VPC-Power-On-off <br>
2 - No IBM Cloud Functions, criar uma Action chamada Get-Token em python 3.7, e então copiar o código do arquivo get-token.py <br>
3 - Criar outra action, também em python 3.7, chamada Power-VPC com o código do arquivo powervpc.py <br>
4 - Criar uma sequence e adicionar a funcao Get-Token e depois a Power-VPC <br>
5 - Antes de acionar a sequence, clique em mudar entrada, e então, utilizar o modelo presente no arquivo entrada.json <br>
