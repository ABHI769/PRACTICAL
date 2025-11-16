def english_hindi(text):
    translate = {
        "hello": "नमस्ते",
        "goodbye": "अलविदा",
        "please": "कृपया",
        "thankyou": "धन्यवाद",
        "yes": "हाँ",
        "no": "नहीं",
        "maybe": "शायद",
        "water": "पानी",
        "sun": "सूर्य",
        "moon": "चाँद",
        "book": "किताब",
        "computer": "कंप्यूटर",
        "love": "प्यार",
        "friend": "दोस्त",
        "family": "परिवार",
        "beautiful": "सुंदर",
        "ready": "तैयार",
        "work": "काम",
        "hard": "कठिन",
        "easy": "आसान",
        "food": "खाना",
        "drink": "पीना",
        "sleep": "सोना",
        "dream": "सपना",
        "fast": "तेज़",
        "i": "मैं",
        "you": "तुम",
        "he": "वह",
        "she": "वह",
        "it": "यह",
        "we": "हम",
        "they": "वे",
        "are": "हैं",
        "am": "हूँ",
        "or": "या",
        "but": "लेकिन",
        "orange": "संतरा",
        "grape": "अंगूर",
        "banana": "केला",
        "fruit": "फल",
        "vegetable": "सब्ज़ी",
        "grain": "अनाज",
        "dairy": "डेयरी"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def hindi_english(text):
    translate = {
        "नमस्ते": "hello",
        "अलविदा": "goodbye",
        "कृपया": "please",
        "धन्यवाद": "thankyou",
        "हाँ": "yes",
        "नहीं": "no",
        "शायद": "maybe",
        "पानी": "water",
        "सूर्य": "sun",
        "चाँद": "moon",
        "किताब": "book",
        "कंप्यूटर": "computer",
        "प्यार": "love",
        "दोस्त": "friend",
        "परिवार": "family",
        "सुंदर": "beautiful",
        "काम": "work",
        "कठिन": "hard",
        "आसान": "easy",
        "खाना": "food",
        "पीना": "drink",
        "सोना": "sleep",
        "सपना": "dream",
        "तेज़": "fast",
        "मैं": "i",
        "तुम": "you",
        "वह": "he",
        "वह": "she",
        "यह": "it",
        "हम": "we",
        "वे": "they",
        "हैं": "are",
        "हूँ": "am"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def english_japanese(text):
    translate = {
        "hello": "konnichiwa",
        "goodbye": "sayonara",
        "please": "onegai shimasu",
        "thankyou": "arigatou",
        "yes": "hai",
        "no": "iie",
        "maybe": "tabun",
        "water": "mizu",
        "sun": "taiyou",
        "moon": "tsuki",
        "book": "hon",
        "computer": "konpyuuta",
        "love": "ai",
        "friend": "yuujin",
        "family": "kazoku",
        "beautiful": "utsukushii",
        "work": "shigoto",
        "hard": "katai",
        "easy": "yasashii",
        "food": "tabemono",
        "drink": "nomimono",
        "sleep": "nemuru",
        "dream": "yume",
        "fast": "hayai",
        "i": "watashi",
        "you": "anata",
        "he": "kare",
        "she": "kanojo",
        "it": "sore",
        "we": "watashitachi",
        "they": "karera"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def japanese_english(text):
    translate = {
        "konnichiwa": "hello",
        "sayonara": "goodbye",
        "onegai shimasu": "please",
        "arigatou": "thankyou",
        "hai": "yes",
        "iie": "no",
        "tabun": "maybe",
        "mizu": "water",
        "taiyou": "sun",
        "tsuki": "moon",
        "hon": "book",
        "konpyuuta": "computer",
        "ai": "love",
        "yuujin": "friend",
        "kazoku": "family",
        "utsukushii": "beautiful",
        "shigoto": "work",
        "katai": "hard",
        "yasashii": "easy",
        "tabemono": "food",
        "nomimono": "drink",
        "nemuru": "sleep",
        "yume": "dream",
        "hayai": "fast",
        "watashi": "I",
        "anata": "you",
        "kare": "he",
        "kanojo": "she",
        "sore": "it",
        "watashitachi": "we",
        "karera": "they"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def english_spanish(text):
    translate = {
        "hello": "hola",
        "goodbye": "adiós",
        "please": "por favor",
        "thankyou": "gracias",
        "yes": "sí",
        "no": "no",
        "tal vez": "maybe",
        "agua": "water",
        "sol": "sun",
        "luna": "moon",
        "libro": "book",
        "computadora": "computer",
        "amor": "love",
        "amigo": "friend",
        "familia": "family",
        "hermoso": "beautiful",
        "trabajo": "work",
        "duro": "hard",
        "fácil": "easy",
        "comida": "food",
        "bebida": "drink",
        "dormir": "sleep",
        "sueño": "dream",
        "rápido": "fast"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def spanish_english(text):
    translate = {
        "hola": "hello",
        "adiós": "goodbye",
        "por favor": "please",
        "gracias": "thankyou",
        "sí": "yes",
        "no": "no",
        "tal vez": "maybe",
        "agua": "water",
        "sol": "sun",
        "luna": "moon",
        "libro": "book",
        "computadora": "computer",
        "amor": "love",
        "amigo": "friend",
        "familia": "family",
        "hermoso": "beautiful",
        "trabajo": "work",
        "duro": "hard",
        "fácil": "easy",
        "comida": "food",
        "bebida": "drink",
        "dormir": "sleep",
        "sueño": "dream",
        "rápido": "fast"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def english_french(text):
    translate = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "please": "s'il vous plaît",
        "thankyou": "merci",
        "yes": "oui",
        "no": "non",
        "maybe": "peut-être",
        "water": "eau",
        "sun": "soleil",
        "moon": "lune",
        "book": "livre",
        "computer": "ordinateur",
        "love": "amour",
        "friend": "ami",
        "family": "famille",
        "beautiful": "beau",
        "work": "travail",
        "hard": "dur",
        "easy": "facile",
        "food": "nourriture",
        "drink": "boisson",
        "sleep": "dormir",
        "dream": "rêve",
        "fast": "rapide"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

def french_english(text):
    translate = {
        "bonjour": "hello",
        "au revoir": "goodbye",
        "s'il vous plaît": "please",
        "merci": "thankyou",
        "oui": "yes",
        "non": "no",
        "peut-être": "maybe",
        "eau": "water",
        "soleil": "sun",
        "lune": "moon",
        "livre": "book",
        "ordinateur": "computer",
        "amour": "love",
        "ami": "friend",
        "famille": "family",
        "beau": "beautiful",
        "travail": "work",
        "dur": "hard",
        "facile": "easy",
        "nourriture": "food",
        "boisson": "drink",
        "dormir": "sleep",
        "rêve": "dream",
        "rapide": "fast"
    }
    for word in text.split():
        if word in translate:
            print(translate[word], end=' ')
        else:
            print(word, end=' ')

text = input("Enter the word: ").lower()
fun_name = input("Enter the function name: ").lower()

if fun_name == "english_hindi":
    english_hindi(text)
elif fun_name == "hindi_english":
    hindi_english(text)
elif fun_name == "english_japanese":
    english_japanese(text)
elif fun_name == "english_spanish":
    english_spanish(text)
elif fun_name == "spanish_english":
    spanish_english(text)
elif fun_name == "english_french":
    english_french(text)
elif fun_name == "french_english":
    french_english(text)
elif fun_name == "japanese_english":
    japanese_english(text)

else:
    print("TRANSLATION NOT AVAILABLE")
