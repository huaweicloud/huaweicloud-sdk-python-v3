# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class AddVaultResourceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'add_resource_ids': 'list[str]'
    }

    attribute_map = {
        'add_resource_ids': 'add_resource_ids'
    }

    def __init__(self, add_resource_ids=None):
        """AddVaultResourceResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._add_resource_ids = None
        self.discriminator = None

        if add_resource_ids is not None:
            self.add_resource_ids = add_resource_ids

    @property
    def add_resource_ids(self):
        """Gets the add_resource_ids of this AddVaultResourceResponse.

        已添加的资源ID列表

        :return: The add_resource_ids of this AddVaultResourceResponse.
        :rtype: list[str]
        """
        return self._add_resource_ids

    @add_resource_ids.setter
    def add_resource_ids(self, add_resource_ids):
        """Sets the add_resource_ids of this AddVaultResourceResponse.

        已添加的资源ID列表

        :param add_resource_ids: The add_resource_ids of this AddVaultResourceResponse.
        :type: list[str]
        """
        self._add_resource_ids = add_resource_ids

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
        if not isinstance(other, AddVaultResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
