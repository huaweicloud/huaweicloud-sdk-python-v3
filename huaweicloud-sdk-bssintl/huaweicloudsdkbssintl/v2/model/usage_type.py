# coding: utf-8

import pprint
import re

import six





class UsageType:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'resource_type_code': 'str',
        'service_type_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'resource_type_code': 'resource_type_code',
        'service_type_code': 'service_type_code'
    }

    def __init__(self, code=None, name=None, resource_type_code=None, service_type_code=None):
        """UsageType - a model defined in huaweicloud sdk"""
        
        

        self._code = None
        self._name = None
        self._resource_type_code = None
        self._service_type_code = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_code is not None:
            self.service_type_code = service_type_code

    @property
    def code(self):
        """Gets the code of this UsageType.

        |参数名称：用量类型编码如：duration| |参数约束及描述：用量类型编码如：duration|

        :return: The code of this UsageType.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UsageType.

        |参数名称：用量类型编码如：duration| |参数约束及描述：用量类型编码如：duration|

        :param code: The code of this UsageType.
        :type: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this UsageType.

        |参数名称：用量类型名称| |参数约束及描述：用量类型名称|

        :return: The name of this UsageType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UsageType.

        |参数名称：用量类型名称| |参数约束及描述：用量类型名称|

        :param name: The name of this UsageType.
        :type: str
        """
        self._name = name

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this UsageType.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :return: The resource_type_code of this UsageType.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this UsageType.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :param resource_type_code: The resource_type_code of this UsageType.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this UsageType.

        |参数名称：服务类型编码| |参数约束及描述：服务类型编码|

        :return: The service_type_code of this UsageType.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this UsageType.

        |参数名称：服务类型编码| |参数约束及描述：服务类型编码|

        :param service_type_code: The service_type_code of this UsageType.
        :type: str
        """
        self._service_type_code = service_type_code

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
