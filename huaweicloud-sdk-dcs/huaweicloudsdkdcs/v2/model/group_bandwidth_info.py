# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupBandwidthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'updated_at': 'str',
        'bandwidth': 'int',
        'max_bandwidth': 'int',
        'assured_bandwidth': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'updated_at': 'updated_at',
        'bandwidth': 'bandwidth',
        'max_bandwidth': 'max_bandwidth',
        'assured_bandwidth': 'assured_bandwidth'
    }

    def __init__(self, group_id=None, updated_at=None, bandwidth=None, max_bandwidth=None, assured_bandwidth=None):
        r"""GroupBandwidthInfo

        The model defined in huaweicloud sdk

        :param group_id: 分片ID。
        :type group_id: str
        :param updated_at: 更新时间，UTC时间。
        :type updated_at: str
        :param bandwidth: 当前带宽(Mbit/s)。
        :type bandwidth: int
        :param max_bandwidth: 最大带宽(Mbit/s)。
        :type max_bandwidth: int
        :param assured_bandwidth: 基准带宽(Mbit/s)。
        :type assured_bandwidth: int
        """
        
        

        self._group_id = None
        self._updated_at = None
        self._bandwidth = None
        self._max_bandwidth = None
        self._assured_bandwidth = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if updated_at is not None:
            self.updated_at = updated_at
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if assured_bandwidth is not None:
            self.assured_bandwidth = assured_bandwidth

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupBandwidthInfo.

        分片ID。

        :return: The group_id of this GroupBandwidthInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupBandwidthInfo.

        分片ID。

        :param group_id: The group_id of this GroupBandwidthInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GroupBandwidthInfo.

        更新时间，UTC时间。

        :return: The updated_at of this GroupBandwidthInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GroupBandwidthInfo.

        更新时间，UTC时间。

        :param updated_at: The updated_at of this GroupBandwidthInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this GroupBandwidthInfo.

        当前带宽(Mbit/s)。

        :return: The bandwidth of this GroupBandwidthInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this GroupBandwidthInfo.

        当前带宽(Mbit/s)。

        :param bandwidth: The bandwidth of this GroupBandwidthInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def max_bandwidth(self):
        r"""Gets the max_bandwidth of this GroupBandwidthInfo.

        最大带宽(Mbit/s)。

        :return: The max_bandwidth of this GroupBandwidthInfo.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        r"""Sets the max_bandwidth of this GroupBandwidthInfo.

        最大带宽(Mbit/s)。

        :param max_bandwidth: The max_bandwidth of this GroupBandwidthInfo.
        :type max_bandwidth: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def assured_bandwidth(self):
        r"""Gets the assured_bandwidth of this GroupBandwidthInfo.

        基准带宽(Mbit/s)。

        :return: The assured_bandwidth of this GroupBandwidthInfo.
        :rtype: int
        """
        return self._assured_bandwidth

    @assured_bandwidth.setter
    def assured_bandwidth(self, assured_bandwidth):
        r"""Sets the assured_bandwidth of this GroupBandwidthInfo.

        基准带宽(Mbit/s)。

        :param assured_bandwidth: The assured_bandwidth of this GroupBandwidthInfo.
        :type assured_bandwidth: int
        """
        self._assured_bandwidth = assured_bandwidth

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
        if not isinstance(other, GroupBandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
