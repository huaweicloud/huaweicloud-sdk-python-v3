# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attribute': 'str',
        'order': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'order': 'order'
    }

    def __init__(self, attribute=None, order=None):
        """Sort

        The model defined in huaweicloud sdk

        :param attribute: 属性
        :type attribute: str
        :param order: 排序枚举值，取值范围DESC、ASC， 默认值ASC
        :type order: str
        """
        
        

        self._attribute = None
        self._order = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if order is not None:
            self.order = order

    @property
    def attribute(self):
        """Gets the attribute of this Sort.

        属性

        :return: The attribute of this Sort.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Sort.

        属性

        :param attribute: The attribute of this Sort.
        :type attribute: str
        """
        self._attribute = attribute

    @property
    def order(self):
        """Gets the order of this Sort.

        排序枚举值，取值范围DESC、ASC， 默认值ASC

        :return: The order of this Sort.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Sort.

        排序枚举值，取值范围DESC、ASC， 默认值ASC

        :param order: The order of this Sort.
        :type order: str
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
        if not isinstance(other, Sort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
