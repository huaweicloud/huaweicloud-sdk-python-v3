# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Order:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column': 'str',
        'sort_order': 'int'
    }

    attribute_map = {
        'column': 'column',
        'sort_order': 'sort_order'
    }

    def __init__(self, column=None, sort_order=None):
        """Order

        The model defined in huaweicloud sdk

        :param column: 列的名称
        :type column: str
        :param sort_order: 指示是按升序 (&#x3D;&#x3D; 1) 还是降序 (&#x3D;&#x3D;0) 对列进行排序
        :type sort_order: int
        """
        
        

        self._column = None
        self._sort_order = None
        self.discriminator = None

        if column is not None:
            self.column = column
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def column(self):
        """Gets the column of this Order.

        列的名称

        :return: The column of this Order.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this Order.

        列的名称

        :param column: The column of this Order.
        :type column: str
        """
        self._column = column

    @property
    def sort_order(self):
        """Gets the sort_order of this Order.

        指示是按升序 (== 1) 还是降序 (==0) 对列进行排序

        :return: The sort_order of this Order.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Order.

        指示是按升序 (== 1) 还是降序 (==0) 对列进行排序

        :param sort_order: The sort_order of this Order.
        :type sort_order: int
        """
        self._sort_order = sort_order

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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
