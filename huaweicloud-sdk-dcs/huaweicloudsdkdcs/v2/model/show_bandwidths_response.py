# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBandwidthsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'int',
        'max_bandwidth': 'int',
        'allow_modify': 'bool',
        'group_bandwidths': 'list[GroupBandwidthInfo]'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'max_bandwidth': 'max_bandwidth',
        'allow_modify': 'allow_modify',
        'group_bandwidths': 'group_bandwidths'
    }

    def __init__(self, bandwidth=None, max_bandwidth=None, allow_modify=None, group_bandwidths=None):
        r"""ShowBandwidthsResponse

        The model defined in huaweicloud sdk

        :param bandwidth: 实例当前带宽(Mbit/s)。
        :type bandwidth: int
        :param max_bandwidth: 实例最大带宽(Mbit/s)。
        :type max_bandwidth: int
        :param allow_modify: 是否支持调带宽。
        :type allow_modify: bool
        :param group_bandwidths: 分片带宽列表。
        :type group_bandwidths: list[:class:`huaweicloudsdkdcs.v2.GroupBandwidthInfo`]
        """
        
        super(ShowBandwidthsResponse, self).__init__()

        self._bandwidth = None
        self._max_bandwidth = None
        self._allow_modify = None
        self._group_bandwidths = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if allow_modify is not None:
            self.allow_modify = allow_modify
        if group_bandwidths is not None:
            self.group_bandwidths = group_bandwidths

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ShowBandwidthsResponse.

        实例当前带宽(Mbit/s)。

        :return: The bandwidth of this ShowBandwidthsResponse.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ShowBandwidthsResponse.

        实例当前带宽(Mbit/s)。

        :param bandwidth: The bandwidth of this ShowBandwidthsResponse.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def max_bandwidth(self):
        r"""Gets the max_bandwidth of this ShowBandwidthsResponse.

        实例最大带宽(Mbit/s)。

        :return: The max_bandwidth of this ShowBandwidthsResponse.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        r"""Sets the max_bandwidth of this ShowBandwidthsResponse.

        实例最大带宽(Mbit/s)。

        :param max_bandwidth: The max_bandwidth of this ShowBandwidthsResponse.
        :type max_bandwidth: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def allow_modify(self):
        r"""Gets the allow_modify of this ShowBandwidthsResponse.

        是否支持调带宽。

        :return: The allow_modify of this ShowBandwidthsResponse.
        :rtype: bool
        """
        return self._allow_modify

    @allow_modify.setter
    def allow_modify(self, allow_modify):
        r"""Sets the allow_modify of this ShowBandwidthsResponse.

        是否支持调带宽。

        :param allow_modify: The allow_modify of this ShowBandwidthsResponse.
        :type allow_modify: bool
        """
        self._allow_modify = allow_modify

    @property
    def group_bandwidths(self):
        r"""Gets the group_bandwidths of this ShowBandwidthsResponse.

        分片带宽列表。

        :return: The group_bandwidths of this ShowBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.GroupBandwidthInfo`]
        """
        return self._group_bandwidths

    @group_bandwidths.setter
    def group_bandwidths(self, group_bandwidths):
        r"""Sets the group_bandwidths of this ShowBandwidthsResponse.

        分片带宽列表。

        :param group_bandwidths: The group_bandwidths of this ShowBandwidthsResponse.
        :type group_bandwidths: list[:class:`huaweicloudsdkdcs.v2.GroupBandwidthInfo`]
        """
        self._group_bandwidths = group_bandwidths

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
        if not isinstance(other, ShowBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
