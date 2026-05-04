# Smart Email Classifier

A machine learning–powered email classifier and priority manager built with Python and Streamlit.

🚀 **Live Demo:** [smart-email-classifier.streamlit.app](https://smart-email-classifier-ldfwnqyjrzvh3aru5zi9mn.streamlit.app/)

## Features

- **Email Classification** — Categorizes emails as `work`, `spam`, `personal`, or `urgent` using TF-IDF + Naive Bayes
- **Priority Detection** — Assigns `High`, `Medium`, or `Low` priority based on email content
- **Email Summarization** — Extracts key sentences using NLTK
- **Interactive Dashboard** — Visualizes category and priority distribution with bar charts
- **Session History** — Tracks all analyzed emails in a table during the session

## Project Structure

```
email_classifier/
├── app/
│   └── main.py          # Streamlit UI
├── data/                # For datasets
├── model/               # For saved models
├── classifier.py        # ML classifier (TF-IDF + Naive Bayes)
├── priority.py          # Keyword-based priority logic
├── email_fetcher.py     # IMAP email fetcher (Gmail)
├── summarizer.py        # NLTK-based email summarizer
├── requirements.txt     # Python dependencies
└── README.md
```

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Jit23456/smart-email-classifier.git
cd smart-email-classifier
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app/main.py
```

Streamlit will automatically open the app in your browser.

## Usage

1. Paste any email content into the text area
2. Click **Analyze**
3. View the predicted category, priority level, and auto-generated summary
4. Analyze multiple emails to see the dashboard charts update

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| scikit-learn | TF-IDF vectorizer + Naive Bayes classifier |
| NLTK | Email summarization |
| Streamlit | Web UI and dashboard |
| pandas | Data handling |
| imaplib | IMAP email fetching |

## Future Improvements

- Gmail API integration (replace IMAP)
- BERT / HuggingFace transformer models for better accuracy
- Auto-reply generator
- Email notifications for urgent messages
- Export history to CSV
