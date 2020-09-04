# coding: utf-8

import pprint
import re

import six





class ServiceRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'server_host': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'server_host': 'server_host'
    }

    def __init__(self, service_name=None, server_host=None):
        """ServiceRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._service_name = None
        self._server_host = None
        self.discriminator = None

        self.service_name = service_name
        self.server_host = server_host

    @property
    def service_name(self):
        """Gets the service_name of this ServiceRequestBody.

        测试类型名称，用于界面显示，不能使用当前保留名，长度小于等于16位字符

        :return: The service_name of this ServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ServiceRequestBody.

        测试类型名称，用于界面显示，不能使用当前保留名，长度小于等于16位字符

        :param service_name: The service_name of this ServiceRequestBody.
        :type: str
        """
        self._service_name = service_name

    @property
    def server_host(self):
        """Gets the server_host of this ServiceRequestBody.

        新测试类型服务域名，用于拼接调用接口，以https/http开头，长度小于等于128位字符

        :return: The server_host of this ServiceRequestBody.
        :rtype: str
        """
        return self._server_host

    @server_host.setter
    def server_host(self, server_host):
        """Sets the server_host of this ServiceRequestBody.

        新测试类型服务域名，用于拼接调用接口，以https/http开头，长度小于等于128位字符

        :param server_host: The server_host of this ServiceRequestBody.
        :type: str
        """
        self._server_host = server_host

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
        if not isinstance(other, ServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
