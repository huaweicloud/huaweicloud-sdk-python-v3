# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListScriptsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'scripts': 'list[ScriptInfo]'
    }

    attribute_map = {
        'total': 'total',
        'scripts': 'scripts'
    }

    def __init__(self, total=None, scripts=None):
        """ListScriptsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._scripts = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if scripts is not None:
            self.scripts = scripts

    @property
    def total(self):
        """Gets the total of this ListScriptsResponse.


        :return: The total of this ListScriptsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListScriptsResponse.


        :param total: The total of this ListScriptsResponse.
        :type: int
        """
        self._total = total

    @property
    def scripts(self):
        """Gets the scripts of this ListScriptsResponse.


        :return: The scripts of this ListScriptsResponse.
        :rtype: list[ScriptInfo]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this ListScriptsResponse.


        :param scripts: The scripts of this ListScriptsResponse.
        :type: list[ScriptInfo]
        """
        self._scripts = scripts

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
        if not isinstance(other, ListScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
