from vkbottle import Bot
import random

bot = Bot(token='ВАШ ТОКЕН')


@bot.on.message(text="играть")
async def start_game(message):
    await message.answer("Давай сыграем! Напиши Камень, Ножницы или Бумага.")


@bot.on.message()
async def game(message):
    user_choice = message.text.lower()
    choices = ['камень', 'ножницы', 'бумага']

    if user_choice not in choices:
        await message.answer("Пожалуйста, выбери 'Камень', 'Ножницы' или 'Бумага'.")
        return

    bot_choice = random.choice(choices)
    await message.answer(f"Я выбрал: {bot_choice.capitalize()}.")

    if user_choice == bot_choice:
        await message.answer("Ничья!")
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
            (user_choice == 'ножницы' and bot_choice == 'бумага') or \
            (user_choice == 'бумага' and bot_choice == 'камень'):
        await message.answer("Ты выиграл!")
    else:
        await message.answer("Я выиграл!")


bot.run_forever()

#WARNING EXCEPTION - @warningexception