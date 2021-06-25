# coding: utf-8

import pprint
import re

import six





class UpdateCertificateRequestBody:


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
        'content': 'str',
        'key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content',
        'key': 'key'
    }

    def __init__(self, name=None, content=None, key=None):
        """UpdateCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._content = None
        self._key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if key is not None:
            self.key = key

    @property
    def name(self):
        """Gets the name of this UpdateCertificateRequestBody.

        证书名

        :return: The name of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateRequestBody.

        证书名

        :param name: The name of this UpdateCertificateRequestBody.
        :type: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this UpdateCertificateRequestBody.

        证书文件，PEM编码

        :return: The content of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateCertificateRequestBody.

        证书文件，PEM编码

        :param content: The content of this UpdateCertificateRequestBody.
        :type: str
        """
        self._content = content

    @property
    def key(self):
        """Gets the key of this UpdateCertificateRequestBody.

        证书私钥，PEM编码

        :return: The key of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateCertificateRequestBody.

        证书私钥，PEM编码

        :param key: The key of this UpdateCertificateRequestBody.
        :type: str
        """
        self._key = key

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
        if not isinstance(other, UpdateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other