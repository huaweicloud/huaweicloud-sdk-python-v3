# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_bandwidth_types': 'list[BandwidthTypeOption]',
        'count': 'int'
    }

    attribute_map = {
        'share_bandwidth_types': 'share_bandwidth_types',
        'count': 'count'
    }

    def __init__(self, share_bandwidth_types=None, count=None):
        r"""ListBandwidthTypesResponse

        The model defined in huaweicloud sdk

        :param share_bandwidth_types: 共享带宽类型列表对象。
        :type share_bandwidth_types: list[:class:`huaweicloudsdkiec.v1.BandwidthTypeOption`]
        :param count: 
        :type count: int
        """
        
        super(ListBandwidthTypesResponse, self).__init__()

        self._share_bandwidth_types = None
        self._count = None
        self.discriminator = None

        if share_bandwidth_types is not None:
            self.share_bandwidth_types = share_bandwidth_types
        if count is not None:
            self.count = count

    @property
    def share_bandwidth_types(self):
        r"""Gets the share_bandwidth_types of this ListBandwidthTypesResponse.

        共享带宽类型列表对象。

        :return: The share_bandwidth_types of this ListBandwidthTypesResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.BandwidthTypeOption`]
        """
        return self._share_bandwidth_types

    @share_bandwidth_types.setter
    def share_bandwidth_types(self, share_bandwidth_types):
        r"""Sets the share_bandwidth_types of this ListBandwidthTypesResponse.

        共享带宽类型列表对象。

        :param share_bandwidth_types: The share_bandwidth_types of this ListBandwidthTypesResponse.
        :type share_bandwidth_types: list[:class:`huaweicloudsdkiec.v1.BandwidthTypeOption`]
        """
        self._share_bandwidth_types = share_bandwidth_types

    @property
    def count(self):
        r"""Gets the count of this ListBandwidthTypesResponse.

        :return: The count of this ListBandwidthTypesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListBandwidthTypesResponse.

        :param count: The count of this ListBandwidthTypesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListBandwidthTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
