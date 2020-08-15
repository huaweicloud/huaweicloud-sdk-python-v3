# coding: utf-8

import pprint
import re

import six





class Encryption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'hls_encrypt': 'HlsEncrypt',
        'multidrm': 'Multidrm',
        'preview_duration': 'int'
    }

    attribute_map = {
        'hls_encrypt': 'hls_encrypt',
        'multidrm': 'multidrm',
        'preview_duration': 'preview_duration'
    }

    def __init__(self, hls_encrypt=None, multidrm=None, preview_duration=0):
        """Encryption - a model defined in huaweicloud sdk"""
        
        

        self._hls_encrypt = None
        self._multidrm = None
        self._preview_duration = None
        self.discriminator = None

        if hls_encrypt is not None:
            self.hls_encrypt = hls_encrypt
        if multidrm is not None:
            self.multidrm = multidrm
        if preview_duration is not None:
            self.preview_duration = preview_duration

    @property
    def hls_encrypt(self):
        """Gets the hls_encrypt of this Encryption.


        :return: The hls_encrypt of this Encryption.
        :rtype: HlsEncrypt
        """
        return self._hls_encrypt

    @hls_encrypt.setter
    def hls_encrypt(self, hls_encrypt):
        """Sets the hls_encrypt of this Encryption.


        :param hls_encrypt: The hls_encrypt of this Encryption.
        :type: HlsEncrypt
        """
        self._hls_encrypt = hls_encrypt

    @property
    def multidrm(self):
        """Gets the multidrm of this Encryption.


        :return: The multidrm of this Encryption.
        :rtype: Multidrm
        """
        return self._multidrm

    @multidrm.setter
    def multidrm(self, multidrm):
        """Sets the multidrm of this Encryption.


        :param multidrm: The multidrm of this Encryption.
        :type: Multidrm
        """
        self._multidrm = multidrm

    @property
    def preview_duration(self):
        """Gets the preview_duration of this Encryption.

        加密预览时长, 单位秒(S), 0 - preview_duration之间的内容不加密

        :return: The preview_duration of this Encryption.
        :rtype: int
        """
        return self._preview_duration

    @preview_duration.setter
    def preview_duration(self, preview_duration):
        """Sets the preview_duration of this Encryption.

        加密预览时长, 单位秒(S), 0 - preview_duration之间的内容不加密

        :param preview_duration: The preview_duration of this Encryption.
        :type: int
        """
        self._preview_duration = preview_duration

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
        if not isinstance(other, Encryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
