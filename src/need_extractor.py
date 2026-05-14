# Part of Project: src/need_extractor.py

import spacy
import subprocess
import sys

def install_dependencies():
    """
    Ensures scispacy and the medical model are installed 
    to avoid the 'No compatible package found' error.
    """
    try:
        import scispacy
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "scispacy"])
    
    # Direct URL for the specific version compatible with current scispacy/spacy
    model_url = "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz"
    subprocess.check_call([sys.executable, "-m", "pip", "install", model_url])

def load_medical_model():
    try:
        return spacy.load("en_core_sci_sm")
    except OSError:
        install_dependencies()
        return spacy.load("en_core_sci_sm")

# Initialize the NLP engine
nlp = load_medical_model()

def extract_access_barriers(text):
    """
    Identifies phrases related to insurance denials or travel issues.
    """
    doc = nlp(text)
    # Medical-specific keywords often found in rare disease patient forums
    keywords = ["denied", "insurance", "distance", "expensive", "travel", "wait", "denial"]
    barriers = [token.text for token in doc if token.text.lower() in keywords]
    return list(set(barriers))
