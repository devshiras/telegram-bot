from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Initialize Logging for Error Handling
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the bot token from BotFather
TOKEN = '7914008264:AAHYQKcxRijxAKtYqQa66T0VDW-ApxldtYw'

# Profile Image URL
PROFILE_IMAGE_URL = "https://i.imgur.com/Dusr1ye.jpeg"

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message and profile image."""
    user = update.effective_user
    await update.message.reply_photo(photo=PROFILE_IMAGE_URL)
    await update.message.reply_text(
        f"Welcome, {user.first_name}! Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Provide help information with available commands."""
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List available commands\n"
        "/command1 - Execute command 1\n"
        "/command2 - Execute command 2\n"
        "/command3 - Execute command 3"
    )

async def command1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle command1."""
    await update.message.reply_text("You executed Command 1!")

async def command2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle command2."""
    await update.message.reply_text("You executed Command 2!")

async def command3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle command3."""
    await update.message.reply_text("You executed Command 3!")

# Error Handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log and send an error message to the user."""
    logger.error(f"Update {update} caused error {context.error}")
    if update.message:
        await update.message.reply_text(
            "An unexpected error occurred. Please try again later."
        )

# Main Function to Set Up Handlers and Start the Bot
def main() -> None:
    """Run the bot."""
    application = Application.builder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("command1", command1))
    application.add_handler(CommandHandler("command2", command2))
    application.add_handler(CommandHandler("command3", command3))

    # Error handler
    application.add_error_handler(error)

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()