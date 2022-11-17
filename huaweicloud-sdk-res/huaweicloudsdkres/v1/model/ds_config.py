# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_interval': 'int',
        'category_type': 'str'
    }

    attribute_map = {
        'time_interval': 'time_interval',
        'category_type': 'category_type'
    }

    def __init__(self, time_interval=None, category_type=None):
        """DsConfig

        The model defined in huaweicloud sdk

        :param time_interval: 数据选择(天)。
        :type time_interval: int
        :param category_type: 物品类别。
        :type category_type: str
        """
        
        

        self._time_interval = None
        self._category_type = None
        self.discriminator = None

        if time_interval is not None:
            self.time_interval = time_interval
        if category_type is not None:
            self.category_type = category_type

    @property
    def time_interval(self):
        """Gets the time_interval of this DsConfig.

        数据选择(天)。

        :return: The time_interval of this DsConfig.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this DsConfig.

        数据选择(天)。

        :param time_interval: The time_interval of this DsConfig.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def category_type(self):
        """Gets the category_type of this DsConfig.

        物品类别。

        :return: The category_type of this DsConfig.
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this DsConfig.

        物品类别。

        :param category_type: The category_type of this DsConfig.
        :type category_type: str
        """
        self._category_type = category_type

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
        if not isinstance(other, DsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
