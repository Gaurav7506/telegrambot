import telebot

API_KEY = "API_KEY"

bot = telebot.TeleBot(API_KEY)

earthquake_points = 0
flood_points = 0
tsunami_points = 0
wildfire_points = 0

@bot.message_handler(commands=['start', 'new_user'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /info \n /help \n /status \n /types")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot created using the telebot library.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")

@bot.message_handler(commands=['types'])
def types(message):
    bot.reply_to(message, """
    1. EARTHQUAKE
2. FLOODS
3. TSUNAMIS
4. WILD FIRES
                 """)

@bot.message_handler(func=lambda message: message.text == '1' and message.chat.type == 'private')
def earthquake_info(message):
    global earthquake_points
    earthquake_points += 1  # Increment points by 1
    # Add more points
    earthquake_points += 5  # Increment points by 5
    earthquake_points += 10  # Increment points by 10
    bot.reply_to(message, """Steps to follow during an Earthquake:
1. Identify safe spots in your surroundings.
2. Prepare an emergency kit.
3. Develop an emergency plan.
4. Consider Earthquake insurance.
5. Stay calm and be mindful of building materials.""")

@bot.message_handler(func=lambda message: message.text == '2' and message.chat.type == 'private')
def flood_info(message):
    global flood_points
    flood_points += 1
    flood_points += 5
    flood_points += 10
    bot.reply_to(message, """Steps to follow during a Flood:
1. Secure outdoor items.
2. Maintain drainage systems.
3. Be prepared to evacuate.
4. Check your getaway kit.
5. Listen to your local stations for updates.""")

@bot.message_handler(func=lambda message: message.text == '3' and message.chat.type == 'private')
def tsunami_info(message):
    global tsunami_points
    tsunami_points += 1
    tsunami_points += 5
    tsunami_points += 10
    bot.reply_to(message, """Steps to follow during a Tsunami:
1. Identify a safe zone.
2. Know the risks.
3. Learn the signs of a tsunami.
4. Anchor heavy objects.
5. Practice tsunami drills.""")

@bot.message_handler(func=lambda message: message.text == '4' and message.chat.type == 'private')
def wildfire_info(message):
    global wildfire_points
    wildfire_points += 1
    wildfire_points += 5
    wildfire_points += 10
    bot.reply_to(message, """Steps to follow during a Wildfire:
1. Use fire-resistant materials.
2. Have a fire escape plan.
3. Create a defensible space.
4. Install smoke detectors.
5. Avoid wearing flammable clothing.""")

@bot.message_handler(func=lambda message: True)
def welcome(message):
    bot.reply_to(message, "Welcome to the crisis-ready bot.")

print("Hey,i am up....")
bot.polling()