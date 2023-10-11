import streamlit as st
import pandas as pd 
import streamlit as st
from pymongo import MongoClient

# 방법1 - URI
# mongodb_URI = "mongodb://localhost:27017/"
# client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
client = MongoClient('mongodb+srv://bkkim:mWwgLmC45pPDL7KD@cluster0.3uf1tpq.mongodb.net/')

db = client['data_hi_mart']
collection = db['hi_mart'].find()

table_name = []
table_desc = []
data_type = []
col_name = []
col_desc = []


for col in list(collection):
    table_name.append(col['테이블명'])
    table_desc.append(col['테이블설명'])
    data_type.append(col['데이터타입'])
    col_name.append(col['컬럼명'])
    col_desc.append(col['변경컬럼'])

print('data_type : ', data_type)
print('col_name : ', col_name)
print('desc : ', col_desc)


df = pd.DataFrame(
    {'테이블명' : table_name,
    '테이블설명' : table_desc,
    '컬럼명': col_desc,
    '컬럼의미': col_name,
    '데이터타입': data_type,
    }
)

unique_table_names = df['테이블명'].drop_duplicates().tolist()
selected_option = st.selectbox("선택하세요:", unique_table_names,  key="dropdown")

filtered_df = df[df['테이블명'] == selected_option]
filtered_df_value = filtered_df[['컬럼명', '컬럼의미', '데이터타입']].reset_index(drop=True)
unique_table_desc = filtered_df['테이블설명'].drop_duplicates().tolist()
st.subheader(unique_table_desc[0])
st.dataframe(filtered_df_value , width=600, height=1200)

st.sidebar.title('Data Hi Mart')



st.markdown(
    f"""
    <style>
        .st-e3 .st-at {{
            width: 20px; /* 드롭다운 메뉴의 너비를 조정 */
            background-color: lightblue; /* 배경색 변경 */
            color: darkblue; /* 글꼴 색상 변경 */
            border-radius: 10px; /* 테두리 모서리를 둥글게 */
            font-size: 16px; /* 글꼴 크기 변경 */
            padding: 10px; /* 패딩 추가 */
        }}
        .st-e3 .st-at:hover {{
            background-color: pink; /* 마우스 호버시 배경색 변경 */
            color: purple; /* 마우스 호버시 글꼴 색상 변경 */
        }}
    </style>
    """,
    unsafe_allow_html=True,
)



# # 선택된 옵션 출력
# st.write("선택한 옵션:", selected_option)