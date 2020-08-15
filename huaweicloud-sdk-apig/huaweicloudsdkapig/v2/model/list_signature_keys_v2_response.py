# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSignatureKeysV2Response(SdkResponse):


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
        'signs': 'list[SignatureCreateResp]',
        'size': 'int'
    }

    attribute_map = {
        'total': 'total',
        'signs': 'signs',
        'size': 'size'
    }

    def __init__(self, total=None, signs=None, size=None):
        """ListSignatureKeysV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._signs = None
        self._size = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if signs is not None:
            self.signs = signs
        if size is not None:
            self.size = size

    @property
    def total(self):
        """Gets the total of this ListSignatureKeysV2Response.

        符合条件的签名密钥的数量

        :return: The total of this ListSignatureKeysV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSignatureKeysV2Response.

        符合条件的签名密钥的数量

        :param total: The total of this ListSignatureKeysV2Response.
        :type: int
        """
        self._total = total

    @property
    def signs(self):
        """Gets the signs of this ListSignatureKeysV2Response.

        本次查询到的签名密钥列表

        :return: The signs of this ListSignatureKeysV2Response.
        :rtype: list[SignatureCreateResp]
        """
        return self._signs

    @signs.setter
    def signs(self, signs):
        """Sets the signs of this ListSignatureKeysV2Response.

        本次查询到的签名密钥列表

        :param signs: The signs of this ListSignatureKeysV2Response.
        :type: list[SignatureCreateResp]
        """
        self._signs = signs

    @property
    def size(self):
        """Gets the size of this ListSignatureKeysV2Response.

        本次返回的列表长度

        :return: The size of this ListSignatureKeysV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListSignatureKeysV2Response.

        本次返回的列表长度

        :param size: The size of this ListSignatureKeysV2Response.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ListSignatureKeysV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
