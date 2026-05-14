
#  Patient-Voice NLP

### *Bridging the "Diagnostic Odyssey" through Bio-Medical Sentiment & Unmet Need Extraction*

`Patient-Voice NLP` is a specialized intelligence tool designed for Life Sciences Patient Advocacy and Medical Affairs teams. It utilizes **scispaCy** (specialized medical NLP) and **Transformer-based emotion models** to transform unstructured patient discourse into actionable strategic insights.


##  The Strategic Objective

Patients with rare diseases often spend 5–7 years in a "Diagnostic Odyssey." Traditional claims data (ICD-10) only captures the *transaction*; it misses the *human barrier*. This project extracts the lived experience to identify why patients are failing to access life-changing therapies.

### Key Capabilities

* **Medical-Grade NER:** Uses the `en_core_sci_sm` model to identify clinical entities and symptoms that standard NLP models miss.
* **Access Barrier Detection:** Automatically flags "Friction Points" such as insurance denials, travel distance to Centers of Excellence (CoE), and financial toxicity.
* **Emotional Sentiment Mapping:** Categorizes community discourse into core emotional states (Fear, Anger, Sadness, Joy) to measure the real-world impact of a therapy.


## Project Architecture

```text
patient-voice-nlp/
├── docs/               # Screenshots, Access Maps, and Visual Reports
├── src/                # Core Engine Room
│   ├── need_extractor.py     # Medical NLP & Barrier logic
│   └── sentiment_analyzer.py  # Emotion classification via Transformers
├── main.py             # Executive Dashboard / Entry Point
├── requirements.txt    # Project Dependencies
└── README.md           # Project Documentation

```


## Installation & Setup

This project requires specialized scientific models from the **Allen Institute for AI**. Follow these steps to ensure a "self-healing" installation of the medical dependencies.

```bash
# 1. Clone the repository
git clone https://github.com/your-username/patient-voice-nlp.git
cd patient-voice-nlp

# 2. Install standard dependencies
pip install -r requirements.txt

# 3. Install scispaCy and the Medical Model (Required for the NLP engine)
pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz

```

##  Featured Module: Access Barrier Extractor

The `need_extractor` module utilizes the scientific pipeline to scan for specific logistics and insurance friction points.

```python
from src.need_extractor import extract_access_barriers

# Example patient forum post
post = "My insurance just denied the claim for the new gene therapy. It's a 400-mile travel distance to the nearest CoE."

barriers = extract_access_barriers(post)
print(f"Detected Barriers: {barriers}")
# Output: ['denied', 'insurance', 'distance', 'travel']

```


## 🏛️ Part of the Life Sciences Executive Suite

This repository is the third pillar of a comprehensive Biotech Commercial Stack:

1. **[Net-Guard-GTN-Optimizer](https://www.google.com/search?q=link-to-repo-1):** Protecting revenue via Gross-to-Net and Outcome-Based Rebate logic.
2. **[Referral-Sense-AI]():** Identifying "Hidden" patients through NPI-level proxy claims and Haversine mapping.
3. **[Patient-Voice-NLP]():** Understanding the human experience and removing barriers to therapy adoption.


## Business Impact

* **Patient Advocacy:** Proactively identify communities needing travel support or lodging vouchers.
* **Market Access:** Quantify "Denial Rates" from social discourse to bolster negotiations with payers.
* **Field Force Excellence:** Alert MSLs to specific clinical concerns trending within a local geographic cluster.


##  License

Distributed under the MIT License. See `LICENSE` for more information.

