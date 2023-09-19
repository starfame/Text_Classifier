from pydantic import BaseModel, Field


class Comment(BaseModel):
    content: str = Field(
        ...,
        title="Comment Content",
        description="The comment text that needs to be classified.",
        example="This is a sample comment."
    )


class CSVUpload(BaseModel):
    file: bytes = Field(
        ...,
        title="CSV File",
        description="Upload a CSV file containing a 'comment_text' column for batch classification.",
    )


class CommentResponse(BaseModel):
    comment_text: str = Field(..., title="Original Comment Text")
    toxic: int = Field(..., title="Toxicity Classification", description="1 indicates toxic, 0 indicates not toxic.")
    severe_toxic: int
    obscene: int
    threat: int
    insult: int
    identity_hate: int


class CSVResponse(BaseModel):
    file: bytes = Field(
        ...,
        title="Processed CSV File",
        description="The returned CSV file after classification with additional columns for each label."
    )
