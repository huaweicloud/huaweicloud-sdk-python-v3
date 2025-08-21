# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPageAssetListResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assets': 'list[Asset]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'assets': 'assets',
        'pagination': 'pagination'
    }

    def __init__(self, assets=None, pagination=None):
        r"""ShowPageAssetListResultResponse

        The model defined in huaweicloud sdk

        :param assets: 资产详情
        :type assets: list[:class:`huaweicloudsdkdcos.v1.Asset`]
        :param pagination: 
        :type pagination: :class:`huaweicloudsdkdcos.v1.Pagination`
        """
        
        super(ShowPageAssetListResultResponse, self).__init__()

        self._assets = None
        self._pagination = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if pagination is not None:
            self.pagination = pagination

    @property
    def assets(self):
        r"""Gets the assets of this ShowPageAssetListResultResponse.

        资产详情

        :return: The assets of this ShowPageAssetListResultResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.Asset`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this ShowPageAssetListResultResponse.

        资产详情

        :param assets: The assets of this ShowPageAssetListResultResponse.
        :type assets: list[:class:`huaweicloudsdkdcos.v1.Asset`]
        """
        self._assets = assets

    @property
    def pagination(self):
        r"""Gets the pagination of this ShowPageAssetListResultResponse.

        :return: The pagination of this ShowPageAssetListResultResponse.
        :rtype: :class:`huaweicloudsdkdcos.v1.Pagination`
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        r"""Sets the pagination of this ShowPageAssetListResultResponse.

        :param pagination: The pagination of this ShowPageAssetListResultResponse.
        :type pagination: :class:`huaweicloudsdkdcos.v1.Pagination`
        """
        self._pagination = pagination

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
        if not isinstance(other, ShowPageAssetListResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
