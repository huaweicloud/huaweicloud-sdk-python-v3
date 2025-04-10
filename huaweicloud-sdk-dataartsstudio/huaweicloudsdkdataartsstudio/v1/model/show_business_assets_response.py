# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBusinessAssetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'assets': 'list[OpenEntity]'
    }

    attribute_map = {
        'count': 'count',
        'assets': 'assets'
    }

    def __init__(self, count=None, assets=None):
        r"""ShowBusinessAssetsResponse

        The model defined in huaweicloud sdk

        :param count: 业务资产总数
        :type count: int
        :param assets: 业务资产列表
        :type assets: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntity`]
        """
        
        super(ShowBusinessAssetsResponse, self).__init__()

        self._count = None
        self._assets = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if assets is not None:
            self.assets = assets

    @property
    def count(self):
        r"""Gets the count of this ShowBusinessAssetsResponse.

        业务资产总数

        :return: The count of this ShowBusinessAssetsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowBusinessAssetsResponse.

        业务资产总数

        :param count: The count of this ShowBusinessAssetsResponse.
        :type count: int
        """
        self._count = count

    @property
    def assets(self):
        r"""Gets the assets of this ShowBusinessAssetsResponse.

        业务资产列表

        :return: The assets of this ShowBusinessAssetsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntity`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this ShowBusinessAssetsResponse.

        业务资产列表

        :param assets: The assets of this ShowBusinessAssetsResponse.
        :type assets: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntity`]
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
        if not isinstance(other, ShowBusinessAssetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
