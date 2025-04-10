# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupBandwidthInfoRequest:

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
        'target_bandwidth': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'target_bandwidth': 'target_bandwidth'
    }

    def __init__(self, group_id=None, target_bandwidth=None):
        r"""UpdateGroupBandwidthInfoRequest

        The model defined in huaweicloud sdk

        :param group_id: 分片ID。
        :type group_id: str
        :param target_bandwidth: 目标带宽（Mbit/s）。
        :type target_bandwidth: int
        """
        
        

        self._group_id = None
        self._target_bandwidth = None
        self.discriminator = None

        self.group_id = group_id
        self.target_bandwidth = target_bandwidth

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateGroupBandwidthInfoRequest.

        分片ID。

        :return: The group_id of this UpdateGroupBandwidthInfoRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateGroupBandwidthInfoRequest.

        分片ID。

        :param group_id: The group_id of this UpdateGroupBandwidthInfoRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def target_bandwidth(self):
        r"""Gets the target_bandwidth of this UpdateGroupBandwidthInfoRequest.

        目标带宽（Mbit/s）。

        :return: The target_bandwidth of this UpdateGroupBandwidthInfoRequest.
        :rtype: int
        """
        return self._target_bandwidth

    @target_bandwidth.setter
    def target_bandwidth(self, target_bandwidth):
        r"""Sets the target_bandwidth of this UpdateGroupBandwidthInfoRequest.

        目标带宽（Mbit/s）。

        :param target_bandwidth: The target_bandwidth of this UpdateGroupBandwidthInfoRequest.
        :type target_bandwidth: int
        """
        self._target_bandwidth = target_bandwidth

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
        if not isinstance(other, UpdateGroupBandwidthInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
