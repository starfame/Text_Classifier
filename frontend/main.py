import streamlit as st

from app.api import enpoints
from app.components import csv_func


def main():
    st.title("Классификация комментариев")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Текстовый ввод")
        user_input = st.text_area("Введите ваш текст:", "")
        if st.button("Отправить"):
            response = enpoints.get_labels(user_input)
            st.write(response)

    with col2:
        st.header("Загрузка CSV")
        uploaded_file = st.file_uploader("Выберите CSV файл", type=["csv"])
        if uploaded_file:
            if csv_func.check_csv_format(uploaded_file):
                response_file = enpoints.process_csv(uploaded_file)
                st.download_button("Скачать результат", response_file, file_name="result.csv", mime="text/csv")


if __name__ == "__main__":
    main()
