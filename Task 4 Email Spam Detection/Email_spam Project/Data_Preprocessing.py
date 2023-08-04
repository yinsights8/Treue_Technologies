import contractions
from nltk.util import ngrams
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer, regexp_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



# ## language Detect
# def lang_detect(data):
#   lang = detect(data)
#   return lang

# # review_translate
# def lang_translator(data):
#   translor = Translator()
#   translated_text = translor.translate(data)
#   return translated_text.text

## Removing Spaces
def remove_spaces(data):
  clean_text = data.replace("\\n", " ").replace('\t',' ').replace('\\', ' ')
  return clean_text

# expand text
def expand(data):
  expand_text = contractions.fix(data)
  return expand_text

# handling accented characters
def handling_accented(data):
  fixed_text = unidecode(data)
  return fixed_text

# removing stopwords
stopword_list = stopwords.words()
stopword_list.remove("no")
stopword_list.remove("nor")
stopword_list.remove("not")

# ceanining text
def clean_data(data):
  tokens = word_tokenize(data)
  clean_text = [word.lower() for word in tokens if (word not in punctuation) and (word.lower() not in stopword_list) and (len(word)>2) and (word.isalpha())]
  return clean_text

# autoCorrecting word
def autocorrect(data):
  spell = autocorrect.Speller(lang="en")
  corrected_text = spell(data)
  return corrected_text

# Lammitization
def lemmatization(data):
    lemmatizer = WordNetLemmatizer()
    final_data = []
    for word in data :
        lemmatized_word = lemmatizer.lemmatize(word)
        final_data.append(lemmatized_word)
    return " ".join(final_data)