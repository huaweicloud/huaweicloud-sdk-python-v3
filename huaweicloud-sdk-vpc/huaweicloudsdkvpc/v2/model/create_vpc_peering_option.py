# coding: utf-8

import pprint
import re

import six





class CreateVpcPeeringOption:


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
        'request_vpc_info': 'VpcInfo',
        'accept_vpc_info': 'VpcInfo'
    }

    attribute_map = {
        'name': 'name',
        'request_vpc_info': 'request_vpc_info',
        'accept_vpc_info': 'accept_vpc_info'
    }

    def __init__(self, name=None, request_vpc_info=None, accept_vpc_info=None):
        """CreateVpcPeeringOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._request_vpc_info = None
        self._accept_vpc_info = None
        self.discriminator = None

        self.name = name
        self.request_vpc_info = request_vpc_info
        self.accept_vpc_info = accept_vpc_info

    @property
    def name(self):
        """Gets the name of this CreateVpcPeeringOption.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :return: The name of this CreateVpcPeeringOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcPeeringOption.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :param name: The name of this CreateVpcPeeringOption.
        :type: str
        """
        self._name = name

    @property
    def request_vpc_info(self):
        """Gets the request_vpc_info of this CreateVpcPeeringOption.


        :return: The request_vpc_info of this CreateVpcPeeringOption.
        :rtype: VpcInfo
        """
        return self._request_vpc_info

    @request_vpc_info.setter
    def request_vpc_info(self, request_vpc_info):
        """Sets the request_vpc_info of this CreateVpcPeeringOption.


        :param request_vpc_info: The request_vpc_info of this CreateVpcPeeringOption.
        :type: VpcInfo
        """
        self._request_vpc_info = request_vpc_info

    @property
    def accept_vpc_info(self):
        """Gets the accept_vpc_info of this CreateVpcPeeringOption.


        :return: The accept_vpc_info of this CreateVpcPeeringOption.
        :rtype: VpcInfo
        """
        return self._accept_vpc_info

    @accept_vpc_info.setter
    def accept_vpc_info(self, accept_vpc_info):
        """Sets the accept_vpc_info of this CreateVpcPeeringOption.


        :param accept_vpc_info: The accept_vpc_info of this CreateVpcPeeringOption.
        :type: VpcInfo
        """
        self._accept_vpc_info = accept_vpc_info

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
        if not isinstance(other, CreateVpcPeeringOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
