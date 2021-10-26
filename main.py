import streamlit as st
# import numpy as np
# import pandas as pd
import time
# from PIL import image

st.title('Streamlit 超入門')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右')

expander = st.beta_expander('contact')
expander.write('write')

option = st.sidebar.selectbox(
  'color',
  list(range(1,11))
)

st.write('progress bar')
'start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


# option1 = st.text_input('あなたの趣味は')
option1 = st.sidebar.text_input('あなたの趣味は')

'あなたの趣味は', option1, 'です'

condition = st.sidebar.slider('あなたのコンディション', 0, 100, 50)

'あなたの調子は', condition, 'です'

'あなたの好きな数字は', option, 'です'

if st.checkbox('SHOW'):
  st.write('Display Image')

# Image.open('IMG_0298.jpg')
# st.image(img, caption='hoge', use_colum_width=True)

df = pd.DataFrame({
  '1列目': [1,2,3,4],
  '2列目': [10,20,30,40]
})

df1 = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a', 'b', 'c']
)

df2 = pd.DataFrame(
  np.random.rand(100,2)/[50,50]+[35.69, 139.70],
  columns=['lat', 'lon']
)

st.map(df2)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

st.table(df)

"""
# 章
## 節
### 項

```python
import stremalit as st
import numpy as np
import pandas as pd
```

"""
