import gradio as gr
from textblob import TextBlob
from gensim.summarization import summarize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        positive_sentences = []
        negative_sentences = []
        positive_score = 0
        negative_score = 0
        for sentence in blob.sentences:
            polarity = sentence.sentiment.polarity
            if polarity > 0:
                positive_sentences.append(str(sentence))
                positive_score += polarity
            elif polarity < 0:
                negative_sentences.append(str(sentence))
                negative_score += polarity
        positive_summary = "\n".join(positive_sentences)
        negative_summary = "\n".join(negative_sentences)
        return positive_summary, negative_summary, positive_score, negative_score

    except Exception as e:
        print(e)

iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.inputs.Textbox(lines=10, label="Input Text"),
    outputs=[
        gr.outputs.Textbox(label="Positive Summary"),
        gr.outputs.Textbox(label="Negative Summary"),
        gr.outputs.Textbox(label="Positive Score"),
        gr.outputs.Textbox(label="Negative Score")
    ],
    title="Sentiment Analysis",
    description="Antara's Analyzer"
)

iface.launch()
