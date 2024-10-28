import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Command handlers
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome! Use /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/start - Welcome message\n'
                              '/help - List commands\n'
                              '/echo <message> - Echo back your message\n'
                              '/time - Current server time\n'
                              '/info - Bot information')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if context.args:
        message = ' '.join(context.args)
        update.message.reply_text(message)
    else:
        update.message.reply_text('Please provide a message to echo. Usage: /echo <message>')

def current_time(update: Update, context: CallbackContext) -> None:
    """Send the current server time."""
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f'Current server time: {now}')

def info(update: Update, context: CallbackContext) -> None:
    """Send bot information."""
    update.message.reply_text('This is a simple Telegram bot example.\n'
                              'Developed using python-telegram-bot library.')

# Error handler
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7914008264:AAHmK63kMCd92TQThVOWqQvGAuIRQslf0eQ")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("echo", echo))
    dispatcher.add_handler(CommandHandler("time", current_time))
    dispatcher.add_handler(CommandHandler("info", info))

    # Register error handler
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()