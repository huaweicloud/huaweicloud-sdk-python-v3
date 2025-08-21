# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepoWebHookSubscriptionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'token': 'str',
        'mention_users': 'str',
        'mention_phone': 'str'
    }

    attribute_map = {
        'url': 'url',
        'token': 'token',
        'mention_users': 'mention_users',
        'mention_phone': 'mention_phone'
    }

    def __init__(self, url=None, token=None, mention_users=None, mention_phone=None):
        r"""UpdateRepoWebHookSubscriptionDto

        The model defined in huaweicloud sdk

        :param url: **参数解释：** webhook的url (需要base64编码)。
        :type url: str
        :param token: **参数解释：** 秘钥。
        :type token: str
        :param mention_users: **参数解释：** userid列表，提醒群中的指定成员（@某个成员），最长1000，每个最长100，“;”分隔符。
        :type mention_users: str
        :param mention_phone: **参数解释：** 手机号列表(需要base64编码)，提醒手机号对应的群成员（@某个成员），最长1000，每个最长30，“;”分隔符。
        :type mention_phone: str
        """
        
        

        self._url = None
        self._token = None
        self._mention_users = None
        self._mention_phone = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if token is not None:
            self.token = token
        if mention_users is not None:
            self.mention_users = mention_users
        if mention_phone is not None:
            self.mention_phone = mention_phone

    @property
    def url(self):
        r"""Gets the url of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** webhook的url (需要base64编码)。

        :return: The url of this UpdateRepoWebHookSubscriptionDto.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** webhook的url (需要base64编码)。

        :param url: The url of this UpdateRepoWebHookSubscriptionDto.
        :type url: str
        """
        self._url = url

    @property
    def token(self):
        r"""Gets the token of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** 秘钥。

        :return: The token of this UpdateRepoWebHookSubscriptionDto.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** 秘钥。

        :param token: The token of this UpdateRepoWebHookSubscriptionDto.
        :type token: str
        """
        self._token = token

    @property
    def mention_users(self):
        r"""Gets the mention_users of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** userid列表，提醒群中的指定成员（@某个成员），最长1000，每个最长100，“;”分隔符。

        :return: The mention_users of this UpdateRepoWebHookSubscriptionDto.
        :rtype: str
        """
        return self._mention_users

    @mention_users.setter
    def mention_users(self, mention_users):
        r"""Sets the mention_users of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** userid列表，提醒群中的指定成员（@某个成员），最长1000，每个最长100，“;”分隔符。

        :param mention_users: The mention_users of this UpdateRepoWebHookSubscriptionDto.
        :type mention_users: str
        """
        self._mention_users = mention_users

    @property
    def mention_phone(self):
        r"""Gets the mention_phone of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** 手机号列表(需要base64编码)，提醒手机号对应的群成员（@某个成员），最长1000，每个最长30，“;”分隔符。

        :return: The mention_phone of this UpdateRepoWebHookSubscriptionDto.
        :rtype: str
        """
        return self._mention_phone

    @mention_phone.setter
    def mention_phone(self, mention_phone):
        r"""Sets the mention_phone of this UpdateRepoWebHookSubscriptionDto.

        **参数解释：** 手机号列表(需要base64编码)，提醒手机号对应的群成员（@某个成员），最长1000，每个最长30，“;”分隔符。

        :param mention_phone: The mention_phone of this UpdateRepoWebHookSubscriptionDto.
        :type mention_phone: str
        """
        self._mention_phone = mention_phone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRepoWebHookSubscriptionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
