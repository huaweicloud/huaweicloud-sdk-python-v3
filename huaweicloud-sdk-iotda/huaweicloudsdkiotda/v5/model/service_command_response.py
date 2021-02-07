# coding: utf-8

import pprint
import re

import six





class ServiceCommandResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'response_name': 'str',
        'paras': 'list[ServiceCommandPara]'
    }

    attribute_map = {
        'response_name': 'response_name',
        'paras': 'paras'
    }

    def __init__(self, response_name=None, paras=None):
        """ServiceCommandResponse - a model defined in huaweicloud sdk"""
        
        

        self._response_name = None
        self._paras = None
        self.discriminator = None

        self.response_name = response_name
        if paras is not None:
            self.paras = paras

    @property
    def response_name(self):
        """Gets the response_name of this ServiceCommandResponse.

        设备命令响应名称。

        :return: The response_name of this ServiceCommandResponse.
        :rtype: str
        """
        return self._response_name

    @response_name.setter
    def response_name(self, response_name):
        """Sets the response_name of this ServiceCommandResponse.

        设备命令响应名称。

        :param response_name: The response_name of this ServiceCommandResponse.
        :type: str
        """
        self._response_name = response_name

    @property
    def paras(self):
        """Gets the paras of this ServiceCommandResponse.

        设备命令响应的参数列表。

        :return: The paras of this ServiceCommandResponse.
        :rtype: list[ServiceCommandPara]
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this ServiceCommandResponse.

        设备命令响应的参数列表。

        :param paras: The paras of this ServiceCommandResponse.
        :type: list[ServiceCommandPara]
        """
        self._paras = paras

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
        if not isinstance(other, ServiceCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
