# Установка и запуск в Windows

## 1. Установка Python 3.10

Программа использует `torch==1.12.1` — для него нужны колёса Python **не выше 3.10**.
Ставим Python **3.10**, не новее.

1. Скачайте установщик: https://www.python.org/downloads/release/python-31011/ → «Windows installer (64-bit)».
2. Запустите установщик:
   - ✅ обязательно отметьте **«Add python.exe to PATH»** (внизу окна);
   - нажмите **Install Now**.
3. Проверка: откройте **PowerShell** (Win+X → Терминал/PowerShell) и выполните:

```powershell
python --version
```

Должно вывести `Python 3.10.11` (или другую версию 3.10.x).
Если пишет «python не является командой» — переустановите с галочкой PATH или перезапустите терминал.

## 2. Установка Git

1. Скачайте: https://git-scm.com/download/win → «64-bit Git for Windows Setup».
2. Установка: на всех шагах можно оставлять настройки по умолчанию (Next → Next → Install).
3. Проверка:

```powershell
git --version
```

## 3. Скачивание проекта

```powershell
cd $HOME\Desktop        # или куда удобно
git clone https://notabug.org/granthin/sastra-vaca.git
cd sastra-vaca
```

(Если notabug недоступен — зеркало: `git@github.com:ISKCON-developers-community/sastra-vaca.git`)

## 4. Создание виртуального окружения и установка зависимостей

В папке проекта:

```powershell
python -m venv env
.\env\Scripts\activate
```

После активации в начале строки появится `(env)`.

> Если PowerShell ругается «выполнение сценариев отключено», один раз выполните:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> и повторите активацию.

Установка зависимостей (torch весит ~700 МБ, займёт время):

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Запуск

```powershell
python main.py
```

При первом запуске нужен интернет — скачается модель Silero TTS (~60 МБ) в кэш torch.

Дальше программа ведёт диалогом (GUI-окна):

1. **Pick an item** → выберите «File» (один файл .txt) или «Folder» (все .txt из папки).
2. Выберите текстовый файл — кодировка UTF-8.
3. Введите имя итогового аудиофайла (без расширения, получится `.wav`).
4. Выберите голос: `baya`, `kseniya`, `xenia`, `aidar`, `eugene`, `random`.

Готовые `.wav` появятся в папке проекта.

## Возможные проблемы

| Симптом | Причина / решение |
|---|---|
| `Could not find a version that satisfies torch==1.12.1` | У вас Python >3.10. Поставьте Python 3.10 и создайте venv им заново. |
| Медленный синтез | Это CPU. Одна книга может озвучиваться часами — оставьте компьютер включённым. |
| Ошибка «You need internet connection» при старте | Нет интернета при первом запуске (или заблокирован raw.githubusercontent.com — включите VPN). |
| Кракозябры/пустой звук | Файл .txt не в UTF-8 — пересохраните (Блокнот → Сохранить как → кодировка UTF-8). |
| Звук обрывается между абзацами | Норма: паузы между абзацами нет, склейка идёт встык. |
