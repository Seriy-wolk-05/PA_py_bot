import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import schedule
import time

bot = telebot.TeleBot('7210738426:AAE_SSKdxnvHW1HG-Y20v5WUxBXJqXbrReU') #@ranepamap_bot (Юры)

# Список пользователей, которые нажали /start
users = []

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, студент! Я – твой путеводитель в Академии.")
    show_menu(message)
    time.sleep(15)

# Функция для отображения меню кнопок
def show_menu(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    btn1 = KeyboardButton('Карта Академии')
    btn2 = KeyboardButton('1 корпус')
    btn3 = KeyboardButton('2 корпус')
    btn4 = KeyboardButton('3 корпус')
    btn5 = KeyboardButton('5 корпус')
    #btn6 = KeyboardButton('❌ 6 корпус')
    btn7 = KeyboardButton('❌ Копировальные центры 🖨')
    btn8 = KeyboardButton('❌ Банкоматы 💵')
    btn9 = KeyboardButton('❌ Мед. центр 💉')
    btn10 = KeyboardButton('❌ Деканат ИПНБ 👨‍🎓')
    btn11 = KeyboardButton('❌ Где поесть? 🥐')
    btn12 = KeyboardButton('Книжные магазины 📚')
    btn13 = KeyboardButton('❌ Военно-учетный стол 🔫')
    btn14 = KeyboardButton('❌ Платная парковка 🚗')
    btn15 = KeyboardButton('Библиотеки 📗')
    btn16 = KeyboardButton('Тех. поддержка ⚙️')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16)
    bot.send_message(message.chat.id, "О чем ты хочешь меня спросить? ↓", reply_markup=markup)
  
attention_delete = 'Через минуту сообщения выше удалятся сами 👆'
attention_time = 60

