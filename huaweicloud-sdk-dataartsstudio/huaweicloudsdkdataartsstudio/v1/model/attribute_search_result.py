# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributeSearchResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'list[str]',
        'values': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values'
    }

    def __init__(self, name=None, values=None):
        """AttributeSearchResult

        The model defined in huaweicloud sdk

        :param name: 名称列表
        :type name: list[str]
        :param values: 值列表
        :type values: list[object]
        """
        
        

        self._name = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this AttributeSearchResult.

        名称列表

        :return: The name of this AttributeSearchResult.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeSearchResult.

        名称列表

        :param name: The name of this AttributeSearchResult.
        :type name: list[str]
        """
        self._name = name

    @property
    def values(self):
        """Gets the values of this AttributeSearchResult.

        值列表

        :return: The values of this AttributeSearchResult.
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AttributeSearchResult.

        值列表

        :param values: The values of this AttributeSearchResult.
        :type values: list[object]
        """
        self._values = values

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
        if not isinstance(other, AttributeSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
