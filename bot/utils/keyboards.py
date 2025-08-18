"""
Keyboard utilities for creating inline and reply keyboards
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from typing import List, Optional


class InlineKeyboards:
    """Utility class for creating inline keyboards"""
    
    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        """Create main menu inline keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("❓ Help", callback_data="help"),
                InlineKeyboardButton("⚙️ Settings", callback_data="settings")
            ],
            [
                InlineKeyboardButton("📚 About RAG", callback_data="about_rag"),
                InlineKeyboardButton("💡 Examples", callback_data="examples")
            ],
            [
                InlineKeyboardButton("📊 Usage Stats", callback_data="stats"),
                InlineKeyboardButton("🔄 Restart", callback_data="restart")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def help_menu() -> InlineKeyboardMarkup:
        """Create help menu inline keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("🚀 Getting Started", callback_data="help_getting_started"),
                InlineKeyboardButton("💬 Chat Commands", callback_data="help_commands")
            ],
            [
                InlineKeyboardButton("📋 Features", callback_data="help_features"),
                InlineKeyboardButton("🔧 Troubleshooting", callback_data="help_troubleshooting")
            ],
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def settings_menu() -> InlineKeyboardMarkup:
        """Create settings menu inline keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("🔔 Notifications", callback_data="settings_notifications"),
                InlineKeyboardButton("🌐 Language", callback_data="settings_language")
            ],
            [
                InlineKeyboardButton("📝 Response Style", callback_data="settings_response_style"),
                InlineKeyboardButton("🎯 RAG Settings", callback_data="settings_rag")
            ],
            [
                InlineKeyboardButton("💾 Export Data", callback_data="settings_export"),
                InlineKeyboardButton("🗑️ Clear History", callback_data="settings_clear")
            ],
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
                InlineKeyboardButton("📖 Ask about Documents", callback_data="example_documents"),
                InlineKeyboardButton("🔍 Search Information", callback_data="example_search")
            ],
            [
                InlineKeyboardButton("💡 General Questions", callback_data="example_general"),
                InlineKeyboardButton("🔗 Related Topics", callback_data="example_related")
            ],
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)


class ReplyKeyboards:
    """Utility class for creating reply keyboards"""
    
    @staticmethod
    def main_menu() -> ReplyKeyboardMarkup:
        """Create main menu reply keyboard"""
        keyboard = [
            ["❓ Help", "⚙️ Settings"],
            ["📚 About RAG", "💡 Examples"],
            ["📊 Stats", "🔄 Restart"]
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
