import streamlit as st
import requests

# Define API details
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
API_TOKEN = "YOUR_API_TOKEN"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Define function to query the sentiment analysis API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to analyze sentiment. Please try again later."}

# Define Streamlit app
def main():
    # Set Streamlit app title
    st.title("Sentiment Analysis")

    # Text input for user input
    user_input = st.text_input("Enter text for sentiment analysis:")

    # Button to trigger sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input.strip() != "":
            # Perform sentiment analysis
            output = query({"inputs": user_input})

            # Display sentiment analysis result as progress bars
            st.write("Sentiment Analysis Result:")

            if isinstance(output, list) and len(output) > 0 and "label" in output[0][0]:
                # Extract labels and scores from the API response
                labels_map = {
                    "LABEL_0": "Negative",
                    "LABEL_1": "Neutral",
                    "LABEL_2": "Positive"
                }
                for item in output[0]:
                    label = labels_map.get(item["label"], "Unknown")
                    score = item["score"]
                    st.write(f"{label}:")
                    st.progress(score)
            else:
                st.write("Failed to analyze sentiment. Please try again later.")
        else:
            st.write("Please enter some text for sentiment analysis.")

# Run Streamlit app
if __name__ == "__main__":
    main()
