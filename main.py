from src.sentiment_analyzer import analyze_patient_discourse
from src.need_extractor import extract_access_barriers

# Mock anonymized community data
posts = [
    "I've been denied by my insurance three times for the new gene therapy. It's so frustrating.",
    "The 5-hour drive to the Mayo Clinic is getting impossible for my family.",
    "Finally saw a specialist who listened! The treatment is starting to work."
]

for post in posts:
    sentiment = analyze_patient_discourse([post])
    barriers = extract_access_barriers(post)
    print(f"Post Analysis: {sentiment[0]['label']} | Barriers Found: {barriers}")
