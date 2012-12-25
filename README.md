Glossary maker
[![endorse](http://api.coderwall.com/antigluk/endorsecount.png)](http://coderwall.com/antigluk)

0) Скачать это: https://github.com/antigluk/glossary-maker/archive/master.zip

0.1) Установить python-yandex-translate: https://github.com/vdmitrij/python-yandex-translate/archive/master.zip
$ sudo python setup.py install


1) Поместить исходный текст в файл, например ~/text.txt
2) Команда $ python glossary.py < ~/text.txt > ~/glossary.txt

Создаст в домашней папке глоссарий - каждое 6 слово в тексте с переводом в формате

    allowing  -  позволяет
    capable  -  способен
    microcontroller  -  микроконтроллер

по алфавиту
