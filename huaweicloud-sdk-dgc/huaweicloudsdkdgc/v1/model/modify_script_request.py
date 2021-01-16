# coding: utf-8

import pprint
import re

import six





class ModifyScriptRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'script_name': 'str',
        'body': 'ScriptInfo'
    }

    attribute_map = {
        'script_name': 'script_name',
        'body': 'body'
    }

    def __init__(self, script_name=None, body=None):
        """ModifyScriptRequest - a model defined in huaweicloud sdk"""
        
        

        self._script_name = None
        self._body = None
        self.discriminator = None

        self.script_name = script_name
        if body is not None:
            self.body = body

    @property
    def script_name(self):
        """Gets the script_name of this ModifyScriptRequest.


        :return: The script_name of this ModifyScriptRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this ModifyScriptRequest.


        :param script_name: The script_name of this ModifyScriptRequest.
        :type: str
        """
        self._script_name = script_name

    @property
    def body(self):
        """Gets the body of this ModifyScriptRequest.


        :return: The body of this ModifyScriptRequest.
        :rtype: ScriptInfo
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ModifyScriptRequest.


        :param body: The body of this ModifyScriptRequest.
        :type: ScriptInfo
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
        if not isinstance(other, ModifyScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
