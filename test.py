import pickle
from scipy.sparse import coo_matrix
import cv2
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
tfidf_transformer_from_pickle = pickle.load(open("TFIDF.sav", 'rb'))
tfidf_transformer_from_pickle = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("TFIDF.sav", "rb")))
desc = "cap crew crew take edge fickle weather clearing condition fastest dry time performance baselayer fabric open knit construction breathes wick keep dry cool weather window shuts wear insulation beneath layer self fabric neck soft skin raglan sleeve flat ribbed underarm panel merge way shoulder strap eliminate chafe made oz polyester recycled gladiodor natural odor control garment recyclable common thread recycling program br br b detail b ul li capilene fabric open knit invite airflow provides exc"
tf_idf_vector = tfidf_transformer_from_pickle.transform(cv.transform([desc]))