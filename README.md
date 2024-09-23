Создайте пустую папку
откройте и  введите команду на терминале git clone https://github.com/whaldeyw/qa_auto.git
перейдите в рабочую папку cd qa_auto
создайте файл .env добавьте в него строки username='ваш username' и password='ваш пароль для входа'
создайте виртуальное окружение python3 -m venv venv
Активируйте виртуальное окружение Linux source venv/bin/activate 
Установите необходимые зависимости pip install -r requirements.txt 
перейдите в папку с первым тестом cd test1
Запустите файл python3 test1.py
Перейдите назад в корневую папку cd ../
Перейдите во вторую папку с тестом cd test2 
Запустите файл python3 github_api.py
