import streamlit as st

st.title('Streamlitの部品（ウィジット）')

st.header('1. ボタン')
if st.button('表示'):
    st.write('ボタン押されました')

st.header('2. チェックボックス')
if st.checkbox('表いj'):
    st.write('チェックされｍした')

st.header('3. ラジオボタン')
option = st.radio('検索条件を選択してください',
    ['条件1','条件2','条件3'])
st.write(f'{option}が選択')

st.header('4. セレクトボックス')

option = st.selectbox('検索条件を選択してください',
    ['条件1','条件2','条件3','条件4','条件5'])
st.write(f'{option}が選択')


st.header('5. セレクトボックス（複数選択）')

option = st.multiselect('検索条件を選択してください(複数選択OK)',
    ['条件1','条件2','条件3','条件4','条件5'],)
st.write(f'{option}が選択')



st.header('6. スライダー')

value=st.slider(label='数値を選んでください', 
    min_value=0,
    max_value=100,
    value=30)
st.write(f'{value}が選択されました')

st.header('7. テキスト入力')

text=st.text_input('検索するテキストを入力してください')
st.write(f'{text}が入力されました。')

st.header('8. テキストエリア')

text=st.text_area('複数')
st.write(f'{text}数入力')

st.header('9. 数値入力')

number=st.number_input('数値を入力してください')
st.write(f'{number}と入力されました')

st.header('10. 日付入力')

date=st.date_input('日付')
st.write(f'{date}が入力されました')
st.header('11. 時間入力')

time=st.time_input('時間')
st.write(f'{time}が入力')
    
st.header('12. ファイルアップロード')

file=st.file_uploader('アップきぼんぬ')
if file is not None:
    data=file.getvalue()
    text=data.decode('utf-8')
    st.write(f'ファイルの内容{text}')
