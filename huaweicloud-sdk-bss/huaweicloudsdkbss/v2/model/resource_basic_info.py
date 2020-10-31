# coding: utf-8

import pprint
import re

import six





class ResourceBasicInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type_code': 'str',
        'product_owner_service': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'resource_type_code': 'resource_type_code',
        'product_owner_service': 'product_owner_service',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, resource_type_code=None, product_owner_service=None, name=None, description=None):
        """ResourceBasicInfo - a model defined in huaweicloud sdk"""
        
        

        self._resource_type_code = None
        self._product_owner_service = None
        self._name = None
        self._description = None
        self.discriminator = None

        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if product_owner_service is not None:
            self.product_owner_service = product_owner_service
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ResourceBasicInfo.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :return: The resource_type_code of this ResourceBasicInfo.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ResourceBasicInfo.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :param resource_type_code: The resource_type_code of this ResourceBasicInfo.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def product_owner_service(self):
        """Gets the product_owner_service of this ResourceBasicInfo.

        |参数名称：资源类型归属的服务类型编码| |参数约束及描述：资源类型归属的服务类型编码|

        :return: The product_owner_service of this ResourceBasicInfo.
        :rtype: str
        """
        return self._product_owner_service

    @product_owner_service.setter
    def product_owner_service(self, product_owner_service):
        """Sets the product_owner_service of this ResourceBasicInfo.

        |参数名称：资源类型归属的服务类型编码| |参数约束及描述：资源类型归属的服务类型编码|

        :param product_owner_service: The product_owner_service of this ResourceBasicInfo.
        :type: str
        """
        self._product_owner_service = product_owner_service

    @property
    def name(self):
        """Gets the name of this ResourceBasicInfo.

        |参数名称：资源名称，按照请求的X-Language返回对应语言的名称| |参数约束及描述：资源名称，按照请求的X-Language返回对应语言的名称|

        :return: The name of this ResourceBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceBasicInfo.

        |参数名称：资源名称，按照请求的X-Language返回对应语言的名称| |参数约束及描述：资源名称，按照请求的X-Language返回对应语言的名称|

        :param name: The name of this ResourceBasicInfo.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ResourceBasicInfo.

        |参数名称：资源描述，按照请求的X-Language返回对应语言的描述| |参数约束及描述：资源描述，按照请求的X-Language返回对应语言的描述|

        :return: The description of this ResourceBasicInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceBasicInfo.

        |参数名称：资源描述，按照请求的X-Language返回对应语言的描述| |参数约束及描述：资源描述，按照请求的X-Language返回对应语言的描述|

        :param description: The description of this ResourceBasicInfo.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, ResourceBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
