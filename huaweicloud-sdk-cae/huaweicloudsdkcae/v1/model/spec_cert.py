# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecCert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'crt': 'str',
        'key': 'str',
        'policy': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'crt': 'crt',
        'key': 'key',
        'policy': 'policy',
        'created_at': 'created_at'
    }

    def __init__(self, crt=None, key=None, policy=None, created_at=None):
        """SpecCert

        The model defined in huaweicloud sdk

        :param crt: 证书内容。
        :type crt: str
        :param key: 私钥内容。
        :type key: str
        :param policy: 安全策略。 - tls-1-2-strict - tls-1-2 - tls-1-1 - tls-1-0
        :type policy: str
        :param created_at: 创建时间。
        :type created_at: datetime
        """
        
        

        self._crt = None
        self._key = None
        self._policy = None
        self._created_at = None
        self.discriminator = None

        if crt is not None:
            self.crt = crt
        if key is not None:
            self.key = key
        if policy is not None:
            self.policy = policy
        if created_at is not None:
            self.created_at = created_at

    @property
    def crt(self):
        """Gets the crt of this SpecCert.

        证书内容。

        :return: The crt of this SpecCert.
        :rtype: str
        """
        return self._crt

    @crt.setter
    def crt(self, crt):
        """Sets the crt of this SpecCert.

        证书内容。

        :param crt: The crt of this SpecCert.
        :type crt: str
        """
        self._crt = crt

    @property
    def key(self):
        """Gets the key of this SpecCert.

        私钥内容。

        :return: The key of this SpecCert.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SpecCert.

        私钥内容。

        :param key: The key of this SpecCert.
        :type key: str
        """
        self._key = key

    @property
    def policy(self):
        """Gets the policy of this SpecCert.

        安全策略。 - tls-1-2-strict - tls-1-2 - tls-1-1 - tls-1-0

        :return: The policy of this SpecCert.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this SpecCert.

        安全策略。 - tls-1-2-strict - tls-1-2 - tls-1-1 - tls-1-0

        :param policy: The policy of this SpecCert.
        :type policy: str
        """
        self._policy = policy

    @property
    def created_at(self):
        """Gets the created_at of this SpecCert.

        创建时间。

        :return: The created_at of this SpecCert.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SpecCert.

        创建时间。

        :param created_at: The created_at of this SpecCert.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, SpecCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
