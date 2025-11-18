from datetime import date


# Часть А. Создайте набор функций для обработки информации о письме.
# Каждая функция должна выполнять ровно одно действие и возвращать результат.

email = {
    "subject": "Conference",
    "from": " Veronika@sberbank.ru ",
    "to": "Kate@sberbank.ru",
    "body": "Hello, Kate! Conference at 12:00 online!",
}


# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы

# функция нормализации email адреса
def normalize_adresses(email: dict) -> dict:
    normalize_email = email.copy() # создание копии, чтобы не менять оригинал
    if 'from' in normalize_email:
        normalize_email['from'] = normalize_email['from'].lower().strip()
    if 'to' in normalize_email:
        normalize_email['to'] = normalize_email['to'].lower().strip()
    return normalize_email

# вызов функции
normalize_email = normalize_adresses(email)

# проверка результата
print(normalize_email)


# 2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")
def add_short_body(email: dict) -> dict:
    short_email = email.copy()
    short_email['body'] = short_email['body'][:10] + '...'
    return short_email

# вызов функции
short_email = add_short_body(email)

# проверка результата
print(short_email)


# 3. Очистка текста письма - заменяет табы и переводы строк на пробелы
def clean_body_text(body: str) -> str:
    clean_text = body.replace('\t', ' ').replace('\n', ' ')
    return clean_text

# Результат сохраняется в новый ключ "clean_body" словаря email.
email['clean_body'] = clean_body_text(email['body'])
print(email)

# 4. Формирование итогового текста письма - создает форматированный текст письма
def build_sent_text(email: dict) -> str:
    # Защита от KeyError + поддержка разных ключей
    to = email.get('recipient') or email.get('to', '—')
    sender = email.get('sender') or email.get('from', '—')
    date = email.get('date', '—')  # add_send_date добавляет 'date'
    subject = email.get('subject', '—')
    clean_body = email.get('clean_body', email.get('body', ''))

    return (
        f"Кому: {to}, от: {sender}\n"
        f"Тема: {subject}, дата: {date}\n"
        f"Текст: {clean_body}"
    )

# добавляем дату
email['date'] = "2025-11-11"

# Результат (сформированная строка) сохраняется в новый ключ "sent_text".
email['sent_text'] = build_sent_text(email)
print(email['sent_text'])


# 5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля
def check_empty_fields(email: dict) -> tuple[bool, bool]:
    # убираем пробелы по краям
    is_subject_empty = not email['subject'].strip()
    is_body_empty = not email['body'].strip()
    return is_subject_empty, is_body_empty

# вызов функции
is_subject_empty, is_body_empty  = check_empty_fields(email)

print('Пустая тема письма', is_subject_empty)
print('Пустое тело письма', is_body_empty)


# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
def mask_sender_email(login: str, domain: str) -> str:
    masked_email = login[:2] + '***@' + domain
    return masked_email

sender = "Veronika@sberbank.ru"
login, domain = sender.split('@')

masked = mask_sender_email(login, domain)
print('Маска отправителя:', masked)


# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_email = [] #list
    for email in email_list:
        clean_email = email.strip().lower()

        if '@' in clean_email and clean_email.endswith(('.com', '.ru', '.net')):
            correct_email.append(clean_email)

    return correct_email

test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]

correct_list = get_correct_email(test_emails)
print('Корректные email адреса:', correct_list)


# 8. Создание словаря письма - создает базовую структуру письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    email = {
        'sender': sender,
        'recipient': recipient,
        'subject': subject,
        'body': body
    }

    return email

my_email = create_email(
    sender = 'Veronika@sberbank.ru',
    recipient = 'Kate@sberbank.ru',
    subject = 'Conference',
    body = 'Hello, Kate! Conference at 12:00 online!'
)

print(my_email)


# 9. Добавление даты отправки - добавляет текущую дату
def add_send_date(email: dict) -> dict:
    send_date = date.today().strftime('%d/%m/%Y')
    email['date'] = send_date
    return email

email = {
    'sender': 'Veronika@sberbank.ru',
    'recipient': 'Kate@sberbank.ru',
    'subject': 'Conference',
    'body': 'Hello, Kate! Conference at 12:00 online!',
}

# вызвать функцию и сохранить результат
email = add_send_date(email)
print(email)


# 10. Получение логина и домена - разделяет email на логин и домен
def extract_login_domain(address: str) -> tuple[str, str]:
    login, domain = address.split('@')
    return login, domain

email = {"from": "Veronika@sberbank.ru"}
login, domain = extract_login_domain(email['from'])

print('Логин отправителя:', login)
print('Домен отправителя', domain)


# Часть В. Создать функцию отправки письма с валидацией и обработкой.
# Функция принимает список получателей, тему, сообщение и отправителя.

def sender_email(recipient_list: list[str], subject: str, message: str, *, sender='default@study.com') -> list[dict]:
    # 1. Проверить что есть получатели
    if not recipient_list:
        return []  # 1 способ

    if len(recipient_list) == 0:
        return []  # 2 способ

    # 2. Проверить корректность email адресов
    valid_sender = get_correct_email([sender])
    valid_recipient = get_correct_email(recipient_list)
    if not valid_sender or not valid_recipient:
        return []

    # 3. Проверить заполненность темы и тела письма
    is_subject_empty, is_body_empty = check_empty_fields({'subject': subject, 'body': message})
    if is_subject_empty or is_body_empty:
        return []

    # 4. Исключить отправку самому себе
    valid_recipient = [r for r in valid_recipient if r != sender]
    if not valid_recipient:
        return []

    # 5. Нормализовать все текстовые данные
    clean_subject = clean_body_text(subject)
    clean_body = clean_body_text(message)

    emails: list[dict] = []


    # 6. Создать письмо для каждого получателя
    all_emails = []

    for r in valid_recipient:
        email = create_email(sender=sender, recipient=r, subject=clean_subject, body=clean_body)

        # 7. Добавить дату отправки
        email = add_send_date(email)

        # 8. Замаскировать email отправителя
        login, domain = extract_login_domain(sender)
        email['masked_sender'] = mask_sender_email(login, domain)

        # 9. Создать короткую версию тела письма
        email = add_short_body(email)  # ← мутируем email (или переприсваиваем)
        email['clean_body'] = clean_body  # ← добавляем clean_body В ТОТ ЖЕ СЛОВАРЬ

        # 10. Сформировать итоговый текст письма
        email['sent_text'] = build_sent_text(email)  # ✅ теперь все поля на месте

        emails.append(email)

        # 10. Сформировать итоговый текст письма
        email['sent_text'] = build_sent_text(email)

        emails.append(email)

    return emails

# проверка функции
emails = sender_email(
    recipient_list = ["admin@company.ru", "manager@study.com", "default@study.com"],
    subject = 'Hello',
    message = 'Привет, коллега!',
    sender = 'default@study.com'
)

for e in emails:
    print(e['sent_text'])