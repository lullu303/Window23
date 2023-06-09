import csv
from collections import Counter
import pandas as pd
\

# 형태소분석 함수
def clean_korean_documents(sentences):

    # KoNLPy 형태소분석기 설정
    tagger = konlpy.tag.Okt()

    # 문장 품사 변수 초기화
    sentences_pos = []

    # 모든 문장 반복
    for sentence in sentences:
        # 정규 표현식 필터
        RE_FILTER = re.compile("[.,!?\"':;~()]")
        # 특수기호 제거
        sentence = re.sub(RE_FILTER, "", sentence)

        # 배열인 형태소분석의 출력을 띄어쓰기로 구분하여 붙임
        sentence = " ".join(tagger.morphs(sentence))
        sentences_pos.append(sentence)

    return sentences_pos
'''