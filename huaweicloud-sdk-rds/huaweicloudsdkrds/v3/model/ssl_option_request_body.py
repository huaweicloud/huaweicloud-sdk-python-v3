# coding: utf-8

import pprint
import re

import six





class SslOptionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ssl_option': 'bool'
    }

    attribute_map = {
        'ssl_option': 'ssl_option'
    }

    def __init__(self, ssl_option=None):
        """SslOptionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._ssl_option = None
        self.discriminator = None

        self.ssl_option = ssl_option

    @property
    def ssl_option(self):
        """Gets the ssl_option of this SslOptionRequestBody.

        - true, 打开ssl开关。 - false, 关闭ssl开关。

        :return: The ssl_option of this SslOptionRequestBody.
        :rtype: bool
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this SslOptionRequestBody.

        - true, 打开ssl开关。 - false, 关闭ssl开关。

        :param ssl_option: The ssl_option of this SslOptionRequestBody.
        :type: bool
        """
        self._ssl_option = ssl_option

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
        if not isinstance(other, SslOptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
