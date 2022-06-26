# app-review
App to find contradicting app reviews from corpus of reviews uploaded.

This app supports authentication.

**Steps to run this app**
* Install the pip packages attached in requirements.txt
* To use this app, create '.streamlit/secrets.toml' file.
* Add below text to the file. Replace _username_ and _password_ appropriately.
```
[secrets]
username = "password"
```
* In the terminal, run `streamlit run app_review.py`
