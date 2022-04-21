# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetsNewResponse(SdkResponse):

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
        'assets': 'list[AssetResponse]'
    }

    attribute_map = {
        'count': 'count',
        'assets': 'assets'
    }

    def __init__(self, count=None, assets=None):
        """ListAssetsNewResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param assets: 资产集，数量不超过limit
        :type assets: list[:class:`huaweicloudsdkiotanalytics.v1.AssetResponse`]
        """
        
        super(ListAssetsNewResponse, self).__init__()

        self._count = None
        self._assets = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if assets is not None:
            self.assets = assets

    @property
    def count(self):
        """Gets the count of this ListAssetsNewResponse.

        总数

        :return: The count of this ListAssetsNewResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAssetsNewResponse.

        总数

        :param count: The count of this ListAssetsNewResponse.
        :type count: int
        """
        self._count = count

    @property
    def assets(self):
        """Gets the assets of this ListAssetsNewResponse.

        资产集，数量不超过limit

        :return: The assets of this ListAssetsNewResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AssetResponse`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ListAssetsNewResponse.

        资产集，数量不超过limit

        :param assets: The assets of this ListAssetsNewResponse.
        :type assets: list[:class:`huaweicloudsdkiotanalytics.v1.AssetResponse`]
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
        if not isinstance(other, ListAssetsNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
