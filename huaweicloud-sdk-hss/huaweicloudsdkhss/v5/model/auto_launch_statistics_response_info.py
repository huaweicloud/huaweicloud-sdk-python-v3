# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoLaunchStatisticsResponseInfo:

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
        'type': 'str',
        'num': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'num': 'num'
    }

    def __init__(self, name=None, type=None, num=None):
        """AutoLaunchStatisticsResponseInfo

        The model defined in huaweicloud sdk

        :param name: 自启动项名称
        :type name: str
        :param type: 自启动项类型
        :type type: str
        :param num: 数量
        :type num: int
        """
        
        

        self._name = None
        self._type = None
        self._num = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if num is not None:
            self.num = num

    @property
    def name(self):
        """Gets the name of this AutoLaunchStatisticsResponseInfo.

        自启动项名称

        :return: The name of this AutoLaunchStatisticsResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutoLaunchStatisticsResponseInfo.

        自启动项名称

        :param name: The name of this AutoLaunchStatisticsResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this AutoLaunchStatisticsResponseInfo.

        自启动项类型

        :return: The type of this AutoLaunchStatisticsResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoLaunchStatisticsResponseInfo.

        自启动项类型

        :param type: The type of this AutoLaunchStatisticsResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def num(self):
        """Gets the num of this AutoLaunchStatisticsResponseInfo.

        数量

        :return: The num of this AutoLaunchStatisticsResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this AutoLaunchStatisticsResponseInfo.

        数量

        :param num: The num of this AutoLaunchStatisticsResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, AutoLaunchStatisticsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
