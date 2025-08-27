from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Help Center</b>\n\n"
        "မင်္ဂလာပါ! ကျွန်ုပ် Pivot ဖြစ်ပါတယ်။ မြန်မာစီးပွားရေးလုပ်ငန်းများအတွက် သတင်းအချက်အလက်လုံခြုံရေးနှင့် ဥပဒေလိုက်နာမှုဆိုင်ရာ အကြံဉာဏ်များ ပေးနိုင်ပါတယ်။\n\n"
        "ကျွန်ုပ်သည် Cyber Law၊ PDPA (Personal Data Protection Act), ISO 27001 စသည့် လိုက်နာမှုလိုအပ်ချက်များနှင့် အွန်လိုင်းခြိမ်းခြောက်မှုများ (Phishing, Scam စသည်) အကြောင်း အလွယ်တကူ နားလည်နိုင်စွမ်းဖြင့် ဖော်ပြပေးနိုင်ပါတယ်။\n\n"
        "ယနေ့တွင် သင့်အား မည်သို့ကူညီရမည်နည်းကို မေးမြန်းနိုင်ပြီး သင်လိုချင်သည့် သတင်းအချက်အလက်လုံခြုံရေး၊ PDPA လိုက်နာမှု၊    ဘ်ဆိုက်လုံခြုံရေး သို့မဟုတ် အခြား မေးခွန်းများအတွက် ညွှန်ကြားချက်များ ရနိုင်ပါသည်။\n\n"
        "💡 <b>Pivot Guide:</b> You can ask me anything about Cyber Laws, Data Protection, Website Security, or any related topic and I will provide step-by-step guidance!"
    )
    image_url = "https://pivotaimm.vercel.app/logo.png"  # Replace with your image URL

    await update.message.reply_photo(
        photo=image_url,
        caption=text,
        parse_mode='HTML'
    )
    
