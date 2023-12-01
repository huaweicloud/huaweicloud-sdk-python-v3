# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMatchHeadersHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exact': 'str',
        'case_insensitive': 'bool'
    }

    attribute_map = {
        'exact': 'exact',
        'case_insensitive': 'caseInsensitive'
    }

    def __init__(self, exact=None, case_insensitive=None):
        """CreateMatchHeadersHeader

        The model defined in huaweicloud sdk

        :param exact: 精确匹配值。
        :type exact: str
        :param case_insensitive: 是否区分大小写。
        :type case_insensitive: bool
        """
        
        

        self._exact = None
        self._case_insensitive = None
        self.discriminator = None

        if exact is not None:
            self.exact = exact
        if case_insensitive is not None:
            self.case_insensitive = case_insensitive

    @property
    def exact(self):
        """Gets the exact of this CreateMatchHeadersHeader.

        精确匹配值。

        :return: The exact of this CreateMatchHeadersHeader.
        :rtype: str
        """
        return self._exact

    @exact.setter
    def exact(self, exact):
        """Sets the exact of this CreateMatchHeadersHeader.

        精确匹配值。

        :param exact: The exact of this CreateMatchHeadersHeader.
        :type exact: str
        """
        self._exact = exact

    @property
    def case_insensitive(self):
        """Gets the case_insensitive of this CreateMatchHeadersHeader.

        是否区分大小写。

        :return: The case_insensitive of this CreateMatchHeadersHeader.
        :rtype: bool
        """
        return self._case_insensitive

    @case_insensitive.setter
    def case_insensitive(self, case_insensitive):
        """Sets the case_insensitive of this CreateMatchHeadersHeader.

        是否区分大小写。

        :param case_insensitive: The case_insensitive of this CreateMatchHeadersHeader.
        :type case_insensitive: bool
        """
        self._case_insensitive = case_insensitive

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
        if not isinstance(other, CreateMatchHeadersHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
