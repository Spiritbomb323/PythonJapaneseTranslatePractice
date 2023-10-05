JapKanjiEng = [
    "a",
    "i",
    "u",
    "e",
    "o",
    "ka",
    "ki",
    "ku",
    "ke",
    "ko",
    "sa",
    "shi",
    "su",
    "se",
    "so",
    "ta",
    "chi",
    "tsu",
    "te",
    "to",
    "na",
    "ni",
    "nu",
    "ne",
    "no",
    "ha",
    "hi",
    "fu",
    "he",
    "ho",
    "ma",
    "mi",
    "mu",
    "me",
    "mo",
    "ya",
    "yu",
    "yo",
    "ra",
    "ri",
    "ru",
    "re",
    "ro",
    "wa",
    "wo",
    "n",
    "ga",
    "gi",
    "gu",
    "ge",
    "go",
    "za",
    "ji",
    "zu",
    "ze",
    "zo",
    "da",
    "de",
    "do",
    "ba",
    "bi",
    "bu",
    "be",
    "bo",
    "pa",
    "pi",
    "pu",
    "pe",
    "po"
]

JapKanji = [
    "あ",
    "い",
    "う",
    "え",
    "お",
    "か",
    "き",
    "く",
    "け",
    "こ",
    "さ",
    "し",
    "す",
    "せ",
    "そ",
    "た",
    "ち",
    "つ",
    "て",
    "と",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ひ",
    "ふ",
    "へ",
    "ほ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "や",
    "ゆ",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "わ",
    "を",
    "ん",
    "が",
    "ぎ",
    "ぐ",
    "げ",
    "ご",
    "ざ",
    "じ",
    "ず",
    "ぜ",
    "ぞ",
    "だ",
    "で",
    "ど",
    "ば",
    "び",
    "ぶ",
    "べ",
    "ぼ",
    "ぱ",
    "ぴ",
    "ぷ",
    "ぺ",
    "ぽ"
]

import random

choiceInput = input("('EngToKan' or 'KanToEng') Enter mode or XXX to quit: ")
result = "N/A"
streak = 0

while choiceInput != "XXX":
    while (choiceInput == "KanToEng"):
        randNum = random.randrange(0, len(JapKanji))
        print(JapKanji[randNum])
        translation = input("enter translation or XXX to quit: ")
        if (translation == JapKanjiEng[randNum]):
            result = "Correct"
            streak += 1
        else:
            result = "Incorrect. Answer was " + str(JapKanjiEng[randNum])
            streak = 0
        print(result + ". " + "streak is " + str(streak))
        if (translation == "XXX"):
            choiceInput = input("('EngToKan' or 'KanToEng') Enter mode or XXX to quit: ")

    while (choiceInput == "EngToKan"):
        randNum = random.randrange(0, len(JapKanji))
        print(JapKanjiEng[randNum])
        translation = input("enter translation or XXX to quit: ")
        if (translation == JapKanji[randNum]):
            result = "Correct"
            streak += 1
        else:
            result = "Incorrect. Answer was " + str(JapKanji[randNum])
            streak = 0
        print(result + ". " + "streak is " + str(streak))
        if (translation == "XXX"):
            choiceInput = input("('EngToKan' or 'KanToEng') Enter mode or XXX to quit: ")