# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateAccessCodeResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'access_code': 'str'
    }

    attribute_map = {
        'access_key': 'access_key',
        'access_code': 'access_code'
    }

    def __init__(self, access_key=None, access_code=None):
        """CreateAccessCodeResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._access_key = None
        self._access_code = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if access_code is not None:
            self.access_code = access_code

    @property
    def access_key(self):
        """Gets the access_key of this CreateAccessCodeResponse.

        接入名，随机生成8位字符串

        :return: The access_key of this CreateAccessCodeResponse.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this CreateAccessCodeResponse.

        接入名，随机生成8位字符串

        :param access_key: The access_key of this CreateAccessCodeResponse.
        :type: str
        """
        self._access_key = access_key

    @property
    def access_code(self):
        """Gets the access_code of this CreateAccessCodeResponse.

        接入凭证。

        :return: The access_code of this CreateAccessCodeResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this CreateAccessCodeResponse.

        接入凭证。

        :param access_code: The access_code of this CreateAccessCodeResponse.
        :type: str
        """
        self._access_code = access_code

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
        if not isinstance(other, CreateAccessCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
