"""
Enhanced menu command handler for Legal Compliance & Cybersecurity RAG Bot
Specialized for SMEs and Startups
"""

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards, ReplyKeyboards


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /menu command - show main navigation menu in Burmese"""
    text = (
        "🤖 <b>Pivot AI Assistant</b>\n\n"
        "မင်္ဂလာပါ! ကျွန်ုပ် Pivot AI ဖြစ်ပါတယ်။\n\n"
        "📝 <b>စာသားဖြင့် မေးမြန်းခြင်း</b> - တိုက်ရိုက်စာရိုက်ပြီး မေးနိုင်ပါတယ်\n"
        "📂 <b>ဖိုင်များဖြင့် မေးမြန်းခြင်း</b> - PDF, DOCX, TXT ဖိုင်များ upload လုပ်နိုင်ပါတယ်\n"
        "🎤 <b>အသံဖြင့် မေးမြန်းခြင်း</b> - အသံပေးပြီး မေးနိုင်ပါတယ်\n"
        "ℹ️ <b>ရည်ရွယ်ချက်</b> - ဘာအတွက် အသုံးပြုရမလဲ\n"
        "📱 <b>ပိုကောင်းတဲ့ အတွေ့အကြုံ</b> - Website နဲ့ Mobile App\n\n"
        "<i>💡 အကြံပြုချက်: တိုက်ရိုက်မေးခွန်းရိုက်နိုင်ပါတယ် သို့မဟုတ် အောက်က menu ကိုအသုံးပြုပါ</i>"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    )


async def show_reply_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show reply keyboard menu with quick actions"""
    text = (
        "⚡ <b>Quick Access Menu</b>\n\n"
        "Use the buttons below for instant access to common compliance tasks!\n\n"
        "🔍 <b>Quick Checks:</b> GDPR, PDPA, Cyber threats\n"
        "📋 <b>Templates:</b> Privacy policies, security checklists\n"
        "🆘 <b>Emergency:</b> Data breach response\n\n"
        "💡 <i>You can also type any question directly.</i>"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=ReplyKeyboards.main_menu(),
        parse_mode='HTML'
    )


async def hide_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hide the reply keyboard"""
    await update.message.reply_text(
        "✅ Keyboard hidden. Bring it back with /keyboard or /menu",
        reply_markup=ReplyKeyboardRemove()
    )


async def handle_reply_keyboard_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle reply keyboard button presses for legal & cyber security actions"""
    text = update.message.text
    
    # Map reply keyboard buttons to actions
    button_actions = {
        "📝 စာသားဖြင့် မေးမြန်းခြင်း": show_text_usage,
        "📂 ဖိုင်များဖြင့် မေးမြန်းခြင်း": show_file_usage,
        "🎤 အသံဖြင့် မေးမြန်းခြင်း": show_voice_usage,
        "ℹ️ ရည်ရွယ်ချက်": show_purpose,
        "📱 ပိုကောင်းတဲ့ အတွေ့အကြုံ": show_better_experience,
        "📋 Menu": menu_command,
        "❌ Hide Keyboard": hide_keyboard
    }
    
    # Check if the message matches any reply keyboard button
    if text in button_actions:
        await button_actions[text](update, context)
        return True
    
    return False


async def show_text_usage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show how to use text input"""
    text = (
        "📝 <b>စာသားဖြင့် မေးမြန်းခြင်း</b>\n\n"
        "အလွယ်ကူဆုံး နည်းလမ်းဖြစ်ပါတယ်:\n\n"
        "• တိုက်ရိုက် မေးခွန်းရိုက်ပြီး ပို့လိုက်ပါ\n"
        "• ဘာသာရပ်မရွေး မေးနိုင်ပါတယ်\n"
        "• ရှည်လျားတဲ့ မေးခွန်းတွေလည်း မေးနိုင်ပါတယ်\n"
        "• အမြန်ဆုံး ဖြေကြားပေးနိုင်ပါတယ်\n\n"
        "<b>ဥပမာ:</b>\n"
        "• \"Python ဘယ်လို သင်ရမလဲ?\"\n"
        "• \"Business plan ဘယ်လို ရေးရမလဲ?\"\n"
        "• \"AI အကြောင်း ရှင်းပြပါ\"\n\n"
        "💡 <i>ယခုပင် မေးကြည့်ပါ!</i>"
    )

    # Send the image first
    await update.message.reply_photo(
        photo="https://pivotaimm.vercel.app/ask.jpg",
        caption=text,
        parse_mode="HTML"
    )


async def show_file_usage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show how to use file upload"""
    text = (
        "📂 <b>ဖိုင်များဖြင့် မေးမြန်းခြင်း</b>\n\n"
        "ဖိုင်များကို upload လုပ်ပြီး သုံးနိုင်ပါတယ်:\n\n"
        "📄 <b>PDF ဖိုင်များ</b> - စာရွက်စာတမ်းများ\n"
        "📝 <b>DOCX ဖိုင်များ</b> - Word documents\n"
        "📋 <b>TXT ဖိုင်များ</b> - Text files\n\n"
        "<b>အသုံးပြုနည်း:</b>\n"
        "1️⃣ ဖိုင်ကို attach လုပ်ပါ\n"
        "2️⃣ ဖိုင်နဲ့ ပတ်သက်တဲ့ မေးခွန်းမေးပါ\n"
        "3️⃣ AI က ဖိုင်ထဲက အကြောင်းအရာကို ဖတ်ပြီး ဖြေပါမယ်\n\n"
        "<b>ဥပမာ:</b>\n"
        "• \"ဒီ PDF ကို အကျဉ်းချုပ်ပေးပါ\"\n"
        "• \"ဒီစာရွက်ထဲမှာ အဓိက အချက်တွေက ဘာတွေလဲ?\"\n\n"
        "💡 <i>ဖိုင်တစ်ခု upload လုပ်ကြည့်ပါ!</i>"
    )

    # Send the image first
    await update.message.reply_photo(
        photo="https://pivotaimm.vercel.app/chat_with_file.JPG",
        caption=text,
        parse_mode="HTML"
    )


