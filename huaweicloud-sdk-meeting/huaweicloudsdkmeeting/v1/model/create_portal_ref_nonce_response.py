# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreatePortalRefNonceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nonce': 'str'
    }

    attribute_map = {
        'nonce': 'nonce'
    }

    def __init__(self, nonce=None):
        """CreatePortalRefNonceResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._nonce = None
        self.discriminator = None

        if nonce is not None:
            self.nonce = nonce

    @property
    def nonce(self):
        """Gets the nonce of this CreatePortalRefNonceResponse.

        用于跳转登录的nonce信息。 说明： 通过链接https://bmeeting.huaweicloud.com/?lang=zh-CN&nonce=xxxxxxxxxxxxx#/login进行免登陆跳转。 

        :return: The nonce of this CreatePortalRefNonceResponse.
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this CreatePortalRefNonceResponse.

        用于跳转登录的nonce信息。 说明： 通过链接https://bmeeting.huaweicloud.com/?lang=zh-CN&nonce=xxxxxxxxxxxxx#/login进行免登陆跳转。 

        :param nonce: The nonce of this CreatePortalRefNonceResponse.
        :type: str
        """
        self._nonce = nonce

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
        if not isinstance(other, CreatePortalRefNonceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
