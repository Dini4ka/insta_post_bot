import time
import sys, traceback
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from insta_post_bot import instabot, BOT
from mouse_coordinates import getting_coordinates
from connect_to_google_disk import check_new_files
from aiogram.utils import executor


bot = Bot(token='1584254213:AAGr7iEilj9n_afn0Bplu_ASVJKbanS2mVc')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Начинаем наш диалог
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Hello! First of all we should make some settings.\nType /get_coordinates for start settings")

@dp.message_handler(commands=['get_coordinates'])
async def cmd_start(message: types.Message):
    await message.answer('wait a little bit, untill u see opend folder')
    BOT.set_up()
    BOT.go_home()
    await message.answer('please put ur cursor on the field for writing \n and write me /get_cursor_coordinates_field')

@dp.message_handler(commands=['get_cursor_coordinates_field'])
async def cmd_start(message: types.Message):
    getting_coordinates()
    await message.answer('Thank u much! please put ur cursor on the button "send"  \n and write me /get_cursor_coordinates_button')

@dp.message_handler(commands=['get_cursor_coordinates_button'])
async def cmd_start(message: types.Message):
    getting_coordinates()
    await message.answer('Thank u much! Bot is starting work')
    time_to_post = 60 * 180
    await message.answer('checking images')
    check_new_files()
    await message.answer('checking is done')
    count_of_posts = len(open('downloaded_files.txt').readlines())
    print(count_of_posts)
    for i in range(count_of_posts):
        try:
            # check new files on google_disk
            await message.answer('checking images')
            new_images = check_new_files()
            if new_images == 0:
                await message.answer('checking is done')
            else:
                count_of_posts += new_images
                await message.answer('find ' + new_images + ' new images')
            text = 'Quiz #' + '['+str(i+1)+']' + ', test your self with this random question. Write your answer in the comments section. Share with friends to make this exciting.\n\
                   #upsc #ias #xpertifyu #history #pcs #ssc #ips\nCheck www.xpertso.com to see other questions like this.'
            way_to_image = open('downloaded_files.txt').readlines()[i]
            a = datetime.datetime.now().hour
            time_to_rest = [23, 24, 0, 1, 2, 3, 4, 5, 6]
            while (a in time_to_rest):
                a = datetime.datetime.now().hour
            BOT.make_posts(way_to_image, text)
            await message.answer(str(i+1) + ' image was publicated')
            time.sleep(time_to_post)
        except:
            await  message.answer('there is problem, trying to fix it...')
            # check new files on google_disk
            count_of_posts += check_new_files()
            text = 'Quiz #' + '[' + str(i + 1) + ']' + ', test your self with this random question. Write your answer in the comments section. Share with friends to make this exciting.\n\
                               #upsc #ias #xpertifyu #history #pcs #ssc #ips\nCheck www.xpertso.com to see other questions like this.'
            way_to_image = open('downloaded_files.txt').readlines()[i]
            a = datetime.datetime.now().hour
            time_to_rest = [23, 24, 0, 1, 2, 3, 4, 5, 6]
            while (a in time_to_rest):
                a = datetime.datetime.now().hour
            BOT.make_posts(way_to_image, text)
            await message.answer('problem is solvec')
            await message.answer(str(i+1) + ' image was publicated')
            time.sleep(time_to_post)

def telegram_polling():
    try:
        executor.start_polling(dp,skip_updates=True) #constantly get messages from Telegram
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()