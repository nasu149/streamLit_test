import streamlit as st
# import openai
import os
import PersonName
import global_value as g

# openai.api_key = os.environ['OPENAI_API_KEY']
# def create_image_from_text(text, photo_count):
    
#     # 応答設定
#     response = openai.Image.create(
#                   prompt = text,             # 画像生成に用いる説明文章
#                   n = photo_count,                     # 何枚の画像を生成するか
#                   size = '256x256',          # 画像サイズ
#                   response_format = "url"    # API応答のフォーマット
#                 )

#     # API応答から画像URLを指定
#     urls = []
#     for i in range(photo_count):
#         image_url = response['data'][i]['url']
#         urls.append(image_url)
        
#     return urls



st.title("名前を覚えてね。")

text = "a japanse man"
question_num = 5
cols = st.columns(2)
# urls = create_image_from_text(text, question_num)
urls = [f'chat-gpt-generated-image_{i}.jpg' for i in range(question_num)]
person_name_instance = PersonName.PersonName(question_num)
person_names = person_name_instance.create_people_name()
print("person names ===== ", person_names)

header_name_list = \
    ['名字: ' + person['名字'] + '\n' + '名前: ' + person['名前'] for person in person_names[1:]]

g.person_names = person_names
g.urls = urls

for i in range(0, question_num, 2):
    with cols[0]:
        st.image(urls[i], use_column_width=True)
        st.text(header_name_list[i])
    if i+1>question_num-1:
        break
    with cols[1]:
        st.image(urls[i+1], use_column_width=True)
        st.text(header_name_list[i+1])