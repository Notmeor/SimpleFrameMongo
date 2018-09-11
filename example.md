
## 简易 pandas.DataFrame 读写接口


```python
from framemongo import SimpleFrameMongo
```

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
print(result_df)
```

       test
    0     1
    1     2
    2     3


### 读取 metadata


```python
with SimpleFrameMongo() as conn:
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
