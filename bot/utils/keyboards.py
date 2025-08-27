"""
Keyboard utilities for creating inline and reply keyboards
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from typing import List


class InlineKeyboards:
    """Utility class for creating inline keyboards"""

    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        """Create main menu inline keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("❓ How to Use", callback_data="help"),
                InlineKeyboardButton("⚡ Better Performance", callback_data="status")
                
            ],
            [
                InlineKeyboardButton("📚 About RAG", callback_data="about_rag"),
                InlineKeyboardButton("💡 Examples", callback_data="examples")
            ],
            
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def help_menu() -> InlineKeyboardMarkup:
        """Create help menu inline keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

 

    @staticmethod
    def confirmation_menu(action: str) -> InlineKeyboardMarkup:
        """Create confirmation menu for destructive actions"""
        keyboard = [
            [
                InlineKeyboardButton("✅ Yes", callback_data=f"confirm_{action}"),
                InlineKeyboardButton("❌ No", callback_data="settings")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def back_button(callback_data: str = "main_menu") -> InlineKeyboardMarkup:
        """Create a simple back button"""
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data=callback_data)]]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def examples_menu() -> InlineKeyboardMarkup:
        """Create examples menu inline keyboard"""
        keyboard = [
             [
            InlineKeyboardButton("💻 What is Phishing?", callback_data="example_phishing"),
            InlineKeyboardButton("🔒 How to protect data?", callback_data="example_data_protection")
        ],
        [
            InlineKeyboardButton("📧 What is PDPA?", callback_data="example_pdpa"),
            InlineKeyboardButton("🛡️ What is Cyber Law?", callback_data="example_cyberlaw")
        ],
        [
            InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
        ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def status_menu() -> InlineKeyboardMarkup:
        """Create status menu with external links"""
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("📱 Android App", url="https://play.google.com/store/apps/details?id=your.app.id")],
            [InlineKeyboardButton("🌐 Web Version", url="https://pivot1.vercel.app/chat")],
            [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
        ])


class ReplyKeyboards:
    """Utility class for creating reply keyboards"""

    @staticmethod
    def main_menu() -> ReplyKeyboardMarkup:
        """Create main menu reply keyboard"""
        keyboard = [
            ["❓ How to Use"],
            ["📚 About RAG", "💡 Examples"],
            ["⚡ Best Performance"],  # Added Status here
            
        ]
        return ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=False,
            input_field_placeholder="Choose an option or type your question..."
        )

    @staticmethod
    def quick_actions() -> ReplyKeyboardMarkup:
        """Create quick actions reply keyboard"""
        keyboard = [
            ["🆘 Help", "⚙️ Settings"],
            ["📋 Menu", "❌ Hide Keyboard"]
        ]
        return ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=True
        )


class KeyboardUtils:
    """General keyboard utilities"""

    @staticmethod
    def create_inline_keyboard(buttons: List[List[dict]]) -> InlineKeyboardMarkup:
        """
        Create inline keyboard from button configuration

        Args:
            buttons: List of button rows, each containing button configs
                     Format: [{"text": "Button Text", "callback_data": "data"}]
        """
        keyboard = []
        for row in buttons:
            keyboard_row = []
            for button in row:
                keyboard_row.append(
                    InlineKeyboardButton(
                        text=button["text"],
                        callback_data=button.get("callback_data"),
                        url=button.get("url")
                    )
                )
            keyboard.append(keyboard_row)
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def create_reply_keyboard(buttons: List[List[str]], **kwargs) -> ReplyKeyboardMarkup:
        """
        Create reply keyboard from button text

        Args:
            buttons: List of button rows, each containing button text
            **kwargs: Additional ReplyKeyboardMarkup parameters
        """
        return ReplyKeyboardMarkup(
            buttons,
            resize_keyboard=kwargs.get("resize_keyboard", True),
            one_time_keyboard=kwargs.get("one_time_keyboard", False),
            input_field_placeholder=kwargs.get("input_field_placeholder")
        )
