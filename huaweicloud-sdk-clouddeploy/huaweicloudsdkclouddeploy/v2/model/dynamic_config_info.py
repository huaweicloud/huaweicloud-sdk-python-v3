# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DynamicConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, key=None, value=None, type=None):
        """DynamicConfigInfo

        The model defined in huaweicloud sdk

        :param key: 执行部署任务时传递的参数名称
        :type key: str
        :param value: 执行部署任务时传递的参数值
        :type value: str
        :param type: 类型，如果填写动态参数，则类型必选
        :type type: str
        """
        
        

        self._key = None
        self._value = None
        self._type = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type

    @property
    def key(self):
        """Gets the key of this DynamicConfigInfo.

        执行部署任务时传递的参数名称

        :return: The key of this DynamicConfigInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DynamicConfigInfo.

        执行部署任务时传递的参数名称

        :param key: The key of this DynamicConfigInfo.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this DynamicConfigInfo.

        执行部署任务时传递的参数值

        :return: The value of this DynamicConfigInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DynamicConfigInfo.

        执行部署任务时传递的参数值

        :param value: The value of this DynamicConfigInfo.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        """Gets the type of this DynamicConfigInfo.

        类型，如果填写动态参数，则类型必选

        :return: The type of this DynamicConfigInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicConfigInfo.

        类型，如果填写动态参数，则类型必选

        :param type: The type of this DynamicConfigInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DynamicConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