# Обработчик нажатий на кнопки (фото)
@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    if message.text == 'Карта Академии':
        photo_url = 'https://disk.yandex.ru/i/1hdDAmaAEF-_JA'
        mes1 = bot.send_photo(message.chat.id, photo_url)
        """
        if message.text == 'Карта Академии':
            att = bot.send_message(message.chat.id, attention_delete)
            time.sleep(attention_time)
            bot.delete_message(message.chat.id, message.id)
            bot.delete_message(message.chat.id, mes1.id)
            bot.delete_message(message.chat.id, att.id)
        """
    elif message.text == '1 корпус':
        photo_url1 = 'https://downloader.disk.yandex.ru/preview/5d0caf99c7939f356f0b9cd9275554e3fef84327d7fb2544e6206fcce1a7561e/66d07e04/vcRXzYG5nWGcWk4HTZ4OHbxM3qqYcXyfBRiJhZD591VL2ONURikrTx0qb3MJQ5456ABn8PcbaXUfOc8TaEs6_g%3D%3D?uid=0&filename=1к1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url2 = 'https://downloader.disk.yandex.ru/preview/bd0a1836fde0ebfbe9ffc4965569797ad56bb99b6dbeb6a7bf108af1e9e56ba5/66d07e04/QUQykMiEuxspXJ_QdBZZrcbTKFmO44GCRlkTAXPVGV2CAVe494AYI3ZKSAaXZWXWwWQRMPJ70Uklpfgnq7xZfA%3D%3D?uid=0&filename=1к2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url3 = 'https://downloader.disk.yandex.ru/preview/df1303524171dbfef61de19b5af1259927589257e86ade7577945e9e8731e93f/66d07e04/J4Iz_HGyOADr09pZXHZL7Gfy1e6rA_5P6a5IhKN-ECJOjBBoXwrfyxGg5J_8Q-lXE5rN_cPRma3mil-NjUJX4Q%3D%3D?uid=0&filename=1к3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        ph1 = bot.send_photo(message.chat.id, photo_url1)
        ph2 = bot.send_photo(message.chat.id, photo_url2)
        ph3 = bot.send_photo(message.chat.id, photo_url3)
        """
        if message.text == '1 корпус':
            att = bot.send_message(message.chat.id, attention_delete)
            time.sleep(attention_time)
            bot.delete_message(message.chat.id, message.id)
            bot.delete_message(message.chat.id, ph1.id)
            bot.delete_message(message.chat.id, ph2.id)
            bot.delete_message(message.chat.id, ph3.id)
            bot.delete_message(message.chat.id, att.id)
        """
    elif message.text == '2 корпус':
        photo_url1 = 'https://downloader.disk.yandex.ru/preview/682ef832e34428d50d2276e51affec415aca23d142adb7807157abef5633d0f4/66d07e8c/-kAVM1YdfnyLMbGBqcuHBValqksvWdcCknufI2HAxQLPUKOSwp7NDeCg17pjKl07t2rDOzrcx_yVaUgdvCNxRQ%3D%3D?uid=0&filename=2%201.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url2 = 'https://downloader.disk.yandex.ru/preview/209768d4b0d84c11e6389759e3241ae8d1f5725c28ce25a18a2db03b7e7acbd2/66d07e8c/-tslpe0OpfOT6RsEmWpeE1alqksvWdcCknufI2HAxQIV_VQPEE1wISK6zIvrQo-m0jezkJ-MvYA9ngr63edUvQ%3D%3D?uid=0&filename=2%202.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url3 = 'https://downloader.disk.yandex.ru/preview/93fe7885839ce31c661f870a4c355c8712c21486d97ea3c08bbffb7a0791c096/66d07e8c/IeYKcY-gTuKKr9yBSlHtnLUL8G9abYctBvvO8R0rZ9ytTPzJErTcYidfn6Dg6ePhrfRf1UukRS2Wz7AwvTr-PQ%3D%3D?uid=0&filename=2%203.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        bot.send_photo(message.chat.id, photo_url1)
        bot.send_photo(message.chat.id, photo_url2)
        bot.send_photo(message.chat.id, photo_url3)
    elif message.text == '3 корпус':
        photo_url1 = 'https://downloader.disk.yandex.ru/preview/f9030c218a734b14e73e77b781744a78e2fca3e99ef280c17fd39a5f85526e91/66d07f06/EMvyWi1VnWqKIPgFat_WBHhwr_zdMCMDU5DYxUz4sNxL6xDJvekEgKbp343aUMt97ofzR-7iFLJCqDraKGmFEA%3D%3D?uid=0&filename=3%201.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url2 = 'https://downloader.disk.yandex.ru/preview/2cbba51216a294dce67da79f81a8b2aebfe6f415c22fdfe272064f08f3ac32fb/66d07f06/qcwyH2K65jQs5a8kIpSKb99Dvyn6Y0seNM5DYp-S5_psKNdENYNJCcBNqqLGrcuDCcz1wossNzhVky3WMUu0UA%3D%3D?uid=0&filename=3%202.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url3 = 'https://downloader.disk.yandex.ru/preview/1c77c2fb61e3f49ae093a9fb49e6eefdaace31711fab94aa13c8f8459ca96ddc/66d07f06/WaM8Ix9ey5S-DYDVE5U8O47Z-gFUdCRQby5xiQYO61cNWYcFuD9SrLKMXyqEEqKPpFaWrGmMKyyLuSGpGEqrCw%3D%3D?uid=0&filename=3%203.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url4 = 'https://downloader.disk.yandex.ru/preview/909b56c97a33008ec1c11d91c010b5f1cb8a3439d3e3b8df8c335a641407d558/66d07f06/b659Np8V33xMytpPzRoAS1wBjBPLSpDvlS00U9B__-ZUKfwqTi6n4BsjF1DS8TnZm-te1JP5yqD8Txo-jGRpIg%3D%3D?uid=0&filename=3%204.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url6 = 'https://downloader.disk.yandex.ru/preview/bdf375b62df54b14d2d271e2cc6bf065f2aa5c31daeedd9026bcaa5bdb63dbce/66d07f06/JpCGagTnCEjtOHMa59KeaI7Z-gFUdCRQby5xiQYO61f_hbF3_-pYnMw9xth3EbTS9NrYDkVBzEQ0iaHcdAawYw%3D%3D?uid=0&filename=3%206.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        bot.send_photo(message.chat.id, photo_url1)
        bot.send_photo(message.chat.id, photo_url2)
        bot.send_photo(message.chat.id, photo_url3)
        bot.send_photo(message.chat.id, photo_url4)
        bot.send_photo(message.chat.id, photo_url6) 
    elif message.text == '5 корпус':
        photo_url1 = 'https://downloader.disk.yandex.ru/preview/042b168b79d4f3b44781c397304cd0b520b8e4553085bf8a896563a6cf699918/66d08033/OJCrF80ixS20aeoZzH56CN9Dvyn6Y0seNM5DYp-S5_oNyjZ5aUdrqCufJ2_YUAcjsOdopbzv269THorDM9FcJg%3D%3D?uid=0&filename=5к1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url2 = 'https://downloader.disk.yandex.ru/preview/0466c7e1fcd8898b064542223d362f74f13ab516ad1f315176e312b6ac6eee97/66d08033/Yzj14uQqv7N_bfOJ5pN2DPp_LoJYD06IHAWIzFVIxTx3w39rCl3imsgv1B9PM92xIFfJIKCKqoFbWl2Wx3OX6w%3D%3D?uid=0&filename=5к2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url3 = 'https://downloader.disk.yandex.ru/preview/d23b590b438368ef36628b03d13cb745930f1071507d0e0fe6b6680631618615/66d08033/V3MsnS0IewIc79AWDJspL99Dvyn6Y0seNM5DYp-S5_rlnEkaz7zE9962yjJ2d1DYUe85o9ABusHd5U7Wy7S0kw%3D%3D?uid=0&filename=5к3.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url4 = 'https://downloader.disk.yandex.ru/preview/794bc90595ee448bdc80edc2a460fc03117c776bedcb2e1e4d81b954cd94a4c3/66d08033/JpCGagTnCEjtOHMa59KeaI7Z-gFUdCRQby5xiQYO61eO4sXjhA3g9lGFRu8cZ7brpP9iU1RKINmSxkWdYaNdpQ%3D%3D?uid=0&filename=5к4.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url5 = 'https://downloader.disk.yandex.ru/preview/be8082fe05dd76d3b835689309134668deae7d1bacb2f03ebf522756de0e42cd/66d08033/G9KdEg7ytbGsHcXTjMcF4fp_LoJYD06IHAWIzFVIxTxyfvYuWyNJuxqepCHU_h_9IZklKUGIQ2fj1y6--EgINA%3D%3D?uid=0&filename=5к5.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        photo_url6 = 'https://downloader.disk.yandex.ru/preview/d9000d1cb632ce1771e7792680ee8c0ce3567727e267c9a628a57e708ad06db8/66d08033/H77UmI6lQDfvJMXj-Uk0WuhIzq6lq1-Lsed8NONxOhVgbiGI4sKWk_ZDPwsdnzMGXQ30K29aWGP9jUQtkzmirg%3D%3D?uid=0&filename=5к6.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1552x784'
        bot.send_photo(message.chat.id, photo_url1)
        bot.send_photo(message.chat.id, photo_url2)
        bot.send_photo(message.chat.id, photo_url3)
        bot.send_photo(message.chat.id, photo_url4)
        bot.send_photo(message.chat.id, photo_url5)
        bot.send_photo(message.chat.id, photo_url6)
    elif message.text == '❌ 6 корпус':
        photo_url = 'https://gas-kvas.com/grafic/uploads/posts/2023-10/1696438352_gas-kvas-com-p-kartinki-smailik-radostnii-26.jpg'
        bot.send_photo(message.chat.id, photo_url)  
    elif message.text == '❌ Копировальные центры 🖨':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == '❌ Банкоматы 💵':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == '❌ Мед. центр 💉':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == '❌ Деканат ИПНБ 👨‍🎓':
        photo_url = "https://avatars.mds.yandex.net/i?id=16789175f2b2e461eb3f9f87b5784de5_l-4230909-images-thumbs&n=13"
        bot.send_photo(message.chat.id, photo_url)
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == '❌ Где поесть? 🥐':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == 'Книжные магазины 📚':
        bot.send_message(message.chat.id, 'Корпуса 1, 2, 5, 6 – 1-й этаж\n\nВ этих же магазинах можно купить продукцию с символикой академии (мерчи, значки, и т.д.)')
    elif message.text == '❌ Военно-учетный стол 🔫':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == '❌ Платная парковка 🚗':
        bot.send_message(message.chat.id, 'Скоро здесь появится информация!')
    elif message.text == 'Библиотеки 📗':
        bot.send_message(message.chat.id, '1 корпус, 9 этаж\n5 корпус, 2 этаж\n\nБиблиотеку могут использовать все студенты академии, вне зависимости от  формы обучения. Для этого  нужно  предоставить администратору карту авторизации. При этом нужно заранее заказать книгу через личный кабинет, либо в специальном терминале, который находиться в библиотеке.\n\nВ 5 корпусе есть компьютерный класс. Каждый студент может воспользоваться отдельным компьютером с персональной системой. Тот же рабочий стол у вас будет и на информатике.')
    elif message.text == 'Тех. поддержка ⚙️':
        bot.send_message(message.chat.id, 'При желании помочь с реализацией бота обращайтесь в личные сообщения @b0drov\n\nСделано ИПНБ для студентов ❤️')

        
# Запуск бота и планировщика задач
def main():
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)
            time.sleep(15)
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()