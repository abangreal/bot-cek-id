import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ini catatan untuk sistem agar mencatat jika ada eror
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ini "Otak" bot. Fungsi ini yang mengatur apa yang harus dijawab bot
async def balas_id_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Mengambil data orang yang mengirim pesan ke bot
    pengirim = update.effective_user
    
    # Menyusun pesan balasan teks rapi menggunakan HTML
    pesan_balasan = (
        f"<b>✨ INFORMASI ID KAMU ✨</b>\n\n"
        f"🆔 <b>ID Telegram:</b> <code>{pengirim.id}</code>\n"
        f"👤 <b>Nama:</b> {pengirim.first_name}\n\n"
        f"<i>Tip: Ketuk nomor ID di atas untuk menyalin otomatis!</i>"
    )
    
    # Menyuruh bot mengirimkan balasan teks di atas ke pengguna
    await update.message.reply_text(pesan_balasan, parse_mode="HTML")

def main():
    # GANTI TULISAN DI BAWAH INI DENGAN TOKEN DARI BOTFATHER KAMU
    TOKEN = '8714004006:AAEacRm_9C6FxBr5b374Sa7p1MiZq1ASkX4'
    
    # Membangun jembatan penghubung bot
    application = Application.builder().token(TOKEN).build()

    # Jika pengguna mengetik /start, jalankan fungsi balas_id_user
    application.add_handler(CommandHandler("start", balas_id_user))
    
    # Jika pengguna mengetik pesan teks apa saja selain /start, tetap jalankan fungsi balas_id_user
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas_id_user))

    # Jalankan bot sekarang!
    print("Bot kamu sudah bangun dan siap bekerja... Hubungi bot kamu di Telegram sekarang!")
    application.run_polling()

if __name__ == '__main__':
    main()
