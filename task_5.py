nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=True):
    """"
    Makes n random jokes from 3 lists
    :param n: number of jokes
    :param flag: if True any word can only be used in 1 joke
    :return: a list with jokes in strings
    """
    from random import choice
    jokes = []
    if flag :
        for i in range(n):
            noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
            jokes.append(f"{noun} {adverb} {adjective}")
    else:
        for i in range(n):
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")

    return jokes


print(get_jokes(5))