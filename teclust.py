import string
import collections

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
    articles = ['SQLAthanor: Serialization / Deserialization for SQLAlchemy ORM And now for something completely different',
     'Framework to do an application a schedule for a University',
     'A nice collection of often useful awesome Python frameworks and libraries',
     'How to use PyDrive to upload files to Google Drive through python', 'Ranking News Bias with Python',
     'I`ve made a clock using pyglet, but I want to change the window bg color every second.Why is the code I’ve used make the bg flicker and not go from white to black all the way',
     'Sending and pulling live data from server.Dreams In Text - Text Based Adventure',
     'I developed a package which will notify your github activity and it is working on mac windows and linux platform.',
     'Getting the active(foreground) window title on windows 10 using python',
     'Chameleon:An HTML / XML template engine for Python',
     'SubstanceDesigner now allows you to script its behavior using Python', 'Fuction and Home key in pyautogui',
     'How to install win32 on Windows 10', 'Python has brought computer programming to a vast new audience',
     'Exceptive: A Library Making Exception Handling More Programmatic and Debuggable']
    articles =  [
    'В идеале у аутсорсинговой компании есть несколько крупных долгосрочных проектов (клиентов) с хорошими рейтами. Проект растет в медленном прогнозируемом темпе, поэтому расширение команды и поиск новых сотрудников не составляет труда. Но такие проекты существуют где-то в идеальном мире. Реальность же такова, что большинство проектов краткосрочны, внедряются специфические технологии, рейты у разработчиков низкие, клиент полностью управляет командой (это больше похоже на аутстаффинг, а не аутсорсинг), цена за проект фиксирована и вам часто приходится бороться с клиентом, доказывая, что необходимо увеличить количество часов',
    'Геймдев хакатон на сутки, сразу после конференции IGDO Conference от Indie Game Developers Odessa Локация: Chapps Space — креативное пространство в центре Одессы от digital агентства Chapps. Хакатон — это когда приходишь, придумываешь и реализуешь идею за короткий срок. Можно идти со своей идеей, можно придумать на месте. Можно присоединиться к понравившейся команде. Хакатон — это драйв, командная работа, соревнование, знакомства, новый опыт, шанс попробовать свои силы в одном флаконе',
    ' конкурс среди команд будущих, возможно уже действующих разработчиков из 2-3 человек, а также всех желающих реализующих СВОЮ идею. Цель хакатона — создание рабочего приложения или прототипа в рамках темы, определенной несколькими критериями. Тематика данного хакатона — «Кампус будущего», а детальные критерии будут объявлены непосредственно на хакатоне, чтобы никто не мог подготовиться к конкурсу заранее, и все команды находились в равных стартовых условиях.',
    'CoE, по сути, влияет на стратегическое развитие компании. Такие «центры» — это не просто R&D, это R&D + бизнес. Ваша наработанная (или нарабатываемая) экспертиза систематизирована, у вас есть команда сейлов, которая работает в тесной связи с R&D для того, чтобы предлагать потенциальному клиенту уникальную экспертизу активнее, а не просто ждать запроса от потенциального клиента и думать, чем занять скучающих на бенче сотрудников. Более того, благодаря СоЕ у компании появляется возможность охватить даже тех клиентов, которые даже не думали о каких- либо новых проектах.'
]
    clusters = cluster_texts(articles, 2)
    print(clusters)
    pprint(dict(clusters))
    dicls = dict(clusters)
    for i in dicls.keys():
        print(dicls[i])
        for j in dicls[i]:
            print(articles[j])

