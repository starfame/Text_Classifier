import io

import pandas as pd

from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from .schema import Comment, CSVResponse, CommentResponse
from ..loader import preprocessor, classifier, db_logs, router


@router.post("/predict_single/", response_model=CommentResponse)
async def predict_single_comment(comment: Comment):
    preprocessed_text = preprocessor.preprocess_text([comment.content])
    vectorized_text = preprocessor.vectorize_text(preprocessed_text)
    raw_predictions = classifier.predict(vectorized_text)

    thresholded_predictions = (raw_predictions >= 0.5).astype(int)

    labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

    response = {"comment_text": comment.content}
    for i, label in enumerate(labels):
        response[label] = thresholded_predictions[:, i]

    await db_logs.add_log(str(comment), str(response))

    return response


@router.post("/predict_csv/", response_class=StreamingResponse)
async def predict_csv(file: UploadFile):
    file_contents = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(file_contents))
    except Exception as e:
        print(f"Error when reading CSV: {e}")  # Add this line
        raise HTTPException(detail=f"Error reading csv: {e}", status_code=400)

    if "comment_text" not in df.columns:
        print(f"Columns in CSV: {df.columns}")  # Add this line to print all columns
        raise HTTPException(detail="CSV should have a column named 'comment_text'", status_code=400)

    preprocessed_texts = preprocessor.preprocess_text(df["comment_text"].tolist())
    vectorized_texts = preprocessor.vectorize_text(preprocessed_texts)
    raw_predictions = classifier.predict(vectorized_texts)

    thresholded_predictions = (raw_predictions >= 0.5).astype(int)

    labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

    for i, label in enumerate(labels):
        df[label] = thresholded_predictions[:, i]

    output_csv = df.to_csv(index=False)
    response = StreamingResponse(io.StringIO(output_csv), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"

    await db_logs.add_log(file.filename, "CSV processed and response sent.")

    return response
