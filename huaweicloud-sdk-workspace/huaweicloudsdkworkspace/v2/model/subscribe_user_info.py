# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'user_name': 'str',
        'user_phone': 'str',
        'ai_func': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_phone': 'user_phone',
        'ai_func': 'ai_func'
    }

    def __init__(self, user_id=None, user_name=None, user_phone=None, ai_func=None):
        r"""SubscribeUserInfo

        The model defined in huaweicloud sdk

        :param user_id: 用户id。
        :type user_id: str
        :param user_name: 桌面用户名。
        :type user_name: str
        :param user_phone: 用户手机号。
        :type user_phone: str
        :param ai_func: ai 功能是否启用。 * true： 启用 * false： 不启用
        :type ai_func: bool
        """
        
        

        self._user_id = None
        self._user_name = None
        self._user_phone = None
        self._ai_func = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_phone is not None:
            self.user_phone = user_phone
        if ai_func is not None:
            self.ai_func = ai_func

    @property
    def user_id(self):
        r"""Gets the user_id of this SubscribeUserInfo.

        用户id。

        :return: The user_id of this SubscribeUserInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this SubscribeUserInfo.

        用户id。

        :param user_id: The user_id of this SubscribeUserInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this SubscribeUserInfo.

        桌面用户名。

        :return: The user_name of this SubscribeUserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SubscribeUserInfo.

        桌面用户名。

        :param user_name: The user_name of this SubscribeUserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_phone(self):
        r"""Gets the user_phone of this SubscribeUserInfo.

        用户手机号。

        :return: The user_phone of this SubscribeUserInfo.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        r"""Sets the user_phone of this SubscribeUserInfo.

        用户手机号。

        :param user_phone: The user_phone of this SubscribeUserInfo.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def ai_func(self):
        r"""Gets the ai_func of this SubscribeUserInfo.

        ai 功能是否启用。 * true： 启用 * false： 不启用

        :return: The ai_func of this SubscribeUserInfo.
        :rtype: bool
        """
        return self._ai_func

    @ai_func.setter
    def ai_func(self, ai_func):
        r"""Sets the ai_func of this SubscribeUserInfo.

        ai 功能是否启用。 * true： 启用 * false： 不启用

        :param ai_func: The ai_func of this SubscribeUserInfo.
        :type ai_func: bool
        """
        self._ai_func = ai_func

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
        if not isinstance(other, SubscribeUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
