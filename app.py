from flask import Flask, render_template, request, jsonify
from generate_email import get_email, get_translation, get_subject, get_summary, get_language, get_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/generate_email', methods=['POST'])

def show_generated_email():
    # Getting comment from front-end
    customer_review = request.form['customer_review']
    # Using API to generate email
    subject = get_subject(customer_review)
    summary = get_summary(customer_review)
    language = get_language(customer_review)
    sentiment = get_sentiment(customer_review)
    generated_email = get_email(customer_review, language, subject, summary, sentiment)
    # Show generated email
    return jsonify({'email_content': generated_email})

@app.route('/translate_email', methods=['POST'])
def show_translated_email():
    # Get target language
    email_content = request.form['email_content']
    target_language = request.form['target_language']
    # Using API to translate email
    translated_email = get_translation(email_content,target_language)
    # Show translation
    return jsonify({'translated_email': translated_email})

if __name__ == '__main__':
    app.run(debug=True)
