# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactHashCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hash_type': 'str',
        'hash_value': 'str'
    }

    attribute_map = {
        'hash_type': 'hash_type',
        'hash_value': 'hash_value'
    }

    def __init__(self, hash_type=None, hash_value=None):
        r"""ArtifactHashCode

        The model defined in huaweicloud sdk

        :param hash_type: 哈希算法
        :type hash_type: str
        :param hash_value: 哈希值
        :type hash_value: str
        """
        
        

        self._hash_type = None
        self._hash_value = None
        self.discriminator = None

        if hash_type is not None:
            self.hash_type = hash_type
        if hash_value is not None:
            self.hash_value = hash_value

    @property
    def hash_type(self):
        r"""Gets the hash_type of this ArtifactHashCode.

        哈希算法

        :return: The hash_type of this ArtifactHashCode.
        :rtype: str
        """
        return self._hash_type

    @hash_type.setter
    def hash_type(self, hash_type):
        r"""Sets the hash_type of this ArtifactHashCode.

        哈希算法

        :param hash_type: The hash_type of this ArtifactHashCode.
        :type hash_type: str
        """
        self._hash_type = hash_type

    @property
    def hash_value(self):
        r"""Gets the hash_value of this ArtifactHashCode.

        哈希值

        :return: The hash_value of this ArtifactHashCode.
        :rtype: str
        """
        return self._hash_value

    @hash_value.setter
    def hash_value(self, hash_value):
        r"""Sets the hash_value of this ArtifactHashCode.

        哈希值

        :param hash_value: The hash_value of this ArtifactHashCode.
        :type hash_value: str
        """
        self._hash_value = hash_value

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
        if not isinstance(other, ArtifactHashCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
