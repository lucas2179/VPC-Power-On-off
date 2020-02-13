# VPC-Power-On-off
#Steps

1 - git clone github.com/lucas2179/VPC-Power-On-off <br>
2 - No IBM Cloud Functions, criar uma Action chamada Get-Token em python 3.7, e então copiar o código do arquivo get-token.py <br>
3 - Criar outra action, também em python 3.7, chamada Power-VPC com o código do arquivo powervpc.py <br>
4 - Criar uma sequence e adicionar a funcao Get-Token e depois a Power-VPC <br>
5 - Antes de acionar a sequence, clique em mudar entrada, e então, utilizar o modelo presente no arquivo entrada.json <br>
<br><br>

# Acessando a api key da IBM Cloud
1 - No menu gerenciar, clicar em acesso IAM <br>
2 - No menu lateral, selecionar chaves de API do IBM Cloud <br>
3 - Clique em "Criar uma chave de API do IBM Cloud" <br>
4 - De um nome para a mesma, depois, clique em Criar<br>
5 - Copie a Apikey<br>

# Descobrindo o Account Id
1 - No menu gerenciar, clique em "Conta"<br>
2 - No menu lateral, clique em "Configurações da Conta" <br>
3 - Copie o ID da conta <br>

