# coding: utf-8

import pprint
import re

import six





class ServiceType:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_type_name': 'str',
        'service_type_code': 'str',
        'abbreviation': 'str'
    }

    attribute_map = {
        'service_type_name': 'service_type_name',
        'service_type_code': 'service_type_code',
        'abbreviation': 'abbreviation'
    }

    def __init__(self, service_type_name=None, service_type_code=None, abbreviation=None):
        """ServiceType - a model defined in huaweicloud sdk"""
        
        

        self._service_type_name = None
        self._service_type_code = None
        self._abbreviation = None
        self.discriminator = None

        if service_type_name is not None:
            self.service_type_name = service_type_name
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if abbreviation is not None:
            self.abbreviation = abbreviation

    @property
    def service_type_name(self):
        """Gets the service_type_name of this ServiceType.

        |参数名称：云服务类型名称| |参数约束及描述：云服务类型名称|

        :return: The service_type_name of this ServiceType.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this ServiceType.

        |参数名称：云服务类型名称| |参数约束及描述：云服务类型名称|

        :param service_type_name: The service_type_name of this ServiceType.
        :type: str
        """
        self._service_type_name = service_type_name

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ServiceType.

        |参数名称：云服务类型编码| |参数约束及描述：云服务类型编码|

        :return: The service_type_code of this ServiceType.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ServiceType.

        |参数名称：云服务类型编码| |参数约束及描述：云服务类型编码|

        :param service_type_code: The service_type_code of this ServiceType.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def abbreviation(self):
        """Gets the abbreviation of this ServiceType.

        |参数名称：云服务缩写| |参数约束及描述：云服务缩写|

        :return: The abbreviation of this ServiceType.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this ServiceType.

        |参数名称：云服务缩写| |参数约束及描述：云服务缩写|

        :param abbreviation: The abbreviation of this ServiceType.
        :type: str
        """
        self._abbreviation = abbreviation

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
        if not isinstance(other, ServiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
