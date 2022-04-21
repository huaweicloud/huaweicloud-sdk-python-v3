# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAssetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_info_array': 'list[AssetInfo]'
    }

    attribute_map = {
        'asset_info_array': 'asset_info_array'
    }

    def __init__(self, asset_info_array=None):
        """PublishAssetsResponse

        The model defined in huaweicloud sdk

        :param asset_info_array: 发布的媒资信息。
        :type asset_info_array: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        """
        
        super(PublishAssetsResponse, self).__init__()

        self._asset_info_array = None
        self.discriminator = None

        if asset_info_array is not None:
            self.asset_info_array = asset_info_array

    @property
    def asset_info_array(self):
        """Gets the asset_info_array of this PublishAssetsResponse.

        发布的媒资信息。

        :return: The asset_info_array of this PublishAssetsResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        """
        return self._asset_info_array

    @asset_info_array.setter
    def asset_info_array(self, asset_info_array):
        """Sets the asset_info_array of this PublishAssetsResponse.

        发布的媒资信息。

        :param asset_info_array: The asset_info_array of this PublishAssetsResponse.
        :type asset_info_array: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        """
        self._asset_info_array = asset_info_array

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublishAssetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
