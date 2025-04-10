# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckedKey:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'is_etag_matching': 'bool',
        'is_object_existing': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'is_etag_matching': 'is_etag_matching',
        'is_object_existing': 'is_object_existing'
    }

    def __init__(self, key=None, is_etag_matching=None, is_object_existing=None):
        r"""CheckedKey

        The model defined in huaweicloud sdk

        :param key: 键
        :type key: str
        :param is_etag_matching: 是否电子标签匹配
        :type is_etag_matching: bool
        :param is_object_existing: 是否存在对象
        :type is_object_existing: bool
        """
        
        

        self._key = None
        self._is_etag_matching = None
        self._is_object_existing = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if is_etag_matching is not None:
            self.is_etag_matching = is_etag_matching
        if is_object_existing is not None:
            self.is_object_existing = is_object_existing

    @property
    def key(self):
        r"""Gets the key of this CheckedKey.

        键

        :return: The key of this CheckedKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CheckedKey.

        键

        :param key: The key of this CheckedKey.
        :type key: str
        """
        self._key = key

    @property
    def is_etag_matching(self):
        r"""Gets the is_etag_matching of this CheckedKey.

        是否电子标签匹配

        :return: The is_etag_matching of this CheckedKey.
        :rtype: bool
        """
        return self._is_etag_matching

    @is_etag_matching.setter
    def is_etag_matching(self, is_etag_matching):
        r"""Sets the is_etag_matching of this CheckedKey.

        是否电子标签匹配

        :param is_etag_matching: The is_etag_matching of this CheckedKey.
        :type is_etag_matching: bool
        """
        self._is_etag_matching = is_etag_matching

    @property
    def is_object_existing(self):
        r"""Gets the is_object_existing of this CheckedKey.

        是否存在对象

        :return: The is_object_existing of this CheckedKey.
        :rtype: bool
        """
        return self._is_object_existing

    @is_object_existing.setter
    def is_object_existing(self, is_object_existing):
        r"""Sets the is_object_existing of this CheckedKey.

        是否存在对象

        :param is_object_existing: The is_object_existing of this CheckedKey.
        :type is_object_existing: bool
        """
        self._is_object_existing = is_object_existing

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
        if not isinstance(other, CheckedKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
