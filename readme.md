# 🧠 Stance Aggregator

### **Description**
An end-to-end stance detection and aggregation API that takes a claim, retrieves supporting documents, extracts features, and predicts whether the documents **support**, **oppose**, or are **neutral** toward the claim.

---

## 🚀 Overview
**Stance Aggregator** automates stance detection by combining document retrieval, feature engineering, and machine learning inference.  
Given a user-provided claim, it searches for related documents online, processes textual features, and predicts each document’s stance relative to the claim.

---

## 🧩 Tech Stack
- **Language & Framework:** Python, Flask  
- **Machine Learning:** Pretrained classifier (Joblib), TF-IDF features  
- **Core Modules:** Document retrieval, feature extraction, stance prediction  

---

## 📁 Project Structure
| File | Description |
|------|--------------|
| `main.py` | Loads the model and vectorizer, performs retrieval, feature extraction, and stance prediction |
| `myproject.py` | Defines the Flask API endpoint for stance prediction |
| `google_search.py` | Retrieves documents related to the input claim |
| `feature_engineering_depoly.py` | Defines and computes the feature set used by the model |
| `test_api.py` | Simple script for testing; edit the claim text (line 5) and run it |
| `source_credibility.csv` | Metadata for source credibility from Media Bias Fact Check |

---

## 🌟 Features
- End-to-end stance classification workflow  
- Automated document retrieval and preprocessing  
- Lightweight and modular Flask API  
- Easy to test, extend, and integrate with other applications  

---

## 🧪 Usage
```bash
# 🧭 Clone the repository
git clone https://github.com/Thanaa-Jaradat/Stance_Aggregator.git
cd Stance_Aggregator

# ⚙️ Install dependencies
pip install -r requirements.txt

# 🚀 Run the Flask API
python3 myproject.py

# 🧠 Test the API
# Send a POST request with a claim, or quickly test it by running:
python3 test_api.py
