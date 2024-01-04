# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSelector:

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
        'values': 'list[str]',
        'operator': 'str'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values',
        'operator': 'operator'
    }

    def __init__(self, key=None, values=None, operator=None):
        """ResourceSelector

        The model defined in huaweicloud sdk

        :param key: 标签键值，取值如下 - node.uid：节点UID。
        :type key: str
        :param values: 标签值列表
        :type values: list[str]
        :param operator: 标签逻辑运算符，当前支持如下取值 - In
        :type operator: str
        """
        
        

        self._key = None
        self._values = None
        self._operator = None
        self.discriminator = None

        self.key = key
        if values is not None:
            self.values = values
        self.operator = operator

    @property
    def key(self):
        """Gets the key of this ResourceSelector.

        标签键值，取值如下 - node.uid：节点UID。

        :return: The key of this ResourceSelector.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ResourceSelector.

        标签键值，取值如下 - node.uid：节点UID。

        :param key: The key of this ResourceSelector.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this ResourceSelector.

        标签值列表

        :return: The values of this ResourceSelector.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResourceSelector.

        标签值列表

        :param values: The values of this ResourceSelector.
        :type values: list[str]
        """
        self._values = values

    @property
    def operator(self):
        """Gets the operator of this ResourceSelector.

        标签逻辑运算符，当前支持如下取值 - In

        :return: The operator of this ResourceSelector.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ResourceSelector.

        标签逻辑运算符，当前支持如下取值 - In

        :param operator: The operator of this ResourceSelector.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, ResourceSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
