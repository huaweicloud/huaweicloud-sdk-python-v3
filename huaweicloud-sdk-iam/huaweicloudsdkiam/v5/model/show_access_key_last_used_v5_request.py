# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessKeyLastUsedV5Request:

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
        'access_key_id': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'access_key_id': 'access_key_id'
    }

    def __init__(self, user_id=None, access_key_id=None):
        r"""ShowAccessKeyLastUsedV5Request

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type user_id: str
        :param access_key_id: 永久访问密钥ID，即AK。
        :type access_key_id: str
        """
        
        

        self._user_id = None
        self._access_key_id = None
        self.discriminator = None

        self.user_id = user_id
        self.access_key_id = access_key_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowAccessKeyLastUsedV5Request.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The user_id of this ShowAccessKeyLastUsedV5Request.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowAccessKeyLastUsedV5Request.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param user_id: The user_id of this ShowAccessKeyLastUsedV5Request.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this ShowAccessKeyLastUsedV5Request.

        永久访问密钥ID，即AK。

        :return: The access_key_id of this ShowAccessKeyLastUsedV5Request.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this ShowAccessKeyLastUsedV5Request.

        永久访问密钥ID，即AK。

        :param access_key_id: The access_key_id of this ShowAccessKeyLastUsedV5Request.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

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
        if not isinstance(other, ShowAccessKeyLastUsedV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
