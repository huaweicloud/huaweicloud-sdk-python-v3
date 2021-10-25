# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'offset': 'int',
        'total': 'int'
    }

    attribute_map = {
        'count': 'count',
        'offset': 'offset',
        'total': 'total'
    }

    def __init__(self, count=None, offset=None, total=None):
        """Metadata2 - a model defined in huaweicloud sdk"""
        
        

        self._count = None
        self._offset = None
        self._total = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total

    @property
    def count(self):
        """Gets the count of this Metadata2.

        当前返回结果条数。

        :return: The count of this Metadata2.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Metadata2.

        当前返回结果条数。

        :param count: The count of this Metadata2.
        :type: int
        """
        self._count = count

    @property
    def offset(self):
        """Gets the offset of this Metadata2.

        下一个开始的标记，用于分页，null表示无更多数据。

        :return: The offset of this Metadata2.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Metadata2.

        下一个开始的标记，用于分页，null表示无更多数据。

        :param offset: The offset of this Metadata2.
        :type: int
        """
        self._offset = offset

    @property
    def total(self):
        """Gets the total of this Metadata2.

        总条数。

        :return: The total of this Metadata2.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Metadata2.

        总条数。

        :param total: The total of this Metadata2.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, Metadata2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
