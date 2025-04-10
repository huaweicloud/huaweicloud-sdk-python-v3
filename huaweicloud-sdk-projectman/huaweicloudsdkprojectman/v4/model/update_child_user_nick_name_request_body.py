# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChildUserNickNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nick_name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'nick_name': 'nick_name',
        'user_id': 'user_id'
    }

    def __init__(self, nick_name=None, user_id=None):
        r"""UpdateChildUserNickNameRequestBody

        The model defined in huaweicloud sdk

        :param nick_name: 用户昵称
        :type nick_name: str
        :param user_id: 用户id
        :type user_id: str
        """
        
        

        self._nick_name = None
        self._user_id = None
        self.discriminator = None

        self.nick_name = nick_name
        self.user_id = user_id

    @property
    def nick_name(self):
        r"""Gets the nick_name of this UpdateChildUserNickNameRequestBody.

        用户昵称

        :return: The nick_name of this UpdateChildUserNickNameRequestBody.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this UpdateChildUserNickNameRequestBody.

        用户昵称

        :param nick_name: The nick_name of this UpdateChildUserNickNameRequestBody.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateChildUserNickNameRequestBody.

        用户id

        :return: The user_id of this UpdateChildUserNickNameRequestBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateChildUserNickNameRequestBody.

        用户id

        :param user_id: The user_id of this UpdateChildUserNickNameRequestBody.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, UpdateChildUserNickNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
