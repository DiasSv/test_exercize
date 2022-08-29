
В данном репозитории находятся файлы и решения для тестового задания от компании Nexign - https://www.notion.so/4efb951fa25f4aa48d3a62a6176f3e9a

Для проверки 1 задания подгтовлена краткая инструкция (см.ниже)
Для проверки 2 задания необходимо найти файл "test_exercise.py", запустить файл, ввести входные данные и получить валидные выходные данные



Прежде,чем тестить мою работу, пожалуйста прочитай

1.

Так как сообщество тестировщиков разделилось в том, чтобы использовать DriverManager и не использовать его
    Прошу учесть то, что я все таки его использую 
    И ЕСЛИ, друг мой, появилась проблема именно с ним, то пожалуйста установи его в свое окружение, в котором ты работаешь
    
Install manager:
```
pip install webdriver-manager
```
Все остальное уже есть в коде, для вызова менеджера


2
Небольшая инструкция по проверке:

1. Скачайте к себе проект, либо скачав и распаковав архив, либо склонировав репозитарий.
Просмотрите содержимое файла README.md, возможно, там будут какие-нибудь полезные комментарии для проверки.
Здесь можно, например, указать ОС и версию Python, с которой Вы работаете. 
2. Деактивируйте текущее виртуальное окружение, если вы в нем находитесь. 
Вспомнить, как работать с виртуальными окружениями можно на этом шаге (для Windows):
https://stepik.org/lesson/25969/step/2?unit=196192
3. Создайте новое виртуальное окружение.
4. Перейдите в папку вновь созданного окружения:
cd \path\to\new_virtual_env\Scripts
5. Активируйте данное виртуальное окружение.
6. Установите пакеты в окружение из файла requirements.txt, который должен быть в скачанном проекте:
pip install -r \path\to\requirements.txt
7. Убедитесь, что путь к chromedriver.exe прописан в PATH
8. Запустите тесты командой:
pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py
9. Проверьте, что все тесты прошли успешно.
