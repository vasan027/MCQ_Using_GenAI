import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            Pdf_r = PyPDF2.PdfFileReader(file)
            text = ""
            for page in Pdf_rdf_r.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error reading PDF File")

    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except Exception as e:
            raise Exception("Error reading txt File")
    else:
        raise Exception("Invalid File type")


def get_table_data(quiz_str):
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_tabledata = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option} -> {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_tabledata.append({"MCQ": mcq, "Options": options, "Answer": correct})

        return quiz_tabledata

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
