import json
import contractions
import re
from string import punctuation


with open('./Data/Pet_Supplies.json', 'r') as file_open:
     for line in file_open:
        try:
            data = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


extracted_data = []

for review in data:
    extracted_data.append({
        'reviewerName': data['reviewerName'],
        'reviewText': data['reviewText']
    })

with open('./Data/review_data.json', 'w') as new_file:
    items = ',\n'.join(map(json.dumps, extracted_data))
    new_file.write(f'[\n{items}\n]')

def clean_text(text):
    #remove contractions
    text = contractions.fix(text)
    #make lowercase
    text = text.lower()
    #remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)
    #remove numbers
    text = re.sub(r'\w*\d\w*', '', text)
    #remove stopwords
    stopwords = [stopword.strip() for stopword in open('./Data/stopwords_en.txt', 'r')]
    return ' '.join([word for word in text.split() if word not in stopwords])

cleaned_text = clean_text(items)
print(cleaned_text)
    
#I hope you found NLP interesting. You will now try to start the project that we will be working on tomorrow. As I mentioned earlier, I have shared the JSON file (pet_supplies) in our data folder on Teams.
#So, what you need to do is:
#Extract a certain number of reviews (choose between 100-1000) and create a new file with only these reviews.
#Clean the text using the steps you learned today.
#Select the reviews and their ratings.
#Use CountVectorizer to get a numerical representation.
#Split 80-20 between training and testing.
#Train and then test.