# yc-bot-bot_certs_domains
Простой бот для напоминания о подходе сроков окончания сертификатов и доменов

Бот на YandexCloud. Используется функционал Cloud Function (FaaS).
Функция читает читает данные из групп JSON файла (в примере domains и certificates, но 
технически кол-во групп и элементов в группе может быть любым при условии сохранения формата
JSON файла) и отправляет уведомление в группу Telegram, начиная с указанного в переменной DAY_EXPIRIEN_ALERT
числа дней (по умолчанию уведомления начинаются с 7-го дня).

Выполнение указанной функции обеспечивается тригером Cloud Function, который в указанное в тригере время 
(в моем случае раз в сутки) выполняет функцию. Но можно хоть ежеминутно его выполнять - вопрос целесообразности и стоимости.

Используется 3 переменных среды:

<b>PREMSG</b> - Фраза перед уведомлением. По идее задумана для размещения смартов 
         для упоминания конкретных людей в чате (можно задать пустой строкой)

<b>CHAT_ID</b> - ID чата, в который будет отправлено уведомление

<b>BOT_TOKEN</b> - токен созданного Вами бота
