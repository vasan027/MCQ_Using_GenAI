import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgen.utils import read_file, get_table_data
from src.mcqgen.logger import logging
from src.mcqgen.MCQGen import generate_evaluate_chain
import streamlit as st
from langchain.callbacks import get_openai_callback


# load JSON
with open("./res.json", "r") as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQ Generator")

with st.form("user_inputs"):
    file = st.file_uploader("Upload a PDF or TXT file")

    mcq_count = st.number_input("Number of MCQs", min_value=2, max_value=25)

    sub = st.text_input("Subject Name", max_chars=20)

    tone = st.text_input("Tone of Questions", max_chars=10, placeholder="Simple")

    button = st.form_submit_button("Generate MCQs")

    if button and file is not None and mcq_count and sub and tone:
        with st.spinner("Generating"):
            try:
                text = read_file(file)

                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": sub,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON),
                    }
                )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                if isinstance(response, dict):
                    quiz = response.get("quiz", None)

                    if quiz is not None:
                        td = get_table_data(quiz)
                        if td is not None:
                            df = pd.DataFrame(td)
                            df.index = df.index + 1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])

                        else:
                            st.error("Error in table data")

                    else:
                        st.write("response")
