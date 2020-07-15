# coding: utf-8

import pprint
import re

import six





class IdentityToken:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'duration_seconds': 'int'
    }

    attribute_map = {
        'id': 'id',
        'duration_seconds': 'duration_seconds'
    }

    def __init__(self, id=None, duration_seconds=900):
        """IdentityToken - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._duration_seconds = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds

    @property
    def id(self):
        """Gets the id of this IdentityToken.

        token的ID。与请求头中的X-Auth-Token填写其一即可，若都填写，优先校验X-Auth-Token。

        :return: The id of this IdentityToken.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityToken.

        token的ID。与请求头中的X-Auth-Token填写其一即可，若都填写，优先校验X-Auth-Token。

        :param id: The id of this IdentityToken.
        :type: str
        """
        self._id = id

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this IdentityToken.

        AK/SK和securitytoken的有效期，时间单位为秒。取值范围：15min ~ 24h ，默认为15min。

        :return: The duration_seconds of this IdentityToken.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this IdentityToken.

        AK/SK和securitytoken的有效期，时间单位为秒。取值范围：15min ~ 24h ，默认为15min。

        :param duration_seconds: The duration_seconds of this IdentityToken.
        :type: int
        """
        self._duration_seconds = duration_seconds

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
        if not isinstance(other, IdentityToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
