# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowIpWhitelistResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enable_whitelist': 'bool',
        'whitelist': 'list[Whitelist]'
    }

    attribute_map = {
        'enable_whitelist': 'enable_whitelist',
        'whitelist': 'whitelist'
    }

    def __init__(self, enable_whitelist=None, whitelist=None):
        """ShowIpWhitelistResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._enable_whitelist = None
        self._whitelist = None
        self.discriminator = None

        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this ShowIpWhitelistResponse.

        是否启用白名单（true/false）。

        :return: The enable_whitelist of this ShowIpWhitelistResponse.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this ShowIpWhitelistResponse.

        是否启用白名单（true/false）。

        :param enable_whitelist: The enable_whitelist of this ShowIpWhitelistResponse.
        :type: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        """Gets the whitelist of this ShowIpWhitelistResponse.

        IP白名单分组列表。

        :return: The whitelist of this ShowIpWhitelistResponse.
        :rtype: list[Whitelist]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this ShowIpWhitelistResponse.

        IP白名单分组列表。

        :param whitelist: The whitelist of this ShowIpWhitelistResponse.
        :type: list[Whitelist]
        """
        self._whitelist = whitelist

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
        if not isinstance(other, ShowIpWhitelistResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
