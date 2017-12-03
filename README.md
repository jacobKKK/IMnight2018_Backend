# IMnight2018_Backend

# API ENDPOINT

# User
- [取得自己資料](#取得自己資料) `GET /users/self`
- [取得用戶資料](#取得用戶資料) `GET /users/user-id:`

# Human
- [抽取本日人物](#抽取本日人物) `GET /human/drawCard/ `
- [擁有的表演者清單](#擁有的表演者清單) `GET /human/listCard/ `


## 取得自己資料
URL : `/users/self`

Method : `GET`

Auth Require : YES

Data constraints :

```json
{
  "data":{
    用戶資料
  }
}
```

## 取得用戶資料
URL : `/users/user-id:`

Method : `GET`

Auth Require : YES

Data constraints :

```json
{
  "data":{
    用戶資料
  }
}
```

## 抽取本日人物
URL : `/human/drawCard/ `

Method : `GET`

Auth Require : YES

Data constraints :

```json
{
  "data":{
    用戶資料
  }
}
```
```python
if 當天抽的人 == null:  
  抽一個人  
  把他加到表演者清單  
  更新當天狀態  
return 當天表演者
```

## 擁有的表演者清單
URL : `GET /human/listCard/ `

Method : `GET`

Auth Require : YES

Data constraints :

```json
{
  "data":{
    "users":[
      {
        "id":,
        "user_name":,
      },
      {
        "id":,
        "user_name":,
      }
    ]
  }
}
```

```python
表演者清單 = client.db.col.find
return 表演者清單
```
