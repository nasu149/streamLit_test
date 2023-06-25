# import openai
import re

class PersonName:

    def __init__(self, count, model="gpt-3.5-turbo", role = "user"):
        self.message = f'''
        日本人ではやや変わった人の名前をフルネームで{count}個あげてください。
        読み方も教えてください。
        出力形式は以下にしてください。
        ###[1]
        名字: 田中(たなか)
        名前: 雄介(ゆうすけ)
        [2]
        名字: 落合(おちあい)
        名前: 遼太郎(りょうたろう)
        '''
        self.model = model
        self.role = role


    def create_people_name(self):
        # row_text = self.get_row_people_names()
        row_text = f'''
        [1]
        名字: 首藤(くびとう)
        名前: 那奈(なな)
        [2]
        名字: 伏見(ふしみ)
        名前: 雄二(ゆうじ)
        [3]
        名字: 鴨志田(かもしだ)
        名前: 清春(きよはる)
        [4]
        名字: 岡崎(おかざき)
        名前: 太郎(たろう)
        [5]
        名字: 岡崎(おかざき)
        名前: 太郎(たろう)'''
        row_text = row_text.replace(' ', '')
        persons_name_list = self.process_row_text(row_text=row_text)
        return persons_name_list


        
    # def get_row_people_names(self):
    #     response = openai.ChatCompletion.create(
    #         model=self.model,
    #         messages=[
    #             {"role": self.role, "content": self.message},
    #         ],
    #     )
    #     row_text = response.choices[0]["message"]["content"].strip()
    #     print('row_text = ', row_text)
    #     return row_text
        

    def process_row_text(self, row_text):
        text_list = re.split('\[[0-9]\]', row_text)
        results = []
        print(text_list)
        print(len(text_list))
        for text in text_list:
            first_last_name = text.split('\n')
            first_last_name_trim = [a for a in first_last_name if a != '' and not a.isspace()]
            print(first_last_name_trim)
            print()
            person_dict = dict()
            for key_value_set in first_last_name_trim:
                key_value_list = key_value_set.split(":")
                print(key_value_list[0])
                print(key_value_list[1])
                print()
                person_dict[key_value_list[0]] = key_value_list[1]
            print("person_dict = ", person_dict)
            results.append(person_dict)
        print("results  = ", results)
        return results
        


