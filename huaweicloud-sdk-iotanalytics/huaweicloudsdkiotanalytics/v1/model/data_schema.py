# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'float',
        'max': 'float',
        'min_length': 'int',
        'max_length': 'int',
        'data_type': 'str'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'min_length': 'min_length',
        'max_length': 'max_length',
        'data_type': 'data_type'
    }

    def __init__(self, min=None, max=None, min_length=None, max_length=None, data_type=None):
        """DataSchema

        The model defined in huaweicloud sdk

        :param min: integer或double类型的的最小值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308
        :type min: float
        :param max: integer或double类型的最大值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308
        :type max: float
        :param min_length: string类型的最小长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096
        :type min_length: int
        :param max_length: string类型的最大长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096
        :type max_length: int
        :param data_type: 数据类型，字符串（string）、整数（integer）、浮点数（double）、对象（object），系统支持的对象型存储大小为1MB，超过时不予存储
        :type data_type: str
        """
        
        

        self._min = None
        self._max = None
        self._min_length = None
        self._max_length = None
        self._data_type = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        self.data_type = data_type

    @property
    def min(self):
        """Gets the min of this DataSchema.

        integer或double类型的的最小值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308

        :return: The min of this DataSchema.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this DataSchema.

        integer或double类型的的最小值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308

        :param min: The min of this DataSchema.
        :type min: float
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this DataSchema.

        integer或double类型的最大值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308

        :return: The max of this DataSchema.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this DataSchema.

        integer或double类型的最大值，当属性值超过范围时系统不予存储，integer时范围：-9223372036854775808 ~ 9223372036854775807；double时范围：-1.7976931348623157E308 ~ 1.7976931348623157E308

        :param max: The max of this DataSchema.
        :type max: float
        """
        self._max = max

    @property
    def min_length(self):
        """Gets the min_length of this DataSchema.

        string类型的最小长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096

        :return: The min_length of this DataSchema.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this DataSchema.

        string类型的最小长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096

        :param min_length: The min_length of this DataSchema.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this DataSchema.

        string类型的最大长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096

        :return: The max_length of this DataSchema.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this DataSchema.

        string类型的最大长度，当属性值超过范围时系统不予存储，范围：0 ~ 4096

        :param max_length: The max_length of this DataSchema.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def data_type(self):
        """Gets the data_type of this DataSchema.

        数据类型，字符串（string）、整数（integer）、浮点数（double）、对象（object），系统支持的对象型存储大小为1MB，超过时不予存储

        :return: The data_type of this DataSchema.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataSchema.

        数据类型，字符串（string）、整数（integer）、浮点数（double）、对象（object），系统支持的对象型存储大小为1MB，超过时不予存储

        :param data_type: The data_type of this DataSchema.
        :type data_type: str
        """
        self._data_type = data_type

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
        if not isinstance(other, DataSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
