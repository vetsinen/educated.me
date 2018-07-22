#!/usr/bin/env python3
# educated.me

import string
import collections
import feedparser
import html2text

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint


def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    # text = text.translate(None, string.punctuation)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens


def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)

    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering


if __name__ == "__main__":
    articles = [
        'Drake`s latest No. 1 hit In My Feelings shot to the top of the charts thanks to a viral dance challenge that had little to do with the rapper himself.',
        'Teach and learn by playing! Showcase your culture and your country in non-verbal forms: dances, videos, pictures, traditional objects and many more! Challenge your communication skills in a group of young English learners and become a child yourself once again! Leave memories of bright international cooperation!',
        'The festival, founded by Jay-Z in 2012, takes place on Philadelphia`s streets. This week, Mayor Jim Kenney`s office announced plans to move the event — sparking fury from the rapper.',
        'The European Court of Human Rights ruling — and the release of new music from the activist and punk collective — comes two days after members of the group interrupted the World Cup final game.',
        'Goal of the project is to present participant’s culture and encourage young people to meet foreigners. Volunteers are going to teach basics of English and arise the interest in social issues and other cultures. Form of workshops should be adapted to age and skills of youth. Trainee should prepare engaging presentations, games and other additional activities.',
        'A few hours earlier, the authorities had cut short Kraviz’s headline show at a nearby festival, claiming – incorrectly – that it was overrunning. So, this otherworldly afterparty feels subversive. It is being livestreamed on Facebook, which is banned in China, along with most western social media. ',
        'Our internship program offers a select number of university students (and university graduates) the opportunity to gain exposure to a thriving law practice. In order to sharpen your legal skills, you will work alongside reputable and talented lawyers and experience an inclusive culture that encourages contribution and helps you to start fulfilling your potential.'
    ]

#     articles =  [
#     'В идеале у аутсорсинговой компании есть несколько крупных долгосрочных проектов (клиентов) с хорошими рейтами. Проект растет в медленном прогнозируемом темпе, поэтому расширение команды и поиск новых сотрудников не составляет труда. Но такие проекты существуют где-то в идеальном мире. Реальность же такова, что большинство проектов краткосрочны, внедряются специфические технологии, рейты у разработчиков низкие, клиент полностью управляет командой (это больше похоже на аутстаффинг, а не аутсорсинг), цена за проект фиксирована и вам часто приходится бороться с клиентом, доказывая, что необходимо увеличить количество часов',
#     'Геймдев хакатон на сутки, сразу после конференции IGDO Conference от Indie Game Developers Odessa Локация: Chapps Space — креативное пространство в центре Одессы от digital агентства Chapps. Хакатон — это когда приходишь, придумываешь и реализуешь идею за короткий срок. Можно идти со своей идеей, можно придумать на месте. Можно присоединиться к понравившейся команде. Хакатон — это драйв, командная работа, соревнование, знакомства, новый опыт, шанс попробовать свои силы в одном флаконе',
#     ' конкурс среди команд будущих, возможно уже действующих разработчиков из 2-3 человек, а также всех желающих реализующих СВОЮ идею. Цель хакатона — создание рабочего приложения или прототипа в рамках темы, определенной несколькими критериями. Тематика данного хакатона — «Кампус будущего», а детальные критерии будут объявлены непосредственно на хакатоне, чтобы никто не мог подготовиться к конкурсу заранее, и все команды находились в равных стартовых условиях.',
#     'CoE, по сути, влияет на стратегическое развитие компании. Такие «центры» — это не просто R&D, это R&D + бизнес. Ваша наработанная (или нарабатываемая) экспертиза систематизирована, у вас есть команда сейлов, которая работает в тесной связи с R&D для того, чтобы предлагать потенциальному клиенту уникальную экспертизу активнее, а не просто ждать запроса от потенциального клиента и думать, чем занять скучающих на бенче сотрудников. Более того, благодаря СоЕ у компании появляется возможность охватить даже тех клиентов, которые даже не думали о каких- либо новых проектах.'
# ]
    d = feedparser.parse(
        'https://dou.ua/calendar/feed/%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D0%BC%D1%8B/%D0%9A%D0%B8%D0%B5%D0%B2')

    # print(d.feed.title)
    # for e in d.entries:
    #     # print(e.title)
    #     print ( html2text.html2text(e.description)[150:290])
    # exit()

    clusters = cluster_texts(articles, 2)
    print(clusters)
    pprint(dict(clusters))
    dicls = dict(clusters)
    for i in dicls.keys():
        print(dicls[i])
        for j in dicls[i]:
            print(articles[j])

