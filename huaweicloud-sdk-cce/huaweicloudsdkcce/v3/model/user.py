# coding: utf-8

import pprint
import re

import six





class User:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'client_certificate_data': 'str',
        'client_key_data': 'str'
    }

    attribute_map = {
        'client_certificate_data': 'client-certificate-data',
        'client_key_data': 'client-key-data'
    }

    def __init__(self, client_certificate_data=None, client_key_data=None):
        """User - a model defined in huaweicloud sdk"""
        
        

        self._client_certificate_data = None
        self._client_key_data = None
        self.discriminator = None

        if client_certificate_data is not None:
            self.client_certificate_data = client_certificate_data
        if client_key_data is not None:
            self.client_key_data = client_key_data

    @property
    def client_certificate_data(self):
        """Gets the client_certificate_data of this User.

        客户端证书。 

        :return: The client_certificate_data of this User.
        :rtype: str
        """
        return self._client_certificate_data

    @client_certificate_data.setter
    def client_certificate_data(self, client_certificate_data):
        """Sets the client_certificate_data of this User.

        客户端证书。 

        :param client_certificate_data: The client_certificate_data of this User.
        :type: str
        """
        self._client_certificate_data = client_certificate_data

    @property
    def client_key_data(self):
        """Gets the client_key_data of this User.

        包含来自TLS客户端密钥文件的PEM编码数据。 

        :return: The client_key_data of this User.
        :rtype: str
        """
        return self._client_key_data

    @client_key_data.setter
    def client_key_data(self, client_key_data):
        """Sets the client_key_data of this User.

        包含来自TLS客户端密钥文件的PEM编码数据。 

        :param client_key_data: The client_key_data of this User.
        :type: str
        """
        self._client_key_data = client_key_data

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
