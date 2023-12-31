from Oristella import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Oristella.utils.lang import *

fbuttons = InlineKeyboardMarkup(
        [InlineKeyboardButton(text="Support Chat", url=f"https://t.me/OristellaSupport"),
        InlineKeyboardButton(text="News Channel", url=f"https://t.me/Oristella_updates")],
        [InlineKeyboardButton(text="Help", callback_data="bot_commands")],
        [InlineKeyboardButton(text="languages ", callback_data="_langs")]]),
        [InlineKeyboardButton("Back", callback_data='startcq')]])

keyboard =InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")],
     [InlineKeyboardButton(text="🇱🇰 සිංහල", callback_data="languages_si"), 
      InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages_hi")], 
     [InlineKeyboardButton(text="🇮🇹 Italiano", callback_data="languages_it"), 
      InlineKeyboardButton(text="🇮🇳 తెలుగు", callback_data="languages_ta")], 
     [InlineKeyboardButton(text="🇮🇩 Indonesia", callback_data="languages_id"), 
      InlineKeyboardButton(text="🇦🇪 عربي", callback_data="languages_ar")], 
     [InlineKeyboardButton(text="🇮🇳 മലയാളം", callback_data="languages_ml"),
           InlineKeyboardButton(text="🇲🇼 Chichewa", callback_data="languages_ny")],
      [InlineKeyboardButton(text="🇮🇳 Mizo", callback_data="languages_lus"), 
     [InlineKeyboardButton(text="🇩🇪 German", callback_data="languages_ge")], 
      InlineKeyboardButton(text="🇷🇺 Russian", callback_data="languages_ru"), 
     [InlineKeyboardButton(text="🇮🇳 Hmar", callback_data="languages_hmr")],
      [InlineKeyboardButton(text="🇮🇳 Lai", callback_data="languages_cnh"),
     [InlineKeyboardButton(text="🇮🇳 Mara", callback_data="languages_mrh")],
      [InlineKeyboardButton(text="🇮🇳 Thahdou/Kuki", callback_data="languages_tcz"),
     [InlineKeyboardButton("Back", callback_data='startcq')]])

@app.on_callback_query(filters.regex("langus"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(text= "Choose Your languages:",reply_markup=keyboard,disable_web_page_preview=True)
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(text=_["menu"],reply_markup=fbuttons,disable_web_page_preview=True)

