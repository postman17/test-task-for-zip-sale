# Test task for https://zipsale.co.uk/
Задача тестового задания – проверить то, как ты пишешь код. Пожалуйста, следуй тем правилам, которым ты обычно следуешь при закрытии ежедневных рабочих задач.

Результат – приватный репозиторий на Гитхабе, в который нужно добавить меня (melevir) с опционально настроенным CI.

Задача – сделать веб-сервис, который позволит узнавать, в какие проекты конкретный пользователь Гитхаба делал пул-реквесты их их смерджили. Сценарий такой:
На главной странице я ввожу ник пользователя на Гитхабе, жму “Send”.
В результате вижу страницу со списком проектов, в которые пользователь делал пул-реквест и его смерджили. По каждому проекту я вижу:
название проекта;
ссылку на проект на Гитхабе;
количество звёзд на Гитхабе;
ссылки на смерженные пул-реквесты от пользователя;
ссылки на несмердженные пул-реквесту от пользователя;
у каждого пул-реквеста я вижу количество комментариев в этом пул-реквесте.

Общаться с Гитхабом через АПИ. Вот справка: https://docs.github.com/en/rest

Пожалуйста, используй Python 3.9 и Django. Джанга тут кажется лишняя, но давай делать на ней: мы используем её в бою, не хочется тестировать вас на других технологиях :)

Пожалуйста, не трать на тестовое больше 8-10 часов и скинь мне его до 22-го марта.
К ссылке на репозиторий было бы круто сразу прикрепить резюме :)


## Установка
- copy .env.example to .env
- Add github token to env file
- docker-compose up