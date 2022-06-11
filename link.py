def get_details(c_name,date):
    pass
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def stopwords_remove(para):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(para)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence=[i for i in filtered_sentence if len(i)>=2]
  return filtered_sentence
def select_regect(para,word):
     for i in para:
        if str(i.lower())==str(word.lower()):
           return True
           break
     return False 
#filtering the key_word       
def paragraph(para,key_word):
    filter_para=stopwords_remove(para)
    sent=select_regect(filter_para,str(key_word))
    if sent == True:
       return para
    else:
         return "no keyword found"
    return sent
def finilised_sentences(df,dept,key_word):
       df=df[df["media"] == dept]
        
       return df
dept="Digital Journal"
key_word="ABB"
df=finilised_sentences(df,dept,key_word)
