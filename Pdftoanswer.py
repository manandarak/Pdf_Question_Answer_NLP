import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

def read_pdf(file):
    pdf_document = fitz.open(file)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    pdf_document.close()
    return text

def main():
    st.title("PDF Question-Answering App")
    st.sidebar.header("User Input")

    # Upload PDF file
    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        st.sidebar.subheader("PDF Preview")
        pdf_text = read_pdf(uploaded_file)
        st.sidebar.text(pdf_text[:500])  # Display a snippet of the PDF text

        # User input for question
        user_question = st.text_input("Ask a question about the PDF:")

        if st.button("Get Answer"):
            if user_question:
                # Use a pre-trained question-answering model (DistilBERT in this case)
                question_answering = pipeline("question-answering")
                answer = question_answering(question=user_question, context=pdf_text)

                st.subheader("Answer:")
                st.write(answer['answer'])
            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()








