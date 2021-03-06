help_message = '''
Через этого бота можно купить медальон самого Геральта из Ривии, чтобы посмотреть, как происходит покупка и оплата в Telegram
Отправьте команду /buy, чтобы перейти к покупке
Узнать правила и положения можно воспользовавшись командой /terms
'''

start_message = 'Привет\\! Это демонстрация работы платежей в Telegram\n' + help_message

pre_buy_demo_alert = '''\
Так как сейчас я запущен в тестовом режиме, для оплаты нужно использовать карточку с номером `4242 4242 4242 4242`
Счёт для оплаты:
'''

terms = '''\
*Спасибо, что выбрали нашего бота\\. Мы надеемся, вам понравится медальон*
1 Если медальон не будет доставлен вовремя, пожалуйста, обратить к нам
2 Если вы хотите вернуть деньги, будьте так любезны подать заявку, и мы немедленно совершим возврат
'''

tm_title = 'Медальон Школы Волка'
tm_description = '''\
Геральт во время книжных событий утратил свой медальон.
Вы удивитесь, но мы смогли найти его.
Хотели бы вы ощутить себя в шкуре волка?
Закажите Медальон у нас прямо сейчас\\!
'''

AU_error = '''\
Попробуйте выбрать другой адрес!
'''

wrong_email = '''\
Нам кажется, что указанный имейл не действителен.
Попробуйте указать другой имейл
'''

successful_payment = '''
Ура\\! Платеж на сумму `{total_amount} {currency}` совершен успешно\\! Приятного пользования\\!
Правила возврата средств смотрите в /terms
'''
MESSAGES = {
    'start': start_message,
    'help': help_message,
    'pre_buy_demo_alert': pre_buy_demo_alert,
    'terms': terms,
    'tm_title': tm_title,
    'tm_description': tm_description,
    'AU_error': AU_error,
    'wrong_email': wrong_email,
    'successful_payment': successful_payment,
}
