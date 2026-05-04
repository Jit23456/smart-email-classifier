from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    # work
    "meeting tomorrow at 9am",
    "please review the project report",
    "schedule a call with the team",
    "quarterly performance review",
    "office hours update",
    "conference call agenda",
    "submit your timesheet by Friday",
    "project status update required",
    # spam
    "limited time offer buy now",
    "click here to claim your prize",
    "you have won a free gift card",
    "earn money from home fast",
    "cheap loans apply today",
    "exclusive deal only for you",
    "unsubscribe from our mailing list",
    "discount 50 percent off today only",
    # personal
    "family dinner tonight at 7",
    "birthday party this weekend",
    "catch up over coffee soon",
    "hope you are doing well",
    "photos from our trip last summer",
    "mom called asking about you",
    "lets plan the vacation",
    "happy anniversary wishes",
    # urgent
    "urgent deadline project submit now",
    "action required immediately",
    "critical system failure alert",
    "respond asap important issue",
    "your account will be suspended",
    "final warning please act now",
    "emergency meeting called",
    "immediate response needed",
]

labels = [
    "work", "work", "work", "work", "work", "work", "work", "work",
    "spam", "spam", "spam", "spam", "spam", "spam", "spam", "spam",
    "personal", "personal", "personal", "personal", "personal", "personal", "personal", "personal",
    "urgent", "urgent", "urgent", "urgent", "urgent", "urgent", "urgent", "urgent",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def classify_email(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]