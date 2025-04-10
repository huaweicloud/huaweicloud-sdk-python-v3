# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field': 'str',
        'order': 'str'
    }

    attribute_map = {
        'field': 'field',
        'order': 'order'
    }

    def __init__(self, field=None, order=None):
        r"""OrderParam

        The model defined in huaweicloud sdk

        :param field: timeUsed：响应时间，startTime：产生时间。
        :type field: str
        :param order: ASC：正序，DESC：逆序。
        :type order: str
        """
        
        

        self._field = None
        self._order = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if order is not None:
            self.order = order

    @property
    def field(self):
        r"""Gets the field of this OrderParam.

        timeUsed：响应时间，startTime：产生时间。

        :return: The field of this OrderParam.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this OrderParam.

        timeUsed：响应时间，startTime：产生时间。

        :param field: The field of this OrderParam.
        :type field: str
        """
        self._field = field

    @property
    def order(self):
        r"""Gets the order of this OrderParam.

        ASC：正序，DESC：逆序。

        :return: The order of this OrderParam.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this OrderParam.

        ASC：正序，DESC：逆序。

        :param order: The order of this OrderParam.
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
        if not isinstance(other, OrderParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
