# IMnight2018_Backend

**switch to "api" branch before edit README.md**

## API ENDPOINT

- [user](#user)
  - [取得自己資料](#取得自己資料) `GET /users/self`
  - [取得某用戶資料](#取得某用戶資料) `GET /users/user-id:`

- [human](#human)
  - [抽取本日人物](#抽取本日人物) `GET /human/daily`
  - [用戶擁有的表演者清單](#用戶擁有的表演者清單) `GET /human/list`
  - [取得某表演者資料](#取得某表演者資料) `GET /human/performer-id:`

# User

## 取得自己資料
**URL** : `/users/self`

**Method** : `GET`

**Auth Require** : YES

**Data constraints** :

```json
{
  "data":{
    用戶資料
  }
}
```

## 取得某用戶資料
**URL** : `/users/user-id:`

**Method** : `GET`

**Auth Require** : YES

**Data constraints** :

```json
{
  "data":{
    用戶資料
  }
}
```

# Human

## 抽取本日人物
**URL** : `/human/list`

**Method** : `GET`

**Auth Require** : YES

**Data constraints** :

```json
{
  "data":{
    表演者資料
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

## 用戶擁有的表演者清單
**URL** : `/human/list`

**Method** : `GET`

**Auth Require** : YES

**Data constraints** :

```json
{
  "data":[
      {
        表演者資料
      },
      {
        表演者資料
      }
  ]
}
```

```python
表演者清單 = client.db.col.find
return 表演者清單
```

## 取得某表演者資料
**URL** : `/human/performer-id:`

**Method** : `GET`

**Auth Require** : YES

**Data constraints** :

```json
{
  "data":{
    表演者資料
  }
}
```
