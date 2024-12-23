import requests

def get_username(bot_token, user_id):
    """
    Telegram Bot API orqali foydalanuvchining username'ini aniqlaydi.
    :param bot_token: Bot uchun token (Telegram orqali olinadi)
    :param user_id: Foydalanuvchining ID'si
    :return: Username yoki xato haqida xabar
    """
    try:
        # Bot API orqali getChat usulini chaqiramiz
        url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={user_id}"
        response = requests.get(url)
        data = response.json()

        if data["ok"]:
            return data["result"].get("username", "Username mavjud emas")
        else:
            return f"Xato: {data['description']}"
    except Exception as e:
        return f"Xato yuz berdi: {e}"

# Foydalanish uchun misol
bot_token = "7172634152:AAEixzwsB8btZaVm6gkMbriveEqFPS84AHg"  # Bu yerga bot tokenini kiriting
user_id = 5185781945  # Bu yerga tekshiriladigan userID ni kiriting

username = get_username(bot_token, user_id)
print(f"Foydalanuvchining username'i: @{username}")
