
#import sys
#sys.stdout = open('output_main_file', 'w')

from joblib import load
from feature_engineering_depoly import *
from google_search import do_research

LABELS = ['agree', 'disagree', 'discuss', 'unrelated']
class Source:
    def __init__(self):
        self.name=""
        self.bias=""
        self.factuality =""
        self.notes =""
        self.url=""
        self.mbfc = ""

def gen_features_for_prediction (text1,text2):
    t1, t2 = [], []  # t1 is the user selected text and t2 is the body of a collected article
    t1.append(text1)
    t2.append(text2)

    X_overlap = generate_baseline_feats(word_overlap_features, t1, t2, "")
    X_belief = generate_additional_features("myproject/expanded_cue_words/belief.txt", t1, t2, "")
    X_denial = generate_additional_features("myproject/expanded_cue_words/denial.txt", t1, t2, "")
    X_doubt = generate_additional_features("myproject/expanded_cue_words/doubt.txt", t1, t2, "")
    X_fake = generate_additional_features("myproject/expanded_cue_words/fake.txt", t1, t2, "")
    X_knowledge = generate_additional_features("myproject/expanded_cue_words/knowledge.txt", t1, t2,"")
    X_negation = generate_additional_features("myproject/expanded_cue_words/negation.txt", t1, t2,"")
    X_question = generate_additional_features("myproject/expanded_cue_words/question.txt", t1, t2,"")
    X_report = generate_additional_features("myproject/expanded_cue_words/report.txt", t1, t2, "")
    X_refuting = generate_baseline_feats(refuting_features, t1, t2, "")
    X_polarity = generate_baseline_feats(polarity_features, t1, t2, "")
    X_hand = generate_baseline_feats(hand_features, t1, t2, "")
    X_tfidf = generate_additional_features("tfidf", t1, t2, "")


    X = np.c_[X_hand, X_polarity, X_overlap, X_refuting, X_belief, X_denial, X_doubt, X_fake, X_knowledge, X_negation, X_question, X_report,X_tfidf]

    return X



def predict_stance(text1,text2):
    print("predicting stance")
    X = gen_features_for_prediction(text1,text2)
    clf = load('myproject/trained_model.joblib')
    predictions = clf.predict(X)
    predicted_labels = [LABELS[int(p)] for p in predictions]
    return predicted_labels



def get_sources():
    print("reading sources list")
    sources = dict()
    with codecs.open("myproject/source_credibility.csv", 'r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            fields = line.split('\t')
            s = Source()
            s.bias= fields[4]
            s.factuality= fields[5]
            s.mbfc= fields[0]
            s.name= fields[1]
            s.notes=fields[6]
            s.url= fields[7]
            if not s.url == "NIL":
                sources[s.url] = s
    return sources


def return_summary(d,i,sources):
    print("composing summary")
    out ="\n\n"
    out+="\nThis document was "
    if d.url != "UNKNOWN":
        out+="\npublished at: " + d.url
    if d.publish_date != "UNKNOWN":
        out+="\npublished on: " + d.publish_date
    for key, source in sources.items():
        if key in d.source or key in d.url:
            out+="\n\nHere are some info about the source of this document:\n\n"
            out+="\nSource name: "+source.name
            out+="\nSource bias:"+source.bias
            if "VERY" in source.factuality: source.factuality= "VERY HIGH"
            out+="\nSource factuality:"+source.factuality
            out+="\nAdditional notes:"+source.notes


    out+='\n'
    print("finished composing summary")
    return out



def generate_report(relevant_docs,claim,sources):
    print("geenrating a report")
    out =""
    labels = ["unrelated", "disagree", "agree", "discuss"]
    stance_groups = {label: [] for label in labels}
    for doc in relevant_docs:
        stance_groups[doc.stance].append(doc)

    total_agree = len(stance_groups['agree'])
    total_disagree = len(stance_groups['disagree'])
    summary = ""
    if total_agree > total_disagree:
        out+="THE MAJORITY OF OUR SOURCES AGREE WITH THE ABOVE CLAIM.\n\n "
        out+= "\nHERE ARE SOME:\n\n"
        i=1
        for d in stance_groups['agree']:
            result = return_summary(d,i,sources)
            summary = summary+result
            i+=1
    elif total_agree < total_disagree:
        out+= "THE MAJORITY OF OUR SOURCES DISAGREE WITH THE ABOVE CLAIM.\n\n "
        out+= "\nHERE ARE SOME:\n\n"
        i=1
        for d in stance_groups['disagree']:
            result = return_summary(d,i,sources)
            summary = summary + result
            i+=1

    out = out + summary
    print("finished generating a report")
    return out


def fact_check(claim):

    sources = get_sources()
    relevant_docs = do_research(claim)
    for doc in relevant_docs:
        predictions = predict_stance(claim, doc.text)
        doc.stance = predictions[0]

    report = generate_report(relevant_docs, claim, sources)
    print("returning the report" +report)
    return report


#print(fact_check("Facebook post says that PepsiCo announced Mountain Dew will be discontinued over health concerns."))







