# Один раз: окружение, БД и игры (Windows PowerShell)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== GameLib: установка ===" -ForegroundColor Cyan

if (-not (Test-Path "venv\Scripts\python.exe")) {
    Write-Host "Создаём venv..."
    python -m venv venv
}

Write-Host "Ставим пакеты..."
& .\venv\Scripts\pip install -r requirements.txt -q

Write-Host "Миграции..."
& .\venv\Scripts\python manage.py migrate

Write-Host "Заполняем БД играми..."
& .\venv\Scripts\python manage.py seed_data

Write-Host ""
Write-Host "Готово!" -ForegroundColor Green
Write-Host "  venv\Scripts\activate"
Write-Host "  python manage.py createsuperuser   # один раз, для админки"
Write-Host "  python manage.py runserver"
Write-Host ""
Write-Host "Сайт:  http://127.0.0.1:8000/"
Write-Host "Админ: http://127.0.0.1:8000/admin/"
