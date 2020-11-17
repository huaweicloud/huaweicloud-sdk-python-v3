# coding: utf-8

import pprint
import re

import six





class CreateServersRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'server': 'PrePaidServer'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'server': 'server'
    }

    def __init__(self, dry_run=None, server=None):
        """CreateServersRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._dry_run = None
        self._server = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.server = server

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateServersRequestBody.

        是否只预检此次请求。  true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式等。 如果检查不通过，则返回对应错误。 如果检查通过，则返回202状态码。 false：发送正常请求，通过检查后并且执行创建云服务器请求。

        :return: The dry_run of this CreateServersRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateServersRequestBody.

        是否只预检此次请求。  true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式等。 如果检查不通过，则返回对应错误。 如果检查通过，则返回202状态码。 false：发送正常请求，通过检查后并且执行创建云服务器请求。

        :param dry_run: The dry_run of this CreateServersRequestBody.
        :type: bool
        """
        self._dry_run = dry_run

    @property
    def server(self):
        """Gets the server of this CreateServersRequestBody.


        :return: The server of this CreateServersRequestBody.
        :rtype: PrePaidServer
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateServersRequestBody.


        :param server: The server of this CreateServersRequestBody.
        :type: PrePaidServer
        """
        self._server = server

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
        if not isinstance(other, CreateServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
