import streamlit as st
import global_value as g
st.title('この人の名前は？')




st.image(g.urls[0], use_column_width=True)
header_name_list = ['名字: ' + person['名字'] + '\n' + '名前: ' + person['名前'] for person in g.person_names[1:]]
# st.text(header_name_list[0])