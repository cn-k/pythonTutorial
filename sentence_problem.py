def sentence_maker(phrase):
    interrogatives = ("How", "Why", "What")
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."
sentence = ""
while True:
    phrase = input('write a sentece')
    lst = ()
    if phrase.__eq__("\end"):
        print(sentence)
        break
    else:
        sentence = sentence + sentence_maker(phrase)
        #lst.append(sentence_maker(phrase))