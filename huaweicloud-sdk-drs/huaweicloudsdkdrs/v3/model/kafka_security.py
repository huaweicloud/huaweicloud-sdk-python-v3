# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaSecurity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trust_store_key_name': 'str',
        'trust_store_key': 'str',
        'trust_store_password': 'str',
        'type': 'str'
    }

    attribute_map = {
        'trust_store_key_name': 'trust_store_key_name',
        'trust_store_key': 'trust_store_key',
        'trust_store_password': 'trust_store_password',
        'type': 'type'
    }

    def __init__(self, trust_store_key_name=None, trust_store_key=None, trust_store_password=None, type=None):
        """KafkaSecurity

        The model defined in huaweicloud sdk

        :param trust_store_key_name: 证书名称，使用安全认证时必填。
        :type trust_store_key_name: str
        :param trust_store_key: 安全证书base64转码后的值，使用安全认证时必填。
        :type trust_store_key: str
        :param trust_store_password: 证书密码，使用安全认证时必填。
        :type trust_store_password: str
        :param type: 认证类型，PLAINTEXT为无认证，，使用安全认证时必填。
        :type type: str
        """
        
        

        self._trust_store_key_name = None
        self._trust_store_key = None
        self._trust_store_password = None
        self._type = None
        self.discriminator = None

        if trust_store_key_name is not None:
            self.trust_store_key_name = trust_store_key_name
        if trust_store_key is not None:
            self.trust_store_key = trust_store_key
        if trust_store_password is not None:
            self.trust_store_password = trust_store_password
        if type is not None:
            self.type = type

    @property
    def trust_store_key_name(self):
        """Gets the trust_store_key_name of this KafkaSecurity.

        证书名称，使用安全认证时必填。

        :return: The trust_store_key_name of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key_name

    @trust_store_key_name.setter
    def trust_store_key_name(self, trust_store_key_name):
        """Sets the trust_store_key_name of this KafkaSecurity.

        证书名称，使用安全认证时必填。

        :param trust_store_key_name: The trust_store_key_name of this KafkaSecurity.
        :type trust_store_key_name: str
        """
        self._trust_store_key_name = trust_store_key_name

    @property
    def trust_store_key(self):
        """Gets the trust_store_key of this KafkaSecurity.

        安全证书base64转码后的值，使用安全认证时必填。

        :return: The trust_store_key of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_key

    @trust_store_key.setter
    def trust_store_key(self, trust_store_key):
        """Sets the trust_store_key of this KafkaSecurity.

        安全证书base64转码后的值，使用安全认证时必填。

        :param trust_store_key: The trust_store_key of this KafkaSecurity.
        :type trust_store_key: str
        """
        self._trust_store_key = trust_store_key

    @property
    def trust_store_password(self):
        """Gets the trust_store_password of this KafkaSecurity.

        证书密码，使用安全认证时必填。

        :return: The trust_store_password of this KafkaSecurity.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """Sets the trust_store_password of this KafkaSecurity.

        证书密码，使用安全认证时必填。

        :param trust_store_password: The trust_store_password of this KafkaSecurity.
        :type trust_store_password: str
        """
        self._trust_store_password = trust_store_password

    @property
    def type(self):
        """Gets the type of this KafkaSecurity.

        认证类型，PLAINTEXT为无认证，，使用安全认证时必填。

        :return: The type of this KafkaSecurity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KafkaSecurity.

        认证类型，PLAINTEXT为无认证，，使用安全认证时必填。

        :param type: The type of this KafkaSecurity.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, KafkaSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
