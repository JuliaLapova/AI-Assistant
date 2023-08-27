import streamlit as st
from fastapi_app.chatbot.assistant import get_answer
from fastapi_app.routes.api_routes import get_answer_with_sources
import os
import requests

##@st.cache(allow_output_mutation=True)
#@st.cache_data()  # Streamlit recommends to use this method
##@st.cache_resource(allow_output_mutation=True)  # Streamlit recommends to use this method
#def get_data_file(url):
##    localpath = "/tmp/tempfile"
#    localpath = "/tmp/index.faiss"
#    r = requests.get(url)
#    with open(localpath, 'wb') as f:
#        f.write(r.content)
#    return localpath

##def main():
#file_url = 'https://github.com/JuliaLapova/AI-Assistant/raw/main/faiss/faiss-hr/index.faiss'
##    file_url = 'https://github.com/JuliaLapova/AI-Assistant/raw/main/faiss/faiss-hr/index.faiss'
#localfile = get_data_file(file_url)

#    # Дальше вы можете использовать localfile в вашем приложении, как если бы это был локальный файл

##if __name__ == "__main__":
##    main()

#    # Выводим путь к файлу
#st.write(f'localfile: {localfile}')

#    # Проверяем наличие файла и выводим результат проверки
#st.write(f'Проверяем наличие файла: {localfile}')    
#st.write(os.path.exists(localfile))


#dir_path = '/tmp/'
#dir_contents = os.listdir(dir_path)

#st.write(dir_contents)

col1, col2 = st.columns(2)

with col1:
#    st.title('Привет, я ваш умный помощник!')
    st.markdown("<h2>Привет, я ваш умный помощник!</h2>", unsafe_allow_html=True)
    st.write('Интеллектуальный консультант для сотрудников СПб ГКУ «МФЦ»')

with col2:
    st.markdown("""
        <div style="padding-left:100px;">
            <img src="https://drive.google.com/uc?export=view&id=1g0KmrIILmwb0Vrxt-J-n0HFvQBDhk0Lr">
        </div>
        """, unsafe_allow_html=True)



#with col2:
#    st.image('https://drive.google.com/uc?export=view&id=1g0KmrIILmwb0Vrxt-J-n0HFvQBDhk0Lr')


# Создаем форму для ввода данных пользователем
with st.form(key='my_form'):
    text_input = st.text_input(label='Введите текст')
    submit_button = st.form_submit_button(label='Отправить')


# Выводим данные, введенные пользователем
#if text_input:
#    st.write(f'Вы ввели: {text_input}')
#    answer = get_answer(document = text_input)
#    st.write(f'Ваш ответ: {answer}')

# Исправляем здесь
if text_input:  # Если text_input не пустой и не None
  user_input = text_input
  api_key = "your_key"
  topic = "main" # yt
  translate_answer = False # передайте True, если вы хотите переводить ответ
  #answer, sources = get_answer_with_sources(user_input, api_key, topic, translate_answer)
  answer, sources = get_answer_with_sources(user_input, api_key, topic, translate_answer)


# Выводим данные, введенные пользователем
#if text_input:
#    st.write(f'Вы ввели: {text_input}')
#    answer = get_answer_with_sources(document = text_input)
#    st.write(f'Ваш ответ:\n {answer}')
#    st.write(f'Источники: {sources}')
#    

if text_input:
    st.write(f'Ваш вопрос: {text_input}')
    answer, sources = get_answer_with_sources(user_input=text_input, api_key=api_key, topic=topic, translate_answer=translate_answer)
    st.write(f'Ответ:\n {answer}')
    st.markdown("---") # Это добавит горизонтальную линию
    st.write(f'**Источник 1:** {sources[0]}')
    st.write(f'**Источник 2:** {sources[1]}')
    st.write(f'**Источник 3:** {sources[2]}')
