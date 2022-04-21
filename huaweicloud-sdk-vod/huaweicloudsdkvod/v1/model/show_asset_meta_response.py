# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """ShowAssetMetaResponse

        The model defined in huaweicloud sdk

        :param asset_info_array: 媒资信息列表。
        :type asset_info_array: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        :param is_truncated: 列表是否被截断。  取值如下： - 1：表示本次查询未返回全部结果。 - 0：表示本次查询已经返回了全部结果。
        :type is_truncated: int
        :param total: 查询媒资总数。  &gt; 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请[提交工单](https://console.huaweicloud.com/ticket/?#/ticketindex/business?productTypeId&#x3D;462902cc39a04ab3a429df872021f970)申请。
        :type total: int
        """
        
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

        媒资信息列表。

        :return: The asset_info_array of this ShowAssetMetaResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        """
        return self._asset_info_array

    @asset_info_array.setter
    def asset_info_array(self, asset_info_array):
        """Sets the asset_info_array of this ShowAssetMetaResponse.

        媒资信息列表。

        :param asset_info_array: The asset_info_array of this ShowAssetMetaResponse.
        :type asset_info_array: list[:class:`huaweicloudsdkvod.v1.AssetInfo`]
        """
        self._asset_info_array = asset_info_array

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ShowAssetMetaResponse.

        列表是否被截断。  取值如下： - 1：表示本次查询未返回全部结果。 - 0：表示本次查询已经返回了全部结果。

        :return: The is_truncated of this ShowAssetMetaResponse.
        :rtype: int
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ShowAssetMetaResponse.

        列表是否被截断。  取值如下： - 1：表示本次查询未返回全部结果。 - 0：表示本次查询已经返回了全部结果。

        :param is_truncated: The is_truncated of this ShowAssetMetaResponse.
        :type is_truncated: int
        """
        self._is_truncated = is_truncated

    @property
    def total(self):
        """Gets the total of this ShowAssetMetaResponse.

        查询媒资总数。  > 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请[提交工单](https://console.huaweicloud.com/ticket/?#/ticketindex/business?productTypeId=462902cc39a04ab3a429df872021f970)申请。

        :return: The total of this ShowAssetMetaResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowAssetMetaResponse.

        查询媒资总数。  > 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请[提交工单](https://console.huaweicloud.com/ticket/?#/ticketindex/business?productTypeId=462902cc39a04ab3a429df872021f970)申请。

        :param total: The total of this ShowAssetMetaResponse.
        :type total: int
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
        if not isinstance(other, ShowAssetMetaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
