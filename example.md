

```python
from framemongo import SimpleFrameMongo
```

## 简易 pandas.DataFrame 读写接口

### 设置连接


```python
SimpleFrameMongo.config_settings = {
    'name': 'your-db-name',
    'mongo_host': 'host:port',
    'username': 'your-username',
    'password': 'your-password'
}
```

### 存入 dataframe


```python
import pandas as pd
```


```python
df = pd.DataFrame({'test': [1, 2, 3]})
```


```python
with SimpleFrameMongo() as conn:
    conn.write('测试_0', df)
```

### 存入 dataframe 以及 metadata


```python
with SimpleFrameMongo() as conn:
    conn.write('测试_1', df, metadata='这是测试数据')
```

### 读取 dataframe


```python
with SimpleFrameMongo() as conn:
    result_df = conn.read('测试_0')
```


```python
result_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### 读取 metadata


```python
with SimpleFrameDB() as conn:
    result_df = conn.read('测试_1')
    meta = conn.read_metadata('测试_1')
```


```python
meta
```




    '这是测试数据'



### 删除 dataframe


```python
with SimpleFrameMongo() as conn:
    conn.delete('测试_0')
    conn.delete('测试_1')
```
