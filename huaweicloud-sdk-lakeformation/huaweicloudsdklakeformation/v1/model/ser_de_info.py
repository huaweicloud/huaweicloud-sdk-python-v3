# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SerDeInfo:

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
        'serialization_library': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'serialization_library': 'serialization_library',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, serialization_library=None, parameters=None):
        """SerDeInfo

        The model defined in huaweicloud sdk

        :param name: 名字信息
        :type name: str
        :param serialization_library: 实现序列化/反序列化的类
        :type serialization_library: str
        :param parameters: 参数数组。 key最小值1，最大值255 value最大值4000
        :type parameters: dict(str, str)
        """
        
        

        self._name = None
        self._serialization_library = None
        self._parameters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if serialization_library is not None:
            self.serialization_library = serialization_library
        if parameters is not None:
            self.parameters = parameters

    @property
    def name(self):
        """Gets the name of this SerDeInfo.

        名字信息

        :return: The name of this SerDeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SerDeInfo.

        名字信息

        :param name: The name of this SerDeInfo.
        :type name: str
        """
        self._name = name

    @property
    def serialization_library(self):
        """Gets the serialization_library of this SerDeInfo.

        实现序列化/反序列化的类

        :return: The serialization_library of this SerDeInfo.
        :rtype: str
        """
        return self._serialization_library

    @serialization_library.setter
    def serialization_library(self, serialization_library):
        """Sets the serialization_library of this SerDeInfo.

        实现序列化/反序列化的类

        :param serialization_library: The serialization_library of this SerDeInfo.
        :type serialization_library: str
        """
        self._serialization_library = serialization_library

    @property
    def parameters(self):
        """Gets the parameters of this SerDeInfo.

        参数数组。 key最小值1，最大值255 value最大值4000

        :return: The parameters of this SerDeInfo.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SerDeInfo.

        参数数组。 key最小值1，最大值255 value最大值4000

        :param parameters: The parameters of this SerDeInfo.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

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
        if not isinstance(other, SerDeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
