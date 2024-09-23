import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurar el registro de errores
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envíar un mensaje de inicio al usuario cuando usa el comando /start."""
    await update.message.reply_text('¡Hola! Soy tu bot de AlmaMatch.')

def main():
    """Inicio del bot."""
    application = ApplicationBuilder().token("7285036779:AAEebqHsHuOQcaw5W8NBQinWxieeRg_tuJM").build()

    # Añadir el manejador de comandos
    application.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
