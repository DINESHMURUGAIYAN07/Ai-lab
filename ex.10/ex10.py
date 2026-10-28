import re

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def ai_fake_news_detector(news):
    suspicious_words = [
        "shocking", "miracle", "100% true",
        "you won't believe", "secret cure"
    ]

    text = news.lower()
    score = sum(word in text for word in suspicious_words)

    if score >= 2:
        return "FAKE / SUSPICIOUS"
    elif score == 1:
        return "UNCERTAIN - VERIFY SOURCE"
    else:
        return "REAL / NEEDS VERIFICATION"

print("=== AI FAKE NEWS DETECTION ===")
news = input("Enter the news article: ")

cleaned_news = clean_text(news)
result = ai_fake_news_detector(cleaned_news)

print("\nAI Analysis Result:", result)
print("Note: AI prediction should be verified using reliable sources.")