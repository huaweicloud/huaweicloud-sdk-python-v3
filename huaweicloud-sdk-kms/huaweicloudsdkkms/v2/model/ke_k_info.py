# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeKInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'domain_id': 'domain_id'
    }

    def __init__(self, key_id=None, domain_id=None):
        r"""KeKInfo

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID。
        :type key_id: str
        :param domain_id: 用户域ID。
        :type domain_id: str
        """
        
        

        self._key_id = None
        self._domain_id = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def key_id(self):
        r"""Gets the key_id of this KeKInfo.

        密钥ID。

        :return: The key_id of this KeKInfo.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this KeKInfo.

        密钥ID。

        :param key_id: The key_id of this KeKInfo.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeKInfo.

        用户域ID。

        :return: The domain_id of this KeKInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeKInfo.

        用户域ID。

        :param domain_id: The domain_id of this KeKInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, KeKInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
