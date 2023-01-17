from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_wordcloud(data):
    sentences = data["Sintomas"].tolist()
    sentences_as_a_string = ' '.join(sentences)
    plt.figure(figsize=(10, 10))
    plt.imshow(WordCloud().generate(sentences_as_a_string))
    plt.axis("off")