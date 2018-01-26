from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from accounts.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    """
    access_token 是 Social Accounts › Social application tokens 裡面的那個token  
    code 是什麼我也不知到
    code 和 access_token 選其中一個就好了
    """
    adapter_class = FacebookOAuth2Adapter
