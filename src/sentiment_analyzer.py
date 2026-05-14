from transformers import pipeline

# Load a medical-sentiment-specific pipeline
classifier = pipeline("sentiment-analysis", model="bhadresh-savani/bert-base-uncased-emotion")

def analyze_patient_discourse(text_list):
    """
    Classifies the emotional state of patient forum posts.
    Categories: Joy (success), Sadness (burden), Anger (access issues), Fear (side effects).
    """
    results = classifier(text_list)
    return results
