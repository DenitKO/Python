# VENV

https://www.youtube.com/watch?v=0i4SPuorMEE

venv — это модуль в Python, который позволяет создавать виртуальные окружения для проектов.

Виртуальное окружение — это локальная копия Python нужной версии с набором библиотек, необходимых конкретному проекту. Обычно оно хранится в скрытой подпапке .venv в папке проекта.

Чтобы создать виртуальное окружение, нужно запустить модуль venv и указать папку, в которой оно будет храниться.

После создания виртуального окружения его следует активировать. Для этого в Windows нужно запустить файл .venv\Scripts\activate.bat, а в Linux или macOS — файл при помощи команды source: source .venv/bin/activate.

После активации виртуального окружения команды Python и pip будут работать с ним.

- "Ctrl" + "L" - очистка терминала


Проверка версии Python:
- python --version
- python -V

Проверить какие пакеты установлены:
- pip list

Установка виртуального окружения:

- python -m venv venv - установить виртуальное окружение в папку -m venv [filepath]
- python -m venv venv --upgrade-deps pip - установка venv и апгрейд pip

Активация виртулаьного окружения скриптом

.\venv\Scripts\activate

Декактивация:

deactivate

Выбор интерпретатора:

- "Ctrl" + "Shift" + "P" или "F1"
- ввести python
- пункт "Python: Выбор интерпретатора"

Как автоматически включать venv в Visual Studio Code

File - Preferences - Settings - Workspace - activate - Activate Env in Current Terminal

Установка пакетов:
- pip install prog1 prog2 prog3

Перенаправка установленных именно мной пакетов в txt
- pip freeze > requirements.txt

Установка зависимостей в venv
- pip install -r .\requirements.txt

Установка venv с определённым интерпритатором
filepath_to_python -m venv venv --upgrade-deps