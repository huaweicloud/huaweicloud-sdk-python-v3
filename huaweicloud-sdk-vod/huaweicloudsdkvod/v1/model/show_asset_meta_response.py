# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowAssetMetaResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_info_array': 'list[AssetInfo]',
        'is_truncated': 'int',
        'total': 'int'
    }

    attribute_map = {
        'asset_info_array': 'asset_info_array',
        'is_truncated': 'is_truncated',
        'total': 'total'
    }

    def __init__(self, asset_info_array=None, is_truncated=None, total=None):
        """ShowAssetMetaResponse - a model defined in huaweicloud sdk"""
        
        super(ShowAssetMetaResponse, self).__init__()

        self._asset_info_array = None
        self._is_truncated = None
        self._total = None
        self.discriminator = None

        if asset_info_array is not None:
            self.asset_info_array = asset_info_array
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if total is not None:
            self.total = total

    @property
    def asset_info_array(self):
        """Gets the asset_info_array of this ShowAssetMetaResponse.


        :return: The asset_info_array of this ShowAssetMetaResponse.
        :rtype: list[AssetInfo]
        """
        return self._asset_info_array

    @asset_info_array.setter
    def asset_info_array(self, asset_info_array):
        """Sets the asset_info_array of this ShowAssetMetaResponse.


        :param asset_info_array: The asset_info_array of this ShowAssetMetaResponse.
        :type: list[AssetInfo]
        """
        self._asset_info_array = asset_info_array

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ShowAssetMetaResponse.


        :return: The is_truncated of this ShowAssetMetaResponse.
        :rtype: int
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ShowAssetMetaResponse.


        :param is_truncated: The is_truncated of this ShowAssetMetaResponse.
        :type: int
        """
        self._is_truncated = is_truncated

    @property
    def total(self):
        """Gets the total of this ShowAssetMetaResponse.


        :return: The total of this ShowAssetMetaResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowAssetMetaResponse.


        :param total: The total of this ShowAssetMetaResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ShowAssetMetaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
