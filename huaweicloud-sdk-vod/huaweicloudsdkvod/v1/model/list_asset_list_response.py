# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetListResponse(SdkResponse):

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
        'assets': 'list[AssetSummary]'
    }

    attribute_map = {
        'total': 'total',
        'assets': 'assets'
    }

    def __init__(self, total=None, assets=None):
        """ListAssetListResponse

        The model defined in huaweicloud sdk

        :param total: 媒资总数  &gt; 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请提交工单申请。
        :type total: int
        :param assets: 媒资列表
        :type assets: list[:class:`huaweicloudsdkvod.v1.AssetSummary`]
        """
        
        super(ListAssetListResponse, self).__init__()

        self._total = None
        self._assets = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if assets is not None:
            self.assets = assets

    @property
    def total(self):
        """Gets the total of this ListAssetListResponse.

        媒资总数  > 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请提交工单申请。

        :return: The total of this ListAssetListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAssetListResponse.

        媒资总数  > 暂只能统计2万个媒资，若您需要查询具体的媒资总数，请提交工单申请。

        :param total: The total of this ListAssetListResponse.
        :type total: int
        """
        self._total = total

    @property
    def assets(self):
        """Gets the assets of this ListAssetListResponse.

        媒资列表

        :return: The assets of this ListAssetListResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AssetSummary`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ListAssetListResponse.

        媒资列表

        :param assets: The assets of this ListAssetListResponse.
        :type assets: list[:class:`huaweicloudsdkvod.v1.AssetSummary`]
        """
        self._assets = assets

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
        if not isinstance(other, ListAssetListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
