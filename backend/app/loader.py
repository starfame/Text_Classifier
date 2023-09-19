import os

import nltk
from fastapi import APIRouter

from .data import config
from .db.logs_db import LogsDb
from .models.classifier import ToxicCommentsClassifier
from .utils.preprocess import TextPreprocessor

base_dir = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(base_dir, "data/nltk_data")
nltk.data.path.append(nltk_data_path)

preprocessor = TextPreprocessor(config.MAX_WORDS,
                                config.MAX_LENGTH,
                                vectorizer_path=config.VECTORIZER_PATH)
classifier = ToxicCommentsClassifier(config.MAX_WORDS,
                                     config.EMBEDDING_DIM,
                                     config.MAX_LENGTH,
                                     weights_path=config.MODEL_WEIGHTS_PATH)

db_logs = LogsDb()


async def init_pool():
    await db_logs.init_pool()


router = APIRouter()
