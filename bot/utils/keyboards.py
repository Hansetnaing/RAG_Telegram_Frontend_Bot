"""
Keyboard utilities for creating inline and reply keyboards
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from typing import List


class InlineKeyboards:
    """Utility class for creating inline keyboards"""

    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        """Create main menu inline keyboard in Burmese"""
        keyboard = [
            [
                InlineKeyboardButton("📝 စာသားဖြင့် မေးမြန်းခြင်း", callback_data="text_usage"),
                InlineKeyboardButton("📂 ဖိုင်များဖြင့် မေးမြန်းခြင်း", callback_data="file_usage")
            ],
            [
                InlineKeyboardButton("🎤 အသံဖြင့် မေးမြန်းခြင်း", callback_data="voice_usage"),
                InlineKeyboardButton("ℹ️ ရည်ရွယ်ချက်", callback_data="purpose")
            ],
            [
                InlineKeyboardButton("📱 ပိုကောင်းတဲ့ အတွေ့အကြုံ", callback_data="better_experience")
            ]
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
    def cybersecurity_menu() -> InlineKeyboardMarkup:
        """Create cybersecurity submenu"""
        keyboard = [
            [
                InlineKeyboardButton("🎯 Threat Assessment", callback_data="cyber_threats"),
                InlineKeyboardButton("🛡️ Security Policies", callback_data="cyber_policies")
            ],
            [
                InlineKeyboardButton("👥 Employee Training", callback_data="cyber_training"),
                InlineKeyboardButton("🚨 Incident Response", callback_data="cyber_incident")
            ],
            [
                InlineKeyboardButton("📋 Compliance Frameworks", callback_data="cyber_compliance"),
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def legal_menu() -> InlineKeyboardMarkup:
        """Create legal compliance submenu"""
        keyboard = [
            [
                InlineKeyboardButton("🏢 Business Setup", callback_data="legal_business"),
                InlineKeyboardButton("📄 Contracts", callback_data="legal_contracts")
            ],
            [
                InlineKeyboardButton("💡 Intellectual Property", callback_data="legal_ip"),
                InlineKeyboardButton("📊 Regulations", callback_data="legal_regulations")
            ],
            [
                InlineKeyboardButton("👨‍💼 Employment Law", callback_data="legal_employment"),
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def privacy_menu() -> InlineKeyboardMarkup:
        """Create privacy & data protection submenu"""
        keyboard = [
            [
                InlineKeyboardButton("🇪🇺 GDPR Compliance", callback_data="privacy_gdpr"),
                InlineKeyboardButton("🇸🇬 PDPA Requirements", callback_data="privacy_pdpa")
            ],
            [
                InlineKeyboardButton("📋 Privacy Policies", callback_data="privacy_policies"),
                InlineKeyboardButton("🗺️ Data Mapping", callback_data="privacy_mapping")
            ],
            [
                InlineKeyboardButton("✅ Consent Management", callback_data="privacy_consent"),
                InlineKeyboardButton("🚨 Breach Response", callback_data="privacy_breach")
            ],
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def quick_actions_menu() -> InlineKeyboardMarkup:
        """Create quick actions submenu"""
        keyboard = [
            [
                InlineKeyboardButton("📋 GDPR Checklist", callback_data="template_gdpr_checklist"),
                InlineKeyboardButton("🔒 Security Audit", callback_data="template_security_audit")
            ],
            [
                InlineKeyboardButton("🏢 Startup Legal Kit", callback_data="template_startup_legal"),
                InlineKeyboardButton("📄 Privacy Policy", callback_data="template_privacy_policy")
            ],
            [
                InlineKeyboardButton("📊 DPA Template", callback_data="template_dpa"),
                InlineKeyboardButton("🚨 Incident Report", callback_data="template_incident")
            ],
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def emergency_menu() -> InlineKeyboardMarkup:
        """Create emergency response submenu"""
        keyboard = [
            [
                InlineKeyboardButton("🚨 Data Breach Guide", callback_data="emergency_breach"),
                InlineKeyboardButton("⚠️ Cyber Attack Response", callback_data="emergency_attack")
            ],
            [
                InlineKeyboardButton("📞 Legal Emergency", callback_data="emergency_legal"),
                InlineKeyboardButton("🔍 Compliance Violation", callback_data="emergency_compliance")
            ],
            [
                InlineKeyboardButton("🏠 Back to Main", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def better_apps_menu() -> InlineKeyboardMarkup:
        """Create better apps menu with external links"""
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("📱 Mobile App", url="https://play.google.com/store/apps/details?id=your.app.id")],
            [InlineKeyboardButton("🌐 Web Version", url="https://pivot1.vercel.app/chat")],
            [InlineKeyboardButton("💡 Why Better?", callback_data="why_better_apps")],
            [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
        ])


class ReplyKeyboards:
    """Utility class for creating reply keyboards"""

    @staticmethod
    def main_menu() -> ReplyKeyboardMarkup:
        """Create main menu reply keyboard in Burmese"""
        keyboard = [
            ["📝 စာသားဖြင့် မေးမြန်းခြင်း", "📂 ဖိုင်များဖြင့် မေးမြန်းခြင်း"],
            ["🎤 အသံဖြင့် မေးမြန်းခြင်း", "ℹ️ ရည်ရွယ်ချက်"],
            ["📱 ပိုကောင်းတဲ့ အတွေ့အကြုံ"],
            ["📋 Menu", "❌ Hide Keyboard"]
        ]
        return ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=False,
            input_field_placeholder="ဘာမေးခွန်းမေးနိုင်ပါတယ်..."
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
