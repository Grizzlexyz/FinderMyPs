# Cria a pasta do projeto na Área de Trabalho
$folder = "$env:USERPROFILE\Desktop\FinderMyPs"
if (!(Test-Path $folder)) { New-Item -ItemType Directory -Path $folder }
Set-Location $folder

Write-Host "--- Configurando FinderMyPs ---" -ForegroundColor Cyan

# Links para os arquivos RAW do seu GitHub
$baseUrl = "https://raw.githubusercontent.com/Grizzlexyz/FinderMyPs/main"

Write-Host "📥 Baixando arquivos..."
Invoke-WebRequest -Uri "$baseUrl/Bot.py" -OutFile "Bot.py"
Invoke-WebRequest -Uri "$baseUrl/requirements.txt" -OutFile "requirements.txt"

# Verifica se o Python existe
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Erro: Python não encontrado! Instale-o pela Microsoft Store." -ForegroundColor Red
    pause
    exit
}

# Instala as dependências (requests)
Write-Host "📦 Instalando bibliotecas..." -ForegroundColor Yellow
pip install -r requirements.txt --user --quiet

Write-Host "✅ Tudo pronto! Iniciando..." -ForegroundColor Green
python Bot.py
pause
