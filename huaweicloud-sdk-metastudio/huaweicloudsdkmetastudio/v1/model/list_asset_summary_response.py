# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_list': 'list[DigitalAssetSummary]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'asset_list': 'asset_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, asset_list=None, x_request_id=None):
        r"""ListAssetSummaryResponse

        The model defined in huaweicloud sdk

        :param asset_list: 资产列表。
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListAssetSummaryResponse, self).__init__()

        self._asset_list = None
        self._x_request_id = None
        self.discriminator = None

        if asset_list is not None:
            self.asset_list = asset_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def asset_list(self):
        r"""Gets the asset_list of this ListAssetSummaryResponse.

        资产列表。

        :return: The asset_list of this ListAssetSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        """
        return self._asset_list

    @asset_list.setter
    def asset_list(self, asset_list):
        r"""Sets the asset_list of this ListAssetSummaryResponse.

        资产列表。

        :param asset_list: The asset_list of this ListAssetSummaryResponse.
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        """
        self._asset_list = asset_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListAssetSummaryResponse.

        :return: The x_request_id of this ListAssetSummaryResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListAssetSummaryResponse.

        :param x_request_id: The x_request_id of this ListAssetSummaryResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListAssetSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
