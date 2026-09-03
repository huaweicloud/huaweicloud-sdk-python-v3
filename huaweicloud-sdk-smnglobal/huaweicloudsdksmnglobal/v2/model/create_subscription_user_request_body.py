# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionUserRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'group': 'list[str]',
        'http': 'CreateSubscriptionUserRequestHttpEndpointInfo',
        'https': 'CreateSubscriptionUserRequestHttpsEndpointInfo',
        'sms': 'CreateSubscriptionUserRequestSmsEndpointInfo',
        'email': 'CreateSubscriptionUserRequestEmailEndpointInfo',
        'callnotify': 'CreateSubscriptionUserRequestCallnotifyEndpointInfo',
        'wechat': 'CreateSubscriptionUserRequestWechatEndpointInfo',
        'dingding': 'CreateSubscriptionUserRequestDingdingEndpointInfo',
        'feishu': 'CreateSubscriptionUserRequestFeishuEndpointInfo',
        'welink': 'CreateSubscriptionUserRequestWelinkEndpointInfo',
        'ding_talk_bot': 'CreateSubscriptionUserRequestDingTalkBotEndpointInfo'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'http': 'http',
        'https': 'https',
        'sms': 'sms',
        'email': 'email',
        'callnotify': 'callnotify',
        'wechat': 'wechat',
        'dingding': 'dingding',
        'feishu': 'feishu',
        'welink': 'welink',
        'ding_talk_bot': 'ding_talk_bot'
    }

    def __init__(self, name=None, group=None, http=None, https=None, sms=None, email=None, callnotify=None, wechat=None, dingding=None, feishu=None, welink=None, ding_talk_bot=None):
        r"""CreateSubscriptionUserRequestBody

        The model defined in huaweicloud sdk

        :param name: 订阅用户名称。
        :type name: str
        :param group: 订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。
        :type group: list[str]
        :param http: 
        :type http: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        :param https: 
        :type https: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        :param sms: 
        :type sms: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        :param email: 
        :type email: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        :param callnotify: 
        :type callnotify: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestCallnotifyEndpointInfo`
        :param wechat: 
        :type wechat: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWechatEndpointInfo`
        :param dingding: 
        :type dingding: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingdingEndpointInfo`
        :param feishu: 
        :type feishu: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestFeishuEndpointInfo`
        :param welink: 
        :type welink: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWelinkEndpointInfo`
        :param ding_talk_bot: 
        :type ding_talk_bot: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingTalkBotEndpointInfo`
        """
        
        

        self._name = None
        self._group = None
        self._http = None
        self._https = None
        self._sms = None
        self._email = None
        self._callnotify = None
        self._wechat = None
        self._dingding = None
        self._feishu = None
        self._welink = None
        self._ding_talk_bot = None
        self.discriminator = None

        self.name = name
        if group is not None:
            self.group = group
        if http is not None:
            self.http = http
        if https is not None:
            self.https = https
        if sms is not None:
            self.sms = sms
        if email is not None:
            self.email = email
        if callnotify is not None:
            self.callnotify = callnotify
        if wechat is not None:
            self.wechat = wechat
        if dingding is not None:
            self.dingding = dingding
        if feishu is not None:
            self.feishu = feishu
        if welink is not None:
            self.welink = welink
        if ding_talk_bot is not None:
            self.ding_talk_bot = ding_talk_bot

    @property
    def name(self):
        r"""Gets the name of this CreateSubscriptionUserRequestBody.

        订阅用户名称。

        :return: The name of this CreateSubscriptionUserRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSubscriptionUserRequestBody.

        订阅用户名称。

        :param name: The name of this CreateSubscriptionUserRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def group(self):
        r"""Gets the group of this CreateSubscriptionUserRequestBody.

        订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。

        :return: The group of this CreateSubscriptionUserRequestBody.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this CreateSubscriptionUserRequestBody.

        订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。

        :param group: The group of this CreateSubscriptionUserRequestBody.
        :type group: list[str]
        """
        self._group = group

    @property
    def http(self):
        r"""Gets the http of this CreateSubscriptionUserRequestBody.

        :return: The http of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        """
        return self._http

    @http.setter
    def http(self, http):
        r"""Sets the http of this CreateSubscriptionUserRequestBody.

        :param http: The http of this CreateSubscriptionUserRequestBody.
        :type http: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        """
        self._http = http

    @property
    def https(self):
        r"""Gets the https of this CreateSubscriptionUserRequestBody.

        :return: The https of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        """
        return self._https

    @https.setter
    def https(self, https):
        r"""Sets the https of this CreateSubscriptionUserRequestBody.

        :param https: The https of this CreateSubscriptionUserRequestBody.
        :type https: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        """
        self._https = https

    @property
    def sms(self):
        r"""Gets the sms of this CreateSubscriptionUserRequestBody.

        :return: The sms of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        r"""Sets the sms of this CreateSubscriptionUserRequestBody.

        :param sms: The sms of this CreateSubscriptionUserRequestBody.
        :type sms: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        """
        self._sms = sms

    @property
    def email(self):
        r"""Gets the email of this CreateSubscriptionUserRequestBody.

        :return: The email of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CreateSubscriptionUserRequestBody.

        :param email: The email of this CreateSubscriptionUserRequestBody.
        :type email: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        """
        self._email = email

    @property
    def callnotify(self):
        r"""Gets the callnotify of this CreateSubscriptionUserRequestBody.

        :return: The callnotify of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestCallnotifyEndpointInfo`
        """
        return self._callnotify

    @callnotify.setter
    def callnotify(self, callnotify):
        r"""Sets the callnotify of this CreateSubscriptionUserRequestBody.

        :param callnotify: The callnotify of this CreateSubscriptionUserRequestBody.
        :type callnotify: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestCallnotifyEndpointInfo`
        """
        self._callnotify = callnotify

    @property
    def wechat(self):
        r"""Gets the wechat of this CreateSubscriptionUserRequestBody.

        :return: The wechat of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWechatEndpointInfo`
        """
        return self._wechat

    @wechat.setter
    def wechat(self, wechat):
        r"""Sets the wechat of this CreateSubscriptionUserRequestBody.

        :param wechat: The wechat of this CreateSubscriptionUserRequestBody.
        :type wechat: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWechatEndpointInfo`
        """
        self._wechat = wechat

    @property
    def dingding(self):
        r"""Gets the dingding of this CreateSubscriptionUserRequestBody.

        :return: The dingding of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingdingEndpointInfo`
        """
        return self._dingding

    @dingding.setter
    def dingding(self, dingding):
        r"""Sets the dingding of this CreateSubscriptionUserRequestBody.

        :param dingding: The dingding of this CreateSubscriptionUserRequestBody.
        :type dingding: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingdingEndpointInfo`
        """
        self._dingding = dingding

    @property
    def feishu(self):
        r"""Gets the feishu of this CreateSubscriptionUserRequestBody.

        :return: The feishu of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestFeishuEndpointInfo`
        """
        return self._feishu

    @feishu.setter
    def feishu(self, feishu):
        r"""Sets the feishu of this CreateSubscriptionUserRequestBody.

        :param feishu: The feishu of this CreateSubscriptionUserRequestBody.
        :type feishu: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestFeishuEndpointInfo`
        """
        self._feishu = feishu

    @property
    def welink(self):
        r"""Gets the welink of this CreateSubscriptionUserRequestBody.

        :return: The welink of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWelinkEndpointInfo`
        """
        return self._welink

    @welink.setter
    def welink(self, welink):
        r"""Sets the welink of this CreateSubscriptionUserRequestBody.

        :param welink: The welink of this CreateSubscriptionUserRequestBody.
        :type welink: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestWelinkEndpointInfo`
        """
        self._welink = welink

    @property
    def ding_talk_bot(self):
        r"""Gets the ding_talk_bot of this CreateSubscriptionUserRequestBody.

        :return: The ding_talk_bot of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingTalkBotEndpointInfo`
        """
        return self._ding_talk_bot

    @ding_talk_bot.setter
    def ding_talk_bot(self, ding_talk_bot):
        r"""Sets the ding_talk_bot of this CreateSubscriptionUserRequestBody.

        :param ding_talk_bot: The ding_talk_bot of this CreateSubscriptionUserRequestBody.
        :type ding_talk_bot: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestDingTalkBotEndpointInfo`
        """
        self._ding_talk_bot = ding_talk_bot

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSubscriptionUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
