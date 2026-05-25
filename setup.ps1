# Один раз: создать venv и поставить зависимости (Windows)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path "venv\Scripts\python.exe")) {
    Write-Host "Создаём venv..."
    python -m venv venv
}

Write-Host "Устанавливаем зависимости..."
& .\venv\Scripts\pip install -r requirements.txt

Write-Host ""
Write-Host "Готово. Дальше:"
Write-Host "  venv\Scripts\activate"
Write-Host "  python manage.py migrate"
Write-Host "  python manage.py seed_data"
Write-Host "  python manage.py runserver"