async def show_voice_usage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show how to use voice input"""
    text = (
        "🎤 <b>အသံဖြင့် မေးမြန်းခြင်း</b>\n\n"
        "အသံပေးပြီး မေးခွန်းမေးနိုင်ပါတယ်:\n\n"
        "🎙️ <b>Voice Message</b> - အသံဖိုင်ပို့ပါ\n"
        "🔊 <b>Audio File</b> - အသံဖိုင် upload လုပ်ပါ\n\n"
        "<b>အသုံးပြုနည်း:</b>\n"
        "1️⃣ Microphone ခလုတ်ကို နှိပ်ပါ\n"
        "2️⃣ မေးခွန်းကို အသံပေးပြီး မေးပါ\n"
        "3️⃣ AI က အသံကို စာသားအဖြစ် ပြောင်းပြီး ဖြေပါမယ်\n\n"
        "<b>အားသာချက်များ:</b>\n"
        "• လက်မသုံးပဲ မေးနိုင်တယ်\n"
        "• ရှည်လျားတဲ့ မေးခွန်းတွေ လွယ်ကူတယ်\n"
        "• သဘာဝကျကျ စကားပြောသလို မေးနိုင်တယ်\n\n"
        "💡 <i>Voice message တစ်ခု ပို့ကြည့်ပါ!</i>"
    )

    # Send the image first
    await update.message.reply_photo(
        photo="https://pivotaimm.vercel.app/talk_to_bot.jpg",
        caption=text,
        parse_mode="HTML"
    )


async def show_purpose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the purpose and about information"""
    text = (
        "ℹ️ <b>Pivot AI ရဲ့ ရည်ရွယ်ချက်</b>\n\n"
        "🎯 <b>အဓိက ရည်ရွယ်ချက်:</b>\n"
        "သင့်ရဲ့ မေးခွန်းတွေကို AI နည်းပညာသုံးပြီး အမြန်ဆုံး၊ \n"
        "တိကျဆုံး ဖြေကြားပေးဖို့ ဖြစ်ပါတယ်။\n\n"
        "🤖 <b>AI နည်းပညာ:</b>\n"
        "• RAG (Retrieval-Augmented Generation) သုံးထားပါတယ်\n"
        "• အမြဲတမ်း update ဖြစ်နေတဲ့ အချက်အလက်တွေ\n"
        "• မြန်မာစာ နဲ့ အင်္ဂလိပ်စာ နှစ်မျိုးလုံး support လုပ်ပါတယ်\n\n"
        "🎓 <b>အသုံးပြုနိုင်သူများ:</b>\n"
        "• ကျောင်းသားများ\n"
        "• အလုပ်သမားများ\n"
        "• လုပ်ငန်းရှင်များ\n"
        "• သုတေသီများ\n\n"
        "💡 <i>သင်ဘာမဆို မေးနိုင်ပါတယ်!</i>"
    )

    # Send the logo first
    await update.message.reply_photo(
        photo="https://pivotaimm.vercel.app/logo.png",
        caption=text,
        parse_mode="HTML"
    )


async def show_better_experience(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show better experience with website and mobile app"""
    text = (
        "📱 <b>ပိုကောင်းတဲ့ အတွေ့အကြုံ</b>\n\n"
        "Telegram ထက် ပိုကောင်းတဲ့ features တွေ ရနိုင်ပါတယ်:\n\n"
        "✅ <b>Session သိမ်းဆည်းခြင်း</b> - စကားပြောချက်တွေ မပျောက်ဘူး\n"
        "✅ <b>Message History</b> - အရင်က စကားပြောချက်တွေ ပြန်ကြည့်နိုင်တယ်\n"
        "✅ <b>User Profile</b> - ကိုယ်ပိုင် profile ရှိမယ်\n"
        "✅ <b>File Management</b> - ဖိုင်တွေကို စုစည်းထားနိုင်တယ်\n"
        "✅ <b>Advanced Search</b> - ရှာဖွေမှု ပိုကောင်းတယ်\n"
        "✅ <b>Offline Access</b> - Internet မရှိလည်း အချို့ features သုံးနိုင်တယ်\n\n"
        "🌐 <b>Website:</b> https://pivotaimm.vercel.app\n"
        "📱 <b>Mobile App:</b> https://pivotaimm.vercel.app/pivot.apk\n\n"
        "💡 <i>ပိုကောင်းတဲ့ အတွေ့အကြုံအတွက် Website သို့မဟုတ် App ကို အသုံးပြုပါ!</i>"
    )
    
    await update.message.reply_text(
        text=text,
        parse_mode='HTML'
    )
