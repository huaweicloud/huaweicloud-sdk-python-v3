# coding: utf-8

import pprint
import re

import six





class VerifyCertificateDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'verify_content': 'str'
    }

    attribute_map = {
        'verify_content': 'verify_content'
    }

    def __init__(self, verify_content=None):
        """VerifyCertificateDTO - a model defined in huaweicloud sdk"""
        
        

        self._verify_content = None
        self.discriminator = None

        self.verify_content = verify_content

    @property
    def verify_content(self):
        """Gets the verify_content of this VerifyCertificateDTO.

        验证证书的内容信息。

        :return: The verify_content of this VerifyCertificateDTO.
        :rtype: str
        """
        return self._verify_content

    @verify_content.setter
    def verify_content(self, verify_content):
        """Sets the verify_content of this VerifyCertificateDTO.

        验证证书的内容信息。

        :param verify_content: The verify_content of this VerifyCertificateDTO.
        :type: str
        """
        self._verify_content = verify_content

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
        if not isinstance(other, VerifyCertificateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
