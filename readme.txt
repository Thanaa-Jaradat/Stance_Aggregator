This is the backend deployed on an amazaon ec2 server to serve the stance aggregation app.
Please read the file "readme.txt" in the folder "stance_detection" as this backend is not but a minimized version of those script.
minimization is done to elimante the files not needed to be deployed, such as training the model, data set files, testing and scoring scripts.
The part we kept here are used for production only, this includes:
1.the Flask API in the file "myproject.py" which receives the client POST requests with the claim to check, and responds with a fact-checking report
2. "main.py" which loads the trained model from "trained_model.joblib" and the tfidf dictionary from "tfidf_vectorizer.pickle" then collects relevant documents using "google_search.py", then extracts features from those documents and the claim, then finally predict stance using the pretrained model and returns the fact-checking report as a response.

To test the backend you can run the test script in "test_api.py":
python3 test_api.py
if you would like to test the backend with a different claim, just change the claim text in line 5 of the script and re run it.
