import streamlit as st
st.text('Загрузка las файла/файлов')
st.button('LAS')
st.text('')
st.text ('Диапазон глубины в скважине(ах) для определения похожести')
st.slider('Smart depth')
st.slider('End depth')
st.text('')
st.selectbox('Выбор предобученной модели (в зависимости от вида каротажей)',('RNN on 4 logs', 'RNN on 6 logs'))
