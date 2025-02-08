import streamlit as st
import pickle
import string

def load_artifacts(model_path='sentiment_model.pkl', vectorizer_path='vectorizer.pkl'):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(vectorizer_path, 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    return model, vectorizer

model, vectorizer = load_artifacts()

def preprocess_input(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = text.lower()
    return text

def predict_sentiment(text, model, vectorizer):
    # Transform text using the same vectorizer used during training
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]
    probabilities = model.predict_proba(text_vectorized)[0]
    return prediction, probabilities

def main():
    st.title("Yelp Review Sentiment Analysis")
    st.write("Enter your review text below to analyze its sentiment")

    user_input = st.text_area("Review text:", height=100)

    if st.button("Analyze Sentiment"):
        if user_input:
            processed_text = preprocess_input(user_input)
            prediction, probabilities = predict_sentiment(processed_text, model, vectorizer)
            
            if prediction == 1:
                st.success("😊 Positive Sentiment - This review appears to be positive!")
            else:
                st.error("😞 Negative Sentiment - This review appears to be negative!")
                
            st.write("\nConfidence Scores:")
            st.write(f"Negative: {probabilities[0]:.2%}")
            st.write(f"Positive: {probabilities[1]:.2%}")
        else:
            st.warning("Please enter some text to analyze")

if __name__ == "__main__":
    main()