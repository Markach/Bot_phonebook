import telebot
import create_durectory as cr
import logger as lg

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name}!\n Бот начал работу! \n/menu -команда вызова меню')

name_it = ''
surname_it = ''
number_it = ''
comment_it = ''
user_id_it = ''

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/menu':
        bot.send_message(message.chat.id, f'Выбери пункт меню, введя соответствующую команду: \n/1 - Показать все записи.\n/2 - Найти номер по фамилии.\n/3 - Найти номер по имени.\n/4 - Добавить новую запись.\n/5 - Удалить запись.')
        cr.init_book('phonebook.csv')

    elif message.text == '/1':
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{cr.extract_data()}')

    elif message.text == '/2':
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == '/3':
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/4':
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, get_surname)

    elif message.text == '/5':
        lg.logging.info('The user has selected item number 5')
        bot.send_message(
            message.chat.id, f'Выберите контакт, который хотите удалить?\nВыберите по:\n/51 - Фамилии')      
        bot.register_next_step_handler(message, delete_contact)
    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /menu.')

def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.extract_data(surname=surname_it)}')


def find_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.extract_data(name=name_it)}')


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Введите имя')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Введите номер телефона')
    bot.register_next_step_handler(message, get_number)

    
def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'Введите комментарий')
    bot.register_next_step_handler(message, get_comment)


def get_comment(message):
    global comment_it
    comment_it = message.text
    lg.logging.info('User entered: {comment_it}')
    cr.create_contact( name_it, surname_it, number_it, comment_it)
    bot.send_message(message.chat.id, f'Контакт успешно добавлен!')


def delete_contact(message):
    if message.text == '/51':
        lg.logging.info('The user has selected item number 5.1')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, delete_surname)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /menu.')


def delete_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.extract_data(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    cr.delete_contact(id=user_id_it)
    bot.send_message(
        message.chat.id, f'Контакт успешно удален!')

bot.infinity_polling()