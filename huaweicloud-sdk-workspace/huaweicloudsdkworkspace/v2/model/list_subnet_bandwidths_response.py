# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetBandwidthsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidths': 'list[SubnetBandwidthDetail]',
        'total_count': 'int'
    }

    attribute_map = {
        'bandwidths': 'bandwidths',
        'total_count': 'total_count'
    }

    def __init__(self, bandwidths=None, total_count=None):
        r"""ListSubnetBandwidthsResponse

        The model defined in huaweicloud sdk

        :param bandwidths: 云办公带宽信息。
        :type bandwidths: list[:class:`huaweicloudsdkworkspace.v2.SubnetBandwidthDetail`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ListSubnetBandwidthsResponse, self).__init__()

        self._bandwidths = None
        self._total_count = None
        self.discriminator = None

        if bandwidths is not None:
            self.bandwidths = bandwidths
        if total_count is not None:
            self.total_count = total_count

    @property
    def bandwidths(self):
        r"""Gets the bandwidths of this ListSubnetBandwidthsResponse.

        云办公带宽信息。

        :return: The bandwidths of this ListSubnetBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SubnetBandwidthDetail`]
        """
        return self._bandwidths

    @bandwidths.setter
    def bandwidths(self, bandwidths):
        r"""Sets the bandwidths of this ListSubnetBandwidthsResponse.

        云办公带宽信息。

        :param bandwidths: The bandwidths of this ListSubnetBandwidthsResponse.
        :type bandwidths: list[:class:`huaweicloudsdkworkspace.v2.SubnetBandwidthDetail`]
        """
        self._bandwidths = bandwidths

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSubnetBandwidthsResponse.

        总数。

        :return: The total_count of this ListSubnetBandwidthsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSubnetBandwidthsResponse.

        总数。

        :param total_count: The total_count of this ListSubnetBandwidthsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListSubnetBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
