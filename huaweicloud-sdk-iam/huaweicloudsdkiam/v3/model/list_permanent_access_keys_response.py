# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPermanentAccessKeysResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'credentials': 'list[Credentials]'
    }

    attribute_map = {
        'credentials': 'credentials'
    }

    def __init__(self, credentials=None):
        """ListPermanentAccessKeysResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._credentials = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials

    @property
    def credentials(self):
        """Gets the credentials of this ListPermanentAccessKeysResponse.

        认证结果信息列表。

        :return: The credentials of this ListPermanentAccessKeysResponse.
        :rtype: list[Credentials]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ListPermanentAccessKeysResponse.

        认证结果信息列表。

        :param credentials: The credentials of this ListPermanentAccessKeysResponse.
        :type: list[Credentials]
        """
        self._credentials = credentials

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
        if not isinstance(other, ListPermanentAccessKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
