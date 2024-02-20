# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Criterion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contains': 'list[str]',
        'eq': 'list[str]',
        'exists': 'bool',
        'neq': 'list[str]'
    }

    attribute_map = {
        'contains': 'contains',
        'eq': 'eq',
        'exists': 'exists',
        'neq': 'neq'
    }

    def __init__(self, contains=None, eq=None, exists=None, neq=None):
        """Criterion

        The model defined in huaweicloud sdk

        :param contains: 要匹配筛选器的“包含”运算符。
        :type contains: list[str]
        :param eq: 要匹配筛选器的“等于”运算符。
        :type eq: list[str]
        :param exists: 要匹配筛选器的“存在”运算符。
        :type exists: bool
        :param neq: 要匹配筛选器的“不等于”运算符。
        :type neq: list[str]
        """
        
        

        self._contains = None
        self._eq = None
        self._exists = None
        self._neq = None
        self.discriminator = None

        if contains is not None:
            self.contains = contains
        if eq is not None:
            self.eq = eq
        if exists is not None:
            self.exists = exists
        if neq is not None:
            self.neq = neq

    @property
    def contains(self):
        """Gets the contains of this Criterion.

        要匹配筛选器的“包含”运算符。

        :return: The contains of this Criterion.
        :rtype: list[str]
        """
        return self._contains

    @contains.setter
    def contains(self, contains):
        """Sets the contains of this Criterion.

        要匹配筛选器的“包含”运算符。

        :param contains: The contains of this Criterion.
        :type contains: list[str]
        """
        self._contains = contains

    @property
    def eq(self):
        """Gets the eq of this Criterion.

        要匹配筛选器的“等于”运算符。

        :return: The eq of this Criterion.
        :rtype: list[str]
        """
        return self._eq

    @eq.setter
    def eq(self, eq):
        """Sets the eq of this Criterion.

        要匹配筛选器的“等于”运算符。

        :param eq: The eq of this Criterion.
        :type eq: list[str]
        """
        self._eq = eq

    @property
    def exists(self):
        """Gets the exists of this Criterion.

        要匹配筛选器的“存在”运算符。

        :return: The exists of this Criterion.
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this Criterion.

        要匹配筛选器的“存在”运算符。

        :param exists: The exists of this Criterion.
        :type exists: bool
        """
        self._exists = exists

    @property
    def neq(self):
        """Gets the neq of this Criterion.

        要匹配筛选器的“不等于”运算符。

        :return: The neq of this Criterion.
        :rtype: list[str]
        """
        return self._neq

    @neq.setter
    def neq(self, neq):
        """Sets the neq of this Criterion.

        要匹配筛选器的“不等于”运算符。

        :param neq: The neq of this Criterion.
        :type neq: list[str]
        """
        self._neq = neq

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
        if not isinstance(other, Criterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
