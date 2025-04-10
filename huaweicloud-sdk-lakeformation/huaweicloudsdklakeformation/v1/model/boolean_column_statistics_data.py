# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BooleanColumnStatisticsData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number_of_true': 'int',
        'number_of_false': 'int',
        'number_of_null': 'int'
    }

    attribute_map = {
        'number_of_true': 'number_of_true',
        'number_of_false': 'number_of_false',
        'number_of_null': 'number_of_null'
    }

    def __init__(self, number_of_true=None, number_of_false=None, number_of_null=None):
        r"""BooleanColumnStatisticsData

        The model defined in huaweicloud sdk

        :param number_of_true: 列中为真的数量
        :type number_of_true: int
        :param number_of_false: 列中为假的数量
        :type number_of_false: int
        :param number_of_null: 列中为空的数量
        :type number_of_null: int
        """
        
        

        self._number_of_true = None
        self._number_of_false = None
        self._number_of_null = None
        self.discriminator = None

        self.number_of_true = number_of_true
        self.number_of_false = number_of_false
        self.number_of_null = number_of_null

    @property
    def number_of_true(self):
        r"""Gets the number_of_true of this BooleanColumnStatisticsData.

        列中为真的数量

        :return: The number_of_true of this BooleanColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_true

    @number_of_true.setter
    def number_of_true(self, number_of_true):
        r"""Sets the number_of_true of this BooleanColumnStatisticsData.

        列中为真的数量

        :param number_of_true: The number_of_true of this BooleanColumnStatisticsData.
        :type number_of_true: int
        """
        self._number_of_true = number_of_true

    @property
    def number_of_false(self):
        r"""Gets the number_of_false of this BooleanColumnStatisticsData.

        列中为假的数量

        :return: The number_of_false of this BooleanColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_false

    @number_of_false.setter
    def number_of_false(self, number_of_false):
        r"""Sets the number_of_false of this BooleanColumnStatisticsData.

        列中为假的数量

        :param number_of_false: The number_of_false of this BooleanColumnStatisticsData.
        :type number_of_false: int
        """
        self._number_of_false = number_of_false

    @property
    def number_of_null(self):
        r"""Gets the number_of_null of this BooleanColumnStatisticsData.

        列中为空的数量

        :return: The number_of_null of this BooleanColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_null

    @number_of_null.setter
    def number_of_null(self, number_of_null):
        r"""Sets the number_of_null of this BooleanColumnStatisticsData.

        列中为空的数量

        :param number_of_null: The number_of_null of this BooleanColumnStatisticsData.
        :type number_of_null: int
        """
        self._number_of_null = number_of_null

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
        if not isinstance(other, BooleanColumnStatisticsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
