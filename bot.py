from aiogram import Bot, Dispatcher, executor, types
import logging
import openai
from dotenv import load_dotenv
import os


load_dotenv()


openai.api_key = os.getenv('TOKEN_OpenAI')

def request(text) -> str:
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {'role': 'user', 'content': text}
    ],
    temperature=0,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  answer = str(response["choices"][0]["message"]["content"])
  return answer



def tel_bot():
  bott = Bot(token=os.getenv('TOKEN'))
  bot = Dispatcher(bott)
  #logging.basicConfig(level=logging.INFO)

  @bot.message_handler(content_types=["text"])
  async def text_send(message: types.Message):
    answer = request(message.text)
    await message.bot.send_message(message.chat.id, answer)

  executor.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
  tel_bot()