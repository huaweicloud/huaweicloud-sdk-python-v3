# coding: utf-8

import pprint
import re

import six





class InvokeFunctionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'x_cff_log_type': 'str',
        'x_cff_request_version': 'str',
        'body': 'dict(str, object)'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'x_cff_log_type': 'X-Cff-Log-Type',
        'x_cff_request_version': 'X-CFF-Request-Version',
        'body': 'body'
    }

    def __init__(self, function_urn=None, x_cff_log_type=None, x_cff_request_version=None, body=None):
        """InvokeFunctionRequest - a model defined in huaweicloud sdk"""
        
        

        self._function_urn = None
        self._x_cff_log_type = None
        self._x_cff_request_version = None
        self._body = None
        self.discriminator = None

        self.function_urn = function_urn
        if x_cff_log_type is not None:
            self.x_cff_log_type = x_cff_log_type
        if x_cff_request_version is not None:
            self.x_cff_request_version = x_cff_request_version
        if body is not None:
            self.body = body

    @property
    def function_urn(self):
        """Gets the function_urn of this InvokeFunctionRequest.


        :return: The function_urn of this InvokeFunctionRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this InvokeFunctionRequest.


        :param function_urn: The function_urn of this InvokeFunctionRequest.
        :type: str
        """
        self._function_urn = function_urn

    @property
    def x_cff_log_type(self):
        """Gets the x_cff_log_type of this InvokeFunctionRequest.


        :return: The x_cff_log_type of this InvokeFunctionRequest.
        :rtype: str
        """
        return self._x_cff_log_type

    @x_cff_log_type.setter
    def x_cff_log_type(self, x_cff_log_type):
        """Sets the x_cff_log_type of this InvokeFunctionRequest.


        :param x_cff_log_type: The x_cff_log_type of this InvokeFunctionRequest.
        :type: str
        """
        self._x_cff_log_type = x_cff_log_type

    @property
    def x_cff_request_version(self):
        """Gets the x_cff_request_version of this InvokeFunctionRequest.


        :return: The x_cff_request_version of this InvokeFunctionRequest.
        :rtype: str
        """
        return self._x_cff_request_version

    @x_cff_request_version.setter
    def x_cff_request_version(self, x_cff_request_version):
        """Sets the x_cff_request_version of this InvokeFunctionRequest.


        :param x_cff_request_version: The x_cff_request_version of this InvokeFunctionRequest.
        :type: str
        """
        self._x_cff_request_version = x_cff_request_version

    @property
    def body(self):
        """Gets the body of this InvokeFunctionRequest.

        执行函数请求体，为json格式。

        :return: The body of this InvokeFunctionRequest.
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this InvokeFunctionRequest.

        执行函数请求体，为json格式。

        :param body: The body of this InvokeFunctionRequest.
        :type: dict(str, object)
        """
        self._body = body

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
        if not isinstance(other, InvokeFunctionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
