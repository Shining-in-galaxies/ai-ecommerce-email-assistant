from openai import OpenAI
import os
from dotenv import load_dotenv

# Get OpenAI API key
load_dotenv() 
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Define delimiter
delimiter = "####"
delimiter_2 = "////////"

# General function to get response with gpt-3.5
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=1000):
    messages_payload = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
    response = client.chat.completions.create(
        model=model,
        messages=messages_payload,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    if response.choices and len(response.choices) > 0:
        last_message = response.choices[-1].message
        last_message_content = last_message.content
        return last_message_content
    else:
        return "No response generated."

# Get the subject from customer's email
def get_subject(comment):
    system_message_subject=comment
    user_message_subject=f"""
    Subject of an email in English from the comment of this e-commerce customer using Inferring technique within 10 words"""
    messages_subject =  [  
    {'role':'system', 
    'content': system_message_subject},    
    {'role':'user', 
    'content': f"{delimiter}{user_message_subject}{delimiter}"},  
    ] 
    subject = get_completion_from_messages(messages_subject)  
    print("Subject of customer comment: ")
    print(subject+"\n")
    return subject

# Get the summary of the customer's comment
def get_summary(comment):
    system_message_summary=comment
    user_message_summary=f"""
    Give the summary of this product review in English of the comment using Summarizing technique within 35 words."""
    messages_summary =  [  
    {'role':'system', 
    'content': system_message_summary},    
    {'role':'user', 
    'content': f"{delimiter}{user_message_summary}{delimiter}"},  
    ] 
    summary=get_completion_from_messages(messages_summary)
    print("Summary of customer comment:")
    print(summary+"\n")
    return summary

# Get the original language of the customer's comment
def get_language(comment):
    system_message_summary=comment
    user_message_summary=f"""
    What's the language is the customer mostly using? Answer within one word."""
    messages_summary =  [  
    {'role':'system', 
    'content': system_message_summary},    
    {'role':'user', 
    'content': f"{delimiter}{user_message_summary}{delimiter}"},  
    ] 
    language=get_completion_from_messages(messages_summary)
    print("Language of customer comment:")
    print(language+"\n")
    return language

# Sentiment analysis of the customer's comment
def get_sentiment(comment):
    system_message_sentiment=comment
    user_message_sentiment=f"""
    Process sentiment analysis in English of the customer's comment using Inferring technique. Positive or Negative?"""
    messages_sentiment =  [  
    {'role':'system', 
    'content': system_message_sentiment},    
    {'role':'user', 
    'content': f"{delimiter}{user_message_sentiment}{delimiter}"},  
    ] 
    sentiment=get_completion_from_messages(messages_sentiment)
    print("Sentiment:")
    print(sentiment+"\n")
    return sentiment

# Generate email
def get_email(comment, language, subject, summary, sentiment):
    system_message_email = comment + subject + summary + sentiment + language
    user_message_email = f"""
    You're an e-commerce store owner. This customer just purchased your item. Please create an email ONLY in {language} to be sent to the customer based on {comment} including the {subject}, {summary} and {sentiment} with proper email format with subject and extra. Email words limit: 100 words."""
    messages_email = [
        {'role': 'system',
         'content': system_message_email},
        {'role': 'user',
         'content': f"{delimiter}{user_message_email}{delimiter}"},
    ]
    email = get_completion_from_messages(messages_email)
    # print("Generated Email:")
    # print(email + "\n")
    return email

# Translate email
def get_translation(generated_email, selected_language):
    system_message_translation = generated_email + selected_language
    user_message_translation = f"""
    You're a translator working at an e-commerce store. This is an email written by your colleague to customer:{generated_email} Please translate this email into language of {delimiter_2}{selected_language}{delimiter_2} and ensure that during translation, there is no addition, alteration, or deletion of the original text, so as to preserve the original meaning."""
    messages_translation = [
        {'role': 'system',
         'content': system_message_translation},
        {'role': 'user',
         'content': f"{delimiter}{user_message_translation}{delimiter}"},
    ]
    translation = get_completion_from_messages(messages_translation)
    # print("Generated Email:")
    # print(translation + "\n")
    return translation

# Test
def main():
    # Simulated user comment
    text = "Hello, I am Alison, reaching out from ABC store regarding your review about the slow startup of your recently purchased computer. We apologize for the inconvenience and are here to help.Could you please share the computer model, operating system, and any specific error messagesThis information will assist our technical team in providing targeted solutions.Thank you for your patience and cooperation."
    language = "Chinese"
    get_translation(text, language)

if __name__ == "__main__":
    main()