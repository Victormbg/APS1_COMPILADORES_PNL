from collections import defaultdict
from heapq import nlargest
from string import punctuation

import pyperclip as pyperclip
from googletrans import Translator
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

translator = Translator()

try:
    
    texto = pyperclip.paste()
    
    if texto == "":
        print("Nenhum texto copiado!!!")
        exit(0)
    
    print(
        "\n=============================================================================================================\n" +
        "TEXTO BASE COPIADO:\n", texto)

    sentencas = sent_tokenize(texto)
    palavras = word_tokenize(texto.lower())

    stopwords = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

    frequencia = FreqDist(palavras_sem_stopwords)

    sentencas_importantes = defaultdict(int)

    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]

    print(
        "\n=============================================================================================================\n" +
        "TEXTO RESUMIDO PELO NLTK:\n")

    idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

    for i in sorted(idx_sentencas_importantes):
        print(sentencas[i])

    print(
        "\n=============================================================================================================\n" +
        "TEXTO TRADUZIDO EM INGLES PELO GOOGLETRANS:\n")

    for i in sorted(idx_sentencas_importantes):
        translated = translator.translate(sentencas[i], src='pt', dest='en')
        print(translated.text)

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
