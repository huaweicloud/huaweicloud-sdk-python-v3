# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Auth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'key': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key'
    }

    def __init__(self, type=None, key=None):
        """Auth

        The model defined in huaweicloud sdk

        :param type: 取值为枚举类型。
        :type type: str
        :param key: - type为枚举值password时，key表示密码； - type为枚举值keypair时，key表示私钥；
        :type key: str
        """
        
        

        self._type = None
        self._key = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if key is not None:
            self.key = key

    @property
    def type(self):
        """Gets the type of this Auth.

        取值为枚举类型。

        :return: The type of this Auth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Auth.

        取值为枚举类型。

        :param type: The type of this Auth.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        """Gets the key of this Auth.

        - type为枚举值password时，key表示密码； - type为枚举值keypair时，key表示私钥；

        :return: The key of this Auth.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Auth.

        - type为枚举值password时，key表示密码； - type为枚举值keypair时，key表示私钥；

        :param key: The key of this Auth.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, Auth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
