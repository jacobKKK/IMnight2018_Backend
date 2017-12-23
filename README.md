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

## Login 
**URL** : `/rest-auth/login/`

**Method** : `POST`

**Parameter** :

> username  
> email  
> password  

**Data constraints** :

```json
{
"key" : ""
}
```

## Logout
**URL** : `/rest-auth/logout/`

**Method** : `POST`

**Data constraints** :

```json

```

**Note** : 

`ACCOUNT_LOGOUT_ON_GET = True` to allow logout using GET - this is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout

## Password reset 
**URL** : `/rest-auth/password/reset/`

**Method** : `POST`

**Parameter** :

> email   

**Data constraints** :

```json
```

## Password reset confirm
**URL** : `/rest-auth/password/reset/confirm/`

**Method** : `POST`

**Parameter** :

> uid  
> token  
> new_password1  
> new_password2  

**Data constraints** :

```json
```

**Note** : 

`uid` and `token` are sent in email after calling `/rest-auth/password/reset/`

## Password change
**URL** : `/rest-auth/password/change/`

**Method** : `POST`

**Parameter** :

> new_password1  
> new_password2  
> old_password

**Data constraints** :

```json
```

**Note** : 

`OLD_PASSWORD_FIELD_ENABLED = True` to use old_password.
`LOGOUT_ON_PASSWORD_CHANGE = False` to keep the user logged in after password change

## user
**URL** : `/rest-auth/user/`

**Method** : `GET`, `PUT`, `PATCH`

**Parameter** :

> username  
> first_name  
> last_name  

**Data constraints** :

```json
Returns pk, username, email, first_name, last_name
```

## Registration

## Registration
**URL** : `/rest-auth/registration/`

**Method** : `POST`

**Parameter** :

> username  
> password1  
> password2  
> email  

**Data constraints** :

```json
```

## Registration verify email
**URL** : `/rest-auth/registration/verify-email/`

**Method** : `POST`

**Parameter** :

> key  

**Data constraints** :

```json
```


## Social Media Authentication

## 用 access_token 登入 facebook
**URL** : `/rest-auth/facebook/`

**Method** : `POST`

**Parameter** :

> access_token  
> code  

**Data constraints** :

```json
```
**Note** : 

`access_token` OR `code` can be used as standalone arguments, see https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/registration/views.py

## Redirect 到 Facebook 登入 
**URL** : `/socail-auth/facebook/login/`

**Method** : `GET`

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
