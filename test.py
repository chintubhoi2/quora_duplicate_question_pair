from app import helper
import pickle

model = pickle.load(open(r'C:\Users\bhoic\OneDrive\Desktop\quora\model.pkl','rb'))
scaler = pickle.load(open(r'C:\Users\bhoic\OneDrive\Desktop\quora\scaler.pkl','rb'))

q1 = "Astrology: I am a Capricorn Sun Cap moon and cap rising...what does that say about me?'"
q2 = "Astrology: I am a Capricorn"

query = helper.query_point_creator(q1,q2)
print(query)
query = scaler.transform(query)
print(query)
result = model.predict(query)
print(result)