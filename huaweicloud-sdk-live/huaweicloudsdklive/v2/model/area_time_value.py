# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaTimeValue:


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
        'data': 'list[TimeValue]'
    }

    attribute_map = {
        'name': 'name',
        'data': 'data'
    }

    def __init__(self, name=None, data=None):
        """AreaTimeValue - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._data = None
        self.discriminator = None

        self.name = name
        self.data = data

    @property
    def name(self):
        """Gets the name of this AreaTimeValue.

        各个大区下的具体省份、区域、国家的名称。  具体取值请参考[国家名称缩写](vod_08_0172.xml)和[省份名称缩写](live_03_0043.xml)。 

        :return: The name of this AreaTimeValue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AreaTimeValue.

        各个大区下的具体省份、区域、国家的名称。  具体取值请参考[国家名称缩写](vod_08_0172.xml)和[省份名称缩写](live_03_0043.xml)。 

        :param name: The name of this AreaTimeValue.
        :type: str
        """
        self._name = name

    @property
    def data(self):
        """Gets the data of this AreaTimeValue.

        当前时间返回指定指标的值

        :return: The data of this AreaTimeValue.
        :rtype: list[TimeValue]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AreaTimeValue.

        当前时间返回指定指标的值

        :param data: The data of this AreaTimeValue.
        :type: list[TimeValue]
        """
        self._data = data

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
        if not isinstance(other, AreaTimeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other