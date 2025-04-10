# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Field:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'order': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'order': 'order'
    }

    def __init__(self, name=None, order=None):
        r"""Field

        The model defined in huaweicloud sdk

        :param name: 字段名。
        :type name: str
        :param order: bool值预留无意义。
        :type order: bool
        """
        
        

        self._name = None
        self._order = None
        self.discriminator = None

        self.name = name
        if order is not None:
            self.order = order

    @property
    def name(self):
        r"""Gets the name of this Field.

        字段名。

        :return: The name of this Field.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Field.

        字段名。

        :param name: The name of this Field.
        :type name: str
        """
        self._name = name

    @property
    def order(self):
        r"""Gets the order of this Field.

        bool值预留无意义。

        :return: The order of this Field.
        :rtype: bool
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this Field.

        bool值预留无意义。

        :param order: The order of this Field.
        :type order: bool
        """
        self._order = order

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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
