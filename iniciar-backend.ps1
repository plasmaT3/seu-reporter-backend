# Caminho para o ambiente virtual
$venvPath = ".\venv\Scripts\Activate.ps1"

# Ativar o ambiente virtual
Write-Host "🔄 Ativando ambiente virtual..."
& $venvPath

# Instalar flask-cors no ambiente ativo
Write-Host "📦 Garantindo flask-cors instalado no ambiente correto..."
pip install flask-cors

# Mostrar pacotes instalados (verificação)
Write-Host "📋 Listando pacotes instalados..."
pip list

# Rodar o backend
Write-Host "🚀 Iniciando o backend (app.main)..."
python -m app.main
