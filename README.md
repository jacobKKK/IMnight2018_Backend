# IMnight2018_Backend

**switch to "api" branch before edit README.md**

## API ENDPOINT

- [Authentication](#authentication)
  - [Basic](#basic)
  - [Registration](#registration)
  - [Social Media Authentication](#social-media-authentication)

- [User](#user)
  - [取得自己資料](#取得自己資料) `GET /users/self`
  - [取得某用戶資料](#取得某用戶資料) `GET /users/user-id:`

- [human](#human)
  - [抽取本日人物](#抽取本日人物) `GET /human/daily`
  - [用戶擁有的表演者清單](#用戶擁有的表演者清單) `GET /human/list`
  - [取得某表演者資料](#取得某表演者資料) `GET /human/performer-id:`


# Authentication

## Basic

- /rest-auth/login/ (POST)

    - username
    - email
    - password

    Returns Token key

- /rest-auth/logout/ (POST)

    .. note:: ``ACCOUNT_LOGOUT_ON_GET = True`` to allow logout using GET - this is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout

- /rest-auth/password/reset/ (POST)

    - email

- /rest-auth/password/reset/confirm/ (POST)

    - uid
    - token
    - new_password1
    - new_password2

    .. note:: uid and token are sent in email after calling /rest-auth/password/reset/

- /rest-auth/password/change/ (POST)

    - new_password1
    - new_password2
    - old_password

    .. note:: ``OLD_PASSWORD_FIELD_ENABLED = True`` to use old_password.
    .. note:: ``LOGOUT_ON_PASSWORD_CHANGE = False`` to keep the user logged in after password change

- /rest-auth/user/ (GET, PUT, PATCH)

    - username
    - first_name
    - last_name

    Returns pk, username, email, first_name, last_name


## Registration

- /rest-auth/registration/ (POST)

    - username
    - password1
    - password2
    - email

- /rest-auth/registration/verify-email/ (POST)

    - key


## Social Media Authentication

Basing on example from installation section :doc:`Installation </installation>`

- /rest-auth/facebook/ (POST)
  用access_token登入  
    - access_token
    - code

    .. note:: ``access_token`` OR ``code`` can be used as standalone arguments, see https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/registration/views.py

- /socail-auth/facebook/login/ (GET)
  redirect到facebook登入  


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
